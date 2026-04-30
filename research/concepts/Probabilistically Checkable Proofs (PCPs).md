---
date: 2026-04-13
type: concept
created: 2026-04-13
updated: 2026-04-13
tags:
  - pcp
  - proof-systems
  - complexity-theory
  - local-checking
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Checking Computations in Polylogarithmic Time]]"
  - "[[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]"
  - "[[Transparent Verification and Verifiable Computation]]"
description: "Proof model in which a verifier uses randomness and queries only a few bits of a proof while still checking correctness with high confidence"
---

# Probabilistically Checkable Proofs (PCPs)

## Definition / framing

A probabilistically checkable proof (PCP) is a proof representation that allows a randomized verifier to decide correctness by reading only a **small number of proof locations**, rather than scanning the whole proof.

The verifier uses random bits to choose which positions to inspect. If the statement is true, there exists a proof that the verifier always or almost always accepts. If the statement is false, then every purported proof is rejected with noticeable probability despite the verifier seeing only a tiny part of it.

In the current wiki, PCPs are one of the key middle layers between:
- classical interactive / multi-prover proof complexity,
- local checking and transparent verification,
- and later oracle-based proof models such as [[Interactive Oracle Proofs (IOPs)]].

## Why it matters

PCPs matter because they made **extreme local verification** feel mathematically natural and complexity-theoretically robust.

They are one of the main conceptual reasons modern proof systems can ask for verifiers that:
- use very little randomness,
- inspect very little of the proof object,
- and still obtain strong soundness guarantees.

In the current branch, PCPs help connect several seemingly different themes:
- the local-checking vision in [[Checking Computations in Polylogarithmic Time]],
- the multi-prover expressiveness results in [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]],
- the oracle-message abstractions of [[Interactive Oracle Proofs (IOPs)]],
- and the practical question of when PCPs stop being only asymptotically attractive and become concretely useful, as emphasized in [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]].

## Key distinctions

- **NP verifier vs PCP verifier**
  - An ordinary NP verifier reads the witness in full polynomial time.
  - A PCP verifier reads only a few bits or symbols of a much more structured proof.
- **PCP vs MIP**
  - A multi-prover interactive proof uses several isolated provers and interaction.
  - A PCP can be viewed as a noninteractive locally testable proof object.
- **PCP vs IOP**
  - PCPs are static proof objects queried by the verifier.
  - IOPs add rounds of interaction while keeping oracle access to prover messages.

## Mathematical background / formulae

The slogan form of the PCP theorem is often written as
$$
NP = PCP(O(\log n), O(1)),
$$
meaning that every NP language has a verifier that uses logarithmically many random bits and queries only a constant number of proof locations.

This is remarkable because the verifier's randomness and query complexity are both tiny compared with the length of the full proof.

## Worked example

A full realistic PCP construction is too elaborate for a toy example here, but the mental model is:
- encode a witness into a highly redundant proof object,
- arrange the encoding so local inconsistencies reveal global falsehood,
- let the verifier sample a tiny number of locations,
- and rely on the structure of the encoding to ensure that a fake proof is likely to be caught.

This is the same broad verification pattern that later reappears in oracle-proof and proximity-testing systems, though with different mathematical packaging.

## Evidence / sources

- [[Probabilistic checking of proofs; a new characterization of NP]]
- [[Proof Verification and the Hardness of Approximation Problems]]
- [[A PCP Theorem for Interactive Proofs and Applications]]
- [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]]
- [[Interactive Oracle Proofs]]
- [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]

## Current map in this wiki

This page should become the canonical hub for the PCP layer connecting:
- [[Probabilistic checking of proofs; a new characterization of NP]] as the Arora–Safra milestone precursor
- [[Proof Verification and the Hardness of Approximation Problems]] as a later constant-query PCP-theorem / hardness landmark
- [[A PCP Theorem for Interactive Proofs and Applications]] as the theorem-level extension of the PCP viewpoint into interactive settings
- [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]] as the practicality / threshold-oriented reality check on positive PCP applications
- [[Checking Computations in Polylogarithmic Time]] as an earlier transparent-verification precursor
- [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]] as a nearby MIP landmark
- [[Interactive Oracle Proofs (IOPs)]] as a later oracle-based generalization
- [[PCP vs MIP vs IOP Lineage]] as the formal-model synthesis linking these traditions
- [[Transparent Verification and Verifiable Computation]] as the broader asymmetry-oriented synthesis

## Related entities

- [[Interactive Oracle Proofs (IOPs)]]

## Open questions

- When should the wiki split PCP theorem content from approximation-hardness consequences into separate concept or synthesis pages?
- What is the clearest way to explain the exact conceptual relationship among PCPs, MIPs, IOPs, and IOPPs without flattening their differences?

## Wiki development

- This page should be strengthened after one or two more PCP-theorem anchor papers are ingested.
- A later dedicated synthesis on PCP / MIP / IOP lineage is likely warranted.
