---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/TR17-134.pdf
authors:
  - Eli Ben-Sasson
  - Iddo Bentov
  - Ynon Horesh
  - Michael Riabzev
year: 2017
tags:
  - fri
  - iopp
  - reed-solomon
  - transparent
  - starks
related:
  - "[[FRI]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[WHIR]]"
  - "[[FRI vs WHIR]]"
  - "[[RS IOPP and STARK Lineage]]"
  - "[[Transparent zkSNARKs]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Foundational FRI paper for linear-time Reed–Solomon proximity testing in transparent systems"
---

# Fast Reed-Solomon Interactive Oracle Proofs of Proximity

## Summary

This paper introduces **FRI** — *Fast Reed–Solomon Interactive Oracle Proofs of Proximity* — the foundational **IOPP** that made Reed–Solomon proximity testing fast enough to become a realistic transparent-proof substrate.

Its headline achievement is unusually strong for its time: a Reed–Solomon IOPP with
- **strictly linear prover arithmetic complexity**,
- **strictly logarithmic verifier arithmetic complexity**,
- **logarithmic query complexity**,
- and **constant soundness**
(Abstract, p. 1; Theorem 1.2, pp. 3–4).

At a high level, FRI repeatedly reduces one Reed–Solomon proximity claim on a large domain to another on a smaller domain via a folding-style transformation reminiscent of FFT structure. This recursive shrinkage yields a verifier that performs only logarithmically many local checks while the prover performs only linear arithmetic work (Abstract, p. 1; Introduction, pp. 1–4).

In the current wiki, FRI is the canonical algorithmic engine of the RS / IOPP / STARK branch.

## Key Claims

- FRI is an IOPP for Reed–Solomon codes with prover arithmetic complexity less than roughly $6n$, verifier arithmetic complexity at most about $21\log n$, query complexity $2\log n$, and constant soundness in the paper's main theorem framing (Abstract, p. 1; Theorem 1.2, pp. 3–4).
- It is the first RS-IOPP combining strictly linear prover arithmetic, strictly logarithmic verifier arithmetic, and constant soundness (Abstract, p. 1).
- It improves over prior RS-PCPP / RS-IOPP systems whose prover costs were superlinear even for polynomially large query complexity (Abstract, p. 1; Table 1, pp. 2–3).
- Its soundness degradation across recursive reductions is mild enough to allow about $\Theta(\log n)$ proof-composition rounds in the useful distance regime, unlike earlier systems that were limited to about $O(\log\log n)$ rounds (Abstract, p. 1; pp. 1, 4–6).
- It is explicitly motivated as a practical step toward concretely efficient transparent zero-knowledge proof and argument systems (Abstract, p. 1; Section 1.3, pp. 6–7).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

For an evaluation set $S$ of size $n$ in a finite field $\mathbb{F}$ and rate parameter $\rho\in(0,1]$, the Reed–Solomon code is
$$
RS[\mathbb{F},S,\rho] = \{f:S\to\mathbb{F} \mid f \text{ is the evaluation of a polynomial of degree } d<\rho n\}
$$
(Introduction, p. 2).

The paper defines an IOPP for a code family $\mathcal{C}$ as an IOP where the first prover message is the purported codeword $f^{(0)}$, the verifier has oracle access to it, and completeness/soundness are stated relative to distance from the code (Definition 1.1, pp. 3–4).

The main theorem is Theorem 1.2 (pp. 3–4): the binary additive RS code family of rate
$$
\rho = 2^{-R}
$$
with $R\ge 2$ has an IOPP with the following properties, where $n$ is the block length:
- prover complexity less than
  $$
  6n
  $$
  arithmetic operations over $\mathbb{F}$;
- proof length less than
  $$
  n/3
  $$
  field elements;
- round complexity at most
  $$
  \frac{\log n}{2};
  $$
- verifier query complexity
  $$
  2\log n;
  $$
- verifier arithmetic complexity at most
  $$
  21\log n;
  $$
- soundness lower bound: every word that is $\delta$-far from the code is rejected with probability at least
  $$
  \min\{\delta,\delta_0\} - 3n/|\mathbb{F}|
  $$
  for
  $$
  \delta_0 \ge \frac{1}{4}(1-3\rho) - \frac{1}{\sqrt n};
  $$
- soundness upper bound: for every $\delta>0$ there exists a $\delta$-far word rejected with probability at most
  $$
  \delta + 4/|\mathbb{F}|.
  $$

The paper also remarks that the theorem extends to arbitrary rates and to smooth multiplicative subgroups with somewhat different constants (Remarks 1.3–1.4, p. 4).

## Methods and Proof Techniques

### 1. IOPP formulation for Reed–Solomon codes

FRI is explicitly an [[Interactive Oracle Proofs of Proximity (IOPPs)|IOPP]], not a standalone zkSNARK. The verifier gets oracle access to a purported codeword and the prover sends additional oracle layers that certify proximity across recursive reductions (pp. 2–4).

### 2. Recursive reduction / folding structure

The protocol repeatedly reduces a large RS proximity claim to a smaller one. The folding step is algebraically analogous to decomposing a polynomial into even and odd parts, which is the main reason the verifier can stay logarithmic while the prover remains linear (Abstract, p. 1; technical overview in the introduction).

### 3. Commit phase / query phase organization

The prover sends a sequence of oracle layers over shrinking domains. Afterwards the verifier samples and checks consistency constraints tying those layers together, which is how FRI trades long proofs for only logarithmically many local checks (Introduction, pp. 2–4).

### 4. Soundness analysis below the unique-decoding radius

A major contribution is the analysis showing that when
$$
\delta < \frac{1-\rho}{2},
$$
recursive reductions incur only negligible additive soundness loss. This is what allows many more proof-composition rounds than earlier systems (Abstract, p. 1; pp. 1, 4–6).

### 5. Concrete-efficiency orientation

The paper explicitly cares about practical transparent proof systems, not only asymptotic existence. This is one reason it became a central substrate paper historically (Abstract, p. 1; Section 1.3, pp. 6–7).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

Theorem 1.2 gives the headline profile:

- **Prover:** less than
  $$
  6n
  $$
  field operations (pp. 3–4).
- **Proof length:** less than
  $$
  n/3
  $$
  field elements (pp. 3–4).
- **Verifier arithmetic:** at most
  $$
  21\log n
  $$
  field operations (pp. 3–4).
- **Verifier queries:**
  $$
  2\log n
  $$
  (pp. 3–4).
- **Rounds:** at most
  $$
  \log n / 2.
  $$

The paper also studies the **concrete efficiency threshold** for RS proximity protocols and shows large practical improvements over previous PCPP/IOPP work; Figure 1 shows substantially smaller thresholds across soundness levels than earlier systems (pp. 5–6).

For the current wiki, the key message is that FRI is not merely asymptotically elegant — it was designed to push RS proximity testing toward practical transparent proof systems.

## Why It Matters

FRI matters because it turned Reed–Solomon proximity testing from a theoretically relevant but expensive subroutine into a practical protocol primitive.

That is why it sits at the base of so much later work:
- STARK-style proof systems,
- RS-based IOPPs,
- hash-based transparent SNARGs,
- and verifier-centric successors like [[WHIR]].

In the current wiki, FRI is the clearest historical anchor for the RS / IOPP / STARK substrate branch.

## Connections to the Wiki

This paper is foundational for:
- [[FRI]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[WHIR]]
- [[FRI vs WHIR]]
- [[RS IOPP and STARK Lineage]]
- [[Transparent zkSNARKs]]
- [[SNARKs and STARKs Reading Map]]

It should often be read together with [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]] to understand how the RS branch evolved from baseline fast proximity testing to verifier-optimized constrained-code systems.

## Open Questions / Limitations

- The current note now captures the theorem-level constants and soundness statement from the introduction, but a future pass could still extract more of the detailed folding/soundness lemmas from later sections.
- FRI's best soundness statements depend on the distance regime, so comparisons against later systems should pay attention to the exact operating range.
- A useful future synthesis would compare FRI's recursive shrinkage directly against multilinear/sum-check systems and against constrained-RS refinements like WHIR.

## Suggested Next Reading

- [[FRI]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[FRI vs WHIR]]
- [[RS IOPP and STARK Lineage]]

## Related
- [[FRI]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[WHIR]]
- [[FRI vs WHIR]]
- [[RS IOPP and STARK Lineage]]
- [[Transparent zkSNARKs]]
- [[SNARKs and STARKs Reading Map]]
