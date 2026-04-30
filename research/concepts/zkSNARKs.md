---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - zero-knowledge
  - proof-systems
related:
  - "[[Transparent zkSNARKs]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[Polynomial Commitments]]"
  - "[[Spartan]]"
description: "Umbrella concept page for zero-knowledge succinct non-interactive arguments of knowledge"
---

# zkSNARKs

## Definition / framing

zkSNARKs are **zero-knowledge succinct non-interactive arguments of knowledge**.

At a high level, they let a prover convince a verifier that a statement is true:
- without revealing the witness,
- with a proof much smaller than naively replaying the computation,
- and with verification that is significantly cheaper than recomputing the full statement.

"Succinct" and "non-interactive" are the headline properties, but concrete systems differ substantially in:
- prover cost,
- verifier cost,
- proof size,
- assumptions,
- arithmetization strategy,
- and whether they require a trusted setup.

## Why it matters

This is one of the core umbrella topics for the current vault direction. Many of the papers in the new corpus appear to live in the design space of modern succinct proof systems, especially around trade-offs between:
- trusted setup vs transparency,
- proof size vs prover time,
- generality vs structured computation models,
- and concrete engineering performance.

## Key distinctions

- **Trusted setup vs transparent systems**
  - Some zkSNARKs require setup ceremonies or structured reference strings.
  - Others, like [[Transparent zkSNARKs]], aim to avoid secret trapdoors.

- **Interactive core vs non-interactive wrapper**
  - Many systems begin as interactive arguments and become non-interactive via Fiat-Shamir in the random oracle model.

- **Arithmetization choices**
  - Systems often compile computation into forms like [[Rank-1 Constraint Satisfiability (R1CS)]], arithmetic circuits, or low-degree polynomial relations.

- **Commitment machinery**
  - Modern systems often depend on [[Polynomial Commitments]] or related cryptographic primitives.


## Mathematical background / formulae

For an NP relation $R(x,w)$, a zkSNARK is typically described by algorithms
$$
\mathsf{Setup}(1^\lambda) \to \mathsf{pp},\qquad
\mathsf{Prove}(\mathsf{pp},x,w) \to \pi,\qquad
\mathsf{Verify}(\mathsf{pp},x,\pi) \in \{0,1\}.
$$
Completeness informally says that if $R(x,w)=1$ then an honest proof verifies, while knowledge soundness informally says that a prover producing an accepting proof must “know” a witness. Zero knowledge says the verifier learns nothing beyond the truth of the statement, up to simulation.

### Formal property definitions

**Completeness.** For all $(x, w)$ with $R(x, w) = 1$:
$$\Pr[\mathsf{Verify}(\mathsf{pp}, x, \mathsf{Prove}(\mathsf{pp}, x, w)) = 1] = 1.$$

**Soundness (knowledge soundness).** For every PPT prover $P^*$, there exists an extractor $E$ such that for all $x$:
$$\Pr[\mathsf{Verify}(\mathsf{pp}, x, \pi) = 1 \;\wedge\; R(x, w^*) \neq 1] \leq \mathsf{negl}(\lambda),$$
where $\pi \leftarrow P^*(x)$ and $w^* \leftarrow E^{P^*}(x)$.

**Succinctness.** The proof is short and verification is fast relative to the computation:
$|\pi| = \mathsf{poly}(\lambda, \log |x|)$ and $T_{\mathsf{Verify}} = \mathsf{poly}(\lambda, |x|, \log |C|)$.

**Zero knowledge.** There exists a PPT simulator $S$ such that for all $(x, w)$ with $R(x, w) = 1$:
$$\{\mathsf{Prove}(\mathsf{pp}, x, w)\} \approx_c \{S(\mathsf{pp}, x)\}.$$

### Worked example: a toy NP statement

Consider the statement “I know $a, b$ such that $a \cdot b = 15$ and $a > 1$ and $b > 1$.”

- **Public input (instance):** $x = 15$.
- **Witness:** $w = (a, b) = (3, 5)$.
- **Relation:** $R(x, (a, b)) = 1$ iff $a \cdot b = x$ and $a > 1$ and $b > 1$.

A zkSNARK for this relation lets the prover produce a short proof $\pi$ that convinces the verifier of the existence of such $a, b$ without revealing their values:

1. **Completeness** guarantees that the honest prover holding $w = (3, 5)$ always produces an accepting proof.
2. **Soundness** guarantees that no cheating prover can produce an accepting proof unless they actually “know” a valid factorisation.
3. **Zero knowledge** guarantees that the proof $\pi$ reveals nothing about which factorisation the prover used — the verifier cannot distinguish a real proof from one produced by the simulator $S$ that never sees $w$.
4. **Succinctness** guarantees that $|\pi|$ and the verification time are much smaller than naively checking every possible factorisation or replaying the prover's computation.

## Current map in this wiki

This is the umbrella hub for the current SNARK/STARK branch:
- setup axis via [[Trusted Setup]] and [[Transparent zkSNARKs]]
- direct transparent design via [[Spartan]]
- transparent recursion via [[Fractal]]
- lightweight zk compilation via [[VEIL]]
- family comparison via [[VEIL vs Spartan vs Fractal]]
- proof-family comparison via [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related entities

- [[Spartan]]
- [[Srinath Setty]]

## Open questions

- What are the concrete efficiency frontiers for each SNARK family — where does each hit diminishing returns?
- How do post-quantum assumptions change the practical landscape of SNARK families?

## Wiki development

- Determine which SNARK families matter most for the user's interests as priorities become clearer.
- Eventually create a synthesis comparing the main families (pairing-based, transparent, STARK-style, recursive).
