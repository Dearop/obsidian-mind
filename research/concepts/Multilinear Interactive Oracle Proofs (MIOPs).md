---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - miop
  - multilinear
  - proof-systems
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[VEIL]]"
  - "[[Polynomial Commitments]]"
description: "Useful abstraction for multilinear hash-based proof systems and their zk compilers"
---

# Multilinear Interactive Oracle Proofs (MIOPs)

## Definition / framing

Multilinear interactive oracle proofs (MIOPs) are interactive oracle proof systems in which prover oracles and verifier checks are organized around **multilinear polynomials** and their evaluations.

In the framing used by *[[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]*, many practical hash-based multilinear systems follow a shared pattern:
- commit to a multilinear extension of the trace,
- run an interactive algebraic phase in the clear,
- then reduce to multilinear evaluation claims relative to the original commitment.

## Why it matters

This is a useful intermediate abstraction for the current corpus because it helps explain the structure shared by many practical multilinear systems without collapsing them into either generic IOP language or specific PCS internals.

VEIL uses this abstraction to explain why zero knowledge can be added in a lightweight wrapper style.

## Key distinctions

- MIOPs are more specialized than generic [[Interactive Oracle Proofs (IOPs)]].
- They are closely tied to multilinear trace representations, multilinear evaluations, and multilinear polynomial commitment schemes.
- In practical systems, much of the proof communication may still be dominated by the final proximity / commitment-opening layer rather than the algebraic transcript itself.


## Mathematical background / formulae

Given a Boolean function $f:\{0,1\}^n \to \mathbb{F}$, its multilinear extension is
$$
\widetilde{f}(X_1,\dots,X_n)=\sum_{b\in\{0,1\}^n} f(b) \prod_{i=1}^n \big(b_i X_i + (1-b_i)(1-X_i)\big).
$$
MIOP-style systems work with commitments, oracle access, and evaluation claims about such multilinear extensions.
A typical endpoint is a claim of the form
$$
\widetilde{f}(z)=v
$$
for some random point $z \in \mathbb{F}^n$.


## Worked example

Let $f:\{0,1\}^2 \to \mathbb{F}$ be given by
$$
f(0,0)=1,\quad f(0,1)=2,\quad f(1,0)=3,\quad f(1,1)=4.
$$
Its multilinear extension is a polynomial $\widetilde f(X_1,X_2)$ agreeing with those four values on the Boolean square.
A MIOP-style protocol may commit to this multilinear extension and eventually reduce correctness to an evaluation claim such as
$$
\widetilde f(z_1,z_2)=v
$$
for a random point $(z_1,z_2)\in\mathbb{F}^2$.
The verifier is thus checking structured polynomial behavior, not reading the whole truth table explicitly.


## Current map in this wiki

This is a useful local hub for the multilinear / compiler side of the branch:
- [[VEIL]] as the clearest current anchor
- [[Spartan]] as a nearby multilinear/sum-check design anchor
- [[Polynomial Commitments]] as the commitment-layer bridge
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]] for the broader family comparison

## Evidence / sources

- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

## Related entities

- [[VEIL]]
- [[Spartan]]

## Open questions

- Which other ingested papers should be recast through the MIOP abstraction?

## Wiki development

- Should the wiki eventually separate multilinear IOPs from multilinear interactive PCPs more explicitly?
