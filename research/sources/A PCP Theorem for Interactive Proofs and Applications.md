---
date: 2026-04-13
type: source
status: processed
source_kind: paper
created: 2026-04-13
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2021-915.pdf
authors:
  - Gal Arnon
  - Alessandro Chiesa
  - Eylon Yogev
year: 2023
tags:
  - iop
  - pcp
  - interactive-proofs
  - snarks
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Probabilistically Checkable Proofs (PCPs)]]"
  - "[[Interactive Oracle Proofs]]"
  - "[[PCP vs MIP vs IOP Lineage]]"
  - "[[Commit-and-Prove SNARKs]]"
description: "Paper generalizing the PCP theorem to interactive proofs by transforming public-coin IPs into local-query IOPs, with applications to approximation hardness and commit-and-prove SNARKs"
---

# A PCP Theorem for Interactive Proofs and Applications

## Summary

This paper asks a natural next question after the PCP theorem and the rise of interactive oracle proofs: if PCPs let a verifier barely read a static proof, can an analogous theorem hold for **interactive proofs**?

The answer is yes. The paper proves a generalization of the PCP theorem to interactive languages: any language with a **public-coin $k(n)$-round interactive proof** also has a **$k(n)$-round public-coin IOP** in which the verifier decides by reading only:
- $O(1)$ bits from each prover message,
- $O(1)$ bits from each verifier random message,
- while using only $O(\log n)$ bits of decision randomness overall
(Abstract, p. 1; Theorem 1, p. 4).

The paper also develops several applications:
- hardness of approximation for stochastic satisfiability,
- IOP-to-IOP transformations previously known only for IPs,
- and a new notion of **index-decodable PCPs** that yields commit-and-prove SNARKs in the random oracle model
(Abstract, p. 1; Sections 1.1–1.2, pp. 4–8).

## Key Claims

- Any language with a public-coin $k(n)$-round IP with constant soundness error has a $k(n)$-round IOP in which the verifier reads only $O(1)$ bits from each prover and verifier message and uses $O(\log n)$ bits of decision randomness (Abstract, p. 1; Theorem 1, p. 4).
- The round complexity is preserved under the IP $\to$ IOP transformation (Theorem 1, p. 4).
- The paper generalizes the PCP theorem from NP-style static proofs to interactive-proof protocols (pp. 3–4).
- The transformation yields new hardness-of-approximation results for $k$-SSAT, showing AM[$k$]-completeness for distinguishing value $1$ from value at most $1-1/O(k)$ (Theorem 2, p. 5).
- The paper introduces **index-decodable PCPs** and uses them to obtain commit-and-prove SNARKs in the random oracle model with argument size $O_\lambda(q\log l)$ from suitable ID-PCPs (Theorem 3, pp. 7–8).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

The paper explicitly recalls the classical PCP theorem as
$$
NP = PCP[O(\log n), O(1)]
$$
(Section 1, p. 3).

Its main theorem is the interactive analogue (Theorem 1, p. 4):

> Let $L$ be a language with a public-coin IP with $k$ rounds and constant soundness error. Then $L$ has an IOP with $k$ rounds, constant soundness error, where the verifier decides by using $O(\log n)$ bits of decision randomness and reading $O(1)$ bits from each prover message and each verifier message. All other parameters are polynomially related.

So the core asymptotic statement is:
- **rounds:** preserved as $k$,
- **per-round local access:** $O(1)$ bits from each communication round,
- **decision randomness:** $O(\log n)$,
- **soundness:** constant.

The first major application is hardness of approximation for stochastic satisfiability. Theorem 2 states that for every $k$, it is AM[$k$]-complete to distinguish whether a $k$-SSAT instance has value $1$ or value at most
$$
1 - \frac{1}{O(k)}
$$
(p. 5).

The paper also states a corollary giving IOP analogues of classical IP transformations: private-coin to public-coin conversion, round reduction, and perfect completeness, while preserving polynomial proof length and $O(1)$ per-round query complexity over a binary alphabet (Corollary 1, p. 6).

Finally, in the cryptographic direction, Theorem 3 states that a suitable index-decodable PCP for relation $R$ with proof length $l$ and query complexity $q$ yields a commit-and-prove SNARK in the ROM for $R$ with argument size
$$
O_\lambda(q \cdot \log l)
$$
where $\lambda$ is the output length of the random oracle (p. 7).

## Methods and Proof Techniques

### 1. IP-to-IOP transformation

The central construction transforms public-coin interactive proofs into interactive oracle proofs while preserving the round structure and forcing the verifier's final decision to depend only on tiny local access to each round's communication (Section 1.1, p. 4; Section 2, p. 9).

### 2. Local access to randomness and prover messages

A key technical issue is not only local access to prover messages, but also local access to the verifier's own random messages. The paper treats both problems as first-class technical components, as reflected in the techniques roadmap: local access to randomness and local access to prover messages (Section 2 table of contents; Section 1.1, pp. 4–6).

### 3. Index-decodable PCPs

The paper introduces **index-decodable PCPs**, a PCP variant for statements involving separately encoded data oracles plus a PCP oracle. The security notion is decodability: if the verifier accepts often enough, each data oracle and the PCP string can be decoded into a collectively valid statement (Section 1.2.1, pp. 6–7).

### 4. Consequence extraction across complexity theory and cryptography

The result is not merely a simulation theorem. The paper pushes the transformation into:
- hardness of approximation for stochastic satisfiability,
- IOP analogues of classic IP transformations,
- and commit-and-prove SNARKs in the random oracle model
(Sections 1.1–1.2, pp. 4–8).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The core performance profile stated in Theorem 1 is:
- **rounds:** $k$ rounds, preserved from the original public-coin IP (p. 4);
- **verifier local access:** $O(1)$ bits from each prover message and each verifier message (p. 4);
- **decision randomness:**
  $$
  O(\log n)
  $$
  (p. 4);
- **other parameters:** polynomially related to those of the original IP (p. 4).

For the hardness application, the approximation gap achieved for $k$-SSAT is of the form
$$
1 \quad \text{versus} \quad 1 - \frac{1}{O(k)}
$$
(Theorem 2, p. 5).

For the SNARK application, the argument size scales as
$$
O_\lambda(q \log l)
$$
from an ID-PCP of query complexity $q$ and proof length $l$ (Theorem 3, p. 7).

The paper's main efficiency message is structural: interaction can be retained while the verifier's *read access* to the transcript becomes PCP-like and extremely sparse.

## Why It Matters

This paper matters because it makes the relationship among PCPs, IPs, and IOPs much tighter and more theorem-like.

Earlier in the wiki:
- [[Probabilistically Checkable Proofs (PCPs)]] say that static NP proofs can be checked by tiny local access.
- [[Interactive Oracle Proofs]] define IOPs as a hybrid model combining interaction and oracle access.
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]] shows that this hybrid model enables strong parameter tradeoffs.

This paper adds a deeper structural statement: the local-checking spirit of PCPs extends beyond static witnesses and reaches the world of interactive proofs directly.

It also directly connects the IOP story back into cryptography through commit-and-prove SNARKs, which is unusually valuable for this wiki.

## Connections to the Wiki

This paper should strongly reinforce:
- [[Interactive Oracle Proofs (IOPs)]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Interactive Oracle Proofs]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Commit-and-Prove SNARKs]]

It is also one of the best pages for explaining why the IOP model is not merely a hybrid convenience but a genuine extension of the PCP-theorem viewpoint into interactive settings.

## Open Questions / Limitations

- The current note now captures the theorem-level front matter and application statements, but a deeper pass could still extract more detail from the technical construction in Sections 4–7.
- The wiki still lacks a dedicated concept page for [[index-decodable PCPs]], which this paper strongly motivates.
- A future synthesis could compare this theorem-level IOP perspective more directly with the older delegation and debate-system branches for PSPACE-like interactive computation.

## Suggested Next Reading

- [[Interactive Oracle Proofs]]
- [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Commit-and-Prove SNARKs]]
- [[PCP vs MIP vs IOP Lineage]]

## Related
- [[Interactive Oracle Proofs (IOPs)]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Interactive Oracle Proofs]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Commit-and-Prove SNARKs]]
