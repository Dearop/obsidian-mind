---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - preprocessing
  - commitments
related:
  - "[[Spartan]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Polynomial Commitments]]"
description: "Spartan's public-preprocessing primitive for amortized sub-linear verification"
---

# Computation Commitments

## Definition / framing

In the framing of [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]], computation commitments are a primitive that lets a verifier preprocess the structure of a computation into a succinct commitment, then later verify proofs more cheaply.

## Why it matters

This is one of Spartan's core conceptual contributions.

The important distinction is that computation commitments aim to recover some of the amortization benefits often associated with setup-heavy systems, but without introducing a secret trapdoor. That makes them a bridge concept between:
- trusted-setup succinct arguments,
- transparent systems,
- and verifier preprocessing.

## Key distinctions

- They are **not** the same thing as a trusted setup ceremony.
- They are public and amortizable over future proofs with shared structure.
- In Spartan, they help make verifier costs sub-linear for arbitrary R1CS instances after an offline preprocessing phase.


## Mathematical background / formulae

A computation commitment can be thought of abstractly as
$$
cc \leftarrow \mathsf{Commit}(C),
$$
where $C$ describes the fixed computation structure. Later proofs target instance-specific claims such as
$$
\exists w\;:\; C(x,w)=1,
$$
while reusing the same committed computation structure $cc$.
This separates the amortizable structural part of the statement from the per-instance witness relation.

### Formal interface

A computation commitment scheme for a family of relations $\{R_C\}$ consists of three algorithms:

- $\mathsf{Commit}(\mathsf{pp}, C) \to cc$: in an offline phase, commit to a circuit or constraint system $C$, producing a short digest $cc$.
- $\mathsf{Prove}(cc, x, w) \to \pi$: in an online phase, prove that $R_C(x, w) = 1$ using the preprocessed commitment.
- $\mathsf{Verify}(cc, x, \pi) \to \{0, 1\}$: verify the proof in time sublinear in $|C|$.

### Binding property

Once $cc$ is computed, a malicious prover cannot silently switch to a different circuit $C' \neq C$:
$$
\Pr\bigl[\mathsf{Verify}(cc, x, \pi) = 1 \;\wedge\; cc = \mathsf{Commit}(\mathsf{pp}, C') \text{ for some } C' \neq C\bigr] \leq \mathsf{negl}(\lambda).
$$
This is the analogue of the binding property for a value-level commitment scheme, lifted to the circuit level.

### Amortization advantage

The offline cost $T_{\mathsf{Commit}} = O(|C|)$ is paid **once**. For each subsequent proof against the same $C$:

| Scheme | $T_{\mathsf{Verify}}$ per proof |
|--------|-------------------------------|
| No computation commitment | $O(|C|)$ (verifier re-reads $C$) |
| Spartan | $O(\sqrt{|C|})$ |
| Generic holographic / preprocessing | $O(\mathsf{polylog}(|C|))$ |

### Worked example

Suppose $C$ is an R1CS instance with $n = 10^6$ constraints. Without a computation commitment, the verifier must inspect all $10^6$ entries of the constraint matrices on every proof. With Spartan's computation commitment, the verifier pays $O(10^6)$ once at setup and then only $O(10^3) = O(\sqrt{n})$ per subsequent proof — three orders of magnitude faster per instance.

Critically, this amortization is obtained **without** a trusted trapdoor: the commitment is a hash-based succinct digest, not a pairing-based structured reference string.

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related entities

- [[Spartan]]

## Open questions

- Which later systems reuse this exact framing explicitly, versus implementing the same idea under a different name?

## Wiki development

- How should this concept be compared with preprocessing in Fractal, SuperSonic, and setup in Groth16-like systems?
