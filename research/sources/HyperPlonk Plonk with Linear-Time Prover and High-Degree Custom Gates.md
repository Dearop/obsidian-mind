---
date: 2023-01-09
description: "HyperPlonk adapts Plonk to multilinear hypercube IOPs, removing prover FFTs and supporting high-degree custom gates with near-linear prover costs."
type: source
status: processed
source_kind: paper
raw_path: raw/papers/SNARKs & STARKs/Hyperplonk.pdf
authors:
  - Binyi Chen
  - Benedikt Bünz
  - Dan Boneh
  - Zhenfei Zhang
year: 2023
tags:
  - snark
  - plonk
  - multilinear
  - sumcheck
  - lookup
  - polynomial-commitments
related:
  - "[[HyperPlonk]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Sum-check Protocol]]"
  - "[[Polynomial Commitments]]"
  - "[[Commit-and-Prove SNARKs]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
---

# HyperPlonk Plonk with Linear-Time Prover and High-Degree Custom Gates

## Summary

This paper re-expresses Plonk over the Boolean hypercube and compiles via multilinear commitments, yielding **HyperPlonk**: a Plonk-like system that removes prover FFTs and targets linear-time proving in important regimes (Abstract, p. 1; Introduction and Technical Overview, pp. 3-9).

The two headline claims are:
- prover complexity drops from Plonk's quasi-linear FFT-driven behavior to linear-time style behavior in the core flow via SumCheck-based reductions over multilinear polynomials,
- high-degree custom gates become practical because prover costs depend more on circuit implementation complexity than directly on gate degree blowup in univariate representations (pp. 4-8).

The paper also defines HyperPlonk+ (lookup support), improves multilinear batch openings, and presents Orion+ style multilinear commitment optimizations with much smaller proofs (Sections 3, 5, 7; pp. 27-49).

## Key Claims

- HyperPlonk avoids FFTs in proof generation by moving Plonk constraints to multilinear polynomials on $B^\mu=\{0,1\}^\mu$ and using SumCheck-driven checks (pp. 4, 7-9).
- For circuits with custom gate $G$, HyperPlonk handles high-degree gates better than Plonk's $O(sd)$-style univariate bottlenecks in practice (pp. 4-8).
- HyperPlonk+ extends the construction to lookup gates by adapting Plookup-style logic to hypercube structure (Sections 3.7 and 5; pp. 27, 37+).
- Pairing-based instantiations produce compact proofs (reported ~4.7KB at $\mu=20$, ~5.5KB at $\mu=25$) and strong prover performance against baseline systems in their benchmarks (Section 6, pp. 40-42; intro evaluation summary, p. 6).
- Orion+ style multilinear PCS refinements reduce proof size dramatically versus prior Orion parameters while preserving linear-time style commitment work (Section 7, pp. 43-49).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> This note captures key formal objects and headline theorem statements from the paper text. For exact constants/quantifiers, re-check the corresponding section theorem numbering directly.

### Hypercube encoding of Plonk witness matrix

Instead of univariate evaluations over subgroup powers, HyperPlonk commits to multilinear $M\in F[X_1,\dots,X_{\mu+2}]$ so that for row index $i\in[0,n+s]$:
$$
M(0,0,\langle i\rangle)=L_i,\quad M(0,1,\langle i\rangle)=R_i,\quad M(1,0,\langle i\rangle)=O_i.
$$
(Technical overview, Eq. (2), p. 7.)

### Gate identity over the hypercube

With selector polynomials $S_1,S_2,S_3$ and input polynomial $I$, the gate check is encoded as a polynomial identity over $x\in B^\mu$ (Eq. (3), pp. 7-8), combining addition/multiplication/custom-gate constraints.

### Wiring identity as permutation consistency

Wiring is reduced to proving
$$
M(x)=M(\hat\sigma(x))\ \ \forall x\in B^{\mu+2},
$$
or equivalently multiset equality over paired values (Eq. (4)-(5), p. 8), then discharged through multiset/product/zerocheck/sumcheck pipeline.

### PCS result highlight

Theorem 7.1 states correctness/binding and knowledge-sound evaluation for their Figure 7 multilinear PCS construction (Section 7, pp. 48-49).

## Methods and Proof Techniques

- **SumCheck-centric decomposition:** Gate/wiring/lookup checks are reduced to composable PIOPs (SumCheck, ZeroCheck, ProductCheck, MultisetCheck, Permutation), replacing large univariate FFT-style proving steps.
- **Hypercube-compatible lookup design:** They adapt Plookup logic where cyclic-order assumptions fail on $B^\mu$, introducing a workaround via structured traversal and linearization modifications.
- **Batch opening improvements:** Section 3.8 gives sumcheck-based batching that lowers opening overhead in both prover/runtime and proof size.
- **Commit-and-prove integration:** CP-SNARK ideas are used to compress verification obligations in their multilinear PCS architecture.
- **Instantiation split:** They discuss pairing-based multilinear commitments and FRI-based multilinear routes (including simpler/shorter Virgo-style FRI multilinear opening variant in appendices/instantiation discussions).

## Complexity and Performance

Paper-level performance framing:
- **Plonk baseline:** prover $O_\lambda(s\log s)$ with substantial FFT work for large circuits (p. 4).
- **HyperPlonk direction:** linear-time style core proving flow over hypercube/SumCheck, no prover FFT in the core protocol path (pp. 4, 7-9).
- **High-degree custom gates:** reported reduction from Plonk's $O(sd)$-type pressure to much milder dependence in HyperPlonk pipeline (pp. 4, 8).
- **Proof size (pairing-based multilinear commitment instance):** approximately 4.7KB ($\mu=20$) and 5.5KB ($\mu=25$) reported in intro/eval summary (p. 6).
- **Benchmark claims:** runtime gains vs commercial-strength Plonk at larger circuit sizes; large improvements on listed workloads (Section 6 and Table 1 references, pp. 40-42).

## Why It Matters

HyperPlonk is a key bridge between "Plonkish ergonomics" and multilinear/SumCheck efficiency. It preserves familiar Plonk-style constraint expressivity while shifting computational geometry from univariate subgroup/FFT machinery to hypercube multilinear machinery.

That makes it strategically important for:
- fast prover engineering at large scale,
- high-degree custom-gate heavy arithmetizations,
- and integration with multilinear commitment and commit-and-prove ecosystems.

## Connections to the Wiki

- Complements [[Sum-check Protocol]] and [[Multilinear Interactive Oracle Proofs (MIOPs)]] style pipelines.
- Connects Plonk-style constraint systems to multilinear commitment design decisions in [[Polynomial Commitments]].
- Related to system-level trade-offs explored by [[Spartan]], [[VEIL]], and hash-based families in this wiki, but with a distinct "Plonk-on-hypercube" angle.
- Useful comparison target for future synthesis against RS/IOPP systems ([[FRI]], [[WHIR]]) and interleaving systems ([[WARP]]).

## Open Questions / Limitations

- How robust are the reported gains across prover implementations/hardware beyond the paper's benchmark setup?
- What is the best regime split between pairing-based multilinear commitments and FRI-based multilinear commitments for concrete deployments?
- How does HyperPlonk compare to newer Plonkish proving systems once modern lookup/batching optimizations are normalized?
- A dedicated synthesis note is still needed to compare HyperPlonk's multilinear route to WHIR/WARP style constrained-code pipelines.

## Suggested Next Reading

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[WARP Linear-Time Accumulation Schemes]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## Related
- [[HyperPlonk]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Sum-check Protocol]]
- [[Polynomial Commitments]]
- [[Commit-and-Prove SNARKs]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
