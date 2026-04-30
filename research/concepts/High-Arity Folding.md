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
  - "[[Folding Schemes]]"
  - "[[Symphony]]"
  - "[[Commit-and-Prove SNARKs]]"
description: "Folding strategy that trades recursion depth for larger one-shot batching"
---

# High-Arity Folding

## Definition / framing

High-arity folding is a folding strategy in which many input statements are compressed in a single folding step, rather than using only 2-to-1 or 3-to-1 folding repeatedly in a deep recursive tree.

## Why it matters

In *[[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]*, high-arity folding is the central architectural move.

The paper argues that low-arity recursive folding causes several problems:
- deeper folding trees,
- worse parallelism,
- more Fiat–Shamir / hashing overhead,
- and, in some settings, weaker depth-related security behavior.

High-arity folding tries to reduce these costs by compressing many statements in one shot.

## Key distinctions

- Higher arity can reduce recursion depth.
- Higher arity can improve batching and parallelism.
- But higher arity can also increase norm growth, commitment size pressure, and some verifier/prover subcosts.
- Symphony's key message is that high arity becomes more practical when combined with a compiler that avoids embedding Fiat–Shamir logic in the proved statements.


## Mathematical background / formulae

If low-arity folding combines only a few instances at a time, high-arity folding instead combines many,
$$
(x_1,\dots,x_k) \mapsto x' = \sum_{i=1}^k \rho_i x_i,
$$
for larger $k$ and random coefficients $\rho_i$.
The benefit is that recursion depth can shrink from roughly $O(\log_2 N)$ levels to roughly $O(\log_k N)$ levels, at the cost of heavier per-round work.

### Depth–arity tradeoff

Standard binary folding ($k = 2$) of $N$ instances requires depth
$$d_2 = \lceil \log_2 N \rceil.$$
With arity $k$ folding, the depth shrinks to
$$d_k = \lceil \log_k N \rceil = \left\lceil \frac{\log N}{\log k} \right\rceil.$$

### Cost per fold step

Each $k$-to-1 fold requires the prover to:
1. Receive $k$ instances $(\phi_1, \pi_1), \dots, (\phi_k, \pi_k)$.
2. Sample a random combiner $\rho \in \mathbb{F}$.
3. Compute the folded instance as a random linear combination:
   $$\phi^* = \sum_{j=1}^{k} \rho^{j-1} \cdot \phi_j.$$

Prover cost per step is $O(k \cdot |\phi|)$. Total prover cost across all steps is
$$T_{\text{prover}} \;=\; O(k \cdot |\phi| \cdot \log_k N) \;=\; O\left(|\phi| \cdot \frac{k \log N}{\log k}\right).$$

**Tradeoff.** Increasing $k$ reduces depth (fewer recursive steps) but increases per-step work. Below some threshold, higher arity wins because the savings from fewer recursive-circuit embeddings outweigh the larger per-step combine cost. Above that threshold, per-step cost dominates and low arity is better.

### Worked example

For $N = 64$ instances:

| Arity $k$ | Depth $d_k$ | Total folds | Work per fold |
|-----------|-------------|-------------|---------------|
| $2$ | $6$ | $63$ | $O(2 \cdot |\phi|)$ |
| $4$ | $3$ | $21$ | $O(4 \cdot |\phi|)$ |
| $8$ | $2$ | $9$ | $O(8 \cdot |\phi|)$ |
| $16$ | $2$ | $5$ | $O(16 \cdot |\phi|)$ |

Symphony uses high-arity lattice-based folding specifically because each recursive step embeds a verifier circuit, and halving depth from $6$ to $3$ is worth the extra per-step work. Lattice settings also require careful control of norm growth, which benefits from fewer recursion levels.

## Evidence / sources

- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]

## Related entities

- [[Symphony]]
- [[Binyi Chen]]

## Open questions

- What are the practical crossover points between low-arity recursive folding and high-arity folding?

## Wiki development

- How should this page compare high-arity folding against multi-instance accumulation schemes such as [[Quasar]]?
