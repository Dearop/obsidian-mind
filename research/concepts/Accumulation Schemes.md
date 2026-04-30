---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - accumulation
  - recursion
  - proof-systems
related:
  - "[[WARP]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Recursive-composition primitive for carrying many verification obligations forward"
---

# Accumulation Schemes

## Definition / framing

Accumulation schemes are cryptographic primitives for incrementally combining many verification obligations into a compact evolving state called an accumulator.

Informally, instead of repeatedly carrying all prior instance-witness pairs forward, one keeps a short accumulator and proves correct updates to it.

## Why it matters

This concept sits near the center of the recursion / proof-composition branch of the current wiki.

In *[[WARP Linear-Time Accumulation Schemes]]*, accumulation schemes are presented as a key substrate for efficient [[Proof-Carrying Data (PCD)]] and closely related recursive systems. The paper's headline achievement is the first accumulation scheme with **linear prover time** and **logarithmic verifier time**.

## Key distinctions

- Accumulation schemes are related to, but not identical with, direct succinct arguments.
- They are especially valuable when proof verification itself becomes part of the next computation.
- Design axes include:
  - prover time,
  - verifier time,
  - witness handling,
  - recursion depth support,
  - underlying commitments/codes,
  - and whether the construction is group-based, lattice-based, or hash-based.


## Mathematical background / formulae

A generic accumulation interface can be sketched as
$$
\mathsf{Accumulate}(\mathsf{acc}_t,x_t,w_t) \to (\mathsf{acc}_{t+1},\pi_t),
$$
where $\mathsf{acc}_t$ is a short accumulator summarizing many prior obligations.
A corresponding decision procedure checks the accumulated state:
$$
\mathsf{Decide}(\mathsf{acc}_T)=1 \implies \bigwedge_{t=1}^T R(x_t,w_t)=1
$$
up to the scheme's soundness error.
The key asymptotic question is how the costs of $\mathsf{Accumulate}$ and $\mathsf{Decide}$ scale with the number of accumulated instances.

## Current map in this wiki

This is the main hub for the recursion branch's accumulation side:
- [[WARP]] as the foundational accumulation anchor
- [[Quasar]] as the multi-instance recursion-overhead optimization anchor
- [[Quasar vs WARP]] for the internal accumulation comparison
- [[Accumulation vs Folding in Recursive Proof Systems]] for the broader branch-level comparison
- [[Mathematical Preliminaries for SNARKs and STARKs]] for the compact study-oriented overview


## Worked example

Suppose we have already accumulated two obligations into $\mathsf{acc}_2$ and now want to add a third claim $(x_3,w_3)$.
Instead of carrying all three claims explicitly, the prover computes
$$
(\mathsf{acc}_3,\pi_2) \leftarrow \mathsf{Accumulate}(\mathsf{acc}_2,x_3,w_3).
$$
The new accumulator $\mathsf{acc}_3$ is intended to summarize all three obligations.
At the end of the recursion pipeline, a decision procedure checks the final state:
$$
\mathsf{Decide}(\mathsf{acc}_3)=1.
$$
The whole point is that recursive systems can carry this short state forward instead of re-verifying all prior obligations from scratch at every step.

## Evidence / sources

- [[WARP Linear-Time Accumulation Schemes]]

## Related entities

- [[WARP]]
- [[Benedikt Bünz]]
- [[Alessandro Chiesa]]

## Open questions

- What are the fundamental limits on accumulation verifier complexity — can sublinear-in-$\ell$ verification be achieved hash-based, or does it inherently require algebraic structure?
- How do accumulation schemes compose with folding schemes — can a system accumulate folded instances, or fold accumulated instances?

## Wiki development

- Compare accumulation schemes against folding schemes and direct recursive SNARK composition as corpus grows.
- Clarify which later papers are best treated as accumulation versus folding papers.
