---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/veil.pdf
authors:
  - Rahul Dalal
  - Tamir Hemo
  - Eugene Rabinovich
  - Ron D. Rothblum
year: 2026
tags:
  - zero-knowledge
  - compiler
  - multilinear
  - hash-based
  - proof-systems
related:
  - "[[VEIL]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Polynomial Commitments]]"
  - "[[Multilinear Interactive Oracle Proofs (MIOPs)]]"
  - "[[Commit-and-Prove SNARKs]]"
  - "[[WHIR]]"
  - "[[Spartan]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Lightweight compiler for adding zero knowledge to hash-based multilinear proof systems"
---

# VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems

## Summary

VEIL introduces a **lightweight compiler for adding zero knowledge** to a broad class of **hash-based multilinear proof systems**.

Its goal is not to redesign a proof system from scratch to be zero knowledge, nor to wrap the entire verifier inside an expensive recursive zk proof. Instead, VEIL tries to add zero knowledge in a way that is:
- **non-intrusive**,
- **maintainable**,
- and **low-overhead** in practice
(Abstract, p. 1; Introduction, pp. 3–4).

The paper's core principle is to **decouple algebraic interaction from cryptographic hashing**:
- protect trace queries using zk-code style padding,
- blind the final proximity test with an extra random column,
- and apply a lightweight zk wrapper only to the small algebraic transcript rather than to all Merkle/hash logic
(Abstract, p. 1; Section 1.2, pp. 4–5).

In the current wiki, VEIL is best read as a **compiler / wrapper paper** for the multilinear transparent-proof branch rather than as a new base proof system.

## Key Claims

- VEIL is a lightweight compiler for suitable **hash-based multilinear proof systems** (Abstract, p. 1; Section 1.1, p. 3).
- It avoids the heavy alternative of proving verifier hash computations inside recursive zk circuits (pp. 3–4).
- It also avoids the engineering burden of manually making every subprotocol natively zero knowledge (pp. 3–4).
- The compiler targets roughly **$(1+o(1))$ multiplicative prover overhead** rather than only asymptotically tiny additive overheads (Section 1.1, p. 4).
- In the paper's proof-of-concept evaluation over a 31-bit base field and a trace of $2^{29}$ field elements, prover overhead is about **3%**, verifier overhead **22%**, and proof-size overhead **12%** (Abstract, p. 1).
- The paper treats the common multilinear hash-based structure itself as an abstraction worth compiling, not just one concrete protocol (Section 1.1, pp. 3–4).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper identifies a common protocol pattern for multilinear hash-based proof systems (Section 1.1, p. 4):
1. the prover commits to the multilinear extension of the computation trace;
2. prover and verifier execute an interactive phase using only field arithmetic;
3. verification reduces to a multilinear evaluation claim relative to the original commitment.

The paper calls such a protocol a **multilinear interactive PCP**, aligning it with the multilinear interactive oracle-proof abstraction developed later in the preliminaries (Section 1.1, p. 4; Section 2.3, pp. 8–9).

Definition 2.11 recalls an interactive oracle proof (IOP) as a public-coin protocol with completeness and soundness, where the key parameters include query complexity, round complexity, communication complexity, and prover / verifier complexity (pp. 7–8). Definition 2.13 then defines a **Multilinear Interactive Oracle Proof (MIOP)** as an IOP in which:
- prover messages are either field elements or oracle access to multilinear polynomials over $\mathbb{F}^n$,
- verifier messages are random coins,
- and the verifier's decision depends only on polynomial relations among prover messages and multilinear evaluations at public points
(Section 2.3.2, pp. 8–9).

VEIL also relies on **zero-knowledge codes**. Definition 2.1 says an error-correcting code
$$
C : \mathbb{F}^n \times \mathbb{F}^k \to \mathbb{F}^m
$$
is $k$-zero-knowledge if for any set of $k$ queried coordinates and any fixed witness part, the projection of
$$
C(w,r)
$$
onto those queried coordinates is uniformly distributed when $r\in \mathbb{F}^k$ is uniform (p. 6).

This definition formalizes the intuition behind VEIL's trace-query masking step.

## Methods and Proof Techniques

### 1. Structural abstraction of multilinear hash-based systems

VEIL first identifies a recurring architecture shared by many multilinear transparent systems. This is important because the paper is not tied to one proof design; it is a compiler over a recognizable family (Section 1.1, pp. 3–4).

### 2. Query protection via zk-code padding

To protect raw computation-trace queries, each trace column is padded with $q$ random field elements before encoding, where $q$ is the query complexity of the proximity test. The paper explains that this relies on the Reed–Solomon code acting as a zk-code, and that the distance loss from this padding is negligible in the intended regime (Section 1.2, p. 4).

### 3. Proximity-test blinding via an extra random column

To prevent the final proximity test from leaking through the verifier's random linear combination of columns, VEIL appends one extra uniformly random column. The paper notes that if the original matrix has $t$ columns, then this yields multiplicative prover overhead of about
$$
1 + \frac{1}{t},
$$
which is below 1% for a typical $t=2^7$ regime (Section 1.2, pp. 4–5).

### 4. Small inner zk proof for the algebraic transcript

The most implementation-relevant move is that VEIL wraps only the **small algebraic interactive transcript** in a zk proof. If the transcript has $c$ field elements, the prover commits to a random vector
$$
r \in \mathbb{F}^c,
$$
sends masked transcript symbols
$$
\tau_i' = \tau_i + r_i,
$$
and finally proves in zero knowledge that the committed mask opens consistently and that the unmasked transcript satisfies the base verifier's decision predicate (Section 1.2, p. 5).

### 5. Non-intrusive wrapper philosophy

The paper explicitly presents VEIL as a middle ground between full recursive wrapping and deeply invasive native-ZK redesign. This architectural point is one of the paper's main contributions, not just an implementation convenience (pp. 3–5).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The design goal is minimal **multiplicative** overhead on realistic systems:
$$
1 + o(1)
$$
relative to the base non-zk system (Abstract, p. 1; Section 1.1, p. 4).

The paper's reported proof-of-concept implementation results are (Abstract, p. 1):
- over a **31-bit base prime field**,
- for a trace of
  $$
  2^{29}
  $$
  field elements,
- **prover overhead:** about **3%**,
- **verifier overhead:** about **22%**,
- **proof-size overhead:** about **12%**.

The introduction also gives two concrete local-overhead pictures:
- padding each column changes the effective code distance from
  $$
  \delta
  $$
  to
  $$
  \delta - q/n,
  $$
  which the paper argues is negligible in its intended regime (p. 4);
- adding one blinding column introduces multiplicative prover overhead approximately
  $$
  1 + 1/t
  $$
  when the original matrix has $t$ columns (pp. 4–5).

The paper's practical punchline is that one can often avoid the massive cost of recursive verifier proving if the only part requiring zk treatment is the algebraic transcript.

## Why It Matters

VEIL matters because it addresses a recurring engineering problem in transparent proof systems:
> adding zero knowledge often breaks either performance or maintainability.

The paper's answer is to add zero knowledge at the right abstraction boundary. Instead of proving all cryptographic plumbing inside a zk system, it protects the algebraic interactions that actually carry semantic leakage.

In the current wiki, VEIL is important because it complements:
- [[Spartan]] as a native transparent-zk system design,
- [[WHIR]] as a fast proximity/compiler substrate,
- and later recursion/compiler techniques that might otherwise be used to add zk more expensively.

## Connections to the Wiki

VEIL strengthens the wiki's understanding of the **zero-knowledge compiler layer** for transparent multilinear systems. It connects to:
- [[VEIL]]
- [[Transparent zkSNARKs]]
- [[Polynomial Commitments]]
- [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- [[Commit-and-Prove SNARKs]]
- [[WHIR]]
- [[Spartan]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]
- [[SNARKs and STARKs Reading Map]]

## Open Questions / Limitations

- VEIL targets suitable multilinear hash-based systems, so the exact applicability boundary remains important.
- The paper explicitly works with honest-verifier / semi-malicious zero knowledge before Fiat–Shamir-style compilation, which is appropriate for its intended setting but should stay visible (Section 1.1, p. 3).
- The current note now captures the paper's front-matter definitions and quantitative overhead claims, but a future pass could still extract more of the formal compilation theorems from Sections 3–4.
- A future synthesis could compare VEIL directly against fully native zk system design and recursive-wrap approaches.

## Suggested Next Reading

- [[Spartan]]
- [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- [[Transparent zkSNARKs]]
- [[Commit-and-Prove SNARKs]]
- [[WHIR]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## Related
- [[VEIL]]
- [[Transparent zkSNARKs]]
- [[Polynomial Commitments]]
- [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- [[Commit-and-Prove SNARKs]]
- [[WHIR]]
- [[Spartan]]
- [[SNARKs and STARKs Reading Map]]
