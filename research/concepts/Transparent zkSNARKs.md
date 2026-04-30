---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - zksnark
  - transparency
related:
  - "[[zkSNARKs]]"
  - "[[Trusted Setup]]"
  - "[[Spartan]]"
description: "Focus page for setup-free/trapdoor-free SNARK design"
---

# Transparent zkSNARKs

## Definition / framing

Transparent zkSNARKs are zkSNARKs that avoid a secret trusted setup. In the framing used by *[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]*, they replace trapdoor-dependent setup with public assumptions and, in some constructions, public preprocessing.

## Why it matters

Transparency is one of the key design axes in succinct proof systems.

It matters because trusted setup introduces operational and trust assumptions that are often undesirable in practice. A transparent system tries to avoid the need for secret setup toxic waste while still preserving succinctness and zero-knowledge.

## Key distinctions

- Transparent does **not** necessarily mean no preprocessing at all.
  - Spartan is important because it highlights the difference between:
    - a **trusted setup** with secret trapdoors, and
    - a **public preprocessing step** that can still be amortized across proofs.

- Transparent does not imply all costs are minimal.
  - Systems may trade proof size, prover time, verifier time, and assumptions differently.

- Some transparent systems only work well for specific computational models.
  - A major claim of [[Spartan]] is that it supports arbitrary R1CS/NP statements rather than only low-depth or uniform/data-parallel structures.


## Mathematical background / formulae

A trusted-setup SNARK often has a hidden-trapdoor generation step such as
$$
(\mathsf{pp},\tau) \leftarrow \mathsf{Gen}(1^\lambda),
$$
where the toxic waste $\tau$ must remain secret.
A transparent system instead aims for public parameters derived without secret trapdoor material, schematically
$$
\mathsf{pp} \leftarrow \mathsf{Gen}(1^\lambda; \rho)
$$
from public randomness $\rho$, or from a public preprocessing/indexing phase.

### Formal transparency property

A SNARK is **transparent** if its setup $\mathsf{Gen}(1^\lambda, C) \to \mathsf{pp}$ satisfies:
- $\mathsf{pp}$ is computed using only public randomness — there is no secret trapdoor $\tau$ held by any party.
- Soundness holds even against an adversary that sees the full setup computation (including the public coins $\rho$ used by $\mathsf{Gen}$).

Equivalently, a transparent SNARK can be simulated by an algorithm that publishes every bit it uses during setup, and the soundness proof goes through unchanged.

### Concrete transparent constructions

Transparent SNARKs replace pairing-trapdoor machinery with alternative commitment and proximity primitives:

- **Sum-check based (Spartan)**: replace pairing-based polynomial commitments with hash-based multilinear commitments. Verification cost comes from running the sum-check protocol, which needs only field arithmetic and hash evaluations. Setup is just sampling a public hash function.
- **FRI / IOPP based (STARK-style)**: replace algebraic commitments with Merkle-hashed Reed–Solomon codewords. Proximity testing via [[FRI]] provides soundness using only collision-resistant hashing.
- **Accumulation based (WARP)**: build recursive composition from hash-based IOPs and IORs, avoiding any structured reference string entirely.

### Cost of transparency

Transparent SNARKs typically pay in proof size:

| Family | Proof size | Verifier time | Prover time |
|--------|-----------|----------------|-------------|
| Pairing-based (trusted) | $O(1)$ group elements | $O(1)$ pairings | $O(|C| \log |C|)$ |
| Hash-based (transparent) | $O(\mathsf{polylog}(|C|))$ hashes | $O(\mathsf{polylog}(|C|))$ hash/field ops | $O(|C|)$ to $O(|C| \log |C|)$ |

In many applications, the larger proof size is acceptable in exchange for eliminating trusted setup — especially when prover time is comparable or better (Spartan achieves linear-time proving in its best variants).

## Current map in this wiki

This hub now splits naturally across three architectural routes:
- [[Spartan]] for native transparent zkSNARK design
- [[Fractal]] for transparent recursion via holography and preprocessing
- [[VEIL]] for lightweight zk compilation on top of transparent multilinear systems
These are compared directly in [[VEIL vs Spartan vs Fractal]], and the proof-family split is compared in [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]].

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

## Related entities

- [[Spartan]]
- [[Fractal]]
- [[VEIL]]
- [[Srinath Setty]]

## Open questions

- What is the practical proof-size vs verification-time frontier for transparent systems compared to pairing-based systems at current security levels?
- Can transparent SNARKs match pairing-based proof sizes with better hash functions or algebraic commitments?

## Wiki development

- Track which later transparent systems supersede or refine Spartan.
- Create a synthesis comparing transparent SNARKs against STARK-family systems.
- Clarify the comparison between built-in zk design and lightweight compilers like [[VEIL]].
