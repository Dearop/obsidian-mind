---
date: 2026-04-11
type: concept
created: 2026-04-11
updated: 2026-04-11
tags:
  - setup
  - zk-snarks
  - proof-systems
related:
  - "[[zkSNARKs]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Spartan]]"
  - "[[Fractal]]"
description: "Setup-assumption page clarifying the contrast between toxic-waste ceremonies and transparent/public preprocessing"
---

# Trusted Setup

## Definition / framing

A trusted setup is a setup procedure that generates secret trapdoor material used to produce public proving and verification parameters for a proof system.

The core risk is that if the secret trapdoor is retained or leaked, then proofs may be forgeable.

## Why it matters

Trusted setup is one of the main fault lines in the modern zkSNARK design space.

A large part of the current corpus is easier to organize if this distinction is explicit:
- some systems accept a setup ceremony in exchange for smaller proofs or faster verification,
- others try to be **transparent**, meaning they avoid secret toxic waste and rely instead on public preprocessing, random oracles, hash-based machinery, or other trapdoor-free assumptions.

In the current wiki:
- [[Spartan]] is important because it emphasizes **public preprocessing without a secret trapdoor**.
- [[Fractal]] is important because it pursues transparent recursion without relying on pairing-friendly recursive setup cycles.

## Key distinctions

- **Trusted setup** is different from **public preprocessing**.
  - Public preprocessing may still amortize verifier work without introducing secret toxic waste.
- **Universal / updatable setup** is different from a one-off circuit-specific trusted setup, though both still live in the broader setup-design space.
- The practical question is rarely only “trusted or transparent?”; it is also about what proof size, verifier cost, recursion story, and implementation complexity come with each choice.


## Mathematical background / formulae

A trusted setup is usually modeled as a generation procedure
$$
(\mathsf{pp},\tau) \leftarrow \mathsf{Gen}(1^\lambda),
$$
where $\mathsf{pp}$ is published and the trapdoor $\tau$ must be destroyed.
The security concern is that if an adversary learns or keeps $\tau$, then it may be able to create forged proofs that still verify under $\mathsf{pp}$.

### Formal definitions

**Trusted setup ceremony.** Given a circuit $C$ describing the relation to be proved:
$$\mathsf{Gen}(1^\lambda, C) \to (\mathsf{pp}, \tau),$$
where $\mathsf{pp}$ is published and $\tau$ is the toxic waste (trapdoor) that must be destroyed.

**Security requirement (simulation-extractability).** Even given $\mathsf{pp}$, no PPT adversary can produce a valid proof for a false statement without knowing $\tau$:
$$\Pr[\mathsf{Verify}(\mathsf{pp}, x, \pi) = 1 \;\wedge\; x \notin L] \leq \mathsf{negl}(\lambda).$$

**Toxic waste risk.** If an adversary learns $\tau$, they can forge proofs: $\exists\; \mathsf{Forge}(\tau, x) \to \pi$ such that $\mathsf{Verify}(\mathsf{pp}, x, \pi) = 1$ for arbitrary $x$.

**Contrast with transparent setup.** In a transparent scheme the generation procedure produces no secret trapdoor:
$$\mathsf{Gen}(1^\lambda, C) \to \mathsf{pp},$$
with no $\tau$ — the setup uses only public randomness.
See [[Transparent zkSNARKs]] for the full transparent story.

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

## Related entities

- [[Spartan]]
- [[Fractal]]
- [[Srinath Setty]]
- [[Alessandro Chiesa]]

## Open questions

- Can universal and updatable setups (e.g., Marlin, PLONK) fully close the trust gap, or does any structured reference string carry residual risk?
- What concrete attacks have been demonstrated against improperly destroyed toxic waste in real deployments?

## Wiki development

- Add canonical anchors for universal and updatable setup models as those papers are ingested.
- Create a synthesis comparing setup assumptions against transparency, recursion, and concrete efficiency.
