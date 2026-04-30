---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/Spartan.pdf
authors:
  - Srinath Setty
year: 2019
tags:
  - zksnark
  - transparent
  - r1cs
  - polynomial-commitments
  - sum-check
related:
  - "[[Spartan]]"
  - "[[Srinath Setty]]"
  - "[[zkSNARKs]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[Polynomial Commitments]]"
  - "[[Computation Commitments]]"
  - "[[SPARK]]"
  - "[[Sum-check Protocol]]"
  - "[[Fiat-Shamir Transform]]"
  - "[[Research Agenda]]"
description: "Foundational source page for transparent zkSNARKs over arbitrary R1CS with sub-linear verification"
---

# Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup

## Summary

Spartan presents a family of zkSNARKs for [[Rank-1 Constraint Satisfiability (R1CS)]] that aims to close an important design gap in proof systems:
- support **arbitrary NP statements** via R1CS,
- avoid a toxic-waste trusted setup,
- retain **sub-linear verification**,
- and in attractive variants achieve **time-optimal or near-time-optimal proving**
(Abstract, p. 1; Introduction, pp. 1–3).

The paper's core architecture is best read as a modern systems assembly of older ingredients:
- encode R1CS as low-degree algebra over the Boolean hypercube,
- use the [[Sum-check Protocol]] as the interactive backbone,
- reduce verification to a small number of polynomial evaluation claims,
- support amortized preprocessing via **computation commitments**,
- and use **SPARK** to make polynomial commitments efficient for **sparse multilinear polynomials**
(Abstract, p. 1; Section 1.1, pp. 3–5).

The resulting system is interactive first and then made non-interactive via prior zero-knowledge and Fiat–Shamir-style compilation in the random oracle model (Abstract, p. 1; pp. 3–5).

## Key Claims

- Spartan gives a transparent zkSNARK family for **arbitrary R1CS**, not only for highly regular or data-parallel computations (Abstract, pp. 1–2).
- It is the first transparent zkSNARK for arbitrary NP statements with **sub-linear verifier work** in the paper's stated sense (Abstract, p. 1; Introduction, p. 3).
- It introduces **computation commitments**, allowing the verifier to preprocess public circuit / constraint structure without any trapdoor (pp. 3–4).
- It introduces **SPARK**, a compiler that upgrades polynomial commitments for multilinear polynomials to efficiently handle sparse multilinear polynomials (Abstract, p. 1; pp. 3–4).
- Spartan's prover can be **linear-time or quasilinear-time** depending on the chosen commitment backend and variant, while verification and proof size range from $O(\log^2 n)$ to $O(\sqrt n)$ depending on the commitment scheme (Abstract, p. 1; Theorem 1.1, p. 5).
- The implementation results make a strong claim that transparency need not imply impractical prover cost (Abstract, p. 1; Section 1.1, pp. 5–6).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

An R1CS instance over a field $\mathbb{F}$ is defined by matrices
$$
A,B,C \in \mathbb{F}^{m\times n},
$$
and a vector $z\in \mathbb{F}^n$ satisfies the constraints if
$$
(Az) \circ (Bz) = Cz,
$$
where $\circ$ denotes the Hadamard product (Introduction, p. 2).

For implementation purposes, one usually thinks of
$$
z = (1, x, w),
$$
where $x$ is the public input and $w$ is the witness.

The paper's main theorem is summarized in Theorem 1.1 (p. 5): there exists a family of public-coin succinct interactive arguments of knowledge for NP under standard cryptographic assumptions in which:
- the prover incurs costs from
  $$
  O(n) \text{ to } O(n\log n),
  $$
- the verifier's costs and communication range from
  $$
  O(\log^2 n) \text{ to } O(\sqrt n),
  $$
depending on the underlying extractable polynomial commitment scheme.

The corresponding zkSNARK corollary in the random oracle model preserves the same asymptotic range for prover time, verifier time, and proof size (Corollary 1.1, p. 5).

The introduction also explains the central algebraic representation: Spartan encodes an R1CS instance as a degree-3 multivariate polynomial that decomposes into four multilinear polynomials, which is key to obtaining a time-optimal prover when combined with sum-check and multilinear commitment machinery (Section 1.1, p. 4).

## Methods and Proof Techniques

### 1. Hypercube / multilinear encoding of R1CS

Spartan's most important systems move is to encode arbitrary R1CS into multilinear polynomials over Boolean hypercubes rather than force the computation into a highly regular circuit format. This matters because arbitrary sparse constraint systems are common in practice (Section 1.1, p. 4).

### 2. Sum-check plus evaluation checks

The core interactive proof follows the now-familiar pattern:
- arithmetize the relation,
- express satisfaction as a low-degree identity,
- use sum-check to reduce a large consistency claim,
- end with a small number of polynomial evaluations
(Abstract, p. 1; Section 1.1, pp. 3–4).

### 3. Computation commitments

The verifier can preprocess the structure of the computation once by committing to sparse multilinear objects derived from the constraint system. This preprocessing is public, amortizable, and reusable across many inputs sharing the same circuit / R1CS shape, without any toxic-waste trapdoor (Section 1.1, pp. 3–4).

### 4. SPARK compiler for sparse multilinear commitments

SPARK is the paper's commitment-layer contribution: a compiler that turns a multilinear polynomial commitment scheme into one that efficiently handles sparse multilinear polynomials. This is crucial for time-optimal proving because real R1CS matrices are sparse (Abstract, p. 1; Section 1.1, p. 4).

### 5. Black-box assembly of variants

Because Spartan treats the polynomial commitment layer abstractly, different commitment backends instantiate different performance points in the overall Spartan family. This is why the paper offers a *family* of zkSNARKs rather than a single fixed point in the prover/verifier/proof-size tradeoff space (Abstract, p. 1; Theorem 1.1, p. 5).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline complexity profile stated in the abstract and Theorem 1.1 is:

- **Prover time:**
  $$
  O(n) \text{ to } O(n\log n)
  $$
  depending on the commitment backend (Abstract, p. 1; Theorem 1.1, p. 5).
- **Verifier time / communication / proof size:** range from
  $$
  O(\log^2 n) \text{ to } O(\sqrt n)
  $$
  depending on the backend (Abstract, p. 1; Theorem 1.1, p. 5).
- **Setup:** transparent for the transparent variants, with public preprocessing rather than toxic waste (Abstract, pp. 1–2).

The experimental evaluation reports the following high-level findings (Abstract, p. 1):
- among transparent zkSNARKs, Spartan gives prover speedups of **36–152×** depending on the baseline,
- produces proofs shorter by **1.2–416×**,
- and gives verification speedups of **3.6–1326×**,
- while also comparing favorably to trusted-setup systems in several regimes.

For the current wiki, the key lesson is that transparency plus arbitrary R1CS support does **not** force catastrophic prover or verifier overhead.

## Why It Matters

Spartan matters because it made a major design thesis plausible:
> one can have arbitrary-NP, transparent, commitment-based succinct arguments without giving up on serious verifier efficiency.

It is one of the clearest system-paper anchors for the multilinear / sum-check side of the field.

In the current wiki, Spartan is especially important because it connects:
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Sum-check Protocol]]
- [[Polynomial Commitments]]
- [[Transparent zkSNARKs]]
- [[Computation Commitments]]
- [[SPARK]]

It also serves as an excellent counterpoint to the RS / FRI / IOPP branch represented by [[FRI]] and [[WHIR]].

## Connections to the Wiki

This paper is a central anchor for:
- [[Spartan]]
- [[zkSNARKs]]
- [[Transparent zkSNARKs]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Polynomial Commitments]]
- [[Computation Commitments]]
- [[SPARK]]
- [[Sum-check Protocol]]
- [[Fiat-Shamir Transform]]

It should often be read alongside RS/IOPP papers to understand the contrast between multilinear transparent SNARKs and Reed–Solomon-based transparent systems.

## Open Questions / Limitations

- The current note now captures the theorem-level tradeoff claims directly from the paper, but a deeper pass could still extract more precise statement-by-statement detail from the internal theorems beyond the introduction.
- Spartan's different performance points depend heavily on the commitment backend, so the "one system" picture should always be read as a family of instantiations.
- A useful future synthesis would compare Spartan more explicitly against WHIR-, FRI-, and folding-based systems at the level of concrete algebraic commitments and verifier bottlenecks.

## Suggested Next Reading

- [[Sum-check Protocol]]
- [[Polynomial Commitments]]
- [[Transparent zkSNARKs]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

## Related
- [[Spartan]]
- [[Srinath Setty]]
- [[zkSNARKs]]
- [[Transparent zkSNARKs]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Polynomial Commitments]]
- [[Computation Commitments]]
- [[SPARK]]
- [[Sum-check Protocol]]
- [[Fiat-Shamir Transform]]
- [[Research Agenda]]
