---
date: 2026-04-14
type: source
status: processed
source_kind: paper
created: 2026-04-14
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2019-1230.pdf
authors:
  - Eli Ben-Sasson
  - Tom Gur
  - Alessandro Chiesa
  - Michael Riabzev
  - Lior Goldberg
  - Nicholas Spooner
year: 2019
tags:
  - iop
  - delegation
  - verifiable-computation
  - reed-solomon
related:
  - "[[Delegating Computation Interactive Proofs for Muggles]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Proofs with Constant Rate and Query Complexity]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
description: "IOP paper for delegation of computation achieving linear-size proofs, constant query complexity, and polylogarithmic verifier time for rich classes of algebraic computations"
---

# Linear-Size Constant-Query IOPs for Delegating Computation

## Summary

This paper studies the design of **IOPs specifically for delegation of computation**.

Its goal is to get as close as possible to an “ideal” delegation-friendly proof protocol: constant query complexity, polylogarithmic verifier time, linear proof length, and near-linear prover complexity (Introduction, pp. 1–3).

The paper proves that a rich class of **NEXP-complete problems**, including machine computations over large fields and succinctly-described arithmetic circuits, has **constant-query IOPs** with:
- **$O(T)$-size proofs** for $T$-size computations,
- **polylogarithmic-time verification**,
- and prover arithmetic complexity **$O(T\log T)$**
(Abstract, p. 1; Theorems 2 and 3, pp. 3–4).

In the current wiki, this is an especially important bridge because it connects:
- the older delegation motivation from [[Delegating Computation Interactive Proofs for Muggles]],
- the IOP design-space advances of [[Interactive Oracle Proofs with Constant Rate and Query Complexity]],
- and the practical transparent-proof substrate built from Reed–Solomon codewords and oracle reductions.

## Key Claims

- A rich class of NEXP-complete problems has **constant-query IOPs** with **linear-size proofs** and **polylogarithmic verifier time** (Abstract, p. 1).
- These problems include machine computations over large fields and succinctly-described arithmetic circuits (Abstract, p. 1; Theorems 2–3, pp. 3–4).
- The prover arithmetic complexity is **$O(T\log T)$** for computations of size $T$ (Abstract, p. 1; Theorem 3, pp. 3–4).
- The construction is the first to simultaneously achieve linear proof length, constant query complexity, constant round complexity, polylogarithmic verifier time, and strictly quasilinear prover arithmetic complexity for this delegation-oriented setting (pp. 2–4).
- The proof consists of a constant number of Reed–Solomon codewords of total size $O(N)$, tightly linking prover time to encoding cost (Section 1.1, p. 2).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The abstract states the central parameter profile clearly: for computations of size $T$, the paper obtains IOPs with
$$
O(T)
$$
proof size and
$$
\operatorname{polylog}(T)
$$
verification time (Abstract, p. 1).

The introduction sharpens this by describing the target parameter package as:
- linear proof length,
- constant query and round complexity,
- prover arithmetic complexity
  $$
  O(N\log N),
  $$
- and polylogarithmic verifier time
(pp. 2–3).

Theorem 1 gives a 4-round IOP for **succinct R1CS** over large smooth fields with:
- proof length
  $$
  O(T(n)\log |\mathbb{F}(n)|),
  $$
- query complexity $4$,
- constant soundness error $\varepsilon_0$,
- prover time
  $$
  O(T(n)\log T(n))
  $$
  field operations,
- verifier time
  $$
  \operatorname{poly}(n,\log T(n))
  $$
  field operations
(p. 3).

Theorem 2 gives a 5-round IOP for **Succinct-ASAT** over large smooth fields with:
- proof length
  $$
  O(N),
  $$
- query complexity $5$,
- constant soundness error $\varepsilon_0$,
- prover time
  $$
  O(N\log N),
  $$
- verifier time
  $$
  \operatorname{poly}(|D|,\log N)
  $$
  field operations
(pp. 3–4).

Theorem 3 gives the analogous result for the satisfiability problem of $T(n)$-time **algebraic machines**, again with 5 rounds, 5 queries, proof length
$$
O(T(n)\log |\mathbb{F}(n)|),
$$
prover time
$$
O(T(n)\log T(n)),
$$
and verifier time
$$
\operatorname{poly}(n,\log T(n))
$$
(pp. 3–4).

## Methods and Proof Techniques

### 1. Delegation-oriented IOP design

The paper is explicit that delegation of computation imposes different design priorities than approximation-hardness PCPs. The central measures are query complexity, verifier time, prover time, and proof length (Introduction, pp. 1–3).

### 2. Oracle reductions and Reed–Solomon structure

A major technical component is a framework of **oracle reductions**, including Reed–Solomon oracle reductions. This gives the paper a direct technical connection to the RS / IOPP / STARK substrate branch (Contents and technical overview, pp. 2, 8–13).

### 3. Trace embeddings and interactive automata

The construction uses trace embeddings and probabilistic checking of interactive automata to reduce more complex computation objects to forms amenable to efficient oracle-proof checking (Sections 6–9 in the table of contents; Introduction, pp. 2–4).

### 4. Linear-checking and algebraic machine reductions

The paper develops succinct linear-checking tools and reductions for bounded-space algebraic computation and succinct arithmetic satisfiability, making the IOPs work for a rich delegation-oriented class rather than only a single narrow problem (Introduction, pp. 2–4).

### 5. Proof-length-driven prover efficiency

The paper emphasizes that the prover's arithmetic complexity is tightly connected to proof length: because the proof is a constant number of Reed–Solomon codewords of total size $O(N)$, the prover is dominated by producing those encodings (Section 1.1, p. 2).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline performance profile across the main results is:

- **Proof length:** linear, either
  $$
  O(T) \quad \text{or} \quad O(N),
  $$
  depending on the computation model (Abstract, p. 1; Theorems 1–3, pp. 3–4).
- **Query complexity:** constant ($4$ or $5$ queries in the stated theorems) (pp. 3–4).
- **Round complexity:** constant ($4$ or $5$ rounds in the stated theorems) (pp. 3–4).
- **Verifier time:** polylogarithmic in the underlying computation size, formalized as
  $$
  \operatorname{poly}(n,\log T(n))
  $$
  or
  $$
  \operatorname{poly}(|D|,\log N)
  $$
  (pp. 3–4).
- **Prover arithmetic complexity:**
  $$
  O(T\log T) \quad \text{or} \quad O(N\log N).
  $$

The paper also notes that if Reed–Solomon encodings could be produced in linear time, then the prover itself would become linear-time without changing the scheme otherwise (Section 1.1, p. 2).

## Why It Matters

This paper matters because it gets unusually close to the “ideal delegation proof” target:
- linear-size proofs,
- constant queries,
- constant rounds,
- polylog verifier,
- near-linear prover.

That makes it one of the clearest papers connecting classical delegation ambitions to the modern oracle-proof design space.

In the current wiki, it is especially valuable because it shows that the path from delegation to practical transparent proofs is not only about cryptographic compilers — it is also about getting the raw IOP parameters right.

## Connections to the Wiki

This paper strongly connects:
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]

It should also be read as part of the RS / IOPP / delegation branch that eventually feeds into transparent proof systems.

## Open Questions / Limitations

- The current note now captures the theorem-level parameters directly from the introduction, but a future pass could still extract more of the actual oracle-reduction machinery from Sections 5–10.
- The results are stated over large smooth fields; extending or comparing them to small-field regimes remains an important practical question.
- A useful future synthesis would compare these delegation-oriented IOPs more explicitly against both FRI-style transparent systems and classical delegated interactive proofs.

## Suggested Next Reading

- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]

## Related
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
