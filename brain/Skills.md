---
date: 2026-04-07
description: "Vault-specific workflows and slash commands — reusable patterns for review prep, project tracking, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Custom slash commands, subagents, and reusable workflows. Defined in `.claude/commands/` and `.claude/agents/`.

## Slash Commands

### Daily Workflow

| Command | Purpose |
|---------|---------|
| `/om-standup` | Morning kickoff — load context, review yesterday, surface tasks, identify priorities |
| `/om-dump` | Freeform capture — dump anything, gets routed to the right notes automatically |
| `/om-wrap-up` | Full session review — verify notes, indexes, links, suggest improvements. Auto-triggered on "wrap up". |

### Editing & Synthesis

| Command | Purpose |
|---------|---------|
| `/om-humanize` | Voice-calibrated editing — makes Claude-drafted text sound like you wrote it |
| `/om-weekly` | Weekly synthesis — cross-session patterns, North Star alignment, uncaptured wins |

### Meeting Prep & Capture

| Command | Purpose |
|---------|---------|
| `/om-prep-1on1` | Prep for an upcoming 1:1 — load person context, open items, wins to share, suggested agenda |
| `/om-capture-1on1` | Capture 1:1 meeting transcript into structured vault note with quotes, action items, DM context |
| `/om-incident-capture` | Capture incident from Slack channels/DMs into structured vault notes — timeline, people, analysis, brag entry |
| `/om-slack-scan` | Deep scan Slack channels/DMs for evidence — extracts timestamped touchpoints, organizes by context |
| `/om-meeting` | Prep for any meeting by topic — subject-forward briefing with open items, blockers, and brainstormed considerations |
| `/om-intake` | Process meeting notes inbox — classify raw exports in `work/meetings/` and route to the right vault notes |

### Performance & Review

| Command | Purpose |
|---------|---------|
| `/om-peer-scan` | Deep scan a peer's GitHub PRs for review prep — produces structured analysis saved to `perf/evidence/` |
| `/om-review-brief` | Generate review brief (manager or peer version) from vault data |
| `/om-self-review` | Write self-assessment for review tool — projects, competencies, principles |
| `/om-review-peer` | Write peer review — projects, principles, performance summary |

### Vault Maintenance

| Command | Purpose |
|---------|---------|
| `/om-vault-audit` | Deep structural audit — indexes, frontmatter, links, Bases, folder placement, stale context |
| `/om-vault-upgrade` | Import content from an existing vault — detects version, classifies notes, transforms frontmatter, rebuilds indexes |
| `/om-project-archive` | Move completed project from `work/active/` to `work/archive/YYYY/`, update all indexes |

## Usage Notes

**Daily:**
- `/om-standup` replaces the manual session start — reads North Star, active work, tasks, git log
- `/om-dump` processes freeform text and routes each piece to the correct note type and folder
- `/om-wrap-up` is auto-triggered when you say "wrap up" — runs full session review

**Editing & Synthesis:**
- `/om-humanize` calibrates against your actual writing samples, not a word blacklist. Detects context from frontmatter (review → corporate-confident, incident → precise, 1:1 → conversational). Run after drafting any note to make it sound human.
- `/om-weekly` bridges standup and review brief — run at end of week for cross-session patterns, North Star drift, and uncaptured wins. Output is transient by default; offer to promote findings to brag doc or North Star.

**Capture:**
- `/om-capture-1on1` handles transcripts, raw notes, or summaries
- `/om-incident-capture` takes Slack URLs and produces structured incident documentation
- `/om-slack-scan` should be run AFTER `/om-peer-scan` to add context beyond code (leadership, communication, collaboration evidence)

**Performance:**
- `/om-peer-scan` works best when launched as parallel agents (one per person)
- `/om-review-brief` needs the private brief to exist first — it generates filtered versions from it

**Maintenance:**
- `/om-vault-audit` should be run at the end of substantial sessions — catches stale indexes and mixed context
- `/om-vault-upgrade` imports content from an existing vault (older obsidian-mind or any Obsidian vault). Detects version, classifies notes, transforms frontmatter, fixes wikilinks, rebuilds indexes. Use `--dry-run` to preview.
- `/om-project-archive` handles the active/ → archive/ move with index updates

## Subagents

| Agent | Purpose | Invoked by |
|-------|---------|------------|
| `brag-spotter` | Proactively finds uncaptured wins and competency gaps | `/om-wrap-up`, `/om-weekly` |
| `context-loader` | Loads all vault context about a person, project, incident, or concept | Direct — "load context on X" |
| `cross-linker` | Finds missing wikilinks, orphans, broken backlinks across the vault | `/om-vault-audit` |
| `people-profiler` | Bulk create/update person notes from Slack profiles | `/om-incident-capture` |
| `review-prep` | Aggregates all performance evidence for a given review period | `/om-review-brief` |
| `slack-archaeologist` | Full Slack reconstruction — reads every message, thread, profile, produces unified timeline | `/om-incident-capture` |
| `vault-librarian` | Deep vault maintenance — orphan detection, broken links, frontmatter validation, stale notes | `/om-vault-audit` |
| `review-fact-checker` | Verify every claim in a review draft against vault sources | `/om-self-review`, `/om-review-peer` |
| `vault-migrator` | Classify, transform, and migrate content from a source vault | `/om-vault-upgrade` |

Subagents run in isolated context windows via `.claude/agents/`. They don't pollute the main conversation.

## Hooks

| Hook | When | What |
|------|------|------|
| SessionStart | On startup/resume | QMD re-index, inject North Star, active work, recent changes, tasks, file listing |
| UserPromptSubmit | Every message | Classify content (decision, incident, 1:1, win, architecture, person, project update) and inject routing hints |
| PostToolUse | After writing `.md` | Validates frontmatter, checks for wikilinks |
| PreCompact | Before context compaction | Back up session transcript to `thinking/session-logs/`; on auto-triggers, launch local ollama summarizer (detached) to write a draft into `thinking/session-summaries/` |
| Stop | End of session | Checklist: archive, update indexes, check orphans |

## Auto-summarizer (local ollama)

On auto-compaction, `pre-compact.sh` launches `.claude/scripts/summarize-session.py` detached. It reads the transcript, retrieves a wikilink vocabulary from QMD, calls a local ollama model, and writes a structured draft to `thinking/session-summaries/<timestamp>.md` plus a `.latest` pointer. `/om-wrap-up` triages the draft; promoted drafts move to `thinking/session-summaries/promoted/`; `/om-vault-audit` deletes those older than 30 days.

Design guarantees:
- Never blocks compaction — runs detached, hook exits in <100ms.
- Never leaves the machine — local ollama, no API calls. Transcripts can contain 1:1s, comp, incidents; keep them local.
- Never pollutes semantic search — `thinking/session-summaries/**` is excluded from the QMD collection mask.
- Never writes authoritative memory — drafts are triage input for `/om-wrap-up`. Only the human-confirmed promotion path lands items in `work/`, `org/`, `perf/`, or `brain/`.
- Only runs on `trigger=auto`. Manual compactions are user-driven; a summary would land too late to matter that session.

Env knobs (set in your shell profile):

| Variable | Effect | Default |
|----------|--------|---------|
| `OM_SUMMARIZER_DISABLE=1` | Skip the summarizer entirely | unset (enabled) |
| `OM_SUMMARIZER_MODEL` | ollama model tag | `qwen2.5:14b` |
| `OLLAMA_HOST` | ollama endpoint | `http://127.0.0.1:11434` |

Troubleshooting:
- **Nothing appears in `thinking/session-summaries/`**: check `thinking/session-summaries/.summarizer.log`. Most common cause: ollama not running (`ollama serve`) or model not pulled (`ollama pull qwen2.5:14b`). The hook is non-fatal — compaction still succeeded, you just didn't get a draft.
- **Draft has no `[[wikilinks]]`**: QMD collection isn't registered. Run `qmd collection add . --name vault --mask "**/*.md,!thinking/session-summaries/**"` then `qmd update && qmd embed`.
- **Runtime feels slow**: qwen2.5:14b does ~30 tok/s prefill on M3 Pro, so a 10K-token session takes ~3–5 minutes including cold model load. Acceptable for a detached background job. Swap to `llama3.1:8b` for ~2× faster at slight quality cost: `export OM_SUMMARIZER_MODEL=llama3.1:8b`.
- **Privacy concern on a given session**: `OM_SUMMARIZER_DISABLE=1` in the shell before starting Claude Code turns it off for the whole session.

## Semantic Search (QMD)

If QMD is installed (`npm install -g @tobilu/qmd`), the vault has semantic search:

- `qmd query "..."` — hybrid BM25 + vector + LLM reranking (best quality)
- `qmd search "..."` — fast BM25 keyword search
- `qmd vsearch "..."` — semantic vector search (exploratory)
- `qmd update && qmd embed` — refresh index after bulk changes

SessionStart hook runs `qmd update` automatically. See `.claude/skills/qmd/SKILL.md` for full reference.

## Workflow: Weekly Review

1. **`/om-weekly`** — synthesize the week's activity, check alignment, find patterns
2. Promote any uncaptured wins to brag doc
3. Update North Star if focus shifted
4. **`/om-wrap-up`** — close the session cleanly

## Workflow: Full Review Cycle Prep

1. **`/om-review-brief manager`** — generate the manager context transfer doc
2. **`/om-review-brief peers`** — generate the peer context transfer doc
3. **`/om-peer-scan`** (parallel, one per peer) — deep scan each peer's PRs
4. **`/om-slack-scan`** — scan relevant channels for your own evidence + peer context
5. **`/om-capture-1on1`** — capture the review 1:1 with your manager
6. **`/om-vault-audit`** — tidy up after all the new data

## Workflow: Project Ramp-Up

1. **`/om-slack-scan`** — scan project channels for history and decisions
2. **`/om-peer-scan`** (if needed) — understand what teammates have already built
3. Create work note from gathered context
4. **`/om-vault-audit`** — ensure everything links properly
