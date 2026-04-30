---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - snark
  - preprocessing
  - recursion
related:
  - "[[Fractal]]"
  - "[[Holographic Proofs]]"
  - "[[Proof-Carrying Data (PCD)]]"
description: "Offline/online SNARK architecture central to Fractal's recursion strategy"
---

# Preprocessing SNARKs

## Definition / framing

Preprocessing SNARKs are SNARKs with an offline phase that preprocesses a circuit / index into a succinct verification key, after which online proofs for different instances can be verified much more cheaply.

In the framing of *[[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]*, preprocessing means the verifier runs in time polylogarithmic in the circuit size rather than needing to read the full circuit description online.

## Why it matters

This concept is central to Fractal's recursion strategy.

The paper's main architectural observation is that **recursive composition is simpler for preprocessing SNARKs** because recursive verification can work with a succinct preprocessed key instead of repeatedly handling a full circuit description.

## Key distinctions

- Preprocessing is a verifier-architecture property, not a standalone cryptographic assumption.
- In Fractal, preprocessing is tightly tied to holography and indexed relations.
- Preprocessing SNARKs are especially useful in recursive settings because they reduce verifier-circuit size.


## Mathematical background / formulae

A preprocessing SNARK separates an offline phase from the online proving phase:
$$
(pk,vk) \leftarrow \mathsf{Setup}(C),
$$
where $C$ is the circuit / indexed computation. Later, for each instance $x$ and witness $w$,
$$
\pi \leftarrow \mathsf{Prove}(pk,x,w),\qquad \mathsf{Verify}(vk,x,\pi)=1.
$$
The point is that the verifier does not need to re-process the full circuit description online.


## Worked example

Suppose many proofs will be generated for the same computation $C$ but with different public inputs $x$ and witnesses $w$.
A preprocessing SNARK first runs
$$
(pk,vk) \leftarrow \mathsf{Setup}(C).
$$
After that, two different users might prove two different statements using the same preprocessed key:
$$
\pi_1 \leftarrow \mathsf{Prove}(pk,x_1,w_1),
\qquad
\pi_2 \leftarrow \mathsf{Prove}(pk,x_2,w_2).
$$
The verifier reuses the same succinct verification key $vk$ each time, which is exactly why preprocessing can be useful for recursion and repeated proving.

### Cost split

The core efficiency argument of a preprocessing SNARK is that costs factor cleanly into one expensive offline step and many cheap online steps:

| Phase | Typical cost | Frequency |
|-------|--------------|-----------|
| $\mathsf{Preprocess}$ | $O(|C|)$ or $O(|C| \log |C|)$ | Once per circuit |
| $\mathsf{Prove}$ | $O(|C|)$ or $O(|C| \log |C|)$ | Per proof |
| $\mathsf{Verify}$ | $O(|x| + \mathsf{polylog}(|C|))$ | Per proof |

The crucial property is that the **verifier's online cost is sublinear in $|C|$** — this is what makes it a succinct argument. The preprocessing cost is folded into the offline phase and amortized across all subsequent proofs.

### Preprocessing with vs without trusted setup

Two variants of preprocessing coexist in the literature:

- **With trusted setup.** $\mathsf{Preprocess}(C) \to (\mathsf{pk}, \mathsf{vk}, \tau)$ produces toxic-waste $\tau$ that must be destroyed. Example: Groth16, where $\tau$ consists of secret scalars used to generate an SRS.
- **With transparent setup (Fractal).** $\mathsf{Preprocess}(C) \to (\mathsf{pk}, \mathsf{vk})$ uses only public randomness. The preprocessing is a **deterministic encoding** of $C$ (a holographic encoding), not a secret-dependent ceremony.

This distinction matters because "preprocessing" and "trusted setup" are often conflated. Fractal's main architectural point is that you can have one without the other: a transparent preprocessing SNARK has all the recursion-friendly properties of Groth16-style preprocessing, but without any trapdoor.

### Amortization across many instances

If the same circuit $C$ is used for $k$ different inputs $(x_1, w_1), \dots, (x_k, w_k)$, total cost is
$$
T_{\text{total}} \;=\; \underbrace{O(|C|)}_{\text{one-time preprocess}} \;+\; k \cdot \underbrace{O(|C|)}_{\text{per proof}} \;+\; k \cdot \underbrace{O(\mathsf{polylog}(|C|))}_{\text{per verify}}.
$$
The verifier side is where preprocessing shines: reading the circuit only once and then verifying $k$ proofs at polylogarithmic cost each, rather than $O(k \cdot |C|)$ total.


## Current map in this wiki

This concept is the main hub for the preprocessing-recursion route in the current branch:
- [[Fractal]] as the main anchor
- [[Holographic Proofs]] as the bridge into preprocessing
- [[Proof-Carrying Data (PCD)]] as the recursive destination
- [[VEIL vs Spartan vs Fractal]] and [[Accumulation vs Folding in Recursive Proof Systems]] as the main comparison pages around alternative architectures

## Evidence / sources

- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

## Related entities

- [[Fractal]]
- [[Alessandro Chiesa]]
- [[Dev Ojha]]
- [[Nicholas Spooner]]

## Open questions

- Which later recursion systems in the corpus truly rely on preprocessing SNARKs as a core architectural move?

## Wiki development

- How should the wiki compare preprocessing recursion with accumulation- and folding-based recursion frameworks?
