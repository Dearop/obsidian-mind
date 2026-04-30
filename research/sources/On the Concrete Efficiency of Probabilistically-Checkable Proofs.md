---
date: 2026-04-14
type: source
status: processed
source_kind: paper
created: 2026-04-14
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2488608.2488681.pdf
authors:
  - Eli Ben-Sasson
  - Alessandro Chiesa
  - Daniel Genkin
  - Eran Tromer
year: 2013
tags:
  - pcp
  - concrete-efficiency
  - reed-solomon
  - verification
related:
  - "[[Probabilistically Checkable Proofs (PCPs)]]"
  - "[[Checking Computations in Polylogarithmic Time]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Reed-Solomon Proximity Testing]]"
description: "PCP paper focused on asymptotic and concrete efficiency, introducing a concrete-efficiency threshold and improving Reed–Solomon PCP-of-proximity practicality"
---

# On the Concrete Efficiency of Probabilistically-Checkable Proofs

## Summary

This paper is a realism check on the positive-applications side of PCPs.

Its starting point is blunt: PCPs are theoretically powerful and central to many cryptographic constructions, but in practice they are often dismissed as the computational bottleneck that makes those constructions unusable. The paper asks whether PCPs are doomed to remain “galactic algorithms” with beautiful asymptotics but terrible constants (Abstract, p. 585; Introduction, pp. 585–586).

The answer it offers is cautiously optimistic. The paper gives:
- the first PCP whose **prover and verifier time are both quasi-optimal** up to polylogarithmic factors,
- a new notion of **concrete-efficiency threshold**, measuring when a PCP becomes cheaper than naive verification,
- and improved PCPs of proximity for **Reed–Solomon codes**, reducing the threshold for those components from about $2^{683}$ to about $2^{43}$
(Abstract, p. 585).

In the current wiki, this paper is valuable because it connects abstract PCP theorem results to the practical question: **when do local-checking proof systems become worth using at all?**

## Key Claims

- There exists a PCP system for verifying RAM computations where both prover and verifier time are quasi-optimal up to polylogarithmic factors (Theorem 1, pp. 585–586).
- The prover and verifier are highly parallelizable (Theorem 1, p. 586).
- The paper introduces a **concrete-efficiency threshold** for PCPs and related objects, asking for the smallest problem size at which using the PCP is actually cheaper than rerunning the computation (pp. 586–587).
- The paper proves that its PCP has a **finite concrete-efficiency threshold**, which is not automatic from prior polylogarithmic-verifier PCP results (Section 1.4, p. 587).
- For PCPs of proximity for Reed–Solomon codes, the paper improves the concrete-efficiency threshold from roughly $2^{683}$ down to roughly $2^{43}$ (Abstract, p. 585; Section 1.6, p. 589).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper's first major result is Theorem 1 (pp. 585–586): there is a PCP system such that, to prove and verify that a program $P$ accepts the input $(x,w)$ within $T$ steps for some witness $w$ with $|x|,|w|\le T$,

- the **sequential prover time** is
  $$
  (|P| + T)\cdot \operatorname{polylog}(T),
  $$
- the **sequential verifier time** is
  $$
  (|P| + |x|)\cdot \operatorname{polylog}(T),
  $$
- the **parallel prover time** is
  $$
  O((\log T)^2),
  $$
  when also given the computation transcript,
- and the **parallel verifier time** is also
  $$
  O((\log T)^2).
  $$

Section 1.3 introduces the **concrete-efficiency threshold** $B$ of a PCP system as the smallest problem size beyond which using the PCP is cheaper than naive verification, after combining normalized prover/verifier overheads via a chosen cost function $C$ (pp. 586–587).

The paper studies PCP systems for the succinct-circuit-satisfiability language and proves the existence of a PCP system with finite concrete-efficiency threshold for every polynomial cost function $C$ (Section 1.4, p. 587).

For Reed–Solomon PCPs of proximity, the paper states a dramatic threshold improvement: the threshold is reduced from approximately
$$
2^{683}
$$
to approximately
$$
2^{43}
$$
(Abstract, p. 585; Section 1.6, p. 589).

## Methods and Proof Techniques

### 1. Quasi-optimal PCP construction for RAM computations

The paper builds a PCP system for random-access machine computations rather than only cleaner algebraic toy models. This matters because practical verification problems often arise from programs rather than already-arithmetized relations (pp. 585–586).

### 2. Concrete-efficiency as a first-class metric

Instead of treating asymptotic verifier complexity as the whole story, the paper explicitly asks when PCP use is cheaper than simply rerunning the computation. This is one of the paper's most practically useful conceptual moves (Section 1.3, pp. 586–587).

### 3. Reed–Solomon PCP-of-proximity core

As in earlier algebraic PCP work, PCPs of proximity for Reed–Solomon codes are the main technical component. The paper improves the concrete efficiency of this subroutine substantially, which is why it matters for the broader transparent-proof story in the wiki (Abstract, p. 585; Section 1.6, p. 589).

### 4. Computational tools for efficient algebraic handling

The introduction highlights linearized polynomials over characteristic-2 field extensions, additive-FFT methods, and related algebraic machinery as key ingredients for making both prover and verifier efficient (p. 586).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline efficiency profile from Theorem 1 is:

- **Sequential prover:**
  $$
  (|P|+T)\cdot \operatorname{polylog}(T).
  $$
- **Sequential verifier:**
  $$
  (|P|+|x|)\cdot \operatorname{polylog}(T).
  $$
- **Parallel prover/verifier:**
  $$
  O((\log T)^2)
  $$
  parallel time (pp. 585–586).

The concrete-efficiency contribution is equally important:
- the paper defines a threshold parameter $B$ indicating when PCP use becomes cheaper than naive verification (Section 1.3, pp. 586–587);
- it shows this threshold can be finite for PCPs satisfying the right efficiency balance (Section 1.4, p. 587);
- and for the RS-PCPP core, it improves the threshold from roughly $2^{683}$ to roughly $2^{43}$ (Abstract, p. 585; Section 1.6, p. 589).

The important lesson for the current wiki is that asymptotic locality is not enough: **practical proof systems live or die on concrete thresholds**.

## Why It Matters

This paper matters because it prevents the wiki's PCP branch from staying too abstract.

Without papers like this, the PCP story can sound like:
- beautiful theorem statements,
- strong asymptotic verifier locality,
- but little guidance about whether any of it is usable.

This paper instead says:
- yes, asymptotics matter,
- but **concrete thresholds** matter too,
- and the bottleneck is often the prover and the underlying PCP-of-proximity machinery rather than the verifier theorem statement alone.

That makes it a natural companion to:
- [[Probabilistically Checkable Proofs (PCPs)]] for the model/theorem viewpoint,
- [[Transparent Verification and Verifiable Computation]] for the motivation viewpoint,
- and the RS/IOPP branch because Reed–Solomon PCP-of-proximity components are central to the efficiency story.

## Connections to the Wiki

This paper should strengthen:
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Checking Computations in Polylogarithmic Time]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]

It is especially useful as the page that explains why concrete efficiency, not just asymptotic verifier time, became a major concern before the transparent-proof era matured.

## Open Questions / Limitations

- The current note now captures the theorem-level efficiency statements and threshold concept directly from the paper's introduction, but a deeper pass could still extract more of the formal threshold definitions and RS-PCPP internals from later sections.
- A threshold around $2^{43}$ is a dramatic improvement over $2^{683}$, but it still underscores how demanding concrete PCP efficiency remained in this era.
- A useful future synthesis would compare this paper's efficiency-threshold worldview directly against later FRI/IOPP papers, where the same practical concerns are addressed in a different protocol model.

## Suggested Next Reading

- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Checking Computations in Polylogarithmic Time]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]

## Related
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Checking Computations in Polylogarithmic Time]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
