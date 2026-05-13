---
date: 2026-05-12
description: "Durable session note for the SYMBT3 accumulator-authoritative cleanup/reporting pass and K6a/K6b benchmark state."
tags:
  - work-note
  - active
  - symbt3
  - whir
  - symphony
  - accumulation
  - benchmarks
  - nonzk
status: active
quarter: Q2-2026
---

# SYMBT3 Accumulator Authority Cleanup

Links: [[Symphony WHIR Public Verifier]], [[Symphony]], [[WHIR]], [[Accumulation Schemes]], [[Commit-and-Prove SNARKs]], [[Key Decisions]], [[Gotchas]]

#symbt3 #whir #symphony #accumulation #benchmarks #nonzk

## Completed Work

This cleanup/reporting pass preserved the protocol boundary while making the implemented SYMBT3 accumulator path easier to audit.

- K1e.2 public-canonical manifest binding: `PublicCanonicalManifestViewV1` remains the product-facing manifest policy; dense manifest/source-view materialization is diagnostic-only.
- K2a typed accumulator scaffolding: `Symbt3AccumulatorInstance` is the compressed public accumulator boundary, and `Symbt3AccumulatorWitness` stays witness-side.
- K2b accumulator transition consistency: the accumulator update remains a single transition claim with a domain-separated `rho_acc`.
- K3 authority profile hardening: `ResearchAuthorityCandidateV0`, `AccumulatorSoundnessAuthorityCandidateV1`, `ProductAuthority`, `NonZKIntegrity`, and `PublicCanonicalManifestViewV1` are now the durable labels for reporting and docs.
- K4 research public accumulator API: `prove_public_symbt3_accumulator_research_non_zk` / `verify_public_symbt3_accumulator_research_non_zk` remain research-only and public-boundary based.
- K4.5 verifier-side source residual batching: logical source R1CS residual claims remain visible, but verifier work is batched to one residual evaluation in the reported fixtures.
- K4.6 compressed public accumulator boundary: public boundary size is the compressed `Symbt3AccumulatorInstance::canonical_bytes()` rather than expanded per-item source material.
- K6a explicit NonZK integrity product route: `Symbt3AccumulatorNonZkIntegrity` is explicit opt-in only and rejects wrong proof-kind markers.
- K6b side-by-side product comparison benchmark: `PRODUCT_COMPARISON_CSV` reports monolithic product verification next to explicit SYMBT3 K6a NonZK integrity verification.

## Benchmark Snapshot

Source: `benchmarks/product_route_comparison.csv` in the Symphony repo.

| k | monolithic verify ms | SYMBT3 K6a verify ms | verify speedup | monolithic prove ms | SYMBT3 prove ms | prove speedup | monolithic proof bytes | SYMBT3 proof bytes | proof ratio | monolithic public bytes | SYMBT3 public bytes | public ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2,109.052 | 17.656 | 119.45x | 3,664.787 | 17.491 | 209.52x | 1,206,465 | 311,568 | 0.258 | 15,171 | 18,715 | 1.234 |
| 2 | 6,232.810 | 24.180 | 257.77x | 7,519.404 | 49.591 | 151.63x | 1,256,159 | 335,935 | 0.267 | 15,187 | 18,715 | 1.232 |
| 4 | 13,326.962 | 24.348 | 547.36x | 23,325.334 | 25.078 | 930.11x | 1,556,795 | 329,707 | 0.212 | 15,219 | 18,715 | 1.230 |
| 8 | 51,182.449 | 30.702 | 1,667.09x | 43,438.693 | 67.128 | 647.10x | 1,613,175 | 387,417 | 0.240 | 15,283 | 18,715 | 1.225 |

Reported SYMBT3 shape counters are fixed in these rows: one top-level WHIR proof, zero family subproofs, one backend table, one accumulator transition claim, one verifier-side source R1CS residual evaluation, `symbt3_product_route_selected=true`, and `symbt3_monolithic_fallback_used=false`.

## Preserved Invariants

- No protocol changes, no proof semantics changes, and no product routing changes.
- Product `verify_public` remains unchanged; SYMBT3 is not the default product route.
- K6a remains explicit opt-in NonZK integrity only, not a zkSNARK or privacy-preserving route.
- One top-level WHIR proof, zero family subproofs, and one backend table are preserved.
- No K5 masking/private-manifest work was implemented.
- Public proof objects remain public-only; witness-side accumulator data stays out of the public boundary.
- Dense manifest/source-view/message-trace materialization remains removed from the product route or marked diagnostic-only where retained for tests/reporting.

## Caveats

- The benchmark table is a one-shot reporter snapshot, not a replacement for repeated Criterion timing.
- SYMBT3 K6a can reveal WHIR-queried private coordinates at query positions; it is an integrity route only.
- The current route does not support private manifest membership or native multi-oracle product semantics.
- Public `verify_public` for the product path still relies on the existing authoritative typed CP route, not SYMBT3.

## Repo Paths Touched

- `src/modular/batched_cp.rs`
- `src/snark/whir/mod.rs`
- `tests/batched_cp.rs`
- `benches/whir_scaling.rs`
- `docs/symbt3_accumulator_authoritative_roadmap.md`
- `docs/whir.md`
- `docs/whir_public_performance_north_star_plan.md`
- `work/active/SYMBT3 Accumulator Authority Cleanup.md`
- `work/Index.md`

## Deferred Work

- K5 ZK/masking.
- Private manifest membership.
- Native multi-oracle product route.
- Making SYMBT3 the default product `verify_public` route.
- Broader protocol changes or new proof semantics.

## Next-Step Checklist

- Run the requested verification gate: `cargo fmt`, `cargo check --features whir --tests`, `cargo test --features whir symbt3 -- --nocapture`, `cargo test --features whir verify_public -- --nocapture`, `cargo test --features whir`, `cargo test`, and `git diff --check`.
- If optimizing further, keep changes independently reviewable and record before/after row counts plus benchmark numbers.
- If changing public proof format or CSV schema, version the spec/schema rather than silently changing stable consumers.
- Before any product route promotion, implement K5/private-manifest/native multi-oracle work and add malformed-input, replay, and splicing tests.
