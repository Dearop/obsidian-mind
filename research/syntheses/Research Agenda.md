---
date: 2026-04-10
type: synthesis
status: active
created: 2026-04-10
updated: 2026-04-13
tags:
  - research-agenda
  - study
  - planning
related:
  - "[[Intake Questions]]"
  - "[[Overview]]"
  - "[[SNARKs and STARKs Reading Map]]"
  - "[[Contradictions]]"
description: "Living map of research interests, study priorities, and reading directions across all domains"
---

# Research Agenda

## Scope

This wiki covers **four long-term domains**, all treated as durable interests:

1. **Mathematics** — algebra, number theory, combinatorics, probability, and the mathematical substrates of the other domains.
2. **Cryptography** — proof systems, zero knowledge, commitments, hash-based constructions, post-quantum directions.
3. **Computer Science** — complexity theory, algorithms, verification, programming languages, distributed systems.
4. **AI** — machine learning theory, architectures, interpretability, alignment, applied ML.

The wiki should grow across all four. New source clusters can be added at any time.

## Active Study Branches

### Cryptography: SNARK/STARK proof systems (primary)
The most developed branch. 14 sources ingested, 26 concept pages, 9 syntheses.

**Current focus areas:**
- Transparent proof systems and the trusted-setup vs transparency trade-off
- Classical algebraic foundations: [[Polynomial Identity Testing]], [[Algebraic Methods for Interactive Proof Systems]], [[Sum-check Protocol]]
- Verifiable computation / delegation foundations: [[Checking Computations in Polylogarithmic Time]], [[Delegating Computation Interactive Proofs for Muggles]]
- Reed-Solomon / IOPP / STARK substrate: [[Interactive Oracle Proofs (IOPs)]] → [[FRI]] → [[WHIR]]
- Recursive proof-system design: [[Fractal]], [[WARP]], [[Quasar]], [[Symphony]]
- Zero-knowledge compilers for hash-based systems: [[VEIL]]

**Gaps to fill:**
- PCP and STARK concept pages (load-bearing, no canonical page yet)
- Dedicated concept or synthesis page for verifiable computation / transparent verification
- Canonical synthesis linking classical foundations → PCP/IOP era → modern SNARK/STARK systems
- Broader syntheses: trusted-setup-vs-transparency, concrete cost tradeoffs across systems

**Reading map:** [[SNARKs and STARKs Reading Map]]

### Mathematics (open branch)
Likely future directions:
- algebra and finite-field methods that support cryptography
- probability, combinatorics, coding theory, and number theory
- standalone mathematical sources when they become useful for durable concept pages

### Computer Science (open branch)
Likely future directions:
- complexity theory and verification
- algorithms and randomized computation
- programming languages, distributed systems, and systems papers that connect to proof or verification themes

### AI (open branch)
Likely future directions:
- ML theory and architectures
- interpretability and alignment
- applied ML / systems papers where a durable concept graph is valuable

## Key Researchers and Groups to Track
- [[Srinath Setty]] — Spartan, transparent zkSNARKs
- [[Alessandro Chiesa]] — WHIR, WARP, Fractal, IOPs
- [[Eli Ben-Sasson]] — FRI, IOPs, STARK foundations
- [[Benedikt Bünz]] — accumulation, recursion
- [[Giacomo Fenzi]] — WHIR, WARP
- [[Binyi Chen]] — Symphony, folding
- Shafi Goldwasser, Yael Tauman Kalai, Guy N. Rothblum, László Babai, Lance Fortnow
- Microsoft Research, EPFL, StarkWare

## Recurring Concepts
- [[Transparent zkSNARKs]] | [[Trusted Setup]]
- [[Interactive Oracle Proofs (IOPs)]] | [[FRI]] | [[Reed-Solomon Proximity Testing]]
- [[Polynomial Commitments]] | [[Sum-check Protocol]]
- [[Accumulation Schemes]] | [[Folding Schemes]]
- [[Proof-Carrying Data (PCD)]] | [[Incrementally Verifiable Computation (IVC)]]

## Workflow Expectations
- **Ingest cadence**: one source at a time with review; no batch processing
- **Paper workflow**: formal, ground-truth-focused breakdowns with mathematical definitions, important formulae, and explicit performance bounds where relevant
- **Lighter-source workflow**: articles, talks, podcasts, and lecture notes may use a lighter summary-first format
- **Primary organizing axis**: concepts first; people and systems remain supporting graph nodes
- **Auto-synthesis from queries**: do not create durable synthesis notes automatically from ad hoc Q&A

## Maintenance Rhythm
- **Lint pass**: every 10 ingested sources
- **Contradictions**: tracked in [[Contradictions]], reviewed during lint
- **Suggestions**: LLM should actively suggest missing sources and next papers after each ingest

## Open Questions
- See [[Intake Questions]] for resolved setup decisions
- What are the next paper clusters beyond SNARK/STARK? (user to add sources)
- Where do lattice-based and post-quantum directions fit in the broader map?
- Which first non-cryptography source cluster should the wiki grow next: mathematics, CS verification/systems, or AI?
