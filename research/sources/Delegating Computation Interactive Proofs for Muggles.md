---
date: 2026-04-13
type: source
status: processed
source_kind: paper
created: 2026-04-13
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2699436.pdf
authors:
  - Shafi Goldwasser
  - Yael Tauman Kalai
  - Guy N. Rothblum
year: 2015
tags:
  - interactive-proofs
  - verifiable-computation
  - delegation
  - classical-foundations
related:
  - "[[Delegating Computation Interactive Proofs for Muggles]]"
  - "[[SNARKs and STARKs Reading Map]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Linear-Size Constant-Query IOPs for Delegating Computation]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[Sum-check Protocol]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Bridge paper on delegating computation via public-coin interactive proofs with efficient provers and super-efficient verifiers"
---

# Delegating Computation Interactive Proofs for Muggles

## Summary

This paper studies interactive proofs for **tractable computations** where both parties must be efficient in meaningful ways:
- the honest prover should be polynomial-time,
- while the verifier should be substantially cheaper than recomputing the task.

The motivating application is modern and concrete: a client outsources a computation to an untrusted server, and the server proves interactively that the output is correct (Abstract, p. 27:1; Introduction, pp. 27:2–27:4).

The paper's main theorem gives a **public-coin interactive proof** for any language computable by an $O(\log S(n))$-space uniform Boolean circuit family of size $S(n)$ and depth $d(n)$. The verifier runs in time
$$
n \cdot \operatorname{poly}(d(n), \log S(n)),
$$
uses space $O(\log S(n))$, has communication complexity
$$
d(n) \cdot \operatorname{polylog}(S(n)),
$$
and the prover runs in time $\operatorname{poly}(S(n))$ (Theorem 1.1, p. 27:5).

In the current wiki, this is a key bridge between classical interactive-proof theory and the later practical dream of verifiable delegated computation.

## Key Claims

- The paper gives public-coin interactive proofs for languages computed by log-space-uniform Boolean circuits of size $S(n)$ and depth $d(n)$ (Abstract, p. 27:1; Theorem 1.1, p. 27:5).
- The verifier is substantially cheaper than full recomputation: linear in input length and only polynomial/polylogarithmic in depth and circuit-description parameters (Theorem 1.1, p. 27:5).
- For log-space-uniform $NC$ computations, the result yields an especially attractive delegation regime: polynomial-time prover, quasi-linear verifier, logarithmic verifier space, and polylogarithmic communication (Abstract, p. 27:1; Corollary 1.2, p. 27:5).
- The paper also derives one-round computationally sound arguments, results about public-coin log-space interactive proofs for all of $P$, zero-knowledge consequences, and probabilistically checkable argument variants (Abstract, p. 27:1; Introduction roadmap, p. 27:4).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The main formal result is Theorem 1.1 (p. 27:5): if a language $L$ is computable by an $O(\log S(n))$-space-uniform family of Boolean circuits of size $S(n)$ and depth $d(n)$, then $L$ has an interactive proof with:
1. prover runtime
   $$
   \operatorname{poly}(S(n));
   $$
2. verifier runtime
   $$
   n \cdot \operatorname{poly}(d(n), \log S(n));
   $$
3. verifier space
   $$
   O(\log S(n));
   $$
4. public coins, perfect completeness, soundness $1/2$;
5. communication complexity
   $$
   d(n) \cdot \operatorname{polylog}(S(n)).
   $$

The theorem also states that if the verifier is given oracle access to the low-degree extension of its input, then its runtime drops to
$$
\operatorname{poly}(d(n), \log S(n))
$$
(Theorem 1.1, p. 27:5).

A highlighted corollary is the $NC$ case (Corollary 1.2, p. 27:5): for $L$ in log-space-uniform $NC$,
- the prover runs in polynomial time,
- the verifier runs in time
  $$
  n \cdot \operatorname{polylog}(n),
  $$
- the verifier uses space $O(\log n)$,
- and communication is $\operatorname{polylog}(n)$.

These are the theorem-level asymptotics that make the paper feel like a true delegation result rather than only a complexity-class characterization.

## Methods and Proof Techniques

### 1. Delegation-oriented proof complexity

The paper does not merely ask what proof systems can verify. It asks how to make verification **economically asymmetric** relative to the underlying computation, so that outsourcing is actually worthwhile (Introduction, pp. 27:2–27:4).

### 2. Circuit-depth-sensitive formulation

The theorem is phrased for structured Boolean circuits, letting costs depend explicitly on input size, circuit size, and circuit depth. This is important because parallelizable tractable computation is exactly where delegated verification becomes attractive (Theorem 1.1, p. 27:5).

### 3. Public-coin interactive protocol design

The public-coin form matters both structurally and practically. It makes the protocol cleaner and supports later transformations to arguments and related proof models, as highlighted in the abstract and introduction (Abstract, p. 27:1; pp. 27:4–27:5).

### 4. Low-degree-extension viewpoint

The theorem explicitly singles out the case where the verifier has oracle access to the low-degree extension of its input, which signals the paper's algebraic verification backbone and its connection to later oracle-based proof systems (Theorem 1.1, p. 27:5).

### 5. Consequence extraction beyond the main theorem

The paper pushes its central protocol into multiple consequences:
- one-round computationally sound arguments under extra assumptions,
- a characterization involving public-coin log-space/poly-time verifiers for all of $P$,
- zero-knowledge consequences,
- and probabilistically checkable argument variants
(Abstract, p. 27:1; roadmap, p. 27:4).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The key performance profile is the one in Theorem 1.1 (p. 27:5):

- **Prover time:**
  $$
  \operatorname{poly}(S(n)).
  $$
- **Verifier time:**
  $$
  n \cdot \operatorname{poly}(d(n), \log S(n)).
  $$
- **Verifier space:**
  $$
  O(\log S(n)).
  $$
- **Communication complexity:**
  $$
  d(n) \cdot \operatorname{polylog}(S(n)).
  $$
- **Completeness / soundness:** perfect completeness and soundness $1/2$.

For log-space-uniform $NC$, this simplifies to the especially attractive delegation regime (Corollary 1.2, p. 27:5):
- prover: polynomial time,
- verifier: $n\cdot\operatorname{polylog}(n)$ time,
- verifier space: $O(\log n)$,
- communication: $\operatorname{polylog}(n)$.

This is not yet the later IOP / STARK / SNARK parameter style, but it is already a very strong delegation profile for tractable computation.

## Why It Matters

This paper matters because it shifts the proof-systems story away from only proving hardness-class containments and toward **useful outsourced computation**.

That makes it one of the most important bridge papers in the current wiki. It explains why later SNARK/STARK systems are interesting even when the underlying task is already tractable: the verifier does not want to redo the whole job.

It also makes the delegation objective explicit in engineering terms: a proof system is valuable when it produces a real asymmetry between the cost of computing and the cost of checking.

## Connections to the Wiki

This paper connects strongly to:
- [[Transparent Verification and Verifiable Computation]]
- [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Sum-check Protocol]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]

It sits squarely on the bridge from classical interactive proofs to practical verifiable-computation systems.

## Open Questions / Limitations

- The current note now captures the theorem-level asymptotics directly from the paper's front matter, but a deeper pass could still extract more of the internal protocol structure and algebraic subroutines from later sections.
- The paper targets delegation for tractable computation, not the succinct non-interactive end state that later SNARK/STARK systems emphasize.
- A useful future synthesis could compare this verifier profile more explicitly against later IOP-based delegation work and modern transparent proof systems.

## Suggested Next Reading

- [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- [[Transparent Verification and Verifiable Computation]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]

## Related
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[SNARKs and STARKs Reading Map]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- [[Transparent Verification and Verifiable Computation]]
- [[Sum-check Protocol]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
