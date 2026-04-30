---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-13
tags:
  - proof-systems
  - iop
  - cryptography
related:
  - "[[WHIR]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[Polynomial Commitments]]"
description: "Oracle-based proof model central to hash-based SNARG and STARK-style compilation"
---

# Interactive Oracle Proofs (IOPs)

## Definition / framing

Interactive oracle proofs (IOPs) are proof systems in which the prover sends oracle-accessible messages and the verifier checks them by making queries rather than reading everything in full.

They are a major bridge between classical PCP-style verification and practical modern proof-system compilation.

## Why it matters

This concept sits near the center of the STARK / hash-based SNARG side of the current wiki.

In *[[Interactive Oracle Proofs with Constant Rate and Query Complexity]]*, the IOP model is used to obtain proof-length / query-complexity tradeoffs not known for PCPs or IPs alone, including linear-length constant-query IOPs for circuit satisfiability and linear-length constant-query IOPPs for Reed–Solomon codes.

In *[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]*, IOPs and IOPPs are the primary formal setting. WHIR itself is an IOP of proximity for constrained Reed–Solomon codes, and the paper uses this layer to build efficient compilers and argument systems.

In *[[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]*, holographic IOPs are the bridge from oracle-proof machinery to preprocessing SNARKs and then to recursive composition.

## Key distinctions

- **IOP vs IOPP**
  - [[Interactive Oracle Proofs of Proximity (IOPPs)]] are the specialized case where the verifier checks that an input oracle is close to a target code or relation.
- **poly-IOP / multilinear-IOP variants**
  - Many modern constructions restrict prover messages to polynomial evaluations.
- **Compilation role**
  - IOPs often become non-interactive arguments through transformations such as BCS.


## Mathematical background / formulae

An IOP consists of rounds in which the prover sends oracle messages
$$
O_1,O_2,\dots,O_r
$$
and the verifier adaptively queries a small number of locations across those oracles.
If the verifier makes $q$ total oracle queries, the hope is that verifier work scales more like $\operatorname{poly}(q,\lambda)$ than like the full length of the prover messages.
An IOPP specializes this picture to the case where the verifier checks closeness to a target code or relation.

## Current map in this wiki

This hub connects several branches:
- foundational model paper [[Interactive Oracle Proofs]]
- parameter-improvement / construction paper [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- theorem-level IP-to-IOP bridge [[A PCP Theorem for Interactive Proofs and Applications]]
- delegation-oriented efficiency bridge [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- RS / STARK substrate via [[Interactive Oracle Proofs of Proximity (IOPPs)]], [[FRI]], [[WHIR]], and [[Reed-Solomon Proximity Testing]]
- recursion/compiler bridge via [[Fractal]]
- reduction-oriented contrast via [[Interactive Oracle Proofs (IOPs) vs Interactive Oracle Reductions (IORs)]]
- family comparison via [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]
- mathematical study overview via [[Mathematical Preliminaries for SNARKs and STARKs]]


## Worked example

Imagine the prover sends a very large table $O$ of field elements, but the verifier only queries three locations:
$$
O(i_1),\; O(i_2),\; O(i_3).
$$
If the table is supposed to encode a low-degree polynomial or codeword, then a sound IOP/IOPP argues that passing a small number of random queries is already strong evidence that the full oracle is globally well-formed.

This is the key shift from ordinary proof checking:
- the verifier does **not** read the whole object,
- the verifier relies on structure plus sparse queries.

## Evidence / sources

- [[Interactive Oracle Proofs]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[A PCP Theorem for Interactive Proofs and Applications]]
- [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related entities

- [[WHIR]]
- [[Alessandro Chiesa]]
- [[Eli Ben-Sasson]]

## Open questions

- What is the cleanest conceptual comparison between IOPs and [[Interactive Oracle Reductions (IORs)]]?

## Wiki development

- Should the wiki split IOPs, IOPPs, and poly-IOPs into separate pages after a few more ingests?
