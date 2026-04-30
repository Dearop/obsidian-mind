---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - soundness
  - compiler-security
  - proof-systems
related:
  - "[[Interactive Oracle Proofs]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Fiat-Shamir Transform]]"
description: "Rewinding-style soundness notion used to analyze IOP-to-NIROP compilation"
---

# State Restoration Attacks

## Definition / framing

State restoration attacks are a rewinding-style attack model introduced in *[[Interactive Oracle Proofs]]* to analyze the soundness of compiling public-coin IOPs into non-interactive random-oracle proofs.

Informally, the malicious prover can reset the verifier to a previously visited internal state and continue from there with fresh randomness.

## Why it matters

This concept is one of the paper's main technical insights.

The key point is that for IOP-to-NIROP compilation, ordinary soundness is not the right robustness notion by itself. The resulting non-interactive protocol's soundness is tightly connected to how the underlying IOP behaves under this stronger rewinding-style adversarial model.

## Key distinctions

- State restoration is stronger than plain soundness analysis.
- It is related to, but distinct from, resettable and backtracking notions discussed in the paper.
- In *[[Interactive Oracle Proofs]]*, it becomes the main lens for characterizing the security of the compiler.


## Mathematical background / formulae

A state-restoration adversary can rewind a verifier to an earlier internal state after some transcript prefix
$$
\tau_{\le i}=(m_1,\rho_1,\dots,m_i,\rho_i)
$$
and then continue execution with fresh later randomness.
So instead of analyzing only one straight-line transcript, the security proof must reason about a branching tree of transcript continuations rooted at previously visited states.

### Formal attack game

Let $\Pi = (P, V)$ be an interactive protocol with transcript $\tau = (\alpha_1, \beta_1, \dots, \alpha_r, \beta_r)$, where $\alpha_i$ are prover messages and $\beta_i$ are verifier challenges.

A state-restoration adversary $A$ can:
1. Run the protocol honestly up to round $i$, reaching state $\sigma_i$.
2. **Fork**: save $\sigma_i$, send a message $\alpha_{i+1}$, and receive the verifier's response $\beta_{i+1}$.
3. **Restore**: reload $\sigma_i$ and send a *different* message $\alpha_{i+1}'$, receiving a fresh verifier response $\beta_{i+1}'$.

The adversary builds a **tree of transcripts** rooted at $\sigma_0$, where each branch corresponds to a different forking choice. Concretely, the adversary's view is a tree $\mathcal{T}$ in which:
- Each internal node at depth $i$ is labelled by a state $\sigma_i$ and the prover message $\alpha_i$ that produced it.
- Each edge from depth $i$ to depth $i+1$ is labelled by a verifier challenge $\beta_i$.
- Different children of the same node correspond to different prover messages sent after restoring the same state.

**Depth bound:** For an $r$-round IOP compiled via Fiat–Shamir, a state-restoration adversary with $q$ queries to the random oracle can explore at most $q$ branches. The soundness error degrades from $\epsilon_{\mathrm{IOP}}$ to roughly $q \cdot \epsilon_{\mathrm{IOP}}$. More precisely, if the IOP has state-restoration soundness error $\epsilon_{\mathrm{sr}}$, then the compiled non-interactive protocol has soundness error at most $q \cdot \epsilon_{\mathrm{sr}}$ in the random-oracle model.

**Contrast with standard rewinding:** In classical rewinding extraction (e.g., knowledge extractors for $\Sigma$-protocols), the *extractor* controls the verifier's coins and rewinds the prover. In state restoration, the roles are reversed: the *adversary* (acting as a malicious prover) controls the fork points against a deterministic compiled verifier whose challenges are random-oracle outputs. The adversary chooses when and where to fork, whereas a rewinding extractor follows a fixed extraction strategy.

### Worked example: 2-round forking attack

Consider a 2-round public-coin protocol where:
- The prover sends $\alpha_1$ (e.g., a commitment).
- The verifier replies with a uniformly random challenge $\beta_1 \in \mathbb{F}$.
- The prover sends $\alpha_2$ (e.g., an opening).
- The verifier checks a relation $R(\alpha_1, \beta_1, \alpha_2) \stackrel{?}{=} 1$.

Suppose soundness relies on the prover not knowing $\beta_1$ when computing $\alpha_1$.

A state-restoration adversary proceeds as follows:
1. Compute $\alpha_1$ and save state $\sigma_0$.
2. Send $\alpha_1$, receive challenge $\beta_1$. Now the adversary knows one challenge.
3. **Restore** to $\sigma_0$ and send the *same* $\alpha_1$ again, receiving a *different* challenge $\beta_1'$ (different random-oracle query or different verifier coins).

The adversary now holds two challenges $\beta_1, \beta_1'$ for the same first message $\alpha_1$. If the protocol's soundness relies on a polynomial identity check — e.g., verifying that a degree-$d$ polynomial $p$ satisfies $p(\beta_1) = 0$ — then learning two evaluation points lets the adversary interpolate or otherwise extract information that a single honest execution would not reveal. In the worst case, two branches suffice to find a fraudulent $\alpha_2$ that passes verification on at least one branch, breaking soundness that was designed for a single-execution setting.

## Evidence / sources

- [[Interactive Oracle Proofs]]

## Related entities

- [[Eli Ben-Sasson]]
- [[Alessandro Chiesa]]
- [[Nicholas Spooner]]

## Open questions

- How often does later literature still reason explicitly in these terms versus treating the compiler as a standard black box?

## Wiki development

- Should the wiki eventually add a separate page for the tree-exploration-game viewpoint used in the paper's analysis?
