---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - snark
  - compiler
  - recursion
related:
  - "[[Symphony]]"
  - "[[High-Arity Folding]]"
  - "[[Fiat-Shamir Transform]]"
description: "Compiler pattern used by Symphony to avoid embedding Fiat–Shamir logic in recursive statements"
---

# Commit-and-Prove SNARKs

## Definition / framing

Commit-and-prove SNARKs are SNARK constructions in which the prover first commits to auxiliary objects and then proves, in a SNARK, that the committed objects satisfy a target relation.

The key benefit is that the proved statement can avoid directly embedding some expensive commitment-opening or transcript-validation logic.

## Why it matters

In *[[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]*, commit-and-prove is the key compiler idea that lets the scheme avoid embedding random-oracle / Fiat–Shamir logic inside the recursive statements themselves.

This is one of Symphony's most important conceptual contributions.

## Key distinctions

- Commit-and-prove is a compiler pattern rather than a single protocol.
- It is especially useful when naively embedding verifier logic into a recursive statement would make the circuit far too large.
- In Symphony, this pattern is used to compress very large folding proofs while avoiding Fiat–Shamir circuits in the application relation.


## Mathematical background / formulae

The basic commit-and-prove pattern is:
$$
c \leftarrow \mathsf{Com}(a;r),
$$
followed by a SNARK proof of a relation of the form
$$
\exists a,r\;:\; c=\mathsf{Com}(a;r) \land R(x,a)=1.
$$
So the verifier checks a succinct proof about the committed auxiliary object rather than directly re-running all commitment logic inside the application relation.

### Formal three-phase interface

A commit-and-prove SNARK splits witness handling into three phases:

1. **Commit phase.** $c_w \leftarrow \mathsf{Com}(w; r)$ — the prover commits to the witness $w$ independently of the statement $x$, using fresh randomness $r$.
2. **Prove phase.** $\pi \leftarrow \mathsf{Prove}(\mathsf{pp}, x, c_w, w, r)$ — the prover shows that the committed witness satisfies the relation: $R(x, w) = 1$ **and** $c_w = \mathsf{Com}(w; r)$.
3. **Verify phase.** $\mathsf{Verify}(\mathsf{pp}, x, c_w, \pi) \to \{0, 1\}$ — the verifier accepts only if both the commitment and the relation hold.

### Why this pattern helps recursion

In standard recursive SNARKs, the verifier circuit of the inner SNARK must be embedded inside the outer SNARK's constraint system. If the inner SNARK uses Fiat–Shamir (hashing the transcript into challenges), the outer circuit must implement the hash function — and modern hash functions (SHA-2, Poseidon, Keccak) add tens to hundreds of thousands of constraints per recursion step.

Commit-and-prove avoids this cost:

- The inner prover commits to its witness **outside** the recursive circuit.
- The outer circuit only checks the commitment opening (typically algebraic or low-depth), rather than recomputing Fiat–Shamir hashes.

The recursive circuit size drops from
$$
O(|H|) \quad \text{(hash circuit for Fiat–Shamir)}
$$
to
$$
O(|\mathsf{Com.Verify}|) \quad \text{(commitment verification)},
$$
which is often one or two orders of magnitude smaller.

### Worked example

Suppose the inner SNARK proves the statement: *"I know $w$ such that $H(w) = y$"* for some hash $y$.

- **Without commit-and-prove.** The outer recursive circuit must embed the full hash function $H$ to re-derive the Fiat–Shamir challenges of the inner proof. For Poseidon this is maybe $10^3$–$10^4$ constraints; for SHA-256, more like $10^5$.
- **With commit-and-prove.** The inner prover commits $c_w = \mathsf{Com}(w; r)$ using an algebraic commitment (e.g., Pedersen). The recursive circuit only checks $\mathsf{Com.Open}(c_w, w, r) = 1$, which is a handful of scalar multiplications — maybe $10^2$ constraints.

This is exactly the architectural lever Symphony pulls to make high-arity lattice folding practical: the recursive statement never has to re-hash the transcript.

## Evidence / sources

- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]

## Related entities

- [[Symphony]]
- [[Binyi Chen]]

## Open questions

- Which other papers in the corpus use commit-and-prove as a first-class design pattern rather than a local implementation trick?

## Wiki development

- How should this page connect to general compiler patterns like BCS and Fiat–Shamir?
