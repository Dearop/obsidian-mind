---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/Warp.pdf
authors:
  - Benedikt Bünz
  - Alessandro Chiesa
  - Giacomo Fenzi
  - William Wang
year: 2025
tags:
  - accumulation-schemes
  - pcd
  - ivc
  - hash-based
  - ior
  - recursion
related:
  - "[[WARP]]"
  - "[[Accumulation Schemes]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
  - "[[Interactive Oracle Reductions (IORs)]]"
  - "[[Polynomial Equation Satisfiability (PESAT)]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Accumulation-scheme anchor for linear-time proving and recursive/PCD composition"
---

# WARP Linear-Time Accumulation Schemes

## Summary

WARP presents the first **accumulation scheme** with **linear prover time** and **logarithmic verifier time**.

Its focus is not a standalone zkSNARK, but the **composition layer** needed for recursive proof systems, [[Incrementally Verifiable Computation (IVC)]], and [[Proof-Carrying Data (PCD)]]. In that setting, the key problem is not just one-shot proof generation, but repeatedly compressing many verification obligations into a smaller carried object (Abstract, p. 1; Introduction, pp. 3–4).

WARP's central thesis is that this accumulation layer can be made:
- hash-based,
- transparent,
- plausibly post-quantum,
- unbounded in accumulation depth,
- and still **linear-time for the prover**
(Abstract, p. 1).

The paper does this via **interactive oracle reductions (IORs)** over **general linear codes**, rather than tying itself only to Reed–Solomon structure (Abstract, p. 1; Theorem 2, pp. 4–5).

## Key Claims

- WARP is the first accumulation scheme with **linear prover time** and **logarithmic verifier time** (Abstract, p. 1).
- It is **hash-based** and secure in the **random oracle model** (Abstract, p. 1).
- It supports **unbounded accumulation depth**, which is crucial for recursive settings (Abstract, p. 1).
- Its core reductions work over **general linear codes**, not only Reed–Solomon codes (Abstract, p. 1; pp. 4–5).
- It introduces a form of **straightline round-by-round knowledge soundness** compatible with codes that may not admit efficient error-tolerant decoding (Abstract, p. 1; p. 5).
- Its main target relation is **polynomial equation satisfiability (PESAT)**, which captures multiple important NP-style algebraic relations including R1CS-like families (Definition 1, p. 4).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper states its main result for **polynomial equation satisfiability (PESAT)**.

Definition 1 describes a polynomial equation system over a field $\mathbb{F}$ as a tuple
$$
(\hat p, M, N, k)
$$
where $\hat p=(\hat p_i)_{i\in[M]}$ is a list of $N$-variate polynomials of constant total degree, and an instance-witness pair
$$
z := (x \in \mathbb{F}^{N-k},\; w \in \mathbb{F}^k)
$$
is a solution if
$$
\hat p_i(z) = 0 \qquad \text{for every } i\in[M]
$$
(Definition 1, p. 4).

Theorem 1 informally states that in the random oracle model there is an accumulation scheme
$$
ACC = (P_{ACC}, V_{ACC}, D_{ACC})
$$
for the PESAT relation with the following efficiency features when accumulating $\ell$ instance-witness pairs and accumulators (pp. 4–5):
- the prover performs
  $$
  O(\ell\cdot |\hat p| + \lambda \log k)
  $$
  field operations;
- the verifier performs
  $$
  O\bigl(\ell(\log N + \log M + \lambda) + \lambda\log k\bigr)
  $$
  field operations;
- the decider performs
  $$
  O(|\hat p|)
  $$
  field operations;
- knowledge-soundness error is at most
  $$
  2^{-\lambda}
  $$
  under the stated field-size and oracle-size conditions.

The paper's main technical theorem is Theorem 2, which constructs two IORs over an arbitrary chosen linear code $C$ (pp. 4–5):
- an IOR from PESAT to an accumulation relation $R_C$,
- and an IOR from $R_C^{\ell}$ to $R_C$.

This is the formal source of WARP's claim that it works over essentially any suitable linear code, inheriting the code's efficiency properties up to low overhead.

## Methods and Proof Techniques

### 1. Hash-based accumulation via IORs

WARP's starting point is that accumulation can be built from **interactive oracle reductions** rather than only from ordinary IOPs or commitment-heavy algebraic accumulators. This places the paper squarely in the reduction / recursion branch (Abstract, p. 1; pp. 4–5).

### 2. General linear-code framework

A major conceptual contribution is moving beyond Reed–Solomon-specific machinery. WARP develops IORs that work over **general linear codes**, which means the resulting accumulation scheme can inherit linear-time encodability and related code-level efficiency from many possible code families (Theorem 2, pp. 4–5).

### 3. PESAT as a unifying algebraic target

The paper routes the accumulation problem through **polynomial equation satisfiability (PESAT)**, an NP-complete algebraic relation that captures R1CS, GR1CS, CCS, and related systems in a uniform way (Definition 1, p. 4).

### 4. Batching and constrained-code reductions

The technical overview highlights several batching subroutines that are assembled into the final IOR stack:
- codeword batching,
- twin-constraint pseudo-batching,
- multilinear constraint batching
(Contents and technical overview, pp. 2–5).

### 5. Straightline extraction via erasure correction

One of the paper's most distinctive technical points is its extraction strategy. Rather than depending on error-tolerant decoding, WARP develops straightline extraction based on **erasure correction**, together with a variant of round-by-round knowledge soundness compatible with this approach (Abstract, p. 1; p. 5).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline asymptotic profile stated in Theorem 1 is:

- **Accumulation prover:**
  $$
  O(\ell\cdot |\hat p| + \lambda \log k)
  $$
  field operations (pp. 4–5).
- **Accumulation verifier:**
  $$
  O\bigl(\ell(\log N + \log M + \lambda) + \lambda\log k\bigr)
  $$
  field operations (pp. 4–5).
- **Decider:**
  $$
  O(|\hat p|)
  $$
  field operations (p. 5).
- **Knowledge soundness error:**
  $$
  2^{-\lambda}
  $$
  under the stated conditions (p. 5).

The prover is called **linear-time** because its runtime is proportional to the algebraic work required to evaluate the target polynomial system, and the verifier is **logarithmic-time** because its field-operation cost depends logarithmically on core size parameters like $N$ and $M$ (pp. 4–5).

For the current wiki, the key performance lesson is that the recursion / accumulation layer itself can now be engineered to be genuinely lightweight, rather than merely asymptotically composable.

## Why It Matters

WARP matters because it pushes the recursive-proof story from “we know how to compose proofs” to “we can compose them with a **linear-time accumulation prover** and **logarithmic-time verifier**.”

That is important for:
- [[Proof-Carrying Data (PCD)]],
- [[Incrementally Verifiable Computation (IVC)]],
- hash-based recursion,
- and the broader post-quantum recursion design space.

In the current wiki, WARP is one of the clearest modern anchors for the idea that recursion efficiency is often dictated by the *accumulation layer*, not just by the base proof system.

## Connections to the Wiki

This paper is a central anchor for:
- [[WARP]]
- [[Accumulation Schemes]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Polynomial Equation Satisfiability (PESAT)]]
- [[Transparent Verification and Verifiable Computation]]
- [[SNARKs and STARKs Reading Map]]

It should often be compared directly against multi-instance accumulation papers such as [[Quasar Sublinear Accumulation Schemes for Multiple Instances]].

## Open Questions / Limitations

- The current note now captures the theorem-level asymptotics from the front matter, but a deeper pass could still extract more precise internal statements about the two IORs and their exact oracle/query profiles.
- The paper's flexibility comes from working over general linear codes, so understanding the *best* instantiations remains a code-selection question as much as a protocol question.
- A useful future synthesis could compare WARP's IOR-based worldview more explicitly against folding-based recursion systems and WHIR-style constrained-code compilation.

## Suggested Next Reading

- [[Accumulation Schemes]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]

## Related
- [[WARP]]
- [[Accumulation Schemes]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Polynomial Equation Satisfiability (PESAT)]]
- [[Transparent Verification and Verifiable Computation]]
- [[SNARKs and STARKs Reading Map]]
