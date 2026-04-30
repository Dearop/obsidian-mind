#!/usr/bin/env python3
"""Summarize a Claude Code transcript into a vault draft via local ollama.

Invoked detached by pre-compact.sh. Never raises — all failure paths exit 0.
Output: thinking/session-summaries/<TS>.md + thinking/session-summaries/.latest

Env:
  OM_SUMMARIZER_DISABLE=1   skip entirely
  OM_SUMMARIZER_MODEL       ollama model tag (default: qwen2.5:14b)
  OLLAMA_HOST               default http://127.0.0.1:11434
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

CHAR_PER_TOKEN = 4
SINGLE_PASS_TOKENS = 30_000
CHUNK_TOKENS = 20_000
CHUNK_OVERLAP_TOKENS = 1_000
TOOL_RESULT_KEEP_CHARS = 2_000
VOCAB_CANDIDATES = 20
VOCAB_MAX = 80
OLLAMA_TIMEOUT_SEC = 300

SYSTEM_PROMPT = """You summarize a Claude Code working session into a structured Markdown draft for an Obsidian vault.

The draft is a triage document — another process will promote items into real vault notes. Be concrete, not generic. Skip anything trivial.

Output EXACTLY this structure, nothing before or after. The examples below show the shape — do not copy their words or use angle brackets in your output.

## Decisions
- [ ] Decision one-liner — why it was made. Related: [[Vocabulary Title]]

## People mentioned
- [[Vocabulary Title]] — context from this session (role, what came up)

## Wins
- [ ] Win one-liner — what was accomplished, why it matters

## Open threads
- Unresolved item to carry forward into next session

## Notable context
- Technical fact, pattern, or gotcha worth remembering but not a decision

Rules:
- Use [[wikilinks]] ONLY for exact titles present in the vocabulary list below, OR titles the user explicitly wrote as [[...]] in the transcript. Do not invent new note titles.
- If a section has no items, write exactly: "- (none)".
- Never output angle brackets (<, >) — they were only for the examples above.
- Keep each bullet to one line. No prose paragraphs.
- No preamble, no closing summary, no code fences around the output.

Existing vault notes you may link to:
{vocab}
"""

REDUCE_PROMPT = """You are consolidating several partial summaries of the SAME session into one final draft.

Merge duplicates. Promote the most important items. Drop trivial ones. Preserve the exact output structure.

{system}"""


def log(msg):
    try:
        sys.stderr.write(f"[summarize-session] {msg}\n")
        sys.stderr.flush()
    except Exception:
        pass


def approx_tokens(text):
    return len(text) // CHAR_PER_TOKEN


def clean_transcript(path):
    """Parse JSONL transcript, strip tool noise, return cleaned text."""
    lines_out = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    entry = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                rendered = render_entry(entry)
                if rendered:
                    lines_out.append(rendered)
    except OSError as e:
        log(f"failed to read transcript: {e}")
        return ""
    return "\n\n".join(lines_out)


def render_entry(entry):
    """Render one transcript entry as plain text, dropping heavy tool payloads."""
    msg = entry.get("message") if isinstance(entry, dict) else None
    if not isinstance(msg, dict):
        # Some entries wrap differently; try top-level role/content
        msg = entry if isinstance(entry, dict) else None
        if not isinstance(msg, dict):
            return ""

    role = msg.get("role") or entry.get("type") or ""
    content = msg.get("content")

    parts = []
    if isinstance(content, str):
        parts.append(content)
    elif isinstance(content, list):
        for block in content:
            if not isinstance(block, dict):
                continue
            btype = block.get("type", "")
            if btype == "text":
                text = block.get("text", "")
                if text:
                    parts.append(text)
            elif btype == "tool_use":
                name = block.get("name", "tool")
                parts.append(f"[tool_use: {name}]")
            elif btype == "tool_result":
                body = block.get("content", "")
                if isinstance(body, list):
                    body = " ".join(
                        b.get("text", "") for b in body if isinstance(b, dict)
                    )
                body = str(body)
                if len(body) > TOOL_RESULT_KEEP_CHARS:
                    body = f"{body[:TOOL_RESULT_KEEP_CHARS]}… [truncated {len(body)} chars]"
                parts.append(f"[tool_result]\n{body}")
            elif btype == "thinking":
                # drop model's internal reasoning
                continue
    if not parts:
        return ""
    label = role.upper() if role else "MSG"
    return f"### {label}\n" + "\n".join(parts)


def chunk_text(text, max_tokens, overlap_tokens):
    """Split text into char-sized chunks approximating token limits."""
    max_chars = max_tokens * CHAR_PER_TOKEN
    overlap_chars = overlap_tokens * CHAR_PER_TOKEN
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap_chars
    return chunks


def extract_candidates(text):
    """Regex-extract proper-noun candidates, tickets, @mentions."""
    candidates = set()
    # Capitalized multi-word sequences (names, projects)
    for m in re.finditer(r"\b([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+){0,3})\b", text):
        s = m.group(1).strip()
        # Drop single-word candidates that are common English
        if " " in s or len(s) >= 6:
            candidates.add(s)
    # Ticket-like tokens (ABC-123)
    for m in re.finditer(r"\b[A-Z]{2,}-\d+\b", text):
        candidates.add(m.group(0))
    # @mentions
    for m in re.finditer(r"@([A-Za-z][A-Za-z0-9_.-]+)", text):
        candidates.add(m.group(1))
    # Rank by frequency
    freq = {}
    for c in candidates:
        freq[c] = text.count(c)
    ranked = sorted(freq.items(), key=lambda x: -x[1])
    return [c for c, _ in ranked[:VOCAB_CANDIDATES]]


def qmd_query(term, vault):
    """Run qmd query; return list of note titles. Silent on failure."""
    try:
        out = subprocess.run(
            ["qmd", "query", term, "--limit", "3"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=vault,
        )
        if out.returncode != 0:
            return []
        titles = []
        for line in out.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            # qmd output varies; accept paths and bare titles
            # strip leading rank numbers, trailing scores
            m = re.search(r"([^/\s][^/]*?)\.md", line)
            if m:
                titles.append(m.group(1).strip())
        return titles
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        return []


def build_vocabulary(text, vault):
    """Return list of real vault note titles referenced by candidates in text."""
    candidates = extract_candidates(text)
    seen = set()
    vocab = []
    for c in candidates:
        for title in qmd_query(c, vault):
            if title not in seen:
                seen.add(title)
                vocab.append(title)
                if len(vocab) >= VOCAB_MAX:
                    return vocab
    return vocab


def ollama_chat(system, user, model, host):
    """Call ollama /api/chat. Return assistant text or '' on failure."""
    url = host.rstrip("/") + "/api/chat"
    body = {
        "model": model,
        "stream": False,
        "options": {"temperature": 0.2},
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT_SEC) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return payload.get("message", {}).get("content", "").strip()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
        log(f"ollama call failed: {e}")
        return ""
    except json.JSONDecodeError as e:
        log(f"ollama response not JSON: {e}")
        return ""


def summarize(text, vocab, model, host):
    """Single-pass or map-reduce summarization."""
    vocab_block = (
        "\n".join(f"- [[{t}]]" for t in vocab) if vocab else "- (none — do not invent wikilinks)"
    )
    system = SYSTEM_PROMPT.format(vocab=vocab_block)

    if approx_tokens(text) <= SINGLE_PASS_TOKENS:
        return ollama_chat(system, text, model, host)

    # Map-reduce
    chunks = chunk_text(text, CHUNK_TOKENS, CHUNK_OVERLAP_TOKENS)
    log(f"map-reduce over {len(chunks)} chunks")
    partials = []
    for i, chunk in enumerate(chunks):
        log(f"chunk {i+1}/{len(chunks)} ({approx_tokens(chunk)} tokens)")
        partial = ollama_chat(system, chunk, model, host)
        if partial:
            partials.append(f"## Partial {i+1}\n\n{partial}")
    if not partials:
        return ""
    combined = "\n\n".join(partials)
    reduce_system = REDUCE_PROMPT.format(system=system)
    return ollama_chat(reduce_system, combined, model, host)


def wrap_frontmatter(body, ts_iso, source_log):
    """Wrap the model output in a vault-compliant frontmatter block."""
    description = (
        "Auto-generated draft from session transcript. "
        "Triage via /om-wrap-up — nothing here is authoritative."
    )
    return f"""---
date: {ts_iso[:10]}
description: {description}
tags: [session-summary, draft, thinking]
status: draft
source: {source_log}
---

# Session summary — {ts_iso}

> [!NOTE]
> Auto-generated draft. Review via `/om-wrap-up` — promote durable items into real vault notes, then this file moves to `promoted/`.

{body}

## Raw transcript

[[{Path(source_log).stem}]]
"""


def main():
    if os.environ.get("OM_SUMMARIZER_DISABLE") == "1":
        return 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--out", default=None, help="optional explicit output path")
    args = parser.parse_args()

    transcript = Path(args.transcript)
    vault = Path(args.vault)
    if not transcript.is_file():
        log(f"transcript not found: {transcript}")
        return 0
    if not vault.is_dir():
        log(f"vault not a directory: {vault}")
        return 0

    model = os.environ.get("OM_SUMMARIZER_MODEL", "qwen2.5:14b")
    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")

    text = clean_transcript(transcript)
    if not text or len(text) < 500:
        log(f"transcript too short ({len(text)} chars); skipping")
        return 0

    log(f"cleaned transcript: {approx_tokens(text)} tokens approx")

    vocab = build_vocabulary(text, str(vault))
    log(f"vocabulary: {len(vocab)} titles")

    summary = summarize(text, vocab, model, host)
    if not summary:
        log("empty summary; skipping write")
        return 0

    now = datetime.now()
    ts_iso = now.strftime("%Y-%m-%d %H:%M")
    ts_stamp = now.strftime("%Y-%m-%d-%H%M")

    out_dir = vault / "thinking" / "session-summaries"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else out_dir / f"{ts_stamp}.md"

    # Link back to the raw transcript — we expect pre-compact.sh's convention
    # session_<trigger>_<YYYYMMDD_HHMMSS>.jsonl. Just record the transcript filename.
    source_log = f"session-logs/{transcript.name}"

    try:
        out_path.write_text(
            wrap_frontmatter(summary, ts_iso, source_log), encoding="utf-8"
        )
        latest = out_dir / ".latest"
        latest.write_text(out_path.name + "\n", encoding="utf-8")
        log(f"wrote {out_path}")
    except OSError as e:
        log(f"failed to write summary: {e}")
        return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log(f"unexpected error: {e}")
        sys.exit(0)
