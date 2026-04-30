---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/Quasar.pdf
authors:
  - Tianyu Zheng
  - Shang Gao
  - Yu Guo
  - Bin Xiao
year: 2025
tags:
  - accumulation-schemes
  - ivc
  - pcd
  - polynomial-commitments
  - post-quantum
  - recursion
related:
  - "[[Quasar]]"
  - "[[Accumulation Schemes]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Polynomial Commitments]]"
  - "[[WARP]]"
  - "[[Accumulation vs Folding in Recursive Proof Systems]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Multi-instance accumulation / IVC paper targeting sublinear verifier dependence on accumulated instances"
---

# Quasar Sublinear Accumulation Schemes for Multiple Instances

## Summary

Quasar studies a specific recursion bottleneck: even when one uses accumulation, the **accumulation verifier** often still scales **linearly in the number of accumulated instances**.

That linear verifier cost becomes expensive when embedded inside recursive circuits. The paper proposes a new **multi-instance accumulation scheme** based on **polynomial commitment schemes (PCSs)** whose verifier complexity is **sublinear in the number of accumulated instances $\ell$**. Building on this, it introduces **Quasar**, a multi-instance IVC construction aimed at reducing practical recursion overhead (Abstract, p. 1; Introduction, pp. 1–4).

Its core idea is to replace the usual heavy random-linear-combination pattern with **partial evaluation of polynomials**, thereby reducing the number of expensive commitment random linear combination (CRC) operations the verifier must perform (Abstract, p. 1).

## Key Claims

- The paper proposes a multi-instance accumulation scheme with verifier complexity **sublinear in $\ell$**, the number of accumulated instances (Abstract, p. 1; pp. 3–5).
- Based on that scheme, it constructs **Quasar**, a multi-instance IVC (Abstract, p. 1; Section 1.2, pp. 4–5).
- The recursive verifier cost is reduced by lowering the number of commitment random linear combination (CRC) operations (Abstract, p. 1; pp. 3–4).
- If the underlying PCS has linear proving complexity, the overall accumulation prover can also be linear-time (Abstract, p. 1; p. 4).
- The construction admits both curve-based and code-based instantiations, including plausibly post-quantum ones (Abstract, p. 1; Table 1, p. 5).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper's motivating setting is **multi-instance IVC**, where the prover accumulates multiple predicate instances and one accumulator at each step, trading off the number of recursive steps against recursion overhead (Section 2.1, p. 6).

The abstract states the main theorem-level claim informally: there exists a multi-instance accumulation scheme based on PCSs whose verifier complexity is sublinear in the number of instances $\ell$ (p. 1).

The concrete asymptotic picture is summarized in Table 1 (p. 5). For the two Quasar instantiations:
- **Quasar (curve)** has verifier cost
  $$
  O(\log \ell)\;RO + O(1)\;G,
  $$
  where $RO$ denotes random-oracle queries and $G$ denotes group operations;
- **Quasar (code)** has verifier cost
  $$
  O\!\left(\frac{\lambda}{\log(1/\rho)}\cdot (\log n + \log \ell)\right) RO,
  $$
  where $\lambda$ is a security parameter and $\rho$ is the code rate.

The introduction also states a key total-recursion claim for Quasar: the recursive circuits across all steps contain only **quasi-linear**
$$
O(\sqrt N)
$$
CRC operations among all steps, while each step uses only
$$
O(\ell)
$$
field operations and
$$
O(1)
$$
CRC operations (Section 1.2, p. 4).

## Methods and Proof Techniques

### 1. Multi-instance IVC abstraction

The paper defines a setting where the prover can accumulate multiple instances together at each step rather than only one. This creates a cleaner framework for asking whether verifier dependence on $\ell$ can be reduced below linear (Section 2.1, p. 6).

### 2. Partial evaluation of polynomials

This is the key optimization idea. Instead of paying for too many full commitment random linear combination operations, Quasar uses **partial evaluation of polynomials** to reduce verifier-side combination costs (Abstract, p. 1).

### 3. PCS-based accumulation design

The scheme is fundamentally a polynomial-commitment construction. Its concrete efficiency profile depends strongly on the underlying PCS, which is why the paper presents both curve-based and code-based instantiations (pp. 4–5).

### 4. Recursion-overhead accounting through CRC operations

The paper tracks recursion overhead in terms of the number of expensive **CRC operations**, because those dominate the recursive circuit cost in practice, especially when commitments are non-native or Merkle-path heavy (pp. 3–4).

### 5. Practical multi-instance recursion viewpoint

Unlike some more general PCD formulations, the paper focuses on the practically important case of sequential computation with multiple accumulated chunk instances and one accumulator, which better matches zkVM and related applications (Section 2.1, pp. 6–7).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

Quasar's headline optimization target is not minimizing prover time at all costs, but minimizing **recursive verifier overhead as a function of $\ell$**.

The paper's introduction and Table 1 highlight the following performance picture:

- **Verifier dependence on accumulated instances:** sublinear in $\ell$ rather than linear (Abstract, p. 1; Table 1, p. 5).
- **Quasar (curve) verifier:**
  $$
  O(\log \ell)\;RO + O(1)\;G
  $$
  (Table 1, p. 5).
- **Quasar (code) verifier:**
  $$
  O\!\left(\frac{\lambda}{\log(1/\rho)}\cdot (\log n + \log \ell)\right) RO
  $$
  (Table 1, p. 5).
- **Recursive-circuit CRC count:** quasi-linear
  $$
  O(\sqrt N)
  $$
  over all steps, with only
  $$
  O(1)
  $$
  CRC operations per step in the stated regime (Section 1.2, p. 4).
- **Prover:** can be linear-time if the underlying PCS prover is linear-time (Abstract, p. 1; p. 4).

For the current wiki, the key message is that Quasar attacks a different bottleneck than many other recursion papers: not the existence of accumulation, but the **scaling law of the accumulation verifier inside recursion**.

## Why It Matters

Quasar matters because it pushes on a different bottleneck than [[WARP]].

WARP is about making the accumulation prover linear-time and the verifier logarithmic in a general-linear-code setting. Quasar focuses instead on **sublinear dependence on the number of accumulated instances** in a multi-instance recursion regime.

That makes it a valuable companion paper in the current wiki: it shows that once recursion is possible, the next optimization frontier is often *how recursion overhead scales with batching size*.

## Connections to the Wiki

This paper strongly connects:
- [[Quasar]]
- [[Accumulation Schemes]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[Polynomial Commitments]]
- [[WARP]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
- [[SNARKs and STARKs Reading Map]]

It should often be read alongside [[WARP Linear-Time Accumulation Schemes]] to compare two different optimization philosophies for accumulation-based recursion.

## Open Questions / Limitations

- The current note now captures the introduction-level asymptotics and instantiation table, but a future pass could still extract more of the internal accumulation protocol and proof details from later sections.
- The strongest practical gains depend heavily on the chosen PCS backend, so backend selection is central to reading the paper correctly.
- A useful future synthesis would compare Quasar's multi-instance accumulation perspective more explicitly against folding-based recursion and general-code accumulation schemes.

## Suggested Next Reading

- [[Accumulation Schemes]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[WARP Linear-Time Accumulation Schemes]]
- [[Accumulation vs Folding in Recursive Proof Systems]]

## Related
- [[Quasar]]
- [[Accumulation Schemes]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Proof-Carrying Data (PCD)]]
- [[Polynomial Commitments]]
- [[WARP]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
- [[SNARKs and STARKs Reading Map]]
