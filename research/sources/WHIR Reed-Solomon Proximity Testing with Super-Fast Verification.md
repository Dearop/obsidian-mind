---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/WHIR.pdf
authors:
  - Gal Arnon
  - Alessandro Chiesa
  - Giacomo Fenzi
  - Eylon Yogev
year: 2024
tags:
  - iopp
  - reed-solomon
  - hash-based-snargs
  - polynomial-commitments
  - generalized-r1cs
  - constrained-rs
related:
  - "[[WHIR]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[Constrained Reed-Solomon Codes]]"
  - "[[Polynomial Commitments]]"
  - "[[RS IOPP and STARK Lineage]]"
  - "[[FRI vs WHIR]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Modern IOPP for constrained Reed–Solomon codes with unusually fast verification"
---

# WHIR Reed-Solomon Proximity Testing with Super-Fast Verification

## Summary

WHIR introduces a new **interactive oracle proof of proximity (IOPP)** for **constrained Reed–Solomon codes** with a deliberately verifier-centric optimization target.

Its high-level thesis is that the Reed–Solomon proximity layer remains one of the main practical bottlenecks in transparent, hash-based proof systems, and that improving this layer can materially improve:
- verifier latency,
- verifier hash complexity,
- compiler efficiency,
- and downstream SNARG performance
(Abstract, p. 1; Introduction, pp. 4–5).

The paper positions WHIR as a replacement candidate for proximity-testing components such as **FRI**, **STIR**, and **BaseFold** in relevant pipelines (Abstract, p. 1; pp. 4–6).

The central conceptual move is to replace plain low-degree / Reed–Solomon proximity with proximity to **constrained Reed–Solomon codes**, allowing the protocol to express richer algebraic conditions — including sumcheck-like structure — while keeping verification extremely fast in practice (pp. 5–6).

## Key Claims

- WHIR is an IOPP for **constrained Reed–Solomon codes**, not just ordinary Reed–Solomon codes (Abstract, p. 1; Definition 1, p. 5).
- It can act as a drop-in replacement for FRI-like proximity layers in relevant transparent-proof compiler stacks (Abstract, p. 1).
- In its target parameter regimes, verifier time is extremely small in practice, often in the **few-hundred-microsecond** range according to the paper's benchmarks (Abstract, p. 1; Section 6, pp. 43–53).
- It supports a compiler from **Σ-IOPs** to ordinary IOPs, making it useful beyond a single isolated proximity-testing problem (Contents and Introduction, pp. 4–6).
- It yields efficient constructions for generalized-R1CS SNARGs and for hash-based polynomial commitment schemes for both univariate and multivariate polynomials (Abstract, p. 1).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper defines a constrained Reed–Solomon code by starting from a smooth Reed–Solomon code and imposing an additional sumcheck-like constraint on the multilinear polynomial underlying the codeword. In the paper's notation,
$$
CRS[\mathbb{F},L,m,\hat w,\sigma]
$$
denotes the code of functions in the Reed–Solomon family whose underlying multilinear polynomial additionally satisfies the weighted constraint encoded by $(\hat w,\sigma)$ (Definition 1, p. 5).

The main theorem on WHIR is stated informally in Theorem 1 (pp. 5–6): for a constrained Reed–Solomon code with rate $\rho$, security parameter $\lambda$, and folding parameter $k$, assuming the paper's list-decoding conjecture and sufficiently large field size, the code has an IOPP with round-by-round soundness error
$$
2^{-\lambda},
$$
round complexity
$$
O(m/k),
$$
and the following performance:
- prover sends
  $$
  O(|L|)
  $$
  field elements and makes $O(|L|)$ field operations;
- verifier makes
  $$
  q_{\mathrm{WHIR}} = O\!\left( \frac{\lambda}{\log(1/\rho)} + \frac{\lambda}{k}\cdot\frac{\log(m/k)}{\log(1/\rho)} + \frac{m}{k} \right)
  $$
  queries over alphabet $\mathbb{F}_{2^k}$;
- verifier arithmetic cost is
  $$
  O\bigl(q_{\mathrm{WHIR}}\cdot (2^k + m)\bigr)
  $$
  field operations.

The introduction further explains that in the typical setting $m\le \lambda$ and $\rho=O(1)$, one chooses
$$
k \approx \log m,
$$
in which case the verifier makes
$$
q_{\mathrm{WHIR}} = O(\lambda)
$$
queries, which the paper describes as optimal up to constant factors (p. 6).

## Methods and Proof Techniques

### 1. Constrained Reed–Solomon codes

This is the paper's most important conceptual contribution. Standard RS proximity captures low-degree structure. Constrained RS codes capture low-degree structure **plus extra algebraic conditions**, making the proximity layer substantially more expressive for downstream proof-system compilation (Introduction, pp. 5–6).

### 2. Folding with parameter $k$

WHIR uses iterative folding with a parameter $k$ controlling how aggressively the instance shrinks. The verifier cost depends explicitly on this parameter through terms like $2^k$, so $k$ is a first-class performance knob (Theorem 1, pp. 5–6).

### 3. Mutual correlated agreement

A major technical ingredient is **mutual correlated agreement**, which the paper uses to control list-decoding behavior across multiple correlated prover objects. This is especially important for soundness in the folding/list-decoding regime (Section 1.1 and Section 4.2 in the contents, pp. 4–8).

### 4. Compiler from Σ-IOPs to IOPs

WHIR does not stop at proximity testing. It gives a compiler that turns suitable Σ-IOPs into ordinary IOPs by using the constrained-RS IOPP as a core compilation primitive (Contents and Introduction, pp. 4–6).

### 5. Hash-based SNARG / PCS applications

The paper pushes the proximity layer into practical constructions:
- generalized-R1CS SNARGs,
- univariate PCS,
- multivariate PCS,
- and related transparent arguments
(Abstract, p. 1; pp. 4–6).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline WHIR performance profile from Theorem 1 is:

- **Rounds:**
  $$
  O(m/k)
  $$
  (pp. 5–6).
- **Prover work:**
  $$
  O(|L|)
  $$
  field operations and $O(|L|)$ transmitted field elements (pp. 5–6).
- **Verifier queries:**
  $$
  q_{\mathrm{WHIR}} = O\!\left( \frac{\lambda}{\log(1/\rho)} + \frac{\lambda}{k}\cdot\frac{\log(m/k)}{\log(1/\rho)} + \frac{m}{k} \right)
  $$
  (pp. 5–6).
- **Verifier arithmetic:**
  $$
  O\bigl(q_{\mathrm{WHIR}}\cdot (2^k + m)\bigr)
  $$
  field operations (pp. 5–6).
- **Soundness:**
  $$
  2^{-\lambda}
  $$
  under the stated assumptions (pp. 5–6).

The abstract also gives a concrete polynomial-commitment example: for degree $2^{22}$ and 100-bit security, WHIR yields commitment/opening time of **1.2 seconds**, sender communication of **63 KiB**, and opening verification time of **360 microseconds** (Abstract, p. 1).

For the current wiki, the key point is that WHIR aims to improve verifier speed *without* sacrificing the attractive prover/argument-size profile of modern hash-based systems.

## Why It Matters

WHIR matters because it shows that the RS / IOPP substrate is still a major optimization frontier.

The field did not end with “FRI solved Reed–Solomon proximity once and for all.” Instead, WHIR argues that verifier-centric improvements to this layer materially change the viability of:
- recursion,
- on-chain verification,
- low-latency proof checking,
- and modern transparent compiler pipelines.

In the current wiki, WHIR is one of the clearest modern endpoints of the branch traced in [[RS IOPP and STARK Lineage]].

## Connections to the Wiki

WHIR is a central anchor for:
- [[WHIR]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[Constrained Reed-Solomon Codes]]
- [[Polynomial Commitments]]
- [[FRI vs WHIR]]
- [[RS IOPP and STARK Lineage]]
- [[SNARKs and STARKs Reading Map]]

It should often be read as the verifier-optimized modern counterpart to [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]].

## Open Questions / Limitations

- The current note now captures the main theorem statement and concrete verifier-centric claims, but a deeper pass could still extract more of the internal soundness theorems and compiler details from later sections.
- WHIR's strongest asymptotic parameters in the introduction rely on a list-decoding conjecture, so the conjectural/unconditional distinction should remain visible in later syntheses.
- A useful future comparison would put WHIR side by side with WARP to clarify the difference between constrained-code IOPP compilation and general-linear-code IOR accumulation.

## Suggested Next Reading

- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[FRI]]
- [[FRI vs WHIR]]
- [[RS IOPP and STARK Lineage]]
- [[Polynomial Commitments]]

## Related
- [[WHIR]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[Constrained Reed-Solomon Codes]]
- [[Polynomial Commitments]]
- [[RS IOPP and STARK Lineage]]
- [[FRI vs WHIR]]
- [[SNARKs and STARKs Reading Map]]
