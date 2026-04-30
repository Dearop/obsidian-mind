---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - pcd
  - recursion
  - proof-systems
related:
  - "[[Accumulation Schemes]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
  - "[[WARP]]"
description: "Distributed integrity setting motivating accumulation and recursive proof composition"
---

# Proof-Carrying Data (PCD)

## Definition / framing

Proof-carrying data (PCD) is a cryptographic primitive for distributed computational integrity in which parties propagate computation together with proofs that the evolving computation remains valid.

## Why it matters

PCD is one of the main application-level motivations for accumulation and recursion papers.

In *[[WARP Linear-Time Accumulation Schemes]]*, PCD is the motivating destination: WARP is important because efficient accumulation schemes feed directly into efficient PCD constructions.

## Key distinctions

- PCD generalizes some incrementally verifiable computation settings.
- It is especially relevant in distributed or multi-party computational pipelines.
- Improvements in accumulation or recursive verification often matter because they improve the cost of each PCD step.


## Mathematical background / formulae

PCD is often described using a local compliance predicate
$$
\Phi(m_1,\dots,m_t; m_{\mathrm{out}}, a)=1,
$$
where a node's output message must be locally consistent with its input messages and auxiliary local data $a$.
Each message carries a proof certifying that the entire history leading to that message is compliant.
So recursion happens over a graph of locally checked transitions rather than only over a single path.


## Worked example

Imagine a path of three computation nodes:
$$
m_0 \to m_1 \to m_2 \to m_3.
$$
At each step, the outgoing message carries not just data but also a proof that the local transition was valid and that all prior proofs in the chain were valid too.
If the local compliance rule is
$$
\Phi(m_t,m_{t+1},a_t)=1,
$$
then the proof attached to $m_{t+1}$ certifies the whole history up to that point, not only the latest transition.
This is why PCD is often described as recursive proof-carrying computation over message graphs.

### Formal PCD definition

A PCD system for a compliance predicate $\Phi$ over a directed acyclic graph of messages consists of:
- $\mathsf{PCD.Prove}\bigl(m, \{(m_j, \pi_j)\}_{j \in \mathrm{parents}(m)}, a\bigr) \to \pi$: given a new message $m$, the parent messages with their proofs, and local auxiliary data $a$, produce a proof $\pi$ for $m$.
- $\mathsf{PCD.Verify}(m, \pi) \to \{0, 1\}$: check that $m$ is the head of a $\Phi$-compliant history.

**Compliance predicate.** $\Phi\bigl(m, \{m_j\}_{j \in \mathrm{parents}(m)}, a\bigr) \to \{0, 1\}$ is a local rule that checks whether $m$ is a valid successor given its parents and auxiliary data.

**Soundness.** No PPT adversary can produce $(m^*, \pi^*)$ with $\mathsf{PCD.Verify}(m^*, \pi^*) = 1$ unless $m^*$ lies at the head of some $\Phi$-compliant DAG rooted at genesis messages. Formally:
$$
\Pr[\mathsf{PCD.Verify}(m^*, \pi^*) = 1 \;\wedge\; m^* \text{ has no } \Phi\text{-compliant history}] \leq \mathsf{negl}(\lambda).
$$

### Relationship to IVC

IVC is the special case of PCD where the DAG is a single chain: every node has exactly one parent. PCD generalizes further to:

| Graph shape | Application |
|-------------|------------|
| Linear chain | IVC (sequential step-by-step computation) |
| Tree | MapReduce / recursive divide-and-conquer |
| Arbitrary DAG | Distributed ledgers, multi-party integrity pipelines |

### Worked example — distributed MapReduce

Two workers $W_1, W_2$ each process a data shard and produce:
$$
(m_1, \pi_1) \leftarrow \mathsf{PCD.Prove}(m_1, \{\}, a_1), \qquad (m_2, \pi_2) \leftarrow \mathsf{PCD.Prove}(m_2, \{\}, a_2).
$$
A reducer $R$ receives both, computes $m_R = \mathsf{combine}(m_1, m_2)$, and calls:
$$
\pi_R \leftarrow \mathsf{PCD.Prove}\bigl(m_R, \{(m_1, \pi_1), (m_2, \pi_2)\}, a_R\bigr)
$$
with compliance rule $\Phi(m_R, \{m_1, m_2\}, a_R) = 1$ iff $m_R = \mathsf{combine}(m_1, m_2)$. The final proof $\pi_R$ attests that **both shards were processed correctly** — and a verifier holding only $m_R$ and $\pi_R$ can be convinced without ever re-reading the original shards.


## Current map in this wiki

This hub connects the main recursive-composition architectures currently represented in the vault:
- [[Fractal]] for preprocessing/transparent recursion
- [[WARP]] for accumulation-oriented recursion
- [[Accumulation vs Folding in Recursive Proof Systems]] for the broader branch comparison
- [[Mathematical Preliminaries for SNARKs and STARKs]] for the compact study overview

## Evidence / sources

- [[WARP Linear-Time Accumulation Schemes]]
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

## Related entities

- [[WARP]]
- [[Fractal]]
- [[Benedikt Bünz]]
- [[Alessandro Chiesa]]

## Open questions

- How do preprocessing-PCD approaches like [[Fractal]] compare against accumulation- and folding-based recursion frameworks in terms of assumptions and efficiency?

## Wiki development

- Should this wiki eventually maintain a dedicated comparison of PCD, IVC, recursive SNARKs, and proof-carrying data in blockchains / distributed systems?
