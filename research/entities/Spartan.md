---
date: 2026-04-10
type: entity
entity_kind: proof-system
created: 2026-04-10
updated: 2026-04-10
tags:
  - zksnark
  - transparent
  - proof-system
related:
  - "[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]"
  - "[[zkSNARKs]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
description: "Proof-system family introduced in the Spartan paper"
---

# Spartan

## Who / what it is

Spartan is a family of zkSNARK constructions introduced by [[Srinath Setty]] in *[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]*.

The system is designed for proving statements expressed as [[Rank-1 Constraint Satisfiability (R1CS)]], with a particular emphasis on **transparent zkSNARKs** that avoid trusted setup while still achieving **sub-linear verification** for arbitrary NP statements.

## Relevance to this wiki

Spartan is currently the first concrete anchor system in the vault's SNARK/STARK reading thread.

It matters because it ties together several recurring proof-system ideas:
- sum-check-based arguments,
- low-degree encodings of R1CS,
- polynomial commitments,
- transparent verifier preprocessing,
- and the distinction between trusted setup and public preprocessing.

## Associated sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related concepts

- [[zkSNARKs]]
- [[Transparent zkSNARKs]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Polynomial Commitments]]

## Notes

A useful one-line memory hook:
- Spartan is the **transparent zkSNARK that proved you don't need a trusted setup for general-purpose R1CS** — it uses sum-check over multilinear extensions instead of pairings, achieving sub-linear verification for arbitrary NP statements.

Additional remembered summary:
- Spartan's headline idea is not just “transparent SNARKs,” but **transparent SNARKs with sub-linear verification for arbitrary R1CS/NP statements**, enabled in part by computation commitments.
