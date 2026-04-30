---
date: 2026-04-15
description: "Migration of whir-p3 benchmarks into a dedicated whir-bench crate, unifying legacy bench binaries behind the compare_bench recursive IVC paths"
tags:
  - work
  - active
  - whir-p3
  - benchmarks
---

# whir-bench Crate Migration

Consolidating whir-p3 benchmarking into a dedicated `whir-bench` crate. See [[whir-bench Scheme Mapping]] for the per-scheme API routing.

## Context

Legacy benches (`warp_bench`, `pipeline_bench`, `accumulation_bench`, older `compare_bench`) drifted from the actual recursive IVC code paths. After parity validation, legacy binaries were removed and the crate now exposes 4 schemes routed through existing `warp_ivc` APIs.

## Status

- Step 10 landed: parity verified, old benchmarks deleted, README updated (commit `e2f0473`).
- Schemes rewritten to match `compare_bench` recursive IVC paths (commit `0965ecb`).
- Plot script + requirements + .venv relocated to project root.

## Links

- [[whir-bench Scheme Mapping]]
- [[Patterns]] — parity-gate-before-delete, thin-wrappers-over-existing-APIs
- [[Gotchas]] — union arity + ivc_steps divisibility
- [[Key Decisions]]
