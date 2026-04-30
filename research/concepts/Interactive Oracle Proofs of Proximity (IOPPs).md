---
date: 2026-04-14
type: concept
created: 2026-04-14
updated: 2026-04-14
tags:
  - iopp
  - iop
  - proof-systems
  - reed-solomon
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[FRI]]"
  - "[[WHIR]]"
  - "[[RS IOPP and STARK Lineage]]"
description: "Oracle-proof model where the verifier checks that an input oracle is close to a target code or relation using interaction plus sparse oracle queries"
---

# Interactive Oracle Proofs of Proximity (IOPPs)

## Definition / framing

An **interactive oracle proof of proximity (IOPP)** is an interactive oracle proof in which the verifier wants to decide whether an input oracle is **close** to some target code or relation.

So an IOPP is not just checking an arbitrary statement from scratch. Instead, it starts with oracle-accessible data already on the table and asks whether that data is near a structured object the verifier cares about.

In the current wiki, the most important target family is **Reed–Solomon codes**, which is why IOPPs sit at the center of the RS / STARK substrate branch.

## Why it matters

IOPPs matter because they are one of the cleanest formal models for the transparent-proof engine used by many STARK-style systems.

They explain how a verifier can:
- treat large prover data as oracle-accessible structure,
- make only sparse local queries,
- and still obtain confidence that the data is globally close to a valid low-degree or codeword object.

In the current branch, IOPPs are the model layer connecting:
- [[Interactive Oracle Proofs (IOPs)]] as the broader oracle-proof abstraction,
- [[Reed-Solomon Proximity Testing]] as the main substrate problem,
- [[FRI]] as the foundational practical engine,
- and [[WHIR]] as a modern verifier-optimized refinement.

## Key distinctions

- **IOP vs IOPP**
  - An IOP is the broader model: the verifier interacts with oracle messages and checks some statement.
  - An IOPP is the specialized case where the verifier checks whether an input oracle is close to a target code or relation.
- **Static PCP vs IOPP**
  - PCPs give a static proof object queried locally.
  - IOPPs preserve oracle-style local querying, but allow interaction across rounds.
- **Low-degree testing vs full proof system**
  - Many important IOPPs are not full standalone SNARKs; they are proximity-testing engines or proof-system subroutines.

## Mathematical background / formulae

A generic proximity-testing goal looks like this.

Let $C \subseteq \mathbb{F}^N$ be a code or structured relation, and let the verifier have oracle access to
$$
w \in \mathbb{F}^N.
$$
The verifier wants to know whether
$$
\operatorname{dist}(w, C)
$$
is small, where distance is usually Hamming distance or normalized Hamming distance.

For Reed–Solomon proximity testing, the target set has the form
$$
RS_{D,d}=\{(f(\alpha))_{\alpha\in D} : \deg f < d\}.
$$
Then the IOPP verifier tries to decide whether the oracle word $w$ is close to this code while querying only a small number of coordinates and interacting over a few rounds.

## Worked example

Suppose a verifier expects an oracle to encode evaluations of a low-degree polynomial on a domain $D$.

If the oracle is
$$
w=(1,3,5,7),
$$
and there is a low-degree polynomial whose evaluations on $D$ match this word exactly, then the proximity claim is easy: the oracle is in the code.

If instead the oracle is
$$
w'=(1,3,5,20),
$$
then the verifier wants to know whether this word is still close to some codeword, or whether the discrepancy indicates that the oracle is globally malformed.

An IOPP gives a protocol where the verifier does not read every coordinate of a huge real-world oracle, but instead uses interaction and sparse queries to estimate whether the oracle is globally near a valid structured object.

## Current map in this wiki

This page should serve as the canonical hub for the IOPP layer connecting:
- [[Interactive Oracle Proofs (IOPs)]] as the broader parent model
- [[Reed-Solomon Proximity Testing]] as the main target problem in the current corpus
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]] as an important IOPP parameter-improvement source
- [[Linear-Size Constant-Query IOPs for Delegating Computation]] as a delegation-oriented oracle-proof construction built from Reed–Solomon codeword structure
- [[FRI]] as the foundational RS-IOPP engine
- [[WHIR]] as a modern constrained-RS IOPP refinement
- [[RS IOPP and STARK Lineage]] as the historical substrate synthesis

## Evidence / sources

- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[Interactive Oracle Proofs]]

## Related entities

- [[FRI]]
- [[WHIR]]

## Open questions

- When should the wiki split generic IOPPs from Reed–Solomon-specific IOPPs more explicitly?
- How much of the current STARK lineage is best understood at the level of generic IOPP theory versus specialized RS / constrained-RS constructions?

## Wiki development

- As the RS branch grows, this page should become the main concept bridge between [[Interactive Oracle Proofs (IOPs)]] and [[Reed-Solomon Proximity Testing]].
- A later pass may want to compare IOPPs more explicitly against PCPPs, LDTs, and other local-testing abstractions once more sources are ingested.
