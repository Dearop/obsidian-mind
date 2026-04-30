---
date: 2026-04-10
type: overview
created: 2026-04-10
updated: 2026-04-13
tags:
  - wiki
  - overview
description: "Top-level map of the wiki, workflow, and current priorities"
---

# Overview

This vault section is a **persistent LLM-maintained research wiki** covering Mathematics, Cryptography, Computer Science, and AI.

## Purpose

Build and maintain a **structured, cumulative, rigorous knowledge base**:
- `raw/` — immutable source material (papers, articles, books, assets). Never edit.
- `research/` — synthesized wiki pages organized by concept.
- Formal paper ingests include mathematical definitions, theorems, and key equations in LaTeX.

## Current State

**SNARK/STARK branch** (well-developed):
- 14 ingested source pages with formal breakdowns
- 26 concept pages with mathematical background and worked examples
- 7 proof-system entity pages, 22 researcher pages (in `org/people/`)
- 9 synthesis / comparison pages
- 1 contradictions tracker
- stronger classical-foundations coverage through polynomial identity testing, algebraic IPs, transparent verification, delegation, and MIP landmarks

**Other domains** (nascent): Mathematics, CS, and AI branches will emerge as sources are added.

## Operating Flow

1. Drop source material into `raw/inbox/` or the relevant `raw/*` subfolder.
2. Ingest **one source at a time** with review.
3. For papers: full formal breakdown — definitions, theorems, formulae, complexity bounds, and a ground-truth-focused summary.
4. For lighter sources: use a lighter summary-first workflow rather than forcing paper-level formality.
5. Update affected concept, entity, and synthesis pages, keeping the graph concept-first.
6. Update [[Index]] and append to [[Log]].
7. Check [[Contradictions]] if the source disagrees with existing wiki content.
8. **Lint pass every 10 sources** — orphans, stale pages, contradictions review, missing concept pages.
9. LLM should **suggest next papers** and missing sources after each ingest.
10. Do **not** auto-promote ad hoc query answers into durable synthesis notes without user review.

## Key Pages

- [[Index]] — navigation catalog
- [[Log]] — chronological activity record
- [[Research Agenda]] — study priorities and domain map
- [[SNARKs and STARKs Reading Map]] — SNARK/STARK paper cluster guide
- [[Contradictions]] — tracked disagreements between sources
- [[Mathematical Preliminaries for SNARKs and STARKs]] — study-oriented math background
