---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - folding
  - recursion
  - proof-systems
related:
  - "[[Symphony]]"
  - "[[Accumulation Schemes]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Recursive-composition primitive that compresses many statements into one combined statement"
---

# Folding Schemes

## Definition / framing

Folding schemes are public-coin protocols that reduce the task of checking multiple related statements to checking a single combined statement.

They are a major route to scalable recursive proof systems, especially in IVC/PCD-style settings.

## Why it matters

Folding is one of the main alternatives to both:
- direct recursive SNARK verification,
- and accumulation schemes in the narrower sense.

In *[[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]*, folding is the central primitive. The paper argues that existing folding-based SNARKs suffer from excessive recursion overhead because they embed Fiat–Shamir / hash logic in recursive circuits and typically use low folding arity.

## Key distinctions

- Folding schemes are related to accumulation schemes, but the literature often emphasizes different compiler patterns and bottlenecks.
- Important axes include:
  - folding arity,
  - recursion depth,
  - verifier-circuit cost,
  - whether Fiat–Shamir logic is embedded in proved statements,
  - and whether the construction is group-based, hash-based, or lattice-based.
- Symphony highlights the distinction between **low-arity recursive folding** and **high-arity folding**.


## Mathematical background / formulae

A folding step informally combines several instances into one new instance,
$$
((x_1,w_1),\dots,(x_k,w_k)) \mapsto (x',w'),
$$
often using random coefficients $\rho_1,\dots,\rho_k$ so that the folded claim preserves soundness with high probability.
In linear settings one often sees the schematic form
$$
x' = \sum_{i=1}^k \rho_i x_i,\qquad w' = \sum_{i=1}^k \rho_i w_i,
$$
though real folding schemes usually include additional structure, commitments, or normalization constraints.

## Current map in this wiki

This is the main hub for the folding side of the recursion branch:
- [[Symphony]] as the current folding anchor
- [[High-Arity Folding]] for the main local design choice in Symphony
- [[Accumulation vs Folding in Recursive Proof Systems]] for the branch-level comparison with accumulation
- [[Mathematical Preliminaries for SNARKs and STARKs]] for the compact study-oriented overview


## Worked example

Suppose two instances are represented algebraically by vectors $x_1,x_2$ and witnesses $w_1,w_2$.
A toy 2-to-1 fold might sample a random scalar $\rho$ and form
$$
x' = x_1 + \rho x_2,
\qquad
w' = w_1 + \rho w_2.
$$
The folded claim says, informally, that if both original instances were valid then the combined instance should also satisfy a derived verification equation. Real folding schemes add commitments, normalization, and soundness machinery, but this linear-combination picture is the basic intuition.

## Evidence / sources

- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]

## Related entities

- [[Symphony]]
- [[Binyi Chen]]

## Open questions

- What is the cleanest conceptual comparison between folding schemes and accumulation schemes?

## Wiki development

- As more recursion papers are ingested, should the wiki split folding schemes from folding-based SNARK compilers more explicitly?
