---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - compiler
  - random-oracle-model
  - proof-systems
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Reductions (IORs)]]"
  - "[[Interactive Oracle Proofs]]"
description: "Core random-oracle compiler idea linking interactive proofs to non-interactive arguments"
---

# Fiat-Shamir Transform

## Definition / framing

The Fiat–Shamir transform is a paradigm for converting certain public-coin interactive proofs into non-interactive arguments in the random oracle model by deriving verifier challenges from a hash / random oracle.

## Why it matters

This is one of the key compiler ideas sitting underneath much of the current corpus.

In *[[Interactive Oracle Proofs]]*, the authors explicitly position their IOP-to-NIROP compiler as a generalization of:
- Fiat–Shamir for public-coin IPs,
- and CS-proof-style compilation for PCPs.

## Key distinctions

- Classical Fiat–Shamir is usually framed for public-coin IPs.
- In the IOP setting, additional machinery is needed because prover messages are oracle strings rather than short transcript messages.
- In practical modern proof systems, Fiat–Shamir-style thinking often appears together with Merkle commitments, transcript hashing, and oracle/message compression.


## Mathematical background / formulae

For a public-coin interactive protocol with prover messages $m_1,m_2,\dots$ and verifier challenges $\rho_1,\rho_2,\dots$, Fiat--Shamir replaces explicit random challenges with
$$
\rho_i = H(x,m_1,\rho_1,\dots,m_i),
$$
where $H$ is modeled as a random oracle.
The resulting protocol is non-interactive because the prover can derive each challenge locally from the transcript prefix.


## Worked example

Suppose a 2-round public-coin protocol has prover messages $m_1,m_2$ and verifier challenges $\rho_1,\rho_2$.
In the interactive version, the verifier samples random coins directly.
In the Fiat--Shamir version, the prover computes instead
$$
\rho_1 = H(x,m_1),
\qquad
\rho_2 = H(x,m_1,\rho_1,m_2).
$$
So the proof transcript can be published as
$$
\pi=(m_1,m_2),
$$
with the verifier recomputing the challenges by hashing the transcript prefix. This is the basic pattern behind many "interactive first, non-interactive later" proof systems.

## Current map in this wiki

This concept is a compiler bridge across multiple branches:
- non-interactive compilation of interactive proof systems from [[Spartan]]-style interactive cores
- model-level compiler discussion in [[Interactive Oracle Proofs]]
- transparent recursion and oracle instantiation issues in [[Fractal]]
- practical transcript hashing / wrapper layers relevant to [[VEIL]] and other transparent systems

## Evidence / sources

- [[Interactive Oracle Proofs]]

## Related entities

- [[Alessandro Chiesa]]
- [[Eli Ben-Sasson]]

## Open questions

- What is the difference between heuristic practical use of Fiat-Shamir and formal ROM security statements, and when does the gap matter?

## Wiki development

- Which future pages should compare Fiat-Shamir with BCS-style transformations more explicitly?
