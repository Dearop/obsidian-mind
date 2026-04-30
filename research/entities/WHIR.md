---
date: 2026-04-10
type: entity
entity_kind: protocol
created: 2026-04-10
updated: 2026-04-14
tags:
  - iopp
  - reed-solomon
  - proof-systems
related:
  - "[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Reed-Solomon Proximity Testing]]"
description: "Fast-verifier constrained-RS IOPP and compiler substrate"
---

# WHIR

## Who / what it is

WHIR is an **interactive oracle proof of proximity** for **constrained Reed–Solomon codes**, introduced in *[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]*.

Its defining goal is unusually fast verification, especially for the hash-based SNARG compilation pipeline.

## Relevance to this wiki

WHIR is currently the clearest modern anchor in the vault for:
- Reed–Solomon proximity testing,
- hash-based SNARG verifier optimization,
- constrained code constructions,
- and the compiler layer between multilinear/poly-IOPs and deployed proof systems.

## Associated sources

- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related concepts

- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[Constrained Reed-Solomon Codes]]
- [[Polynomial Commitments]]
- [[RS IOPP and STARK Lineage]]

## Notes

A useful one-line memory hook:
- WHIR is a **fast-verifier constrained-RS IOPP** that aims to replace FRI/STIR/BaseFold-like components in hash-based SNARG pipelines.
