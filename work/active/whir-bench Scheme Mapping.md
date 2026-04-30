---
date: 2026-04-15
description: "Mapping of the 4 whir-bench schemes to underlying warp_ivc APIs, clarifying that benches are thin wrappers over production code paths"
tags:
  - work
  - active
  - whir-p3
  - benchmarks
---

# whir-bench Scheme Mapping

Companion to [[whir-bench Crate Migration]]. The 4 benchmark schemes are thin wrappers over existing `warp_ivc` APIs — no parallel implementations.

## Schemes

Each scheme routes to a corresponding `warp_ivc_*` entry point in `src/ivc/warp_ivc.rs`. Batch reduction, recursive fold verification, and terminal WHIR are all shared with production pipeline code.

## Constraints on inputs

- Union arity must be ≥ 4.
- `ivc_steps % (arity - 1) == 0` must hold, otherwise the fold chain cannot terminate cleanly.

See [[Gotchas]].

## Rationale

See [[Key Decisions]] entry 2026-04-15. Parity was gated before deleting legacy benches — see [[Patterns]].
