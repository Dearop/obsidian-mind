---
date: 2026-04-10
type: index
created: 2026-04-10
updated: 2026-04-30
tags:
  - wiki
  - navigation
description: "A compact catalog of the current wiki. Start here when navigating the vault"
---

# Index

A compact catalog of the current wiki. Start here when navigating the vault.

## Overview
- [[Overview]] — Top-level map of the wiki, workflow, and current priorities.
- [[research/Index|Index]] is also embedded from [[Home]] as the main research navigation hub.

## Syntheses
- [[Research Agenda]] — Initial scaffold for the user's interests, study directions, and reading priorities.
- [[SNARKs and STARKs Reading Map]] — Topic clusters, reading paths, and ingest strategy for the SNARK/STARK paper collection.
- [[Mathematical Preliminaries for SNARKs and STARKs]] — Compact study guide to the main algebraic objects, proof templates, and formulae used across the current SNARK/STARK branch.
- [[Interactive Oracle Proofs (IOPs) vs Interactive Oracle Reductions (IORs)]] — Structural comparison between oracle-based proof systems and oracle-based accumulation/reduction systems.
- [[FRI vs WHIR]] — Comparison of the canonical FRI foundation against the newer verifier-optimized WHIR design.
- [[Quasar vs WARP]] — Comparison of linear-time hash-based accumulation against sublinear-verifier multi-instance accumulation.
- [[Accumulation vs Folding in Recursive Proof Systems]] — Recursion-branch map comparing accumulation-based and folding-based design strategies.
- [[VEIL vs Spartan vs Fractal]] — Comparison of three architectural routes to practical transparent zero knowledge: native design, recursive architecture, and lightweight zk compilation.
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]] — Comparison of relation-centric multilinear/sum-check systems against code-centric RS/FRI/IOPP systems.
- [[Transparent Verification and Verifiable Computation]] — Historical and conceptual synthesis of cheap-verification goals from classical transparent proofs through delegation and recursive proof systems.
- [[PCP vs MIP vs IOP Lineage]] — Synthesis of the conceptual evolution from multi-prover and locally checkable proof models to oracle-based interactive proof systems.
- [[RS IOPP and STARK Lineage]] — Historical map of the Reed–Solomon / IOPP branch from oracle-proof abstractions to modern STARK-style compiler substrates.

## Sources
- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]] — Foundational source page for transparent zkSNARKs over arbitrary R1CS with sub-linear verification.
- [[Interactive Oracle Proofs]] — Foundational IOP paper linking PCPs, IPs, random-oracle compilation, and state restoration security.
- [[Algebraic Methods for Interactive Proof Systems]] — Classical algebraic IP paper introducing the sum-check worldview and proving polynomial-hierarchy languages admit interactive proofs.
- [[Fast Probabilistic Algorithms for Verification of Polynomial Identities]] — Classical paper on randomized polynomial identity testing and related algebraic verification methods.
- [[Checking Computations in Polylogarithmic Time]] — Classical bridge paper on transforming computations and proofs into forms checkable in polylogarithmic Monte Carlo time.
- [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]] — Classical MIP paper proving that two-prover interactive proofs characterize nondeterministic exponential time.
- [[Probabilistic checking of proofs; a new characterization of NP]] — Arora–Safra PCP-theorem milestone, serving here as a historically important precursor to the later constant-query PCP theorem paper.
- [[Proof Verification and the Hardness of Approximation Problems]] — Landmark PCP paper proving NP has verifiers with logarithmic randomness and constant query complexity, with major approximation-hardness consequences.
- [[Delegating Computation Interactive Proofs for Muggles]] — Bridge paper on delegating computation with efficient provers and super-efficient public-coin verification.
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]] — IOP paper showing constant-round oracle proofs can achieve linear proof length with constant query complexity and introducing IOP composition and sublinear sumcheck tools.
- [[A PCP Theorem for Interactive Proofs and Applications]] — Paper extending the PCP theorem viewpoint to public-coin interactive proofs via local-query IOPs, with applications to SNARKs and approximation hardness.
- [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]] — PCP paper focused on asymptotic and concrete efficiency, introducing a concrete-efficiency threshold and improving Reed–Solomon PCP-of-proximity practicality.
- [[Linear-Size Constant-Query IOPs for Delegating Computation]] — IOP paper for delegation of computation achieving linear-size proofs, constant query complexity, and polylogarithmic verifier time for rich classes of algebraic computations.
- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]] — Foundational FRI paper for linear-time Reed–Solomon proximity testing in transparent systems.
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]] — Modern IOPP for constrained Reed–Solomon codes with unusually fast verification.
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]] — Bridge paper connecting holographic IOPs, preprocessing SNARKs, and transparent post-quantum recursion.
- [[WARP Linear-Time Accumulation Schemes]] — Accumulation-scheme anchor for linear-time proving and recursive/PCD composition.
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]] — Multi-instance accumulation / IVC paper targeting sublinear verifier dependence on accumulated instances.
- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]] — Folding-based SNARK anchor built around high-arity lattice folding and commit-and-prove compilation.
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]] — Lightweight compiler for adding zero knowledge to hash-based multilinear proof systems.
- [[Zero-Knowledge IOPPs for Constrained Interleaved Codes]] — HVZK IOPP framework for constrained interleaved codes with composable IOR privacy and near-zero overhead.
- [[HyperPlonk Plonk with Linear-Time Prover and High-Degree Custom Gates]] — Plonk-on-hypercube multilinear proof system with FFT-free prover flow and stronger high-degree custom-gate handling.

## Concepts
- [[zkSNARKs]] — Umbrella concept page for zero-knowledge succinct non-interactive arguments of knowledge.
- [[Transparent zkSNARKs]] — Focus page for setup-free/trapdoor-free SNARK design.
- [[Trusted Setup]] — Setup-assumption page clarifying the contrast between toxic-waste ceremonies and transparent/public preprocessing.
- [[Rank-1 Constraint Satisfiability (R1CS)]] — Core arithmetization target used by Spartan.
- [[Polynomial Commitments]] — Commitment primitive family underlying many succinct proof trade-offs.
- [[Computation Commitments]] — Spartan's public-preprocessing primitive for amortized sub-linear verification.
- [[SPARK]] — Compiler for efficient sparse multilinear polynomial handling.
- [[Polynomial Identity Testing]] — Randomized method for checking whether a polynomial expression is identically zero by evaluating it at random points.
- [[Probabilistically Checkable Proofs (PCPs)]] — Proof model where a verifier uses randomness and a constant number of proof queries to check correctness with high confidence.
- [[Sum-check Protocol]] — Classical interactive-proof primitive reused inside Spartan.
- [[Interactive Oracle Proofs (IOPs)]] — Oracle-based proof model central to hash-based SNARG and STARK-style compilation.
- [[Interactive Oracle Proofs of Proximity (IOPPs)]] — Oracle-proof model where the verifier checks closeness of an input oracle to a target code or relation using interaction plus sparse queries.
- [[Reed-Solomon Proximity Testing]] — Core RS/IOPP substrate for modern transparent and hash-based proof systems.
- [[Constrained Reed-Solomon Codes]] — WHIR's richer code abstraction for sumcheck-like constraints.
- [[FRI]] — Foundational fast Reed–Solomon proximity-testing protocol underlying many transparent systems.
- [[Fiat-Shamir Transform]] — Core random-oracle compiler idea linking interactive proofs to non-interactive arguments.
- [[State Restoration Attacks]] — Rewinding-style soundness notion used to analyze IOP-to-NIROP compilation.
- [[Holographic Proofs]] — Oracle-indexed proof model that enables preprocessing-style succinct verification.
- [[Preprocessing SNARKs]] — Offline/online SNARK architecture central to Fractal's recursion strategy.
- [[Accumulation Schemes]] — Recursive-composition primitive for carrying many verification obligations forward.
- [[Proof-Carrying Data (PCD)]] — Distributed integrity setting motivating accumulation and recursive proof composition.
- [[Incrementally Verifiable Computation (IVC)]] — Stepwise proof-carrying computation model closely tied to recursion.
- [[Interactive Oracle Reductions (IORs)]] — Reduction-oriented oracle protocols central to WARP's compiler stack.
- [[Polynomial Equation Satisfiability (PESAT)]] — WARP's NP-complete algebraic target relation.
- [[Folding Schemes]] — Recursive-composition primitive that compresses many statements into one combined statement.
- [[High-Arity Folding]] — Folding strategy that trades recursion depth for larger one-shot batching.
- [[Commit-and-Prove SNARKs]] — Compiler pattern used by Symphony to avoid embedding Fiat–Shamir logic in recursive statements.
- [[Multilinear Interactive Oracle Proofs (MIOPs)]] — Useful abstraction for multilinear hash-based proof systems and their zk compilers.
- [[Constrained Interleaved Codes]] — Interleaving-based constrained-code object for modern code-agnostic IOPP/IOR constructions.

## Systems
- [[Spartan]] — Proof-system family introduced in the Spartan paper.
- [[WHIR]] — Fast-verifier constrained-RS IOPP and compiler substrate.
- [[WARP]] — Linear-time hash-based accumulation scheme for recursion and proof composition.
- [[Quasar]] — Multi-instance accumulation / IVC construction targeting sublinear verifier dependence on accumulated instances.
- [[Fractal]] — Transparent post-quantum recursive-proof methodology built from holography and preprocessing.
- [[Symphony]] — High-arity folding-based SNARK avoiding Fiat–Shamir circuits inside proved statements.
- [[VEIL]] — Lightweight zk compiler for hash-based multilinear proof systems.
- [[HyperPlonk]] — Plonk-family multilinear protocol over the Boolean hypercube emphasizing linear-time proving.

## Researchers (in `org/people/`)
- [[Srinath Setty]] — Researcher associated with Spartan and related proof-system work.
- [[Alessandro Chiesa]] — Recurring proof-systems researcher appearing across WHIR and WARP.
- [[Benedikt Bünz]] — Researcher associated with accumulation and recursion-oriented proof systems.
- [[Eli Ben-Sasson]] — Foundational IOP / PCP / STARK-side researcher.
- [[Nicholas Spooner]] — Coauthor of the Interactive Oracle Proofs paper and Fractal.
- [[Giacomo Fenzi]] — Coauthor appearing in both WHIR and WARP.
- [[Gal Arnon]] — WHIR coauthor.
- [[Eylon Yogev]] — WHIR coauthor.
- [[William Wang]] — WARP coauthor.
- [[Iddo Bentov]] — FRI coauthor.
- [[Ynon Horesh]] — FRI coauthor.
- [[Michael Riabzev]] — FRI coauthor.
- [[Dev Ojha]] — Fractal coauthor.
- [[Tianyu Zheng]] — Quasar coauthor.
- [[Shang Gao]] — Quasar coauthor.
- [[Yu Guo]] — Quasar coauthor.
- [[Bin Xiao]] — Quasar coauthor.
- [[Binyi Chen]] — Author of the Symphony paper.
- [[Rahul Dalal]] — VEIL coauthor.
- [[Tamir Hemo]] — VEIL coauthor.
- [[Eugene Rabinovich]] — VEIL coauthor.
- [[Ron D. Rothblum]] — VEIL coauthor.

## Open Questions
- [[Intake Questions]] — Resolved intake questions capturing user preferences for scope, rigour, workflow, and maintenance.

## Maintenance
- [[Contradictions]] — Tracked disagreements between sources, reviewed and cleared during lint passes.
