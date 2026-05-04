---
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

- **whir-p3 WARP IVC input constraints** — union arity must be ≥ 4, and `ivc_steps % (arity - 1) == 0` must hold. Violating either will break the fold chain. Source: [[whir-bench Scheme Mapping]].
- **Plonky3 `ext_mul` W constant is field-specific** — BabyBear uses W=11, KoalaBear uses W=3. Every `ext_mul` / extension-field call site must update the constant, not just the type alias. Source: `p3-koala-bear/src/koala_bear.rs:92`. See [[Plonky3 Field Migration Checklist]].
- **Plonky3 Poseidon2 round numbers are field-specific** — at width=16: BabyBear `d=7 → (rf=8, rp=13)`, KoalaBear `d=3 → (rf=8, rp=20)`. Prefer `p3_poseidon2::poseidon2_round_numbers_128::<F>(WIDTH, D)` over hardcoded tuples; mismatches fail only at runtime via `debug_assert`. See [[Plonky3 Field Migration Checklist]].
- **Contrastive doc comments silently corrupt under blanket rename** — a comment like `"3 for KoalaBear, 7 for BabyBear"` becomes `"3 for KoalaBear, 7 for KoalaBear"` after `sed s/BabyBear/KoalaBear/g`. Grep manually after any cross-field rename. See [[Plonky3 Field Migration Checklist]].
- **`cargo check --workspace --all-targets` is insufficient for Plonky3 field migrations** — circuit tests verify computed output against the actual permutation via runtime assertions. Parameter mismatches surface only under `cargo test`. See [[Plonky3 Field Migration Checklist]].

- **WHIR typed output helper is not authority** — transcript-binding a typed folded-output object and validating it in the prover helper is not enough for adversarial soundness. A malicious prover can bypass helper validation, so `has_authoritative_typed_output()` must stay false until the proof relation itself enforces typed output semantics. Source: [[Symphony WHIR Public Verifier]], [[rules]].
