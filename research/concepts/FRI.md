---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-14
tags:
  - fri
  - iopp
  - reed-solomon
  - proof-systems
related:
  - "[[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[WHIR]]"
description: "Foundational fast Reed–Solomon proximity-testing protocol underlying many transparent systems"
---

# FRI

## Definition / framing

FRI stands for **Fast Reed–Solomon Interactive Oracle Proofs of Proximity**.

It is a foundational IOPP for Reed–Solomon proximity testing that repeatedly reduces a large proximity claim to smaller ones, yielding a prover with linear arithmetic complexity and a verifier with logarithmic arithmetic complexity.

## Why it matters

FRI is one of the core algorithmic building blocks in the transparent / STARK-style part of the modern proof-systems landscape.

If [[Interactive Oracle Proofs]] explains the broader oracle-proof model, then [[Interactive Oracle Proofs of Proximity (IOPPs)]] explain the specialized proximity-testing model that FRI inhabits, and FRI explains one of the key *engines* that makes transparent hash-based proof systems practical.

## Key distinctions

- FRI is about **Reed–Solomon proximity testing**, not a full SNARK by itself.
- It is a canonical example of an **IOPP**.
- Later systems such as [[WHIR]] can be understood in part as refinements, alternatives, or successors in the same broad Reed–Solomon / IOPP design space.


## Mathematical background / formulae

A Reed--Solomon codeword has the form
$$
(f(\alpha))_{\alpha\in D} \quad \text{for a polynomial } f \text{ with } \deg f < d.
$$
FRI repeatedly reduces a large low-degree claim to a smaller one. A standard intuition is to decompose
$$
f(X) = f_0(X^2) + X f_1(X^2)
$$
and then define a folded polynomial
$$
g(Y) = f_0(Y) + \beta f_1(Y)
$$
for a random challenge $\beta$. This shrinks the domain / degree relationship while preserving useful soundness.

## Worked example

Take the quadratic polynomial
$$
f(X)=1+2X+3X^2.
$$
Write it in the form
$$
f(X)=f_0(X^2)+Xf_1(X^2)
$$
by grouping even and odd powers:
$$
f_0(Y)=1+3Y,
\qquad
f_1(Y)=2.
$$
Then for a verifier challenge $\beta$, the folded polynomial is
$$
g(Y)=f_0(Y)+\beta f_1(Y)=1+3Y+2\beta.
$$
So a degree-2 claim about $f$ is transformed into a degree-1 claim about $g$. FRI repeats this type of reduction recursively until the verifier is checking a much smaller residual low-degree claim.

## Evidence / sources

- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related entities

- [[Eli Ben-Sasson]]
- [[Iddo Bentov]]
- [[Ynon Horesh]]
- [[Michael Riabzev]]

## Current map in this wiki

This page connects:
- [[Interactive Oracle Proofs of Proximity (IOPPs)]] as the model-layer category FRI belongs to
- [[Reed-Solomon Proximity Testing]] as the underlying problem layer
- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]] as the canonical source paper
- [[WHIR]] and [[FRI vs WHIR]] as the main modern refinement/comparison branch
- [[RS IOPP and STARK Lineage]] as the historical substrate synthesis

## Open questions

- Which later proof systems still use FRI essentially as-is, versus adapting or replacing it?

## Wiki development

- How should this wiki compare FRI directly against WHIR and STIR once more sources are ingested?
