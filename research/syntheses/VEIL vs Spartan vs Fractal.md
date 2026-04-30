---
date: 2026-04-10
type: synthesis
status: stable
created: 2026-04-10
updated: 2026-04-10
tags:
  - veil
  - spartan
  - fractal
  - comparison
  - transparent
  - zero-knowledge
related:
  - "[[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]"
  - "[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]"
  - "[[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Polynomial Commitments]]"
  - "[[Holographic Proofs]]"
  - "[[Preprocessing SNARKs]]"
description: "Comparison of three architectural routes to practical transparent zero knowledge: native design, recursive architecture, and lightweight zk compila..."
---

# VEIL vs Spartan vs Fractal

## Thesis / purpose

This page compares three different ways the current corpus approaches **transparent practical zero knowledge**:
- [[Spartan]] — design a transparent zkSNARK directly,
- [[Fractal]] — obtain transparent recursive zk from holography and preprocessing,
- [[VEIL]] — retrofit zero knowledge onto suitable hash-based multilinear proof systems with a lightweight compiler.

These papers are not competing on a single benchmark axis. They represent **three different architectural strategies**.

A useful durable summary is:

> **Spartan builds a transparent zkSNARK. Fractal builds a transparent recursive architecture. VEIL builds a lightweight zk wrapper for multilinear hash-based systems.**

## Main takeaways

- **Spartan** is the best anchor for understanding transparent zkSNARK design for arbitrary R1CS.
- **Fractal** is the best anchor for understanding how transparent / post-quantum recursion can be assembled from holographic proof machinery.
- **VEIL** is the best anchor for understanding how to add zero knowledge to an already-good multilinear hash-based system without rebuilding the whole stack.
- Spartan is primarily a **base proof-system design** paper.
- Fractal is primarily a **recursive system architecture** paper.
- VEIL is primarily a **compiler / wrapper** paper.
- Spartan and Fractal are trying to produce end-to-end systems.
- VEIL is trying to keep an existing end-to-end system performant while adding zk with low engineering disruption.

## Formal cost comparison

The three systems occupy different layers and target different cost axes, so a direct apples-to-apples comparison is not fully possible. The table below captures the key asymptotic properties for each system's central contribution, given a constraint system of size $N$ over a field $\mathbb{F}$ with security parameter $\lambda$.

| Metric | Spartan | Fractal | VEIL |
|--------|---------|---------|------|
| **Setup** | Transparent: $O(N)$ public preprocessing | Transparent: $O(N \log N)$ holographic encoding | Inherits underlying system's setup |
| **Prover time** | $O(N)$ (with SPARK for sparse R1CS) | $O(N \log N)$ per recursive step | Underlying prover + $O(N)$ zk overhead |
| **Verifier time** | $O(\sqrt{N})$ (computation commitments) | $O(\mathsf{polylog}(N))$ per step (preprocessing) | Underlying verifier + $O(\lambda)$ overhead |
| **Proof size** | $O(\sqrt{N} \cdot \log N)$ | $O(\mathsf{polylog}(N))$ per step | Underlying proof + $O(\lambda)$ blinding |
| **Zero knowledge** | Built-in (random masking in sum-check) | Built-in (inner SNARK is zk) | Compiled: query padding + column blinding |
| **Recursion** | Not a recursion system | Native: holographic IOP $\to$ preprocessing SNARK $\to$ PCD | Not recursive; avoids recursive wrapping |
| **Post-quantum** | Depends on commitment scheme (hash-based variant: yes) | Yes (hash-based holography + Merkle) | Yes (hash-based, no algebraic assumptions) |

**Key architectural distinction.** Spartan's verifier time is $O(\sqrt{N})$ — sublinear but not polylogarithmic — because it uses computation commitments rather than holographic encoding. Fractal achieves $O(\mathsf{polylog}(N))$ verification by paying more at preprocessing. VEIL doesn't improve verification cost at all; it adds zk to a system that already has good performance, with overhead proportional to the security parameter rather than the instance size.

## Comparison / synthesis

| Axis | Spartan | Fractal | VEIL |
|---|---|---|---|
| Core identity | Transparent zkSNARK for arbitrary R1CS | Transparent/post-quantum recursive methodology from holography | Lightweight zk compiler for hash-based multilinear systems |
| Main question | Can transparent zkSNARKs get sublinear verification for arbitrary NP? | Can recursion be transparent and post-quantum without curve cycles? | Can we add zk to multilinear hash-based systems cheaply and non-intrusively? |
| Primary layer | Base proof-system design | Recursive architecture / preprocessing / PCD | Compiler / wrapper layer |
| Key machinery | Sum-check, computation commitments, SPARK, polynomial commitments | Holographic IOPs, preprocessing SNARKs, FRI-style verifier machinery, PCD | Query padding, random-column blinding, lightweight inner zk proof |
| Relation to transparency | Transparent via public/trapdoor-free preprocessing | Transparent via URS / public preprocessing architecture | Helps make transparent hash-based systems zk with low overhead |
| Relation to recursion | Not primarily a recursion paper | Directly about recursion / PCD | Avoids recursive-wrap overhead rather than building recursion |
| Practical bottleneck attacked | Transparent zkSNARKs for arbitrary R1CS without trusted setup | Efficient transparent recursion and verifier-circuit feasibility | ZK-ification overhead and maintainability in hash-based multilinear systems |

## Spartan: transparent zk built into the design

[[Spartan]] is the clearest “native transparent zkSNARK design” paper in the current corpus.

Its main contribution is not merely removing trusted setup, but doing so while preserving:
- support for **arbitrary R1CS / NP statements**,
- **sub-linear verification**,
- and competitive prover behavior.

### Spartan's architectural stance
Spartan says, roughly:
- start from the statement class you care about,
- encode it algebraically,
- design the proof system around sum-check and polynomial commitments,
- and make verifier preprocessing public rather than trapdoor-based.

So Spartan is a **system design from first principles** paper.

## Fractal: transparent recursion from holography + preprocessing

[[Fractal]] addresses a different problem.

It asks:
- how do we get **transparent recursive composition**,
- in a **post-quantum-flavored** setting,
- without depending on pairing-friendly recursive curve cycles?

### Fractal's architectural stance
Fractal says, roughly:
- recursion becomes easier if the underlying SNARK is a **preprocessing SNARK**,
- preprocessing SNARKs can be obtained from **holographic IOPs**,
- and then those preprocessing SNARKs can be compiled into **PCD / recursion**.

So Fractal is best understood as a **bridge architecture**:
- IOP/holography → preprocessing SNARK → recursive proof system.

## VEIL: zk as a lightweight compiler layer

[[VEIL]] asks a different engineering question.

Suppose you already have a performant multilinear hash-based proof stack. Must you either:
- redesign every subprotocol to be zk, or
- wrap the whole thing in an expensive recursive zk proof?

VEIL's answer is: **not necessarily**.

### VEIL's architectural stance
VEIL says, roughly:
- identify the parts of the protocol that actually leak,
- shield trace queries cheaply,
- blind the final proximity step,
- and only wrap the small algebraic transcript with a lightweight inner zk proof.

So VEIL is a **modular retrofitting** paper rather than a base-system paper.

## The most important distinction: where is zk introduced?

This is the cleanest durable lens.

### Spartan
Zero knowledge is part of the **system design itself**.

### Fractal
Zero knowledge appears in a **transparent recursive architecture** built through holographic compilation and preprocessing.

### VEIL
Zero knowledge is introduced as a **compiler layer on top of an existing multilinear system**.

That means these papers answer different design questions:
- Spartan: *How do I build the proof system?*
- Fractal: *How do I get transparent recursion?*
- VEIL: *How do I zk-ify a practical multilinear system cheaply?*

## Transparency contrast

### Spartan's transparency
Transparency means:
- no toxic-waste trusted setup,
- public preprocessing is allowed,
- and the system is aimed at arbitrary R1CS.

### Fractal's transparency
Transparency means:
- URS/public-coin style setup after oracle instantiation,
- recursion that does not rely on trusted setup or curve cycles,
- and a methodology compatible with post-quantum aspirations.

### VEIL's transparency
VEIL is not mainly redefining transparency. Instead, it helps ensure that **transparent hash-based systems can also be practical zero-knowledge systems**.

So VEIL is best seen as strengthening the transparent ecosystem rather than defining a new transparent-SNARK architecture by itself.

## What each paper optimizes

### Spartan optimizes
- transparent zk for arbitrary R1CS,
- sub-linear verification,
- and good prover performance via careful algebraic design.

### Fractal optimizes
- transparent recursion,
- preprocessing-based verifier succinctness,
- and the feasibility threshold for recursive verifier circuits.

### VEIL optimizes
- low concrete zk overhead,
- code maintainability,
- and avoiding expensive “prove the hashes” approaches.

## Practical reading advice

### Read Spartan first if:
- you want the core transparent-zkSNARK anchor,
- you care about arbitrary R1CS,
- you want a direct alternative to trusted-setup SNARKs.

### Read Fractal next if:
- you care about recursion,
- you care about post-quantum transparent proof systems,
- you want to understand holography/preprocessing as a route to recursive architecture.

### Read VEIL if:
- you already understand multilinear hash-based systems,
- you care about making them zk in practice,
- you care about engineering overhead and maintainability more than asymptotic optimality.

## Evidence and citations

### Spartan
From [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]:
- transparent zkSNARK for arbitrary R1CS,
- public computation commitments,
- SPARK for sparse multilinear commitments,
- sub-linear verification.

### Fractal
From [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]:
- holographic IOP to preprocessing SNARK compilation,
- transparent/post-quantum recursion,
- preprocessing PCD,
- practical recursive verifier-circuit threshold.

### VEIL
From [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]:
- lightweight zk compiler,
- query padding and proximity blinding,
- low prover overhead,
- non-intrusive zk retrofit for multilinear hash-based systems.

## Tensions / contradictions

### Native design vs wrapper design
- Spartan and Fractal are end-to-end architectural papers.
- VEIL is intentionally a wrapper/compiler paper.

### General-purpose base proof vs recursive system vs retrofit
- Spartan is about the base zkSNARK.
- Fractal is about recursion architecture.
- VEIL is about practical zk compilation on top of an existing system family.

### Asymptotic elegance vs practical maintenance
- VEIL explicitly prioritizes low practical overhead and maintainability.
- Spartan and Fractal make broader architectural commitments that are less about minimally invasive integration.

## Provisional conclusion

A durable summary for the wiki is:

> **Spartan, Fractal, and VEIL are three different answers to the question of practical transparent zero knowledge. Spartan designs it in natively, Fractal composes it into a transparent recursive architecture, and VEIL retrofits it onto multilinear hash-based systems with low overhead.**

That is the cleanest way to remember why all three matter.

## Next steps

- Compare [[VEIL]] more directly with recursive-wrap approaches once more such papers are ingested.
- Create a broader synthesis on transparent proof systems that spans:
  - direct zkSNARK design,
  - STARK/IOPP pipelines,
  - preprocessing recursion,
  - and zk compilers/wrappers.
- Revisit this page after ingesting more multilinear and zk-compiler papers.
