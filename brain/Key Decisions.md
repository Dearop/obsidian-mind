---
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

- **2026-04-15** — Unify whir-p3 benchmarks behind a single `whir-bench` crate whose schemes are thin wrappers over `warp_ivc` recursive IVC paths. Legacy `warp_bench`, `pipeline_bench`, `accumulation_bench`, and older `compare_bench` removed after parity validation. See [[whir-bench Crate Migration]] and [[whir-bench Scheme Mapping]].
