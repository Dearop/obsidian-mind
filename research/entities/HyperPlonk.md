---
date: 2026-04-30
description: "Plonk-on-hypercube system using multilinear IOP/commitment machinery to avoid prover FFT bottlenecks and better support high-degree custom gates."
type: entity
entity_kind: protocol
tags:
  - snark
  - plonk
  - multilinear
  - proof-systems
related:
  - "[[HyperPlonk Plonk with Linear-Time Prover and High-Degree Custom Gates]]"
  - "[[Sum-check Protocol]]"
  - "[[Polynomial Commitments]]"
  - "[[Commit-and-Prove SNARKs]]"
---

# HyperPlonk

## What It Is

HyperPlonk is a Plonk-family protocol that moves arithmetization/proving from univariate subgroup representation to multilinear representation over the Boolean hypercube.

In the wiki's terms: it is a **Plonkish multilinear IOP route** that uses SumCheck-based checks to remove FFT-heavy prover bottlenecks.

## Relevance to This Wiki

- It is a central node for understanding how "Plonk ergonomics" and "multilinear efficiency" can be combined.
- It complements RS/IOPP systems ([[FRI]], [[WHIR]]) and interleaving/constrained-code lines ([[WARP]]) by operating in a different algebraic substrate.
- It matters for any synthesis comparing custom-gate-heavy proving pipelines.

## Associated Sources

- [[HyperPlonk Plonk with Linear-Time Prover and High-Degree Custom Gates]]

## Related
- [[Sum-check Protocol]]
- [[Polynomial Commitments]]
- [[Commit-and-Prove SNARKs]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Spartan]]
- [[VEIL]]
