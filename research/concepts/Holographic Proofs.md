---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - holography
  - proof-systems
  - preprocessing
related:
  - "[[Fractal]]"
  - "[[Preprocessing SNARKs]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
description: "Oracle-indexed proof model that enables preprocessing-style succinct verification"
---

# Holographic Proofs

## Definition / framing

A proof is holographic if the verifier does not receive the full circuit or index description explicitly, but instead makes a small number of queries to an encoding of that description.

In the indexed-relations viewpoint, part of the statement is treated as an **index** that is encoded offline and accessed oracle-style by the verifier.

## Why it matters

In *[[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]*, holography is the key bridge between oracle-proof machinery and **preprocessing SNARKs**.

The central idea is that holographic IOPs can be compiled into preprocessing SNARKs because the index can remain encoded and succinctly authenticated rather than being fed explicitly to the verifier each time.

## Key distinctions

- Holography is about **sublinear verification relative to a large index**.
- It is related to preprocessing, but not identical to preprocessing.
- In Fractal, holography is especially important because it makes transparent preprocessing compatible with efficient recursion.


## Mathematical background / formulae

A holographic setting separates an instance into a short online part $x$ and a large indexed part $i$.
Instead of reading $i$ explicitly, the verifier queries an encoding
$$
\mathsf{Enc}(i)
$$
at a small number of locations. Informally, the verifier's online cost is sublinear in $|i|$ because it only inspects
$$
q \ll |\mathsf{Enc}(i)|
$$
positions together with succinct authentication data.

### Formal definition

A holographic proof system for a relation $R$ consists of:

- An encoder $\mathsf{Encode}(C) \to \hat{C}$ that maps a circuit/index $C$ to a holographic oracle $\hat{C}$.
- An interactive prover $P^{\hat{C}}$ and verifier $V^{\hat{C}}$, **both** with oracle access to $\hat{C}$.

**Efficiency requirement.** The holographic verifier $V^{\hat{C}}$ makes at most $q = O(\mathsf{polylog}(|C|))$ queries to $\hat{C}$ during verification, independent of $|C|$ itself.

### Why this enables preprocessing

In a non-holographic proof system, the verifier must read all of $C$, costing $O(|C|)$ work per proof. Holography replaces this with:

1. **Offline phase.** Compute $\hat{C} = \mathsf{Encode}(C)$ and a succinct digest $d_C = \mathsf{Hash}(\hat{C})$ (for example, the root of a Merkle tree over $\hat{C}$). Cost: $O(|C|)$, done **once**.
2. **Online phase.** The verifier holds only $d_C$ and makes $q = O(\mathsf{polylog}(|C|))$ authenticated queries to $\hat{C}$ via Merkle paths. Cost per proof: $O(\mathsf{polylog}(|C|))$.

This is exactly the structure of a **preprocessing SNARK**: an expensive one-time offline encoding followed by many cheap online proofs.

### Connection to Fractal

Fractal's main result is that holographic IOPs can be compiled into preprocessing SNARKs with transparent setup. The compilation path is:
$$
\text{Holographic IOP} \;\xrightarrow{\text{Merkle hash}}\; \text{Preprocessing SNARK} \;\xrightarrow{\text{PCD composition}}\; \text{Recursive transparent proofs}
$$
At each step, no trusted trapdoor is introduced — the encoding $\hat{C}$ is a deterministic function of $C$ and the hash function is public.


## Worked example

Suppose the statement naturally decomposes as:
- a short online input $x$
- a huge indexed object $i$.

Instead of handing the verifier the whole index $i$, the system encodes it as
$$
\mathsf{Enc}(i)
$$
and lets the verifier query only a few locations, such as positions $7$, $19$, and $42$.
The verifier then checks consistency using those queried symbols plus authentication information.
This is the core idea behind “holography”: the verifier interacts with a large indexed object through sparse access rather than full explicit input.


## Current map in this wiki

This is a bridge hub between the oracle-proof branch and the preprocessing-recursion branch:
- [[Interactive Oracle Proofs (IOPs)]] for the surrounding oracle-proof model
- [[Preprocessing SNARKs]] for the main architectural destination
- [[Fractal]] as the anchor system using this route
- [[Mathematical Preliminaries for SNARKs and STARKs]] for the compact study overview

## Evidence / sources

- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

## Related entities

- [[Fractal]]
- [[Alessandro Chiesa]]
- [[Dev Ojha]]
- [[Nicholas Spooner]]

## Open questions

- Which later systems still rely directly on holographic ideas, versus using them mainly as a stepping stone to preprocessing?

## Wiki development

- Should the wiki eventually split holographic PCPs, holographic IOPs, and algebraic holographic proofs into separate pages?
