---
date: 2026-04-13
type: source
status: processed
source_kind: paper
created: 2026-04-13
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/BF01200056.pdf
authors:
  - László Babai
  - Lance Fortnow
  - Carsten Lund
year: 1991
tags:
  - interactive-proofs
  - mip
  - complexity-theory
  - classical-foundations
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Probabilistically Checkable Proofs (PCPs)]]"
  - "[[PCP vs MIP vs IOP Lineage]]"
  - "[[Algebraic Methods for Interactive Proof Systems]]"
  - "[[Checking Computations in Polylogarithmic Time]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Classical MIP paper proving that two-prover interactive proofs characterize nondeterministic exponential time"
---

# Non-deterministic Exponential Time Has Two-Prover Interactive Protocols

## Summary

This paper proves a landmark expressive-power result for **two-prover interactive proofs**: they characterize **NEXP**.

In the model, a randomized polynomial-time verifier interacts with two all-powerful provers that cannot communicate with each other. The paper shows that this noncommunication structure is powerful enough to certify computations all the way up to nondeterministic exponential time (Abstract, p. 3; Theorem 1.1, p. 4).

Technically, the proof combines:
- algebraic extrapolation ideas extending the single-prover algebraic-IP tradition,
- and a verification scheme for **multilinearity** of oracle-held functions (Abstract, p. 3; Section 1, pp. 4–5).

In the current wiki, this is a major MIP milestone on the path from algebraic IPs toward PCP and later oracle-proof thinking.

## Key Claims

- Two-prover interactive proofs characterize **NEXP** (Theorem 1.1, p. 4).
- For languages in **EXP**, honest provers need only **EXP** computational power (Abstract, p. 3; Section 1, p. 4).
- The proof extends algebraic methods from the single-prover setting (Abstract, p. 3).
- A key ingredient is a multilinearity-verification procedure for large encoded functions (Abstract, p. 3; Section 1, p. 5).
- The result is historically upstream of the later PCP / local-checking worldview.

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

Let **MIP** denote the class of languages having multi-prover interactive proof systems. Section 2 defines a protocol for a language $L$ using provers $P_1,\dots,P_k$ and verifier $V$ such that (Section 2, pp. 6–7):
- if $x\in L$, then the honest provers make $V$ accept with probability at least $1-2^{-n}$,
- if $x\notin L$, then every cheating prover strategy is accepted with probability at most $2^{-n}$.

The paper's headline theorem is stated explicitly as (Theorem 1.1, p. 4):
$$
\mathrm{MIP} = \mathrm{NEXP}.
$$
Section 1 also notes that only two provers are necessary, so one can read the result as the expressive sufficiency of two-prover systems for nondeterministic exponential time (pp. 4–5).

A second formal ingredient is the oracle-verifier characterization recalled in Section 2: languages accepted by probabilistic oracle machines are exactly those accepted by multi-prover protocols (Theorem 2.3, p. 7). This is historically important because it makes MIP look like a locally checked proof model rather than just an interactive game.

The technical core of the main theorem includes multilinearity testing for functions over large domains. Section 1 emphasizes that the verifier must test whether an oracle-held function is multilinear, and that this subroutine has independent program-verification interest (p. 5).

## Methods and Proof Techniques

### 1. Noncommunication as verification leverage

The verifier asks related questions to two provers who cannot coordinate during the protocol. This makes cross-checking powerful enough to detect global inconsistency from partial views (Section 2, pp. 6–8).

### 2. Algebraic extension of single-prover techniques

Part of the proof extends the algebraic extrapolation style already visible in [[Algebraic Methods for Interactive Proof Systems]]. The introduction explicitly situates the result relative to the Lund–Fortnow–Karloff–Nisan / Shamir line (Section 1, pp. 3–5).

### 3. Multilinearity testing

One of the most important subroutines is a test for whether a large encoded function is multilinear. This is historically significant because multilinear consistency checking becomes a recurring theme in later proof-system design (Section 1, p. 5).

### 4. Complexity-class lifting

As with several classical papers in this area, the significance is not just the protocol itself but the exact complexity-class characterization it yields: the protocol model is shown to be neither a mild variant of NP nor a small extension of IP, but a full characterization of NEXP (Theorem 1.1, p. 4).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The main performance interpretation is complexity-theoretic rather than deployment-oriented:

- **Verifier time:** polynomial time in the input length (Section 2, pp. 6–7).
- **Communication:** polynomially bounded, because message lengths are polynomially bounded in the input size (Section 2, p. 6).
- **Number of provers:** two suffice for the full expressive power result (Theorem 2.4, p. 7).
- **Expressive power:**
  $$
  \mathrm{MIP} = \mathrm{NEXP}
  $$
  (Theorem 1.1, p. 4).
- **Honest-prover complexity for languages in EXP:** the paper states that honest provers need only EXP computational power in that regime (Abstract, p. 3; Section 1, p. 4).

For a modern reader, the most important lesson is structural rather than benchmark-driven: local algebraic consistency checks become dramatically more powerful when the verifier can compare multiple isolated views.

## Why It Matters

This paper matters because it makes the MIP branch impossible to ignore.

Without it, the historical graph would look like classical algebraic IPs leading directly to PCPs. This paper shows an important intermediate stage where local consistency, randomness, and oracle-like access patterns already become strong enough to characterize an enormous complexity class.

That is one of the reasons the later progression
- MIP → PCP → IOP
is historically meaningful rather than artificial.

## Connections to the Wiki

This paper belongs in the classical-foundations layer connecting:
- [[Algebraic Methods for Interactive Proof Systems]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Checking Computations in Polylogarithmic Time]]
- [[SNARKs and STARKs Reading Map]]

It is especially useful as the MIP anchor preceding the PCP theorem papers.

## Open Questions / Limitations

- The paper establishes the power of MIPs, but does not yet give the later static-PCP packaging that became canonical.
- The current note now cites the main theorem and model definitions, but a deeper pass could still extract more precise detail from the multilinearity-test sections.
- A future concept page specifically for multi-prover interactive proofs may still be worthwhile if this branch grows further.

## Suggested Next Reading

- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Proof Verification and the Hardness of Approximation Problems]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Algebraic Methods for Interactive Proof Systems]]

## Related
- [[Interactive Oracle Proofs (IOPs)]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Algebraic Methods for Interactive Proof Systems]]
- [[Checking Computations in Polylogarithmic Time]]
- [[SNARKs and STARKs Reading Map]]
