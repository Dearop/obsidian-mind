---
date: 2026-04-10
type: entity
entity_kind: protocol
created: 2026-04-10
updated: 2026-04-10
tags:
  - folding
  - recursion
  - post-quantum
related:
  - "[[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]"
  - "[[Folding Schemes]]"
  - "[[High-Arity Folding]]"
description: "High-arity folding-based SNARK avoiding Fiat–Shamir circuits inside proved statements"
---

# Symphony

## Who / what it is

Symphony is a **folding-based SNARK** introduced in *[[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]*.

Its defining idea is to use **high-arity folding** together with a **commit-and-prove compiler** so that random-oracle / Fiat–Shamir logic does not need to be embedded inside the proved SNARK statements.

## Relevance to this wiki

Symphony is currently the main folding-oriented anchor in the recursion branch of the wiki.

A useful memory hook is:
- [[WARP]] = accumulation foundation,
- [[Quasar]] = multi-instance verifier-overhead optimization,
- **Symphony** = high-arity folding plus hash-avoidance inside recursive circuits.

## Associated sources

- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]

## Related concepts

- [[Folding Schemes]]
- [[High-Arity Folding]]
- [[Commit-and-Prove SNARKs]]
- [[Incrementally Verifiable Computation (IVC)]]

## Notes

This page should become richer once the wiki adds a broader synthesis comparing accumulation-based and folding-based recursion.
