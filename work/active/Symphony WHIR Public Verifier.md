---
date: 2026-05-01
description: "Active implementation note for moving Symphony's WHIR backend toward a public-only verifier without weakening typed CP/output authority."
tags:
  - work-note
  - active
  - symphony
  - whir
  - cryptography
status: active
quarter: Q2-2026
---
# Symphony WHIR Public Verifier

Links: [[Symphony]], [[WHIR]], [[Key Decisions]], [[Gotchas]], [[Patterns]], [[rules]], [[North Star]]

## Context

The project North Star is a fully functional Symphony implementation with a real public-only verifier boundary. In code, that boundary is `verify_v2`: public inputs, public Fiat-Shamir commitments/digests, folded output instance, CP proof, and output proof. It must not inspect witness bundles, original witnesses, FS openings, fold inputs, or folded witnesses.

The current validated WHIR path is still the legacy/modular verifier with explicit witness-side checks. `verify_v2` correctly fails closed because WHIR does not yet provide authoritative typed CP, and typed output is not yet authoritative on the real folded-output path.

## Implemented Today

- Added a direct WHIR typed-output proving and verification hook for `FoldedOutputInstance` / `FoldedOutputWitness`.
- Split WHIR output proving into an R1CS assignment projection and a separate transcript instance, so the full typed folded-output instance is bound into Fiat-Shamir.
- Added public-coordinate WHIR openings for output proofs so the committed assignment is explicitly bound to the public R1CS prefix.
- Added focused tests for direct typed WHIR output roundtrip and malformed typed-output rejection.
- Kept `WhirSnark::has_authoritative_typed_output()` false after the real modular WHIR path exposed a mismatch when the flag was temporarily enabled.
- Updated legacy and modular orchestrators so non-authoritative typed-output hooks are ignored. They are only selected when a backend explicitly advertises authority.
- Added a regression test proving a non-authoritative typed-output hook is not selected.

## Current Security Boundary

`verify_v2` remains fail-closed. This is intentional.

A backend flag is not a capability hint; it is a security claim. `has_authoritative_typed_cp()` and `has_authoritative_typed_output()` must only return true when verification of the backend proof enforces the full typed relation. Prover-side validation is useful for honest-prover hygiene but is not soundness.

## Why WHIR Typed Output Is Still Non-Authoritative

The direct typed-output hook validates the typed relation before proving and binds the typed folded-output instance into the transcript. That is not enough for adversarial soundness: a malicious prover cannot be assumed to call the honest `prove_typed_output` helper. The verifier must be convinced by the proof itself that the typed folded-output relation is satisfied.

The next output milestone is to align the actual WHIR output proof relation with the typed folded-output semantics, not merely transcript-bind typed bytes.

## CP Blocker

The larger blocker is typed CP authority. Current WHIR CP-R1CS proves the algebraic folding constraints, but not the full `CpRelation::check_with_algebra` relation:

- transcript reconstruction
- FS commitment/opening/message consistency
- fold root and challenge digest binding
- folded-output consistency
- original witness commitment validity
- original R1CS witness validity
- folded witness recomputation

Until those checks are proved inside the backend proof, `has_authoritative_typed_cp()` must stay false.

## Verification Run

```text
cargo test --features whir
cargo test --features whir snark::whir
cargo test --features whir typed_output
cargo test --features whir verify_v2
cargo test --features whir modular_whir_backend::end_to_end -- --ignored
cargo bench --bench whir_scaling --features whir --no-run
```

All relevant runs passed after keeping WHIR typed output non-authoritative and preserving fail-closed `verify_v2` behavior.

## Next Steps

1. Specify the authoritative typed-output relation as a verifier-enforced proof relation.
2. Decide whether WHIR should prove typed output directly or remain a low-degree/evaluation backend under a separate typed relation layer.
3. Design a SNARK-friendly typed CP relation. Avoid proving SHA-256 inside WHIR if a Poseidon2/BabyBear transcript can be made canonical.
4. Implement typed CP only after the relation is explicit enough to test adversarial bypasses.
5. Add `public_verify_v2_vs_k` only after typed CP and typed output are both authoritative.

## 2026-05-01 Update — Public Proof Spec Frozen

The public proof boundary is now explicit in code and documentation:

- Added `docs/public_proof_v2.md` as the canonical public verifier spec.
- Added product-facing aliases:
  - `PublicProofBundle` for modular proofs.
  - `PublicSymphonyProof` for legacy/single-backend proofs.
- Added `prove_public` / `verify_public` aliases on both prover/verifier APIs.
- Kept `prove_v2` / `verify_v2` as compatibility names.
- Added `public_boundary_is_well_formed` helpers for backend-independent digest checks.
- Added helpers to reconstruct the typed CP public instance from the public proof object.
- Updated README and crate spec to point to the frozen public proof boundary.

This does not make WHIR public verification pass yet. It makes the intended product boundary explicit and test-covered while preserving fail-closed behavior until typed CP and typed output are truly authoritative.

Verification run:

```text
cargo test --features whir
```

Result: passed.


## 2026-05-01 Update — Typed Output Authority Promoted

Implemented the first security milestone from the public verifier plan: WHIR typed output is now authoritative for the final folded R1CS statement. The verifier proof binds the full `FoldedOutputInstance` into the transcript and checks the public folded R1CS prefix against the committed assignment.

This is intentionally narrower than CP authority. The CP backend still owns the stronger statement that the folded output was derived correctly from original statements, FS commitments, fold inputs, challenges, and original witness algebra. `verify_public` / `verify_v2` therefore still fail closed for WHIR because `has_authoritative_typed_cp()` remains false.

Added field-native public digest scaffolding for the WHIR/PQ CP milestone: `PublicDigestScheme::Poseidon2BabyBear` serializes eight BabyBear limbs as 32 bytes. The default public proof digest scheme remains SHA-256 until typed CP is authoritative.

Verification run this session:

```text
cargo test --features whir digest_core --lib
cargo test --features whir typed_output --lib
cargo test --features whir public_verify_fails_closed_when_only_output_is_authoritative
cargo test --features whir v2_
```

## 2026-05-01 Update — Typed CP Field Relation Staged

Implemented the next staged CP milestone without flipping public WHIR authority:

- `CpPublicStatement` is now the typed CP API boundary. It carries the compact CP digests plus public inputs, R1CS dimensions, folded output, and the selected public digest scheme.
- `CpPublicInstance` remains the legacy compact digest object for compatibility and full-verifier internals.
- Added scheme-aware CP bindings. SHA-256 remains the compatibility/default scheme; WHIR-target typed CP can use Poseidon2/BabyBear commitments and public digests.
- Added `CpFieldRelation` as the software source of truth for typed CP. It checks public/R1CS metadata binding, FS opening/message consistency, GR1CS message reconstruction, fold-root/challenge/transcript digest binding, folded-output consistency, original Ajtai witness opening validity, and original R1CS witness validity.
- Public proof construction now uses the CP backend digest scheme when deriving FS commitments and public digests.

Security status: WHIR typed CP is still not authoritative. `has_authoritative_typed_cp()` must remain false until WHIR verification enforces every security-relevant `CpFieldRelation` check inside the proof. `verify_public` / `verify_v2` therefore remain fail-closed for WHIR, which is the correct boundary at this stage.

Verification added/targeted this session:

```text
cargo test --features whir typed_cp
cargo test --features whir cp_field_relation
cargo test --features whir verify_public
```


## 2026-05-01 Update — Typed CP Authority Prerequisites

Implemented the next safe prerequisite for authoritative WHIR typed CP:

- Added `TypedCpSetupDescriptor` as the backend setup shape for future typed CP relations that depend on original R1CS matrices and Ajtai parameters, not only global CP dimensions.
- Added a `serialize_typed_cp_context` backend hook. It defaults to `None`; returning a context is not itself an authority claim.
- Extended private `CpWitnessBundle` / legacy `ProofWitnessData` with shared Hadamard challenge material so typed CP proving can reconstruct CP-R1CS witnesses from typed inputs. This remains witness-side data and is not present in public v2 proofs.
- Added a WHIR typed CP proving/verifying hook over the existing CP-R1CS core. It binds `CpPublicStatement` into the WHIR transcript, but it is deliberately non-authoritative.

Security status: `has_authoritative_typed_cp()` remains false and WHIR public verification remains fail-closed. The new hook is scaffolding; it does not prove the Poseidon2/BabyBear digest/opening checks from `CpFieldRelation` inside WHIR.

Verification run:

```text
cargo test --features whir typed_cp
cargo test --features whir cp_field_relation
cargo test --features whir verify_public
cargo test --features whir
cargo test
cargo bench --bench whir_scaling --features whir --no-run
```

All passed. The `public_verify_v2_vs_k` benchmark is still intentionally absent until typed CP authority is real.

## 2026-05-01 Update — Typed Routing Tightened

Finished a routing hardening pass after inspecting the current codebase:

- Both the modular orchestrator and the single-backend `SymphonyProver` / `SymphonyVerifier` now cache setup keys for backend-provided typed CP relation descriptions.
- If `has_authoritative_typed_cp()` is true, proving and verification must use the typed CP relation and fail closed if the backend does not provide it.
- If `has_authoritative_typed_cp()` is false, the orchestrators stay on the legacy CP proof path and deliberately ignore typed CP helper hooks.
- Added regression tests for modular and legacy/single-backend routing to prove non-authoritative typed CP hooks are not selected.
- Re-ran the full WHIR suite.

Security status is unchanged in the important way: WHIR typed CP is still non-authoritative. The partial WHIR arithmetization now covers Poseidon2/BabyBear digest gadget tests, Ajtai opening validity, original R1CS validity, and partial composition with the CP-R1CS core. The missing production-grade layer is still the in-circuit binding of FS openings/messages, GR1CS message reconstruction, fold-root/challenge derivation, transcript seed, and folded output derivation.

Verification run:

```text
cargo test --features whir non_authoritative_typed_cp -- --nocapture
cargo test --features whir
```

Both passed. Do not add `public_verify_v2_vs_k` or flip WHIR to `Poseidon2BabyBear` public digests until the remaining `CpFieldRelation` checks are verifier-enforced inside WHIR.

## 2026-05-02 Update — Typed CP Arithmetization Slice

Started the authoritative typed CP milestone, but did not flip authority:

- Added a private-input Poseidon2/BabyBear digest R1CS primitive. This is the circuit shape needed for CP digests: public digest output, private absorbed body.
- Added tests showing the private digest gadget accepts honest witnesses and rejects tampered private input or public digest.
- Added a statement-level typed CP R1CS wrapper that exposes original public inputs as public coordinates and constrains the CP core's private `x_in` variables to match them exactly.
- Added a test showing public input replay/tampering is rejected by this statement-level wrapper.

Security status: still not production-grade public WHIR CP. The missing work remains connecting private GR1CS/fold byte bodies to structured CP core variables, recomputing Poseidon roots/digests over those bodies, and binding `beta`/folded output derivation to the public statement. `has_authoritative_typed_cp()` must remain false.

Verification run:

```text
cargo test --features whir poseidon2_private_digest -- --nocapture
cargo test --features whir typed_cp_statement -- --nocapture
cargo check --features whir
```

## 2026-05-02 Update — Canonical Typed CP Digest Binding Layer

Implemented the next fixed-shape typed CP checkpoint without flipping WHIR CP authority:

- Added canonical Poseidon2/BabyBear body encoders for FS commitments, FS root, fold root, challenge digest, transcript seed, and per-round challenge bodies.
- Added `TypedCpDigestR1csLayout`, which composes the typed CP statement wrapper with private-input Poseidon digest gadgets.
- Public digest coordinates are now circuit-addressable as eight BabyBear limbs for each FS commitment plus `fs_root`, `fold_root`, `challenge_digest`, and `transcript_seed_digest`.
- The same layer also carries the public inputs and folded CP instance coordinates from the statement wrapper.
- Private witness data carries FS messages/openings, fold-input bodies, challenge bodies, and Poseidon auxiliary values.
- The digest witness encoder rejects bodies whose BabyBear absorption length differs from the setup-derived fixed layout.
- Added tests for honest digest-layer satisfaction, tampered private digest input/opening, wrong public digest coordinates, public input replay, and non-canonical body lengths.

Security status: WHIR typed CP is still non-authoritative. This milestone proves digest correctness for fixed bodies, but not yet that those bodies are the structured GR1CS/folding bodies required by `CpFieldRelation`. The next step is binding digest bodies to GR1CS message reconstruction, fold input reconstruction, `beta`, challenge derivation, and folded-output derivation.

## 2026-05-02 Update — Structured Digest Body Reconstruction Tightened

Continued the WHIR typed CP authority plan without flipping public authority:

- Bound the Hadamard prefix of `encode_gr1cs_round_message` to existing CP-R1CS Hadamard columns: round count, per-round evaluation count, sumcheck evaluations, and evaluation-matrix values.
- Fixed signed `i64` byte binding so the sign correction uses the high bit of byte 7, not byte 0.
- Added canonical in-circuit checks for FS commitment message length prefixes, `fs_root` count/length prefixes, `fold_root` count and per-entry lengths, `challenge_digest` count/length prefixes, and `transcript_seed` public-input/R1CS metadata.
- Bound static canonical transcript bytes for per-round `challenge` Poseidon bodies while leaving public-input and FS-commitment payloads tied to their structured public coordinates.
- Kept `WhirSnark::has_authoritative_typed_cp()` false and `WhirSnark::public_digest_scheme()` on SHA-256.

Security status: this is still a checkpoint, not production public WHIR CP. Remaining work is range-proof serialization reconstruction, challenge-to-`beta` binding, folded-output derivation, and then replacing WHIR's non-authoritative typed CP relation with the full typed CP R1CS.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
```

## 2026-05-02 Update — Monomial Commitment Openings

Continued Milestone 1 from [[rules]] and the WHIR typed CP authority plan:

- Added deterministic verifier-reconstructable Ajtai parameters for range-proof monomial commitments via `AjtaiParams::setup_deterministic(..., b"range-proof-monomial")`.
- Switched range-proof monomial commitments to that deterministic matrix so typed CP can reproduce the commitment relation.
- Added typed CP R1CS constraints proving each structured monomial commitment opens to the structured monomial vector, with q-wrap witnesses for BabyBear embedding.
- Kept the existing local monomial-vector constraints: coefficient squares, at-most-one nonzero coefficient per ring element, and `projected_values` reconstruction with `d_prime = D - 2`.
- Extended `CpSharedChallengeData` with monomial sumcheck seed/challenge material so the next R1CS block can address monomial verifier equations.

Security status is unchanged: WHIR typed CP remains non-authoritative, `WhirSnark::public_digest_scheme()` remains SHA-256, and `verify_public` remains fail-closed for WHIR. Remaining range blockers are monomial sumcheck/evaluation consistency and square-evaluation consistency.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
```

## 2026-05-02 Update — Full Range-Proof Payload Byte Binding

Finished the byte-binding part of Milestone 1 for range-proof serialization:

- Added structured private columns for monomial commitments, monomial vectors,
  monomial sumcheck evaluations, monomial evaluation tensors, square
  evaluations, and `projected_values`.
- Constrained each payload section's canonical `encode_gr1cs_round_message`
  bytes to match those structured columns with signed `i64` byte semantics.
- Extended the typed CP digest witness encoder to populate all range-proof
  payload variables from private GR1CS proof data.
- Extended the negative test so tampering any structured range payload variable
  or any serialized range payload byte rejects.

Security status is still non-authoritative. This proves that the digest body
bytes are no longer arbitrary for those range-proof payloads, but it does not
yet prove the semantic range relation: monomial commitment openings, monomiality,
monomial sumcheck consistency, square-evaluation consistency, or
projected-value decomposition/reconstruction. `verify_public` remains
fail-closed for WHIR.

Verification run:

```text
cargo test --features whir typed_cp_digest_r1cs_binds_range_message_shape_prefixes -- --nocapture
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir verify_public -- --nocapture
```

## 2026-05-02 Update — Local Range Semantics

Added the first semantic constraints over the structured range-proof payload
variables:

- Monomial-vector coefficients now have square witness variables constrained as
  `square = coeff * coeff`.
- Each structured monomial ring element constrains the sum of coefficient
  squares to be boolean, so the element has at most one nonzero coefficient and
  each coefficient is in `{0, -1, 1}`.
- `projected_values` are reconstructed from the monomial-vector decomposition
  digits using the table-polynomial constant-term weights and `d_prime = D - 2`.
- The synthetic range fixture now uses monomial vectors whose decomposition
  reconstructs the projected values, so the typed CP digest R1CS checks this
  path directly.

Security status remains non-authoritative. The current code still cannot
honestly claim monomial commitment opening validity or monomial
sumcheck/square-evaluation consistency because the typed CP setup does not yet
carry the per-proof monomial Ajtai parameters, and the private GR1CS proof
message does not expose the monomial verifier challenges needed to replay the
sumcheck verifier inside R1CS. `verify_public` remains fail-closed.

Verification run:

```text
cargo test --features whir typed_cp_digest_r1cs_binds_range_message_shape_prefixes -- --nocapture
cargo test --features whir typed_cp_digest -- --nocapture
```

## 2026-05-02 Update — Range-Proof Shape Prefix Binding

Continued Milestone 1 of the WHIR typed CP authority plan:

- Extended the typed CP digest setup shape with parsed GR1CS message structure.
- For GR1CS messages backed by private proof data, the circuit now constrains the canonical range-proof count/length prefixes:
  - monomial commitment count and commitment element lengths;
  - monomial vector count and vector lengths;
  - monomial sumcheck round count and per-round evaluation counts;
  - monomial evaluation tensor count;
  - square-evaluation count;
  - projected-value count.
- Added a synthetic range-shape fixture and negative test proving tampered range-proof section prefixes reject.

Security status: still non-authoritative. This fixes section boundaries and prevents a class of arbitrary byte-shape drift, but the range-proof payload bytes are not yet semantically tied to structured monomial/range variables. Challenge-to-`beta` and folded-output derivation are also still open.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir verify_public -- --nocapture
```

## 2026-05-02 Update — Structured CP Digest Body Reconstruction

Extended the typed CP digest layer from arbitrary private digest bodies to structured byte reconstruction while keeping WHIR typed CP non-authoritative:

- FS commitment message bytes are now tied to the structured GR1CS message bytes carried through the fold-root body.
- Fold-root commitment bytes are constrained against the CP-core commitment columns, including signed `i64::to_le_bytes()` semantics for centered coefficients.
- Fold-root and transcript-seed public input bytes are constrained against the typed CP public statement coordinates.
- Per-round private `challenge` Poseidon blocks now reconstruct their transcript bytes from public inputs, R1CS metadata, and public FS commitments.
- `challenge_digest` body bytes are constrained against those per-round challenge digest outputs.
- Added regression tests for tampered FS message bytes, fold-root commitment/public-input bytes, transcript-seed bytes, challenge transcript bytes, and challenge output bytes.

Security status is unchanged: this is still not full typed CP authority. Range-proof serialization is bound as bytes but not semantically proven, and the circuit still needs challenge-to-`beta` binding plus folded-output derivation before WHIR can switch to Poseidon2/BabyBear public digests or set `has_authoritative_typed_cp()` true.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
cargo test --features whir
```

All passed. `verify_public` still fails closed for WHIR, as intended.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir
```

## 2026-05-02 Update — Range-Proof Projected-Value Payload Binding

Continued Milestone 1 from [[rules]] and the WHIR typed CP authority plan:

- Added structured private columns for the range-proof `projected_values`
  payload in typed CP digest R1CS.
- Constrained the canonical serialized `projected_values` bytes inside
  `encode_gr1cs_round_message` to match those structured private columns.
- Extended the digest witness encoder so honest witnesses populate the new
  projected-value payload variables from private GR1CS proof data.
- Added a negative test proving the structured projected-value variable and the
  serialized message byte cannot diverge.

Security status is unchanged: WHIR typed CP is still non-authoritative,
`WhirSnark::public_digest_scheme()` remains SHA-256, and `verify_public`
continues to fail closed for WHIR. The next range-proof payload work is binding
monomial commitments, monomial vectors, monomial sumcheck evaluations, monomial
evaluation tensors, and square evaluations to structured variables, then adding
semantic projection/decomposition constraints.

Verification run:

```text
cargo test --features whir typed_cp_digest_r1cs_binds_range_message_shape_prefixes -- --nocapture
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
```

## 2026-05-02 Update — Exact-Byte Digest Body Binding

Extended the typed CP digest layer to bind private digest bodies byte-for-byte to the same Poseidon2/BabyBear absorption semantics used by `digest_core`:

- Each digest block now carries private body bytes and 8 boolean bit variables per byte.
- The R1CS constrains every body byte to its bit decomposition, then constrains every private Poseidon input limb to the exact `"symphony-v2" || len(domain) || domain || len(body) || body` packing with the final length sentinel.
- FS root body bytes are additionally tied to the verifier-visible FS commitment limbs, so the root body cannot drift from the public commitment list.
- Added tests for honest body packing, tampered body bytes, invalid byte/bit witnesses, length sentinel tampering, and tampered root/challenge/transcript body bytes.

Security status: still non-authoritative typed CP. This proves exact digest-body bytes are what the Poseidon gadgets absorb, and it binds FS root bytes to public FS commitments. The remaining authority work is semantic reconstruction: GR1CS message bytes from structured proof variables, fold inputs from commitments/public inputs/GR1CS messages, challenge derivation body construction, `beta` binding, and folded-output derivation.

Verification run:

```text
cargo test --features whir typed_cp_digest -- --nocapture
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
```

## 2026-05-02 Update — Monomial Sumcheck Semantics

Implemented the next typed CP range-proof semantic block without flipping WHIR authority:

- Encoded monomial sumcheck seed and round challenge variables into the typed CP R1CS witness layout.
- Added verifier-equation constraints for the monomial sumcheck: degree-4 round consistency, challenge evaluation, final claim equality, coefficient cubic checks, and square-evaluation boolean consistency.
- Fixed the witness encoder to track raw extension-field linear combinations when computing q-wraps, so nontrivial monomial challenges satisfy the BabyBear R1CS exactly while still enforcing inner q arithmetic.
- Updated the range fixture to use a real monomial prover output under nonzero challenges and added negative tests for tampered monomial seed, challenge, alpha, sumcheck evaluations, monomial evaluations, square evaluations, multiplication auxiliaries, and q-wraps.

Security status: WHIR typed CP remains non-authoritative. The remaining Milestone 1 gap is binding monomial and square evaluation claims back to the structured monomial-vector multilinear extensions at the sumcheck output point. Challenge-to-beta binding and folded-output derivation are still later milestones. `verify_public` remains expected to fail closed for WHIR.

Verification run so far:

```text
cargo test --features whir typed_cp_digest -- --nocapture
```

Result: passed.

Follow-up verification completed:

```text
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
cargo test --features whir
cargo test
```

Result: all passed.

## 2026-05-02 Update — Monomial Evaluation MLE Binding

Finished the remaining Milestone 1 semantic gap for the current fixed-shape typed CP range payload:

- Added typed CP R1CS folding constraints that evaluate each structured monomial-vector coefficient table at the monomial sumcheck output point.
- Bound each claimed monomial evaluation tensor column to that structured multilinear evaluation.
- Added the same binding for square-evaluation claims against the structured square tables.
- Extended the monomial semantic witness encoder with the fold auxiliary values and q-wraps needed for those MLE checks.
- Added targeted negatives for the new evaluation-binding aux/wrap region.

Security status: WHIR typed CP remains non-authoritative. Milestone 1 is implemented for this fixed-shape payload; the next source-of-truth milestone is challenge-to-beta binding. `verify_public` is still expected to fail closed for WHIR.

Verification run so far:

```text
cargo test --features whir typed_cp_digest -- --nocapture
```

Result: passed.

Follow-up verification completed:

```text
cargo test --features whir typed_cp -- --nocapture
cargo test --features whir poseidon -- --nocapture
cargo test --features whir verify_public -- --nocapture
cargo test --features whir
cargo test
git diff --check
```

Result: all passed. Authority flags and public benchmark guardrails remain unchanged.
