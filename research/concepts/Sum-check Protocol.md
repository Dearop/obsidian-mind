---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-13
tags:
  - interactive-proofs
  - cryptography
  - algebra
related:
  - "[[zkSNARKs]]"
  - "[[Spartan]]"
  - "[[Polynomial Identity Testing]]"
  - "[[Algebraic Methods for Interactive Proof Systems]]"
description: "Classical interactive-proof primitive reused inside Spartan"
---

# Sum-check Protocol

## Definition / framing

The sum-check protocol is a classical interactive proof protocol for verifying claims about sums of low-degree polynomials over the Boolean hypercube.

In [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]], it is the central interactive-proof backbone from which the succinct argument is built.

## Why it matters

[[Polynomial Identity Testing]] supplies the earliest randomized-algebraic intuition in this branch: turn correctness into a polynomial-consistency claim and use random evaluation to catch cheating efficiently. [[Algebraic Methods for Interactive Proof Systems]] is one of the clearest classical sources for the algebraic worldview behind sum-check-style reasoning. [[Spartan]] is a good reminder that many modern SNARK constructions are not entirely new from first principles. Instead, they often combine older interactive-proof machinery with newer commitment and compilation techniques.

## Key distinctions

- The raw sum-check protocol is powerful but not by itself a practical transparent zkSNARK.
- Spartan's contribution is not “inventing sum-check” but showing how to combine it with compact encoding, polynomial commitments, computation commitments, and zero-knowledge compilers.
- Understanding sum-check appears likely to be foundational for understanding this whole paper cluster.


## Mathematical background / formulae

Given a low-degree polynomial $g(X_1,\dots,X_n)$ and a claimed sum
$$
S = \sum_{b\in\{0,1\}^n} g(b),
$$
sum-check proceeds round by round. In the first round the prover sends
$$
g_1(X)=\sum_{x_2,\dots,x_n\in\{0,1\}^{n-1}} g(X,x_2,\dots,x_n),
$$
and the verifier checks
$$
g_1(0)+g_1(1)=S.
$$
The verifier then samples a random challenge $r_1$ and the process continues on the restricted polynomial $g(r_1,X_2,\dots,X_n)$.

## Worked example

Take
$$
g(X_1,X_2)=X_1+2X_2.
$$
Over the Boolean hypercube, the claimed sum is
$$
S=\sum_{(b_1,b_2)\in\{0,1\}^2} g(b_1,b_2)=0+2+1+3=6.
$$
In the first round, the prover sends the univariate polynomial
$$
g_1(X)=g(X,0)+g(X,1)=X+(X+2)=2X+2.
$$
The verifier checks
$$
g_1(0)+g_1(1)=2+4=6=S.
$$
Now the verifier samples a random challenge $r_1$ and reduces the claim to checking the one-variable polynomial
$$
g(r_1,X_2)=r_1+2X_2.
$$
The remaining sum is
$$
\sum_{b_2\in\{0,1\}} g(r_1,b_2)=r_1+(r_1+2)=2r_1+2,
$$
which is exactly $g_1(r_1)$. This illustrates the core invariant of sum-check: each round turns a large Boolean-hypercube sum into a smaller one while preserving consistency.

## Evidence / sources

- [[Polynomial Identity Testing]]
- [[Algebraic Methods for Interactive Proof Systems]]
- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related entities

- [[Spartan]]

## Open questions

- Which later papers in the folder continue to rely directly on sum-check rather than switching to FRI-centric or other approaches?

## Wiki development

- Should this wiki eventually have a dedicated synthesis page on the line from classical IPs/PCPs to modern SNARKs?
