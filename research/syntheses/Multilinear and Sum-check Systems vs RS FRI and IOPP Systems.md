---
date: 2026-04-11
type: synthesis
status: stable
created: 2026-04-11
updated: 2026-04-11
tags:
  - multilinear
  - sum-check
  - fri
  - iopp
  - comparison
  - snarks
  - starks
related:
  - "[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]"
  - "[[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]"
  - "[[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]"
  - "[[Sum-check Protocol]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[FRI]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]"
  - "[[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]"
description: "Comparison of relation-centric multilinear/sum-check systems against code-centric RS/FRI/IOPP systems"
---

# Multilinear and Sum-check Systems vs RS FRI and IOPP Systems

## Thesis / purpose

This page compares two major design families that now appear clearly in the wiki:

- **multilinear / sum-check systems**, represented most clearly by [[Spartan]] and parts of [[VEIL]],
- **RS / FRI / IOPP systems**, represented most clearly by [[FRI]], [[WHIR]], and the broader [[Interactive Oracle Proofs (IOPs)]] branch.

These are not perfectly disjoint camps, and some papers bridge them. But the distinction is still one of the most useful ways to organize the field.

A durable summary is:

> **Multilinear / sum-check systems tend to reason directly about multilinear encodings of computation, while RS / FRI / IOPP systems tend to reason about oracle-accessible codewords and low-degree proximity.**

Or even shorter:

> **Multilinear systems center the algebraic relation; RS/FRI systems center the codeword and its proximity test.**

## Main takeaways

- [[Spartan]] is the clearest anchor for the **multilinear / sum-check** worldview in the current corpus.
- [[FRI]] is the clearest anchor for the **RS / proximity-testing** worldview.
- [[WHIR]] is a modern refinement of the RS / IOPP branch, not a replacement for the multilinear branch.
- [[VEIL]] is useful because it shows that many practical multilinear hash-based systems have their own recognizable compiler structure.
- [[Fractal]] is a bridge paper because it uses **FRI / RS-encoded verifier infrastructure** inside a broader recursive transparent architecture.
- The two families often optimize different bottlenecks:
  - multilinear systems often emphasize compact algebraic checking for arbitrary relations such as R1CS,
  - RS/FRI systems often emphasize scalable oracle proofs, low-degree testing, and transparent hash-based compilation.

## Comparison / synthesis

| Axis | Multilinear / sum-check systems | RS / FRI / IOPP systems |
|---|---|---|
| Canonical intuition | Verify algebraic identities over multilinear extensions | Verify proximity to low-degree / Reed–Solomon codewords |
| Current anchors in this wiki | [[Spartan]], [[Sum-check Protocol]], [[SPARK]], parts of [[VEIL]] | [[Interactive Oracle Proofs]], [[FRI]], [[Reed-Solomon Proximity Testing]], [[WHIR]] |
| Core object | Multilinear polynomials, sparse multilinear structure, R1CS encodings | Reed–Solomon codewords, oracle layers, proximity proofs |
| Verifier worldview | Algebraic reduction via sum-check and evaluation claims | Oracle queries plus low-degree / proximity testing |
| Typical proof substrate | Multilinear commitments / evaluations | IOPs, IOPPs, FRI-like recursive reductions, Merkle/oracle compilation |
| Strength in current corpus | Arbitrary R1CS / NP-friendly algebraic modeling | Transparent hash-based scalability and strong STARK-style substrate |
| Common bottleneck focus | Commitment support for sparse/multilinear structure | Query complexity, verifier hash cost, proximity-testing efficiency |
| Representative refinement in current corpus | [[SPARK]] for sparse multilinear commitments | [[WHIR]] for constrained-RS fast verification |

## The multilinear / sum-check worldview

## Core idea

The multilinear branch starts from the computation relation itself.

In the current corpus, the clearest example is [[Spartan]], which:
- starts from [[Rank-1 Constraint Satisfiability (R1CS)]],
- encodes it as a low-degree algebraic object,
- and uses the [[Sum-check Protocol]] plus polynomial-evaluation checks to verify the relation succinctly.

The core feeling of this branch is:
- represent the computation directly as algebra,
- reduce correctness to polynomial identities and evaluations,
- and make the commitment machinery fit the multilinear structure.

## Why it is attractive

This branch looks especially natural when:
- the target relation is already expressed as R1CS or a similar algebraic relation,
- arbitrary NP statements matter,
- sparse structure matters,
- and the system designer wants tight control over how the computation relation is algebraized.

This is why [[Spartan]] feels so relation-centric.

## What the current corpus emphasizes here

### 1. Sum-check as the backbone
In [[Spartan]], sum-check is the main interactive skeleton.

### 2. Sparse multilinear commitment support matters a lot
[[SPARK]] exists because the commitment layer is not incidental; efficiently handling sparse multilinear polynomials changes prover cost materially.

### 3. Multilinear systems can still be hash-based and compiler-friendly
[[VEIL]] shows that many practical multilinear hash-based systems share a recognizable structure:
- commit to multilinear trace data,
- run an algebraic interaction,
- reduce to multilinear evaluation claims,
- then handle zero knowledge with a lightweight wrapper.

So the multilinear branch is not only “old-school algebra.” It also has a modern systems/compiler form.

## The RS / FRI / IOPP worldview

## Core idea

The RS / FRI branch starts less from the original computation relation and more from the question:

> can the verifier cheaply check that oracle-accessible data behaves like a low-degree codeword, or is close to one?

In the current corpus, the canonical progression is:
- [[Interactive Oracle Proofs]] for the model,
- [[FRI]] for the key Reed–Solomon proximity engine,
- [[WHIR]] for a later constrained-RS, verifier-optimized refinement.

The core feeling of this branch is:
- expose structured oracle data,
- query it sparsely,
- use low-degree / proximity structure to get confidence,
- and compile the whole thing into a transparent hash-based argument.

## Why it is attractive

This branch looks especially natural when:
- transparency is a top priority,
- one wants a STARK-like or hash-based pipeline,
- low-degree testing and oracle access are central abstractions,
- and system performance depends heavily on proximity-testing efficiency.

## What the current corpus emphasizes here

### 1. FRI as the canonical engine
[[FRI]] made RS proximity testing practical enough to serve as a real systems substrate.

### 2. WHIR as the modern refinement
[[WHIR]] shows that even after FRI, this layer remains highly optimizable:
- verifier time,
- query structure,
- constrained code expressiveness,
- and compiler-friendliness are all still active fronts.

### 3. IOPs as the surrounding proof model
[[Interactive Oracle Proofs (IOPs)]] provide the model-level language that makes this whole branch coherent.

## The most useful distinction: what is the verifier fundamentally checking?

This is the cleanest durable comparison.

### In multilinear / sum-check systems
The verifier is fundamentally checking that a claimed algebraic relation about a multilinear encoding is consistent.

The interactive logic often feels like:
- reduce a large algebraic sum/identity claim,
- collapse it to smaller claims,
- and verify a few evaluation facts against commitments.

### In RS / FRI / IOPP systems
The verifier is fundamentally checking that oracle data is close to a structured low-degree codeword and that various local queries are mutually consistent.

The interactive logic often feels like:
- ask about codeword behavior,
- reduce to smaller proximity claims,
- and use sparse oracle access plus code structure to obtain confidence.

This is why the two families feel different even when both are “algebraic” and “transparent.”

## Where the current corpus shows overlap

The branch boundary is useful, but not absolute.

### Fractal as a bridge
[[Fractal]] is important precisely because it connects these worlds:
- it lives in the transparent recursive / preprocessing world,
- uses holographic IOP machinery,
- and its verifier infrastructure explicitly leans on **FRI** and RS-encoded IOP structure.

So Fractal reminds us that the RS/FRI branch is not only about “STARKs” in a narrow sense; it also feeds into broader recursive proof architectures.

### VEIL as another bridge-like signal
[[VEIL]] sits closer to the multilinear side, but it explicitly references proximity layers such as BaseFold and [[WHIR]].

So even practical multilinear hash-based systems may depend on RS / constrained-RS machinery at their commitment/proximity layer.

## Design trade-off intuition

## Multilinear / sum-check systems tend to shine when:
- the relation itself is the natural unit of abstraction,
- arbitrary R1CS support matters,
- sparse multilinear structure can be exploited,
- and one wants a clean algebraic reduction from computation to evaluation claims.

## RS / FRI / IOPP systems tend to shine when:
- transparency and hash-based compilation are central,
- one wants scalable oracle-proof infrastructure,
- one cares a lot about low-degree/proximity efficiency,
- and the system is naturally organized around codewords, queries, and low-degree tests.

## Practical mental model

A simple way to remember the distinction:

### Ask:
> what is the main heavy object that the verifier is reasoning about?

If the answer is:
- “a multilinear encoding of the computation relation” → think **multilinear / sum-check**.
- “an oracle-accessible codeword whose low-degree structure must be checked” → think **RS / FRI / IOPP**.

## Tensions / contradictions

### Relation-centric vs code-centric design
- Multilinear systems feel more relation-centric.
- RS/FRI systems feel more code-centric.

### Commitment bottlenecks vs proximity bottlenecks
- In multilinear systems, commitment support for sparse/multilinear structure is often a central cost driver.
- In RS/FRI systems, proximity testing and verifier query/hash cost are often central cost drivers.

### Cleaner relation modeling vs cleaner transparent infrastructure
- Multilinear systems may feel cleaner when starting from R1CS.
- RS/FRI systems may feel cleaner when starting from transparent oracle-proof infrastructure.

## Reading advice

### Read the multilinear branch first if:
- you want the clearest route from arbitrary R1CS to a transparent zkSNARK,
- you want to understand why [[Spartan]] looks so different from FRI-style systems,
- you want a sum-check-centered mental model.

### Read the RS / FRI branch first if:
- you want the clearest route to STARK-style thinking,
- you want to understand why low-degree testing dominates so much of the transparent proof landscape,
- you want the historical line from [[Interactive Oracle Proofs]] to [[FRI]] to [[WHIR]].

## Provisional conclusion

A durable summary for the wiki is:

> **Multilinear / sum-check systems and RS / FRI / IOPP systems are two different transparent-proof design lenses. The first starts from algebraic relations over multilinear encodings; the second starts from oracle-accessible codewords and proximity testing. Modern systems increasingly mix ideas from both, but the distinction remains one of the best ways to navigate the field.**

## Next steps

- Strengthen [[zkSNARKs]] and [[Reed-Solomon Proximity Testing]] so they point to this comparison explicitly.
- Eventually create a broader synthesis that includes pairing-based and trusted-setup systems, not only transparent families.
- Revisit this page after more STARK-substrate and multilinear-system papers are ingested.
