---
date: 2026-05-01
description: "Operational guardrails for Symphony WHIR implementation work, especially typed proof authority and public verifier safety."
tags:
  - brain
  - rules
  - symphony
  - whir
---
# rules

Links: [[Symphony WHIR Public Verifier]], [[Symphony]], [[WHIR]], [[Key Decisions]], [[Gotchas]], [[Patterns]], [[North Star]]

## Symphony WHIR Directives

- Treat `verify_v2` as the product boundary for public verification. It must remain public-only and fail closed when typed backend authority is missing.
- Do not set `has_authoritative_typed_cp()` to true until the proof verifier enforces the full typed CP relation. `has_authoritative_typed_output()` may be true only for the narrower final folded R1CS statement, with CP still owning folded-output derivation.
- Prover-side validation is not soundness. A malicious prover can bypass helper functions and construct backend proofs directly.
- Non-authoritative typed hooks are development scaffolding. Orchestrators must not select them automatically.
- Typed CP relation descriptors are authority-gated. If `has_authoritative_typed_cp()` is false, use the legacy CP proof path even when `prove_typed_cp` / `verify_typed_cp` exist.
- If `has_authoritative_typed_cp()` is true, proving and verification must use the typed CP relation description and fail closed when setup/proving/verification cannot use that relation.
- WHIR output proofs must bind public R1CS coordinates to the committed assignment, not only to transcript bytes.
- WHIR CP-R1CS is not authoritative typed CP until it proves the full `CpRelation::check_with_algebra` semantics.
- Use Poseidon2/BabyBear, not SHA-256-in-WHIR, for the authoritative WHIR typed CP public digest path. Keep SHA-256 only as the compatibility/full-verifier digest scheme until typed CP flips authoritative.
- Keep benchmark labels honest: `folding_only_vs_k` measures folding prover cost, full `verify` includes witness-side checks, and `public_verify_v2_vs_k` should not exist until the public verifier is real.
- Every authority-flag change needs negative tests showing tampered typed public data, witness data, and backend proof splicing are rejected.
- Prefer explicit relation specs before optimizing. Performance claims are only meaningful after the security boundary is correct.

## Documentation Rules

- Link implementation notes back to [[Symphony WHIR Public Verifier]].
- Record security-sensitive decisions in [[Key Decisions]].
- Record traps in [[Gotchas]].
- Record recurring engineering patterns in [[Patterns]].

## Typed CP Field Relation Rules

- `CpPublicStatement` is the public typed CP boundary. Do not reduce typed CP back to opaque digest-only `CpPublicInstance` for public verification.
- `CpFieldRelation` is the software spec for authoritative typed CP. WHIR authority requires the verifier proof to enforce every security-relevant check in that relation, not merely to run the checker during honest proving.
- SHA-256 is compatibility-only for WHIR public CP. The WHIR/PQ public CP path should use Poseidon2/BabyBear field-native commitments and digests.
- Do not add `public_verify_v2_vs_k` or advertise public WHIR verification until both typed output and typed CP are authoritative.


## WHIR Typed CP Authority Guardrail

- A WHIR typed CP hook over the existing CP-R1CS core is not enough to set `has_authoritative_typed_cp()` true.
- Typed CP authority requires verifier-enforced `CpFieldRelation` checks, especially Poseidon2/BabyBear FS opening, fold root, challenge digest, transcript seed, folded output, Ajtai opening, and original R1CS validity.
- Private shared challenge material may live in full/debug proof data, but must never enter public v2 proofs.

## Typed CP Digest Layer Rules

- Fixed-shape digest bodies are setup data. Do not silently accept variable-length FS messages, openings, fold-input bodies, challenge bodies, or transcript bodies once a typed CP digest layout is generated.
- Exact-byte digest binding must preserve `digest_core` semantics: `"symphony-v2" || len(domain) || domain || len(body) || body`, 3-byte little-endian BabyBear packing, and the final length sentinel.
- Digest correctness is not full CP authority. A Poseidon digest gadget only proves that private bytes hash to public digests; it does not prove those bytes are the correct GR1CS/folding objects until structured reconstruction constraints bind them.
- Keep `public_digest_scheme()` on SHA-256 for WHIR until the full field-native typed CP relation is verifier-enforced.
- Structured digest body reconstruction must preserve exact byte semantics, including signed `i64::to_le_bytes()` for CP commitment and public-input coordinates. Do not replace this with unsigned field packing unless the public proof spec changes.
- Private per-round challenge digest outputs may be internal witness variables, but only the aggregate public `challenge_digest` belongs in the public proof boundary.
