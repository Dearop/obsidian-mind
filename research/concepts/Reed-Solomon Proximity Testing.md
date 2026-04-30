---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-14
tags:
  - reed-solomon
  - iopp
  - proof-systems
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[WHIR]]"
  - "[[Transparent zkSNARKs]]"
description: "Core RS/IOPP substrate for modern transparent and hash-based proof systems"
---

# Reed-Solomon Proximity Testing

## Definition / framing

Reed–Solomon proximity testing asks whether a function is close to a Reed–Solomon codeword. In modern proof systems, this is one of the core subroutines behind many transparent and hash-based proof constructions.

## Why it matters

This is a central substrate for the STARK/IOPP side of the field.

In *[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]*, the core contribution is a new Reed–Solomon proximity-testing protocol for **constrained Reed–Solomon codes** with especially fast verification.

## Key distinctions

- **Standard RS proximity testing** versus **constrained RS proximity testing**.
- FRI-style, STIR-style, BaseFold-style, and WHIR-style protocols can all be viewed as inhabiting this design space, though with different trade-offs.
- Improvements here can directly affect verifier time, proof size, and hash complexity in compiled hash-based SNARGs.


## Mathematical background / formulae

For a domain $D \subseteq \mathbb{F}$ and degree bound $d$, the Reed--Solomon code is
$$
RS_{D,d}=\{(f(\alpha))_{\alpha\in D} : \deg f < d\}.
$$
Proximity testing asks whether a word $w \in \mathbb{F}^{|D|}$ is close to this code, e.g. by studying
$$
\operatorname{dist}(w,RS_{D,d})=\min_{c\in RS_{D,d}} \frac{\Delta(w,c)}{|D|},
$$
where $\Delta$ is Hamming distance.
In proof systems, the verifier wants to test this with only sparse oracle access to $w$.

## Worked example

Let the field be large enough to contain the domain
$$
D=\{0,1,2\}.
$$
Consider degree bound $d=2$, so valid codewords come from linear polynomials
$$
f(X)=a+bX.
$$
If we take
$$
f(X)=1+2X,
$$
then the associated Reed--Solomon codeword is
$$
(f(0),f(1),f(2))=(1,3,5).
$$
Now suppose a prover oracle instead gives
$$
w=(1,3,8).
$$
Then $w$ is not exactly this codeword, and in fact differs from it in one position. A proximity test asks whether $w$ is still close to some low-degree codeword, without the verifier having to read every symbol of a much larger oracle in realistic settings.

This tiny example captures the key point: the verifier is not checking a whole computation relation directly, but rather whether an oracle behaves like a low-degree codeword.

## Current map in this wiki

This is the main hub for the RS / STARK-substrate branch:
- [[Interactive Oracle Proofs of Proximity (IOPPs)]] as the model-layer bridge from generic oracle proofs to proximity testing
- [[FRI]] as the canonical historical engine
- [[WHIR]] as the modern constrained-RS refinement
- [[FRI vs WHIR]] as the direct local comparison
- [[RS IOPP and STARK Lineage]] as the historical substrate synthesis
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]] as the broader family comparison
- [[Mathematical Preliminaries for SNARKs and STARKs]] as the compact study-oriented overview

## Evidence / sources

- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related entities

- [[FRI]]
- [[WHIR]]
- [[Alessandro Chiesa]]
- [[Eli Ben-Sasson]]

## Open questions

- What are the key trade-offs between FRI-, STIR-, BaseFold-, and WHIR-style proximity-testing protocols?

## Wiki development

- This page should gradually become a real comparison page for FRI-, STIR-, BaseFold-, and WHIR-style protocols.
- When should the wiki split algorithmic RS-proximity testing from downstream hash-based SNARG compilation?
