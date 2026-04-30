---
date: 2026-04-30
description: "Code families formed by interleaving a base code and imposing extra linear/algebraic constraints, enabling expressive and efficient constrained-code IOPP/IOR constructions."
type: concept
tags:
  - iopp
  - coding-theory
  - interleaving
  - constraints
  - zero-knowledge
related:
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Interactive Oracle Reductions (IORs)]]"
  - "[[Sum-check Protocol]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[Zero-Knowledge IOPPs for Constrained Interleaved Codes]]"
  - "[[WARP]]"
  - "[[WHIR]]"
---

# Constrained Interleaved Codes

## Definition / Framing

A constrained interleaved code starts from a base code $C \subseteq \Sigma^m$, forms an interleaving $C^{\equiv K}$ by stacking $K$ codewords coordinate-wise, and then restricts to words satisfying additional constraints (usually linear/algebraic conditions over underlying message variables).

At the interleaving layer:
$$
u \in C^{\equiv K}\iff \exists v_1,\dots,v_K\in C\ \text{s.t.}\ u(z)=(v_1(z),\dots,v_K(z))\ \forall z\in[m].
$$

The constrained version keeps only interleavings that satisfy side conditions such as succinctly-described linear forms:
$$
\langle \bar f, v\rangle = \mu
$$
or related structured checks used inside IOR/IOPP reductions.

In this wiki, this concept is the primary object behind "constrained-code testing" in modern interleaving-based proof systems.

## Why It Matters

- It bridges "pure code proximity testing" and "relation-specific proving": constraints encode statement structure without abandoning efficient code-based machinery.
- It lets modern IOPP/IOR designs avoid a large privacy tax by integrating HVZK-friendly masking/composition around constrained checks.
- It is a key route from low-level coding primitives to higher-level relations such as [[Rank-1 Constraint Satisfiability (R1CS)]].

## Key Distinctions

- **Unconstrained interleaved code**: only checks membership in $C^{\equiv K}$.
- **Constrained interleaved code**: checks membership plus additional relation constraints.
- **Tensor-code route vs interleaving route**: tensoring can favor local testability/query optimality; interleaving often preserves base-code rate/distance characteristics while growing alphabet and enabling efficient code-agnostic transformations.
- **RS-constrained vs general-code constrained**: RS-based constructions (e.g. WHIR-style constrained RS) and general-code interleaving constructions share a constrained-code viewpoint but use different algebraic substrates and trade-offs.

## Mathematical Background

### Interleaving

If $C\subseteq\Sigma^m$, then $C^{\equiv K}\subseteq(\Sigma^K)^m$ is obtained by stacking $K$ codewords. This preserves much of the base-code structure while changing alphabet size.

### Constraint relation viewpoint

A common formal pattern is to define a relation over encoded witnesses:
$$
R^{\mathrm{lin}}_{C,T}=\{(x,y,w): y=\mathrm{Enc}_C(\bar f,r)\ \wedge\ \langle \bar f,v\rangle=\mu\},
$$
with succinctly represented $v$ and complexity parameter $T$ for evaluating derived linear forms.

### Zero-knowledge layer

The privacy layer typically relies on zero-knowledge encodings for the code:
$$
\mathrm{Enc}_C:F^\ell\times F^r\to\Sigma^m,
$$
plus simulator-compatible composition across reductions (not just a single terminal protocol). This is where IOR-specific HVZK definitions become important.

## Evidence / Sources

- [[Zero-Knowledge IOPPs for Constrained Interleaved Codes]] - primary source for HVZK IOPP/IOR formulation over constrained interleaved codes.
- [[WARP Linear-Time Accumulation Schemes]] - related interleaving/code-switching reduction perspective in accumulation contexts.
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]] - constrained-code worldview on the RS side; useful contrast for substrate-level trade-offs.

## Current Map in This Wiki

- This concept links [[Interactive Oracle Proofs of Proximity (IOPPs)]] and [[Interactive Oracle Reductions (IORs)]].
- It is a bridge between code-level primitives and statement-level reductions like [[Rank-1 Constraint Satisfiability (R1CS)]].
- It should feed future syntheses comparing interleaving-based constrained-code systems against RS-constrained systems and multilinear/sum-check systems.

## Related
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Sum-check Protocol]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Zero-Knowledge IOPPs for Constrained Interleaved Codes]]
- [[WARP]]
- [[WHIR]]
