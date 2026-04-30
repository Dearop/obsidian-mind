---
date: 2026-04-16
description: "Checklist and gotchas when renaming between Plonky3 31-bit fields (BabyBear / KoalaBear / Mersenne31) — the things a blanket sed will miss"
tags:
  - reference
  - plonky3
  - cryptography
  - field-migration
---

# Plonky3 Field Migration Checklist

Reusable checklist for migrating a Plonky3-based codebase between 31-bit fields (BabyBear ↔ KoalaBear ↔ Mersenne31). A blanket `sed s/BabyBear/KoalaBear/g` is **not sufficient** — several field-specific constants and parameter tuples are decoupled from the type name and must be updated separately.

Derived from a real migration of [[whir-bench Crate Migration|whir-p3]] from BabyBear to KoalaBear (~236 references across 65 files).

## Checklist

1. **Imports** — rewrite `p3_baby_bear::*` → `p3_koala_bear::*` (or target field crate).
2. **Extension field `W` constant** — per-field, not per-type. Look up the new W in the target crate and update every `ext_mul` / `BinomialExtensionField` construction call site.
3. **Poseidon2 round numbers `(rf, rp, d)`** — field-specific. Prefer calling `p3_poseidon2::poseidon2_round_numbers_128::<F>(WIDTH, D)` over hardcoded magic tuples.
4. **Contrastive doc comments** — grep manually; comments of the form "X for FieldA, Y for FieldB" silently corrupt under blanket rename.
5. **Cargo.toml dedupe** — both `p3-baby-bear` and `p3-koala-bear` often coexist as workspace deps pre-migration. Blanket rename produces duplicate lines; dedupe after.
6. **Validation** — `cargo check --workspace --all-targets` is not enough. Must run `cargo test` — parameter mismatches surface only at runtime via `debug_assert_eq`.

## Extension Field W Constant

`BinomialExtensionField<F, 4>` uses a field-specific non-residue `W`:

| Field     | W  | Source                                                      |
|-----------|----|-------------------------------------------------------------|
| BabyBear  | 11 | `p3-baby-bear` crate                                        |
| KoalaBear | 3  | `p3-koala-bear/src/koala_bear.rs:92` — `const W: KoalaBear = KoalaBear::new(3)` |

Any `ext_mul` or extension-field arithmetic site that inlines the W constant (rather than going through a generic `BinomiallyExtendable` trait bound) must be updated.

## Poseidon2 Round Numbers

For 31-bit fields at `WIDTH=16`:

| Field     | d | rf | rp |
|-----------|---|----|----|
| BabyBear  | 7 | 8  | 13 |
| KoalaBear | 3 | 8  | 20 |

Authoritative source: `p3_poseidon2::poseidon2_round_numbers_128::<F>(WIDTH, D)`. In the whir-p3 migration, hardcoded `(8, 13, 7)` tuples appeared at 10+ call sites and were the biggest source of post-rename runtime failures. Prefer the function call.

## Gotchas (what sed will NOT catch)

- **Per-field W constants** — sed leaves the old numeric value in every `ext_mul` site.
- **Hardcoded Poseidon2 parameter tuples** — `(8, 13, 7)` survives `s/BabyBear/KoalaBear/g` unchanged but is now wrong.
- **Contrastive doc comments** — `"3 for KoalaBear, 7 for BabyBear"` becomes `"3 for KoalaBear, 7 for KoalaBear"`. Must grep after rename.
- **`cargo check` false-green** — circuit tests compare computed output against the actual permutation via runtime assertions. Only `cargo test` exercises these.
- **Duplicate Cargo.toml deps** — if both field crates were present pre-migration, rename produces identical duplicate lines.

## Related

- [[Patterns]] — Plonky3 31-bit field migration checklist (short form)
- [[Gotchas]] — individual entries for each post-rename trap
- [[WHIR]] — scheme instantiated over these fields
- [[whir-bench Crate Migration]] — whir-p3 project context
