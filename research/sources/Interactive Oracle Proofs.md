---
date: 2026-04-10
type: source
status: processed
source_kind: paper
created: 2026-04-10
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2016-116.pdf
authors:
  - Eli Ben-Sasson
  - Alessandro Chiesa
  - Nicholas Spooner
year: 2016
tags:
  - iop
  - proof-systems
  - random-oracle-model
  - compiler
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Proofs (IOPs) vs Interactive Oracle Reductions (IORs)]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Fiat-Shamir Transform]]"
  - "[[State Restoration Attacks]]"
  - "[[WHIR]]"
  - "[[WARP]]"
  - "[[SNARKs and STARKs Reading Map]]"
description: "Foundational IOP paper linking PCPs, IPs, random-oracle compilation, and state restoration security"
---

# Interactive Oracle Proofs

## Summary

This paper introduces **interactive oracle proofs (IOPs)** as a formal model combining two earlier proof traditions:
- **interactive proofs (IPs)**, where prover and verifier exchange rounds of messages,
- and **probabilistically checkable proofs (PCPs)**, where the verifier queries a large proof rather than reading it in full.

In an IOP, the prover's round messages are treated as **oracle strings**. The verifier interacts over multiple rounds but only queries small portions of those messages (Abstract, p. 1; Section 1.3.1, p. 5).

The paper's two main contributions are:
1. defining and analyzing IOPs as a formal proof-system model;
2. giving a compiler from **public-coin IOPs** to **non-interactive random-oracle proofs (NIROPs)**, with soundness characterized by the new notion of **state restoration attacks**
(Abstract, p. 1; Theorem 1.2, pp. 6–7).

In the current wiki, this is the foundational model paper for the entire oracle-proof middle layer.

## Key Claims

- The paper introduces IOPs as a model combining interaction and local oracle access (Abstract, p. 1; Section 1.3.1, p. 5).
- IOPs characterize **NEXP**, like PCPs and MIPs, rather than only PSPACE like ordinary IPs (Section 1.3.1, p. 5; Appendix A).
- Public-coin IOPs can be compiled into non-interactive random-oracle proofs, generalizing both Fiat–Shamir-style IP compilation and PCP-style CS-proof compilation (Abstract, p. 1; Theorem 1.2, pp. 6–7).
- The relevant soundness notion for the compiler is resistance to **state restoration attacks** (pp. 6–8).
- The compiler preserves important properties such as zero knowledge, proofs of knowledge, and linear runtime overhead up to polynomial factors in the security parameter (Theorem 1.2 discussion, pp. 6–7).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

Section 1.3.1 defines a $k$-round IOP as a protocol in which, in round $i$, the verifier sends a message $m_i$ that is read in full by the prover, and the prover replies with an oracle string $f_i$ that the verifier may query in that and later rounds (p. 5).

The model measures efficiency by:
- proof length $p$, the total number of bits in prover messages;
- query complexity $q$, the total number of queried locations;
- round complexity $k$
(Section 1.3.1, p. 5).

The paper states that IOPs characterize NEXP, like PCPs, and can be public-coin transformed and repeated analogously to IPs (Section 1.3.1, p. 5; Appendix A and Appendix B).

The main compilation result is Theorem 1.2 (pp. 6–7): there exists a polynomial-time transformation $T$ such that if $(P,V)$ is a public-coin IOP for relation $R$ with state-restoration soundness $ssr(x,b)$, then $T(P,V)$ is a NIROP for $R$ with soundness
$$
ssr(x,m) + O(m^2 2^{-\lambda}),
$$
where $m$ bounds the malicious prover's number of random-oracle queries and $\lambda$ is the security parameter.

The paper also defines state-restoration soundness and proves general bounds on it. Theorem 1.5 states that for a public-coin $k$-round IOP and instance $x$ outside the language,
$$
\binom{b}{k(x)+1} s(x) (1-o(1)) \le ssr(x,b) \le \binom{b}{k(x)+1} s(x),
$$
up to the more precise constant-factor formulation in the paper, where $s(x)$ is the ordinary soundness error and $b$ is the round budget of the restoring prover (p. 8).

## Methods and Proof Techniques

### 1. Formalizing the IOP model

The paper isolates a clean hybrid model where the prover's large messages are queried rather than fully read. This is the conceptual move that makes much later STARK-style and oracle-proof protocol language feel natural (Section 1.3.1, p. 5).

### 2. Complexity-theoretic sanity checks

The paper proves that the model is robust and non-pathological by establishing NEXP expressivity, soundness-error reduction by repetition, and public-coin conversion (Section 1.3.1, p. 5; Appendices A–B).

### 3. Random-oracle compilation

The NIROP compiler is one of the paper's most consequential contributions. It generalizes both Fiat–Shamir for public-coin IPs and CS-proof-style compilation for PCPs (Section 1.3.2, pp. 6–7).

### 4. State restoration soundness

The paper introduces **state restoration attacks**, where a malicious prover can rewind the verifier to previously seen states with fresh randomness. This yields the right soundness lens for random-oracle compilation of oracle-based interactive systems (Section 1.3.2–1.3.3, pp. 6–8).

### 5. Tree-exploration interpretation

The paper further relates state restoration to tree exploration games, giving a structural interpretation of optimal attacks and clarifying the combinatorics of rewinding in these models (Section 1.3.3, p. 8; Section 8 in the roadmap, p. 2).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

This paper is more model-theoretic and compiler-theoretic than benchmark-driven, so the most important performance features are structural:

- **IOP proof length:** total prover message length $p$ (Section 1.3.1, p. 5).
- **IOP query complexity:** total number of queried locations $q$ (Section 1.3.1, p. 5).
- **IOP round complexity:** $k$ (Section 1.3.1, p. 5).
- **Compilation soundness loss:**
  $$
  ssr(x,m) + O(m^2 2^{-\lambda})
  $$
  for NIROP soundness (Theorem 1.2, pp. 6–7).
- **Compiler overhead:** the NIROP prover and verifier runtimes are linear in those of the IOP prover and verifier up to polynomial factors in the security parameter $\lambda$ (Theorem 1.2 discussion, p. 7).

For implementation intuition, the main message is:
- transcript discipline matters,
- oracle-message commitment structure matters,
- challenge derivation order matters,
- and soundness cannot be understood purely through ordinary non-rewinding intuition.

## Why It Matters

This paper matters because it provides the model language for a large portion of the modern proof-systems landscape.

Without it, later systems like WHIR, many RS/IOPP pipelines, and random-oracle compiled transparent arguments are harder to describe cleanly. With it, the picture becomes much clearer:
- PCPs explain static local checking,
- IOPs explain interactive local checking over oracle messages,
- and later specialized subclasses such as [[Interactive Oracle Proofs of Proximity (IOPPs)]] explain proximity-testing systems.

It is also crucial because it does not stop at definition: it gives the compilation story that connects the model directly to cryptographic proof systems.

## Connections to the Wiki

This paper is foundational for:
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Fiat-Shamir Transform]]
- [[State Restoration Attacks]]
- [[WHIR]]
- [[WARP]]
- [[PCP vs MIP vs IOP Lineage]]
- [[SNARKs and STARKs Reading Map]]

It also helps clarify the distinction between:
- IOP-based proximity / STARK-substrate systems,
- and IOR-based accumulation / recursion systems.

## Open Questions / Limitations

- The current note now captures the model definition, compilation theorem, and state-restoration bounds from the introduction, but a future pass could still extract more detail from the formal definitions in Sections 4–7.
- Later work often abstracts away the full state-restoration analysis once the model becomes familiar; revisiting that nuance may still matter in security-sensitive settings.
- A useful future comparison is how much of modern proof-system practice is best understood at the level of generic IOPs versus more specialized models like IOPPs, holographic IOPs, and polynomial IOPs.

## Suggested Next Reading

- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[A PCP Theorem for Interactive Proofs and Applications]]
- [[PCP vs MIP vs IOP Lineage]]

## Related
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs (IOPs) vs Interactive Oracle Reductions (IORs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Fiat-Shamir Transform]]
- [[State Restoration Attacks]]
- [[WHIR]]
- [[WARP]]
- [[SNARKs and STARKs Reading Map]]
