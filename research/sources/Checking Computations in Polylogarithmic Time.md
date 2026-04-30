---
date: 2026-04-13
type: source
status: processed
source_kind: paper
created: 2026-04-13
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/103418.103428.pdf
authors:
  - László Babai
  - Lance Fortnow
  - Leonid A. Levin
  - Mario Szegedy
year: 1991
tags:
  - interactive-proofs
  - verifiable-computation
  - transparent-proofs
  - classical-foundations
related:
  - "[[Checking Computations in Polylogarithmic Time]]"
  - "[[Delegating Computation Interactive Proofs for Muggles]]"
  - "[[Transparent Verification and Verifiable Computation]]"
  - "[[Algebraic Methods for Interactive Proof Systems]]"
  - "[[SNARKs and STARKs Reading Map]]"
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Classical bridge paper on transforming computations and proofs into forms checkable in polylogarithmic Monte Carlo time"
---

# Checking Computations in Polylogarithmic Time

## Summary

This paper studies how to transform computations and proof objects into representations that a small trusted checker can verify in **polylogarithmic Monte Carlo time**.

Its core vision is strikingly modern: if a computation or proof is too expensive to re-run directly, perhaps it can be encoded so that correctness becomes checkable through very small randomized local tests. The paper frames such transformed objects as **transparent proofs** (Abstract, p. 21; Section 1.2, p. 22).

In the current wiki, this is one of the clearest early statements of the broader verification-asymmetry dream later seen in delegation, succinct arguments, and recursive proof systems.

## Key Claims

- Every nondeterministic computational task can be transformed so that accepted instances remain the same while witness checking becomes possible in polylogarithmic Monte Carlo time (Abstract, p. 21).
- Every deterministic proof system has a probabilistic extension in which ordinary proofs can be converted into **transparent proofs** checkable in polylogarithmic time (Theorem 1.1, Section 1.2, p. 22).
- Strong error-correcting encodings are essential because ultra-fast checkers cannot read enough of the object to recover from arbitrary corruption by exhaustive inspection (Section 1.2, p. 22).
- The paper gives an early and explicit operational framing of verification asymmetry: a tiny trusted checker can monitor much larger unreliable computations or proof objects (Abstract, p. 21; Section 1.1, pp. 21–22).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

Let $S(x,y)$ be a nondeterministic polynomial-time relation between an instance $x$ and witness $y$. The abstract states that the paper constructs a modified task $S'$ such that (Abstract, p. 21):
- the same instances remain accepted,
- each instance/witness pair becomes checkable in polylogarithmic Monte Carlo time,
- and a witness satisfying $S'$ can be computed in polynomial time from a witness satisfying $S$.

The paper then reformulates this in proof-system language. In Section 1.2 it defines a proof $P$ of a theorem candidate $T$ to be **transparent** if it is accepted in polylogarithmic time in the total encoded size of $(T,P)$ (Section 1.2, p. 22).

It also defines a proof system to be **friendly** if every ordinary proof can be transformed in polynomial time into a transparent proof of the same theorem (Section 1.2, p. 22). The main theorem on this front is:

> **Theorem 1.1.** Each deterministic proof system has a friendly probabilistic extension (Section 1.2, p. 22).

If we write
$$
N := \mathrm{size}(T,P),
$$
then Section 1.2 sharpens the asymptotic claim for the specific complete proof system constructed in the paper: for any $c>0$, proofs can be transformed in time
$$
N^{1+c}
$$
into transparent proofs verifiable in time
$$
(\log N)^{O(1/c)}
$$
(Section 1.2, p. 22; Abstract, p. 21).

The paper also stresses that the theorem candidate must be supplied in an error-correcting encoding, because otherwise slight alterations to the statement could not be reliably detected by a checker that only inspects polylogarithmically many positions (Section 1.2, p. 22).

## Methods and Proof Techniques

### 1. Transparent-proof viewpoint

The paper explicitly elevates a new verification target: not merely polynomial-time verification, but verification so fast that the checker sees only a tiny fraction of the encoded object (Section 1.2, p. 22).

### 2. Reduction to specially structured complete problems

Rather than handling arbitrary proof systems directly, the paper routes through specially structured complete problems for nearly-linear nondeterministic computation, so that proof objects can be encoded into locally testable forms (Section 2, pp. 23–24).

### 3. Error-correcting encoding and local checking

The theorem candidate must itself be supplied in error-correcting form, because a checker running in polylogarithmic time cannot reliably detect small adversarial changes by full inspection. The paper emphasizes this as a necessary condition, not a cosmetic encoding choice (Section 1.2, p. 22).

### 4. Reliability / monitoring framing

The abstract and introduction repeatedly frame the result as a reliability architecture: a single trusted checker can monitor a large collection of unreliable machines or very long formal proofs (Abstract, p. 21; Section 1.1, pp. 21–22).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The strongest concrete asymptotic claims stated near the front of the paper are (Abstract, p. 21; Section 1.2, p. 22):

- **Checker / verifier time:** polylogarithmic Monte Carlo time.
- **Transparent-proof conversion time:** for any $c>0$,
  $$
  N^{1+c}
  $$
  where $N = \mathrm{size}(T,P)$.
- **Transparent-proof verification time:**
  $$
  (\log N)^{O(1/c)}.
  $$
- **Error-correcting code overhead:** messages of length $N$ can be mapped to codewords of length less than
  $$
  N^{1+c}
  $$
  while still allowing recovery of any bit of the nearest codeword in polylogarithmic time, for the corruption regime stated in the abstract (Abstract, p. 21).

This is not a modern benchmark paper, so the key implementation lesson is structural rather than empirical: verification becomes dramatically cheaper only after aggressively redesigning the representation being checked.

## Why It Matters

This paper matters because it is one of the earliest and clearest formulations of the idea that correctness should become **dramatically cheaper to check than to produce**.

In the current wiki, it sits naturally between:
- classical algebraic verification papers,
- later delegation-oriented papers,
- and modern recursion/IVC/PCD motivations.

It is especially valuable because it makes explicit a systems intuition that later literature sometimes takes for granted: proof systems are useful not only because of language characterization theorems, but because they can turn very large computations into cheaply checkable evidence.

## Connections to the Wiki

This paper belongs on the bridge between:
- the classical proof-complexity branch,
- the delegation / verifiable-computation branch,
- and the recursive / carried-evidence branch.

It connects especially well to:
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Transparent Verification and Verifiable Computation]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]

## Open Questions / Limitations

- The paper is conceptually close to later succinct-proof ambitions, but it predates the now-standard PCP / IOP / commitment vocabulary.
- The current note now captures the theorem-level front matter of the paper, but a deeper pass could still extract more of the complete-problem machinery from later sections.
- Another open explanatory task is whether this paper is best read as an ancestor of PCP-style proof encoding, delegation systems, or both.

## Suggested Next Reading

- [[Transparent Verification and Verifiable Computation]]
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Linear-Size Constant-Query IOPs for Delegating Computation]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]

## Related
- [[Delegating Computation Interactive Proofs for Muggles]]
- [[Transparent Verification and Verifiable Computation]]
- [[SNARKs and STARKs Reading Map]]
- [[Proof-Carrying Data (PCD)]]
- [[Incrementally Verifiable Computation (IVC)]]
- [[Algebraic Methods for Interactive Proof Systems]]
