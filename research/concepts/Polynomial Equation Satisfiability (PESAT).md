---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - np-relations
  - arithmetization
  - proof-systems
related:
  - "[[Accumulation Schemes]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[WARP]]"
description: "WARP's NP-complete algebraic target relation"
---

# Polynomial Equation Satisfiability (PESAT)

## Definition / framing

Polynomial equation satisfiability (PESAT) is an NP-complete formulation in which a witness satisfies a collection of constant-degree polynomial equations over a field.

## Why it matters

In *[[WARP Linear-Time Accumulation Schemes]]*, PESAT is the main target relation for which the accumulation scheme is stated.

It matters because the paper uses PESAT as an expressive relation that naturally captures:
- [[Rank-1 Constraint Satisfiability (R1CS)]],
- generalized R1CS,
- CCS,
- and related algebraic statement systems.

## Key distinctions

- PESAT is a relation-level abstraction, not a specific commitment or proof primitive.
- It plays a similar role to R1CS as a convenient NP-complete algebraic target, but in a form adapted to WARP's accumulation framework.


## Mathematical background / formulae

PESAT asks whether there exists a witness $w \in \mathbb{F}^n$ such that a collection of polynomial equations all vanish:
$$
P_j(w)=0 \qquad \text{for all } j\in[m].
$$
Equivalently, one may view the relation as
$$
R(x,w)=1 \iff \forall j\in[m],\; P_j(x,w)=0,
$$
with each $P_j$ having bounded degree.

### NP-completeness

PESAT is NP-complete over any finite field $\mathbb{F}$ with $|\mathbb{F}| \geq 2$. The reduction from Circuit-SAT is standard: each Boolean gate becomes a degree-$2$ equation (e.g., $z - xy = 0$ for AND, $z - x - y + xy = 0$ for OR), plus Booleanity constraints $x(x-1) = 0$ for each wire.

### Relationship to R1CS

An R1CS instance $(A, B, C, x, w)$ with $A z \circ B z = C z$ (where $z = (x, w)$ and $\circ$ is Hadamard product) translates directly to PESAT. Each constraint row $i$ becomes the polynomial equation
$$
\left(\sum_{j} A_{i,j} \, z_j\right) \cdot \left(\sum_{j} B_{i,j} \, z_j\right) \;-\; \left(\sum_{j} C_{i,j} \, z_j\right) \;=\; 0.
$$
So R1CS is a special case of PESAT where **every equation has degree exactly 2** with a rigid bilinear structure. PESAT is strictly more general: it allows higher-degree equations and does not require the rank-1 multiplicative form.

### Why WARP uses PESAT instead of R1CS

PESAT's generality is load-bearing for WARP's design. WARP's IOR compiler works natively over arbitrary polynomial equations, which lets it handle richer constraint systems (such as CCS, custom-gate arithmetizations, and lookups) without first reducing everything to degree-2 rank-1 form. This flexibility is part of what enables WARP's linear-time proving: the compiler does not pay the blowup that a reduction to R1CS would introduce.

### Worked example

A tiny PESAT instance over $\mathbb{F}_{17}$ with witness $w = (w_1, w_2)$:
$$
P_1(w) = w_1^2 + w_2 - 10 = 0, \qquad P_2(w) = w_1 w_2 - 6 = 0.
$$
Witness $(w_1, w_2) = (3, 1)$: $P_1 = 9 + 1 - 10 = 0$ ✓, $P_2 = 3 \cdot 1 - 6 = -3 \neq 0$ ✗ (not a solution).
Witness $(w_1, w_2) = (2, 3)$: $P_1 = 4 + 3 - 10 = -3 \neq 0$ ✗ (not a solution).
Witness $(w_1, w_2) = (3, 2)$: $P_1 = 9 + 2 - 10 = 1 \neq 0$ ✗.

An honest solver would search or reduce to find a genuine satisfying assignment. The PESAT relation is the question itself: does **any** $w \in \mathbb{F}^2$ make both equations vanish?

## Evidence / sources

- [[WARP Linear-Time Accumulation Schemes]]

## Related entities

- [[WARP]]

## Open questions

- What are the concrete advantages and disadvantages of PESAT vs R1CS vs generalized R1CS vs CCS as target relations?

## Wiki development

- As more papers are ingested, should PESAT get folded into a broader page comparing algebraic NP-complete statement formats?
