---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - commitments
  - polynomials
related:
  - "[[zkSNARKs]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Spartan]]"
description: "Commitment primitive family underlying many succinct proof trade-offs"
---

# Polynomial Commitments

## Definition / framing

Polynomial commitments are cryptographic primitives that let one commit to a polynomial and later prove evaluation claims about it.

In modern proof-system design, they often serve as a modular bridge between algebraic relations and succinct verification.

## Scope note

**Scope note.** This page covers the abstract commit/open/verify interface. Concrete instantiations — KZG (pairing-based), IPA (discrete-log), FRI-based (hash-based) — are not yet surveyed here; see [[FRI]] for the hash-based variant most relevant to this wiki's current corpus.

## Why it matters

This appears to be one of the central recurring primitives in the user's new paper set.

In *[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]*, polynomial commitments are used as a black-box component in the underlying interactive argument. The paper's SPARK contribution is specifically about adapting commitment machinery so it can efficiently handle **sparse multilinear polynomials**.

## Key distinctions

- Different commitment schemes induce different proof-size, verifier-time, prover-time, and setup trade-offs.
- Supporting **multilinear** vs **sparse multilinear** polynomials efficiently can materially affect prover complexity.
- A paper may look “about SNARKs” at a high level while much of the actual trade-off surface is determined by the underlying commitment primitive.


## Mathematical background / formulae

A polynomial commitment scheme usually exposes algorithms of the form
$$
c \leftarrow \mathsf{Commit}(f),\qquad \pi \leftarrow \mathsf{Open}(f,z),
$$
with verification condition
$$
\mathsf{Verify}(c,z,v,\pi)=1 \iff f(z)=v.
$$
In multilinear settings, $f$ may be a multilinear extension over $\mathbb{F}^n$; in univariate settings, $f$ may be a low-degree polynomial over $\mathbb{F}[X]$. The concrete commitment design strongly influences prover time, verifier time, proof size, and setup assumptions.

## Worked example

Suppose the prover commits to the polynomial
$$
f(X)=X^2+1.
$$
Later the verifier asks for the value at $z=3$. The true evaluation is
$$
f(3)=3^2+1=10.
$$
The prover sends an opening proof
$$
\pi \leftarrow \mathsf{Open}(f,3),
$$
and the verifier checks
$$
\mathsf{Verify}(c,3,10,\pi)=1.
$$
The cryptographic goal is that the prover should not be able to open the same commitment $c$ convincingly both to $10$ and to some different value $10'\neq 10$ at the same point.

In multilinear settings the point is a vector $z\in\mathbb{F}^n$ rather than a single field element, but the interface idea is the same.

## Current map in this wiki

This is a major bridge hub across multiple branches:
- multilinear / sum-check design via [[Spartan]] and [[SPARK]]
- RS / compiler-oriented systems via [[WHIR]]
- recursion / accumulation via [[Quasar]]
- lightweight zk wrapping via [[VEIL]]
- higher-level family comparison via [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

## Related entities

- [[Spartan]]
- [[WHIR]]
- [[Quasar]]
- [[VEIL]]
- [[Srinath Setty]]

## Open questions

- Which commitment schemes are most important to track across the rest of the paper set?

## Wiki development

- Should the wiki split this into subpages for multilinear commitments, KZG-style schemes, IPA-style schemes, and FRI-adjacent approaches?
- When should the wiki split out a dedicated page for multilinear PCS design as distinct from polynomial commitments broadly?
