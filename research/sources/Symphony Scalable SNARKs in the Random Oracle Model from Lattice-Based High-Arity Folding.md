---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/Symphony.pdf
authors:
  - Binyi Chen
year: 2025
tags:
  - folding
  - snark
  - post-quantum
  - random-oracle-model
  - lattice
  - recursion
related:
  - "[[Symphony]]"
  - "[[Folding Schemes]]"
  - "[[High-Arity Folding]]"
  - "[[Commit-and-Prove SNARKs]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Quasar]]"
  - "[[WARP]]"
  - "[[Accumulation vs Folding in Recursive Proof Systems]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Folding-based SNARK anchor built around high-arity lattice folding and commit-and-prove compilation"
---

# Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding

## Summary

Symphony argues that many existing folding-based SNARKs pay too much overhead because they:
- use low folding arity,
- rely on deep recursive folding trees,
- and embed random-oracle / hash logic inside the proved statement
(Abstract, p. 1; Introduction, pp. 3–4).

The paper proposes a different route:
- **high-arity folding**,
- plus a **commit-and-prove SNARK compiler**,
- designed so that the folding verifier and Fiat–Shamir logic do not need to be embedded inside recursive SNARK circuits
(Abstract, p. 1; Section 1.1, pp. 4–5).

Its headline claim is that Symphony is the **first folding-based SNARK that avoids embedding hashes in SNARK circuits**. It is also framed as memory-efficient, parallelizable, streaming-friendly, and plausibly post-quantum via lattice-based ingredients (Abstract, p. 1).

## Key Claims

- Symphony introduces a **lattice-based high-arity folding scheme** for compressing many NP-complete statements at once (Abstract, p. 1; Section 1.1, p. 4).
- It introduces a generic compiler from folding schemes to SNARKs in the random oracle model (Abstract, p. 1; pp. 4–5).
- It avoids embedding Fiat–Shamir / random-oracle logic inside the proved statement (Abstract, p. 1; pp. 3–4).
- It is presented as the first folding-based SNARK with this property (Abstract, p. 1).
- The paper emphasizes high-arity folding as a way to reduce depth and improve scalability in recursive settings (pp. 3–5).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The core new cryptographic primitive is a **lattice-based high-arity folding scheme** that compresses a large number of NP-complete statements into one in a single shot (Abstract, p. 1; Section 1.1, p. 4).

The introduction states that Symphony supports efficient proof generation for approximately
$$
2^{16}
$$
standard R1CS statements over a 64-bit field, each with over
$$
2^{16}
$$
constraints, with expected resulting proofs under **200KB** (and under **50KB** without post-quantum security), verification in **tens of milliseconds**, and prover cost dominated by about
$$
3\cdot 2^{32}
$$
multiplications between arbitrary elements and low-norm elements over the ring
$$
R_q := \mathbb{Z}_q[X]/\langle X^{64}+1\rangle
$$
(Section 1.1, p. 4).

The introduction also describes the compiler structure informally: from a folding protocol $\Pi_{fold}$ and commitment scheme $\Pi_{cm}$, the paper constructs a non-interactive scheme via Fiat–Shamir and then a SNARK layer using a **commit-and-prove SNARK** that proves correctness of the folding proof *without embedding the Fiat–Shamir circuit in the statement itself* (Section 1.2, pp. 6–7).

The paper further states that the high-arity folding prover is dominated by computing the input witness commitments, while the verifier is mainly combining commitments using a random vector derived from Fiat–Shamir (Section 1.2, pp. 5–6).

## Methods and Proof Techniques

### 1. High-arity folding

The paper's most distinctive move is to increase folding arity, reducing the depth of folding trees and changing the systems tradeoff surface. Rather than repeatedly folding only 2 or 3 instances, Symphony compresses many statements in a single shot (Abstract, p. 1; pp. 4–5).

### 2. Lattice-based commitment / low-norm structure

Because the instantiation is lattice-based, witness and commitment objects must satisfy low-norm constraints. The paper therefore develops supporting machinery including random projection and monomial-embedding-style range-proof ideas to make the high-arity lattice folding practical (Section 1.2, pp. 5–6).

### 3. Commit-and-prove compiler

A central contribution is the compiler from folding schemes to SNARKs in the ROM. Rather than embedding the full folding verifier and Fiat–Shamir logic into the recursive statement, the system proves correctness of the folding proof externally via a commit-and-prove layer (Abstract, p. 1; Section 1.2, pp. 6–7).

### 4. Separation of folding logic from application logic

The compiler is designed so that each input statement depends only on the application relation, not on the internal folding verifier. This is the main conceptual reason Symphony avoids the standard “hashes inside SNARK circuits” problem (pp. 6–7).

### 5. Higher-depth support via two-layer folding

The paper further extends the framework to support higher effective folding depth through a two-layer splitting technique, rather than relying solely on a single monolithic fold (Contents; Section 8 in the roadmap, p. 2).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The introduction-level performance profile is:

- **Proof size:** under roughly **200KB** in the candidate post-quantum instantiation, and under **50KB** without post-quantum security (p. 4).
- **Verification:** **tens of milliseconds** (p. 4).
- **Scale:** supports about
  $$
  2^{16}
  $$
  R1CS statements, each with over
  $$
  2^{16}
  $$
  constraints (p. 4).
- **Prover bottleneck:** dominated by witness commitments, about
  $$
  3\cdot 2^{32}
  $$
  ring multiplications in the stated candidate regime (p. 4).

The abstract additionally characterizes the system qualitatively as having:
- **polylogarithmic proof size and verification**,
- a prover dominated by committing to the input witnesses,
- memory efficiency,
- parallelizability,
- and streaming friendliness (Abstract, p. 1).

For the current wiki, the main efficiency story is that Symphony tries to recover the best qualitative benefits of folding — streaming and memory friendliness — without paying the usual recursive-hash overhead.

## Why It Matters

Symphony matters because it rethinks a standard assumption in folding-based SNARK design: that one must embed the Fiat–Shamir / hash machinery inside recursive circuits.

By attacking that assumption directly, it opens a different route to scalable folding-based proof systems, especially in settings where:
- post-quantum security matters,
- memory efficiency matters,
- and very large batches of uniform statements are available.

In the current wiki, it is especially useful as a counterpoint to accumulation-based recursion systems like [[WARP]] and [[Quasar]], and as a major representative of the **high-arity folding** branch.

## Connections to the Wiki

This paper strongly connects:
- [[Symphony]]
- [[Folding Schemes]]
- [[High-Arity Folding]]
- [[Commit-and-Prove SNARKs]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[Quasar]]
- [[WARP]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
- [[SNARKs and STARKs Reading Map]]

It should often be read as the high-arity folding counterpart to accumulation-centered recursion papers.

## Open Questions / Limitations

- The current note now captures the front-matter theorem claims and compiler picture, but a deeper pass could still extract more precise formal theorem statements from Sections 4–8.
- The concrete instantiation is promising but still candidate-level, so the paper should be read as both a conceptual framework and an early systems argument.
- A useful future synthesis would compare Symphony's high-arity folding and commit-and-prove route directly against multi-instance accumulation and general-code accumulation schemes.

## Suggested Next Reading

- [[Folding Schemes]]
- [[High-Arity Folding]]
- [[Commit-and-Prove SNARKs]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
- [[WARP Linear-Time Accumulation Schemes]]
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]

## Related
- [[Symphony]]
- [[Folding Schemes]]
- [[High-Arity Folding]]
- [[Commit-and-Prove SNARKs]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[Quasar]]
- [[WARP]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
- [[SNARKs and STARKs Reading Map]]
