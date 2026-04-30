---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - compiler
  - polynomial-commitments
related:
  - "[[Spartan]]"
  - "[[Polynomial Commitments]]"
description: "Compiler for efficient sparse multilinear polynomial handling"
---

# SPARK

## Definition / framing

In [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]], SPARK is a compiler that transforms an extractable polynomial commitment scheme for multilinear polynomials into one that can efficiently handle **sparse multilinear polynomials**.

## Why it matters

SPARK is presented as the ingredient that helps Spartan achieve a **time-optimal prover** in important variants.

This matters because many succinct-proof bottlenecks are not only about the outer protocol but about whether the commitment machinery aligns with the sparsity structure of the algebraic objects being proved about.

## Key distinctions

- SPARK is not the whole Spartan construction; it is a key subcomponent.
- Its role is specifically tied to sparse multilinear polynomial handling.
- In the paper, it is framed as a compiler layered atop an existing extractable polynomial commitment scheme.


## Mathematical background / formulae

A sparse multilinear polynomial has the schematic form
$$
f(X_1,\dots,X_n)=\sum_{\alpha\in S} c_\alpha \prod_{i=1}^n X_i^{\alpha_i},
$$
where $S \subseteq \{0,1\}^n$ is small relative to the full Boolean cube.
SPARK's role is to turn commitment support for generic multilinear polynomials into commitment support that respects this sparse structure more efficiently.

### Multilinear extension of a sparse function

Let $f: \{0,1\}^n \to \mathbb{F}$ be a function with only $s \ll 2^n$ nonzero entries. Its multilinear extension is:
$$
\tilde{f}(x_1, \dots, x_n) \;=\; \sum_{\mathbf{b} \in \{0,1\}^n} f(\mathbf{b}) \cdot \prod_{i=1}^{n} \bigl(b_i x_i + (1 - b_i)(1 - x_i)\bigr).
$$
The naive cost of evaluating $\tilde{f}$ at a random point is $O(2^n)$, because every point of the cube contributes a term. But when $f$ is sparse, only $s$ of those terms are nonzero.

### SPARK's key insight — exploiting sparsity

SPARK makes the sparsity structurally exploitable by:
1. Representing nonzero entries as an explicit list of $(\text{index}, \text{value})$ pairs of length $s$.
2. Committing to the sparse representation using a hash-based memory-checking argument (so the verifier can spot-check claimed entries).
3. Running sum-check over $\tilde{f}$ with $O(s)$ prover work per round, rather than $O(2^n)$.

The total prover cost for a sum-check over a sparse multilinear polynomial drops from $O(n \cdot 2^n)$ to $O(n \cdot s)$, which is what enables Spartan's time-optimal prover in its best variants.

### Worked example

Let $n = 3$, so the full table has $2^3 = 8$ entries. Suppose $f$ has only $s = 2$ nonzero evaluations:

| $\mathbf{b}$ | $f(\mathbf{b})$ |
|--------------|-----------------|
| $(0, 1, 0)$ | $7$ |
| $(1, 0, 1)$ | $3$ |
| all others | $0$ |

The dense sum-check prover would iterate over all $8$ cube points. SPARK's sparse prover stores only the two nonzero pairs and evaluates:
$$
\tilde{f}(r_1, r_2, r_3) \;=\; 7 \cdot (1 - r_1) r_2 (1 - r_3) \;+\; 3 \cdot r_1 (1 - r_2) r_3
$$
at any random point in $O(2)$ work proportional to $s$, not $O(8)$ proportional to $2^n$. For real R1CS instances where $s$ is $10^6$ and $2^n$ would be $10^{12}$, the savings are dramatic.

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related entities

- [[Spartan]]
- [[Srinath Setty]]

## Open questions

- Does SPARK's memory-checking approach remain competitive against newer sparse-polynomial commitment schemes?

## Wiki development

- Determine which later papers build directly on SPARK-like ideas.
- Assess whether SPARK is mainly of historical interest or remains a live design pattern.
