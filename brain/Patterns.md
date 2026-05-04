---
description: "Recurring patterns and conventions discovered across work — architecture, naming, tooling, and implementation patterns"
tags:
  - brain
---

# Patterns

Recurring patterns discovered across work.

- **Parity-gate-before-delete** — before removing legacy/duplicate implementations, first prove output parity with the replacement (numerical equality, test fixtures, or observed benchmark agreement). Only then delete. Source: [[whir-bench Crate Migration]].
- **Thin-wrappers-over-existing-APIs** — when building benchmark/measurement/demo surfaces, wrap the production APIs rather than re-implementing logic. Keeps benches honest and prevents drift. Source: [[whir-bench Scheme Mapping]].
- **Plonky3 31-bit field migration checklist** — when renaming BabyBear ↔ KoalaBear ↔ Mersenne31: (a) imports, (b) per-field `W` constant, (c) Poseidon2 `(rf, rp, d)` via `poseidon2_round_numbers_128`, (d) grep contrastive doc comments, (e) dedupe Cargo.toml, (f) run `cargo test` not just `check`. Full detail in [[Plonky3 Field Migration Checklist]].

- **Authority-flags-are-security-claims** — backend `has_authoritative_typed_*` flags should only change after the verifier proof enforces the full typed relation, with adversarial negative tests. Do not treat optional typed hooks as automatic fallback paths. Source: [[Symphony WHIR Public Verifier]], [[rules]].
