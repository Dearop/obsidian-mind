---
date: 2026-02-25
type: source
status: processed
source_kind: paper
created: 2026-04-30
updated: 2026-04-30
raw_path: raw/papers/SNARKs & STARKs/2026-391.pdf
authors:
  - Alessandro Chiesa
  - Giacomo Fenzi
  - Guy Weissenberg
year: 2026
tags:
  - iopp
  - zero-knowledge
  - interleaved-codes
  - code-switching
  - sumcheck
  - r1cs
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Proofs of Proximity (IOPPs)]]"
  - "[[Interactive Oracle Reductions (IORs)]]"
  - "[[Constrained Interleaved Codes]]"
  - "[[Sum-check Protocol]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[WARP]]"
  - "[[WHIR]]"
description: "HVZK IOPPs for constrained interleaved codes with 1+o(1) overhead, composable HVZK IOR definitions, and zero-knowledge sumcheck/code-switching building blocks."
---

# Zero-Knowledge IOPPs for Constrained Interleaved Codes

## Summary

This paper gives a concretely efficient **honest-verifier zero-knowledge (HVZK) IOPP** for testing proximity to constrained interleaved codes, with essentially no asymptotic overhead versus non-private state-of-the-art constructions (Abstract, p. 1; Section 1.1, pp. 4-6).

The core technical move is to formalize HVZK for **interactive oracle reductions (IORs)** in a composition-friendly way, then build the final protocol from modular HVZK components:
- a zero-knowledge sumcheck IOR,
- a zero-knowledge code-switching IOR,
- and a constrained-code protocol assembly that preserves round-by-round knowledge soundness (Technical overview and sections listed in Contents, pp. 2-3).

The paper also provides an HVZK reduction from [[Rank-1 Constraint Satisfiability (R1CS)]], and studies high-distance code constructions from dispersers as an efficiency/soundness lever (Contents, pp. 2-3; Sections 11-12).

## Key Claims

- Existing efficient code-agnostic interleaving-based IOPs lacked privacy, and this work adds HVZK while keeping overhead negligible in key regimes (Introduction, pp. 3-4).
- For constrained interleaved-code testing, they obtain a sublinear-regime IOPP with communication roughly $O(m_C)+\tilde O(k\lambda)$ symbols and soundness error $2^{-\lambda}$ under field-size / mutual-correlated-agreement conditions (Theorem 1 informal, pp. 4-5).
- They provide an HVZK code-switching IOR that maps one constrained interleaved-code relation to another, enabling broader parameter regimes beyond the basic sublinear case (Theorem 2 informal, pp. 5-6).
- They define HVZK for IORs in a way that supports composition (Section 2.3 in overview, p. 2; formalized later in Section 4).
- They provide an HVZK reduction from R1CS to constrained-code testing (Section 11, pp. 66+), positioning this as a path to private hash-based arguments.

## Formal Definitions and Results

> [!important] Mathematical Rigour
> Statement-level summary only; verify constants and side conditions against the formal theorem numbering in Sections 4-12 when using this note for proofs.

### Zero-knowledge encodings for codes

For an $F$-additive code $C\subseteq\Sigma^m$, an encoding
$$
\mathrm{Enc}_C:F^\ell\times F^r\to\Sigma^m
$$
is $t$-query zero-knowledge if (i) $\mathrm{Im}(\mathrm{Enc}_C)\subseteq C$, and (ii) for any message and any query set $S\subseteq [m]$ with $|S|\le t$, the local view on $S$ can be simulated without the message up to error $\zeta_C$ (Introduction, p. 4).

### Target constrained relation (informal)

The paper studies linear-constraint relations over encoded witnesses, informally of the form
$$
R^{\mathrm{lin}}_{C,T}=\{(x,y,w): y=\mathrm{Enc}_C(\bar f,r)\ \wedge\ \langle \bar f,v\rangle=\mu\},
$$
with succinctly described linear functional data and complexity parameter $T$ (Eq. (1), p. 4).

### Main theorem (informal, constrained interleaved IOPP)

For interleaving parameter $k$, security $\lambda$, and proximity $\delta$, they construct an $O(k)$-round IOPP for $R^{\mathrm{lin}}_{C^{\equiv 2^k},T}$ with:
- prover communication $O(m_C)+\tilde O(k\lambda)$ symbols,
- verifier query complexity $t=O\!\left(\frac{\lambda}{-\log(1-\delta)}\right)$ over alphabet $\Sigma^{2^k}$,
- RBR knowledge soundness error at most $2^{-\lambda}$ under mutual-correlated-agreement assumptions,
- HVZK error inherited from the code encoding ($\zeta_C$) when encoding query budget suffices
(Theorem 1 informal, pp. 4-5).

### HVZK code-switching theorem (informal)

Given two codes with ZK encodings, they build an $O(k)$-round IOR reducing a constrained interleaved instance over $C_1$ to one over $C_2$, preserving negligible-error RBR soundness and HVZK (against bounded-query distinguishers), with communication scaling by $m_{C_2}$ plus low-order terms (Theorem 2 informal, pp. 5-6).

## Methods and Proof Techniques

### 1) Composable HVZK for IORs

The paper's foundational contribution is defining HVZK for IORs so that composition works without leaking through later-stage oracle interactions. This addresses a gap in standard HVZK notions when protocols are chained (overview Section 2.3, p. 2; formal development in Section 4).

### 2) HVZK sumcheck IOR

They adapt sumcheck-style reductions to preserve privacy under the strict communication/query constraints needed by modern IOPPs, with explicit simulator constructions and RBR extraction analysis (Sections 6 and proofs around pp. 37-42).

### 3) HVZK code switching

They private-ize code-switching reductions (which shrink/transform instances) while keeping extraction/soundness guarantees and low overhead (Section 9, pp. 51-60).

### 4) Layered construction strategy

The final constrained-code HVZK IOPP is assembled from these primitives, then lifted to an R1CS reduction pipeline (Sections 10-11, pp. 62-71).

### 5) Disperser-based distance amplification

The paper includes high-distance code constructions from dispersers and discusses implications for soundness-error terms and Merkle-compiled argument size (Section 12, pp. 72-75).

## Complexity and Performance

From Theorem 1 (informal, pp. 4-5), with $N=2^k m_C$:
- **Rounds:** $O(k)$.
- **Communication:** $O(m_C)+\tilde O(k\lambda)$ alphabet symbols; in common parameterizations this is $o(N)$ and can be around $\tilde O(\sqrt N)$ in the sublinear regime.
- **Verifier queries:** $t=O\!\left(\frac{\lambda}{-\log(1-\delta)}\right)$.
- **RBR soundness error:** at most $2^{-\lambda}$ under field-size and agreement assumptions.
- **Zero-knowledge overhead:** claimed as $1+o(1)$ relative to non-private state of the art (Section 1.1 discussion, pp. 4-6).

Operationally, the key claim is not merely asymptotic HVZK existence but practical parameter competitiveness with existing non-private interleaving-based pipelines.

## Why It Matters

This fills a major gap in the code-agnostic IOPP line: efficient interleaving-based protocols had excellent performance but weak privacy support. The paper argues that HVZK can be added without paying the historical $\ge 2\times$ overhead that discouraged deployment (Introduction, pp. 3-4).

It also strengthens the systems bridge from interactive-oracle machinery to private transparent arguments by combining:
- composable privacy definitions,
- straightline round-by-round extractability,
- and constrained-code friendliness needed by modern compilers.

## Connections to the Wiki

- Extends the wiki's [[Interactive Oracle Proofs of Proximity (IOPPs)]] trajectory from non-private to private constructions.
- Sits near [[WARP]] and [[WHIR]] as part of the post-FRI specialized proximity-machinery wave, but emphasizes HVZK composition for interleaving/code-switching.
- Directly relevant to [[Constrained Interleaved Codes]], [[Interactive Oracle Reductions (IORs)]], and [[Sum-check Protocol]].
- Important bridge node for [[Rank-1 Constraint Satisfiability (R1CS)]] reductions and transparent SNARK pipelines.

## Open Questions / Limitations

- Which parts of the best parameter claims are fully unconditional versus tied to agreement/list-size assumptions in concrete code families?
- How do prover constants compare in practice against modern non-private baselines and RS-centric private systems at equal security?
- This note still needs theorem-by-theorem extraction of formal statements (with exact numbering and constants) for citation-grade use.
- Relationship to PCS-centric systems should be made explicit in a future synthesis note.

## Suggested Next Reading

- [[WARP Linear-Time Accumulation Schemes]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## Related
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs of Proximity (IOPPs)]]
- [[Interactive Oracle Reductions (IORs)]]
- [[Constrained Interleaved Codes]]
- [[Sum-check Protocol]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[WARP]]
- [[WHIR]]