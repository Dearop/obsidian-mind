---
date: 2026-04-10
type: entity
entity_kind: protocol
created: 2026-04-10
updated: 2026-04-10
tags:
  - accumulation
  - ivc
  - recursion
related:
  - "[[Quasar Sublinear Accumulation Schemes for Multiple Instances]]"
  - "[[Accumulation Schemes]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Multi-instance accumulation / IVC construction targeting sublinear verifier dependence on accumulated instances"
---

# Quasar

## Who / what it is

Quasar is a **multi-instance accumulation / IVC construction** introduced in *[[Quasar Sublinear Accumulation Schemes for Multiple Instances]]*.

Its defining goal is to reduce recursion overhead by obtaining **sublinear verifier complexity in the number of accumulated instances**.

## Relevance to this wiki

Quasar is currently the strongest counterpoint to [[WARP]] in the recursion / accumulation branch.

A useful memory hook is:
- [[WARP]] emphasizes **linear-time accumulation proving** in a broad hash-based setting.
- **Quasar** emphasizes **sublinear verifier dependence on the number of accumulated instances** in multi-instance IVC.

## Associated sources

- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]

## Related concepts

- [[Accumulation Schemes]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[Polynomial Commitments]]

## Notes

This page should become richer once the wiki adds a dedicated synthesis comparing Quasar and WARP.
