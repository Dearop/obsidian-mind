---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - reed-solomon
  - coding-theory
  - proof-systems
related:
  - "[[WHIR]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[Polynomial Commitments]]"
description: "WHIR's richer code abstraction for sumcheck-like constraints"
---

# Constrained Reed-Solomon Codes

## Definition / framing

In the framing of *[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]*, constrained Reed–Solomon codes are Reed–Solomon codes augmented with additional **sumcheck-like constraints** on the underlying multilinear polynomial.

## Why it matters

This is one of the key conceptual moves in WHIR.

It allows the proximity-testing layer to directly express richer queries than ordinary low-degree testing alone, including queries naturally related to polynomial evaluation and generalized R1CS compilation.

## Key distinctions

- Standard Reed–Solomon codes only capture low-degree structure.
- Constrained Reed–Solomon codes add extra algebraic conditions, increasing expressiveness.
- In WHIR, this richer code family enables both:
  - fast IOPPs for proximity testing, and
  - a compilation path from Σ-IOPs to standard IOPs.


## Mathematical background / formulae

A standard Reed--Solomon code over domain $D \subseteq \mathbb{F}$ and degree bound $d$ is
$$
RS_{D,d}=\{(f(\alpha))_{\alpha\in D} : \deg f < d\}.
$$
A constrained Reed--Solomon family informally refines this to codewords whose underlying polynomial also satisfies extra algebraic conditions, e.g.
$$
CRS_{D,d,\Phi}=\{f|_D \in RS_{D,d} : \Phi(f)=1\},
$$
where $\Phi$ may encode sumcheck-like or evaluation-consistency constraints.

### Concrete constraint examples

The predicate $\Phi$ can encode many natural algebraic conditions:

1. **Evaluation constraint.** $\Phi(f) \equiv \bigl(f(\alpha) = v\bigr)$ for a fixed point $\alpha \in \mathbb{F}$ and target value $v$. This is the simplest case and corresponds to the opening of a polynomial commitment at a public point.
2. **Sum constraint.** $\Phi(f) \equiv \Bigl(\sum_{a \in H} f(a) = s\Bigr)$ for a subgroup $H \subset D$. This is sum-check-like and lets a single proximity test also verify a claimed sum.
3. **Degree-respecting constraint.** $\Phi(f) \equiv \bigl(\deg(f) < d' < d\bigr)$ — the polynomial must have strictly lower degree than the ambient RS code.
4. **Zero-on-subset constraint.** $\Phi(f) \equiv \bigl(f(a) = 0 \text{ for all } a \in S\bigr)$ for some subset $S \subset D$. Equivalently, $f$ is divisible by $\prod_{a \in S}(X - a)$.

### Why this matters for WHIR

WHIR's proximity test operates over constrained RS codes rather than plain RS codes. In a naive stack, a protocol would first run a proximity test to show $f$ is close to some low-degree polynomial, and then separately run an algebraic constraint test to show that polynomial satisfies the desired property. WHIR collapses these into **one IOPP pass**: the same protocol simultaneously checks proximity *and* the constraint $\Phi$, saving verifier rounds and queries.

### Worked example

Let $D = \{1, 2, 3, 4\}$ over a small field, degree bound $d = 3$ (polynomials of degree $< 3$), and $\Phi(f) \equiv \bigl(f(1) = 5\bigr)$.

- $f(X) = 5 + 2X - X^2$: $\deg(f) = 2 < 3$ ✓, and $f(1) = 5 + 2 - 1 = 6 \neq 5$ ✗. **Not in $CRS_{D, 3, \Phi}$.**
- $f(X) = 5 - X + X^2$: $\deg(f) = 2 < 3$ ✓, and $f(1) = 5 - 1 + 1 = 5$ ✓. **In $CRS_{D, 3, \Phi}$.**

A WHIR-style verifier receiving the evaluation vector $(f(1), f(2), f(3), f(4))$ would simultaneously check that the vector is close to a degree-$< 3$ polynomial **and** that the implied polynomial evaluates to $5$ at $X = 1$.

## Evidence / sources

- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related entities

- [[WHIR]]

## Open questions

- Is constrained-RS likely to remain a lasting abstraction, or mainly a useful local viewpoint for WHIR and nearby work?

## Wiki development

- Track which later papers reuse this exact abstraction versus encoding similar constraints differently.
