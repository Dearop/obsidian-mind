---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2019-1076.pdf
authors:
  - Alessandro Chiesa
  - Dev Ojha
  - Nicholas Spooner
year: 2020
tags:
  - recursion
  - transparent
  - post-quantum
  - holographic-proofs
  - preprocessing-snarks
  - pcd
related:
  - "[[Fractal]]"
  - "[[Holographic Proofs]]"
  - "[[Preprocessing SNARKs]]"
  - "[[FRI]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Bridge paper connecting holographic IOPs, preprocessing SNARKs, and transparent post-quantum recursion"
---

# Fractal Post-Quantum and Transparent Recursive Proofs from Holography

## Summary

Fractal presents a methodology for **transparent, post-quantum recursive composition of SNARKs**.

Its key architectural move is to observe that recursion is much simpler for **preprocessing SNARKs**, and then to obtain such preprocessing SNARKs from **holographic IOPs** in the random oracle model. The overall pipeline is:
1. construct a holographic IOP for R1CS,
2. compile it into a preprocessing SNARK in the (Q)ROM,
3. compile that preprocessing SNARK into preprocessing [[Proof-Carrying Data (PCD)]] in the URS model
(Abstract, p. 1; Introduction, pp. 1–3).

In the current wiki, Fractal is a major bridge linking:
- IOP / holography,
- transparent proof design,
- and recursive proof composition.

## Key Claims

- Fractal gives an efficient methodology for recursive composition that is both **transparent** and **post-quantum** (Abstract, p. 1; Introduction, pp. 1–2).
- It constructs a holographic IOP for **R1CS** (Theorem 2, pp. 2–3).
- It gives a route from holographic IOPs to preprocessing SNARKs in the random oracle model (Theorem 1, p. 2).
- It obtains preprocessing PCD in the URS model from preprocessing SNARKs (Theorem 4, p. 3).
- It reports the first practical demonstration of transparent post-quantum recursion in the paper's setting (pp. 3–4).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The introduction frames recursive composition as proving statements that validate prior SNARK verifications, which in turn supports both [[Incrementally Verifiable Computation (IVC)]] and [[Proof-Carrying Data (PCD)]] (p. 1).

Theorem 1 states an efficient transformation from any holographic IOP for an indexed relation into a preprocessing SNARG in the random oracle model, preserving zero knowledge / knowledge properties under the stated conditions and extending to the quantum random oracle model (p. 2).

Theorem 2 states that there exists a public-coin holographic IOP for the indexed R1CS relation with the following efficiency features (pp. 2–3):
- the index encoding is computable in
  $$
  O(m\log m)
  $$
  field operations and has size $O(m)$ field elements;
- the online protocol has
  $$
  O(\log m)
  $$
  rounds;
- the prover uses
  $$
  O(m\log m)
  $$
  field operations;
- the verifier uses
  $$
  O(|x| + \log m)
  $$
  field operations;
- proof length is
  $$
  O(m)
  $$
  field elements;
- query complexity is
  $$
  O(\log m).
  $$

Applying Theorem 1 to Theorem 2 yields Theorem 3: a preprocessing zkSNARK for R1CS in the (quantum) random oracle model where (pp. 2–3):
- offline preprocessing costs
  $$
  O_\lambda(m\log m),
  $$
- the verification key has size
  $$
  O_\lambda(1),
  $$
- prover runtime is
  $$
  O_\lambda(m\log m),
  $$
- verifier runtime is
  $$
  O_\lambda(|x| + \log^2 m),
  $$
- argument size is
  $$
  O_\lambda(\log^2 m).
  $$

Finally, Theorem 4 states an efficient transformation from any preprocessing SNARK in the URS model into a preprocessing PCD scheme in the URS model, preserving post-quantum security (p. 3).

## Methods and Proof Techniques

### 1. Preprocessing-first view of recursion

The paper's foundational insight is that recursive composition becomes much simpler if one first works with **preprocessing SNARKs**, where expensive statement structure is summarized offline and online verification can be sublinear in circuit size (Introduction, pp. 1–2).

### 2. Holography to preprocessing

One of the paper's key conceptual contributions is showing that **holographic IOPs** can be compiled into preprocessing SNARKs. Holography means the verifier queries an encoding of the statement index rather than reading the full statement description directly (Theorem 1 discussion, pp. 2–3).

### 3. Efficient holographic IOP for R1CS

Fractal constructs an efficient holographic IOP for R1CS, giving the concrete protocol layer that makes the overall methodology practical rather than purely existential (Theorem 2, pp. 2–3).

### 4. Transparent and post-quantum compiler stack

The paper carefully threads its construction through the random oracle / quantum random oracle / URS models so that the final recursive system is both transparent and plausibly post-quantum (Abstract, p. 1; Theorems 1, 3, and 4, pp. 2–3).

### 5. Verifier-circuit engineering

The paper explicitly recognizes that recursion is only useful if the verifier itself can be encoded cheaply enough as a constraint system. This is a major engineering and asymptotic concern in the implementation sections (Introduction, p. 3; Sections 12–13 in the contents).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The theorem-level performance profile from the introduction is:

- **Holographic IOP indexer:**
  $$
  O(m\log m)
  $$
  field operations (Theorem 2, p. 2).
- **Holographic IOP prover:**
  $$
  O(m\log m)
  $$
  field operations (Theorem 2, p. 2).
- **Holographic IOP verifier:**
  $$
  O(|x| + \log m)
  $$
  field operations (Theorem 2, p. 2).
- **Preprocessing zkSNARK verifier:**
  $$
  O_\lambda(|x| + \log^2 m)
  $$
  time (Theorem 3, p. 3).
- **Preprocessing zkSNARK argument size:**
  $$
  O_\lambda(\log^2 m)
  $$
  (Theorem 3, p. 3).

The paper also reports concrete implementation results in the introduction (p. 3):
- argument sizes roughly **80–160 kB** at 128-bit security,
- proving times in the **minutes** range,
- verification times in the **milliseconds** range,
- and a recursion threshold around computations of at least **2 million constraints**, where the verifier circuit becomes small enough for practical recursion.

For the current wiki, the key lesson is that Fractal does not merely prove recursion is possible in a transparent post-quantum style — it explicitly engineers toward a regime where it becomes *practically realizable*.

## Why It Matters

Fractal matters because it is one of the clearest papers showing how model-level oracle-proof machinery becomes an actual recursive proof architecture.

It is especially important in the current wiki because it sits at the crossroads of multiple branches:
- [[Interactive Oracle Proofs (IOPs)]]
- [[FRI]]
- [[Transparent zkSNARKs]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]].

Without Fractal, the recursion branch would look much more disconnected from the transparent-proof and RS/IOPP substrate branches.

## Connections to the Wiki

Fractal is a bridge source connecting:
- [[Holographic Proofs]]
- [[Preprocessing SNARKs]]
- [[FRI]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Transparent zkSNARKs]]
- [[Transparent Verification and Verifiable Computation]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[SNARKs and STARKs Reading Map]]

It should be read as one of the key transition papers from transparent proof-system design into recursive composition.

## Open Questions / Limitations

- The current note now captures the introduction-level theorem stack, but a future pass could still extract more detail from the internal holographic IOP construction and verifier-circuit engineering sections.
- Fractal's recursion threshold remains significant, so practical deployment still depends heavily on implementation choices and application scale.
- A useful future synthesis would compare Fractal-style recursive transparent systems more explicitly against accumulation- and folding-based recursion schemes.

## Suggested Next Reading

- [[Holographic Proofs]]
- [[Preprocessing SNARKs]]
- [[FRI]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Accumulation vs Folding in Recursive Proof Systems]]

## Related
- [[Fractal]]
- [[Holographic Proofs]]
- [[Preprocessing SNARKs]]
- [[FRI]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Transparent zkSNARKs]]
- [[Transparent Verification and Verifiable Computation]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[SNARKs and STARKs Reading Map]]
