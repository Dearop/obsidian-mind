---
date: 2026-02-25
type: source
status: processed
source_kind: paper
created: 2026-04-30
updated: 2026-04-30
raw_path: raw/papers/SNARKs & STARKs/2026-391.pdf
authors:
  - Alessandro Chiesa
  - Giacomo Fenzi
  - Guy Weissenberg
year: 2026
tags:
  - iop
  - zero-knowledge
  - linear-codes
  - dispersers
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Zero-Knowledge Proofs]]"
  - "[[Constrained Interleaved Codes]]"
---

# Zero-Knowledge IOPPs for Constrained Interleaved Codes

**Authors:** Alessandro Chiesa, Giacomo Fenzi, Guy Weissenberg  
**Affiliation:** EPFL  
**Date:** February 25, 2026  

## Abstract
Succinct arguments based on interactive oracle proofs (IOPs) have achieved remarkable efficiency improvements and are now widely adopted in applications. State-of-the-art IOPs involve protocols for testing proximity to constrained interleaved linear codes, and enjoy essentially optimal parameters. However, recent IOP constructions provide no privacy guarantees, which remain a must for many applications.
We present an IOP of proximity for testing constrained interleaved linear codes that achieves (honest-verifier) zero-knowledge, while incurring a negligible overhead compared to the (non-zero-knowledge) state of the art. In line with recent constructions, our construction satisfies round-by-round knowledge soundness with a straightline extractor and negligible error.
We propose a definition of (honest-verifier) zero-knowledge for interactive oracle reductions (IORs) that we prove is compatible with composition, and then obtain our result by constructing and modularly composing several lightweight zero-knowledge IORs. Our key technical contributions are a zero-knowledge sumcheck IOR and a zero-knowledge code-switching IOR that fit the strict efficiency requirements of our setting; these contributions and other technical complications entailed overcoming several challenges with new notions and protocols. Finally, along the way, we highlight the efficiency benefits of high-distance codes obtained from dispersers, which may be of independent interest.
Keywords: interactive oracle reductions; zero-knowledge; linear codes; dispersers

## Contents
(Full extracted text follows)

Zero-Knowledge IOPPs for Constrained Interleaved Codes
Alessandro Chiesa

Giacomo Fenzi

Guy Weissenberg

alessandro.chiesa@epfl.ch
EPFL

giacomo.fenzi@epfl.ch
EPFL

guy.weissenberg@epfl.ch
EPFL

February 25, 2026

Abstract
Succinct arguments based on interactive oracle proofs (IOPs) have achieved remarkable efficiency improvements and are now widely adopted in applications. State-of-the-art IOPs involve
protocols for testing proximity to constrained interleaved linear codes, and enjoy essentially
optimal parameters. However, recent IOP constructions provide no privacy guarantees, which
remain a must for many applications.
We present an IOP of proximity for testing constrained interleaved linear codes that achieves
(honest-verifier) zero-knowledge, while incurring a negligible overhead compared to the (nonzero-knowledge) state of the art. In line with recent constructions, our construction satisfies
round-by-round knowledge soundness with a straightline extractor and negligible error.
We propose a definition of (honest-verifier) zero-knowledge for interactive oracle reductions
(IORs) that we prove is compatible with composition, and then obtain our result by constructing
and modularly composing several lightweight zero-knowledge IORs. Our key technical contributions are a zero-knowledge sumcheck IOR and a zero-knowledge code-switching IOR that fit the
strict efficiency requirements of our setting; these contributions and other technical complications entailed overcoming several challenges with new notions and protocols. Finally, along the
way, we highlight the efficiency benefits of high-distance codes obtained from dispersers, which
may be of independent interest.
Keywords: interactive oracle reductions; zero-knowledge; linear codes; dispersers

1

Contents
1 Introduction
1.1 Our results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3
4

2 Technical overview
2.1 Basic notions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Warmup: a simple zero-knowledge IOPP for constrained codes . . . . . . . . . . . . . . . . .
2.3 Composition for honest-verifier zero-knowledge IORs . . . . . . . . . . . . . . . . . . . . . . .
2.4 A “committed” relation for zero-knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5 An honest-verifier zero-knowledge sumcheck reduction . . . . . . . . . . . . . . . . . . . . . .
2.6 HVZK code switching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3 Preliminary definitions
3.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Linear codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Interactive oracle proofs (IOPs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Interactive oracle reductions (IORs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5 Polynomial commitment schemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4 Zero-knowledge sumcheck IOR
4.1 The sumcheck problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Zero-knowledge sumcheck protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Proof of zero-knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4 Proof of knowledge soundness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5 Zero-knowledge code-switching IOR
5.1 The code-switching problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Zero-knowledge code-switching protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Proof of zero-knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4 Proof of knowledge soundness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6 Zero-knowledge IOPP for constrained interleaved codes
6.1 Constrained interleaved linear codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2 Zero-knowledge IOP of proximity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Proof of zero-knowledge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4 Proof of knowledge soundness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7 High-distance codes from dispersers
7.1 Dispersers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2 High-distance codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Applications to constrained interleaved codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8 References