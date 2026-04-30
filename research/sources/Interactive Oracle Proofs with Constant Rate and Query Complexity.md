---
date: 2026-04-13
type: source
status: processed
source_kind: paper
created: 2026-04-13
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/2016-324.pdf
authors:
  - Eli Ben-Sasson
  - Alessandro Chiesa
  - Ariel Gabizon
  - Michael Riabzev
  - Nicholas Spooner
year: 2017
tags:
  - iop
  - pcp
  - proof-composition
  - sum-check
related:
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[Interactive Oracle Proofs]]"
  - "[[Probabilistically Checkable Proofs (PCPs)]]"
  - "[[PCP vs MIP vs IOP Lineage]]"
  - "[[Sum-check Protocol]]"
description: "IOP paper showing constant-round oracle proofs can achieve linear proof length with constant query complexity and introducing IOP composition and sublinear sumcheck tools"
---

# Interactive Oracle Proofs with Constant Rate and Query Complexity

## Summary

This paper studies whether interactive oracle proofs can achieve proof-length / query-complexity tradeoffs that are not known for PCPs or IPs alone.

Its main message is yes: even **constant-round IOPs** can beat the best known tradeoffs from the older models. In particular, the paper gives:
- **3-round IOPs for circuit satisfiability** with **linear proof length** and **constant query complexity**,
- **2-round IOPs of proximity for Reed–Solomon codes** with **linear proof length** and **constant query complexity**,
- **1-round IOPs of proximity for tensor product codes** with **sublinear proof length** and **constant query complexity**
(Abstract, p. 1; Section 1.4, pp. 4–6).

The paper also contributes two major tools that it frames as IOP analogues of classical PCP/IP ingredients:
- **interactive proof composition for IOPs**,
- and **sublinear sumcheck for IOPs**
(Abstract, p. 1; Section 1.5, pp. 6–10).

In the current wiki, this is one of the strongest bridge papers from the abstract IOP model to concrete parameter improvements that matter for modern oracle-based proof systems.

## Key Claims

- IOPs can achieve proof-length / query-complexity tradeoffs not known for PCPs or IPs alone (Abstract, p. 1; Section 1, p. 3).
- Circuit satisfiability has **3-round IOPs** with **linear proof length** and **constant query complexity** (Theorem 1.1, p. 5).
- Reed–Solomon codes have **2-round IOPs of proximity** with **linear proof length** and **constant query complexity** (Theorem 1.2, p. 5).
- Tensor product codes have **1-round IOPs of proximity** with **sublinear proof length** and **constant query complexity** (Theorem 1.3, p. 6).
- The paper proves an **interactive proof composition theorem** where proof-length blowup becomes additive rather than exponential in verifier randomness (Section 1.5, pp. 6–7).
- The paper proves a **sublinear-sumcheck theorem for IOPs**, where verifier cost can be sublinear in code block length (Section 1.5, pp. 7–8).

## Formal Definitions and Results

> [!important] Mathematical Rigour
> State definitions, theorems, and key equations precisely. Use LaTeX notation. Cite section/page numbers from the source.

Section 1.2 defines a $k$-round IOP for a relation $R$ as a protocol in which, in round $i$, the verifier sends a message $m_i$ and the prover replies with an oracle string $f_i$ that the verifier may query in the current and later rounds (Section 1.2, pp. 3–4).

The paper measures IOP complexity using parameters such as:
- round complexity $k$,
- answer alphabet size $a$,
- proof length $\ell$,
- verifier randomness $r$,
- query complexity $q$,
- soundness error $\varepsilon$
(Section 1.2, p. 4).

Its first headline theorem states informally that the circuit-satisfiability relation lies in an IOP class with parameters (Theorem 1.1, p. 5):
- $k(n)=3$ rounds,
- alphabet $\mathbb{F}_2$,
- proof length $\ell(n)=a\cdot n$,
- query complexity $q(n)=a$,
- soundness error $1/2$,
for some absolute constant $a>0$.

The next two headline theorems give analogous statements for code proximity:
- Reed–Solomon codes over binary fields admit 2-round IOPPs with linear proof length and constant query complexity (Theorem 1.2, p. 5).
- Tensor product codes admit 1-round IOPPs with sublinear proof length and constant query complexity (Theorem 1.3, p. 6).

The paper also states an **interactive proof composition theorem** in which, given an outer robust PCPP and an inner IOPP for the outer verifier’s relation, one obtains a composed IOPP whose proof length is
$$
\ell = \ell_{\mathrm{out}} + \ell_{\mathrm{in}}
$$
rather than the classical PCP-composition blowup of
$$
\ell_{\mathrm{out}} + 2^{r_{\mathrm{out}}}\ell_{\mathrm{in}}
$$
(Section 1.5, pp. 6–7).

Finally, the paper states a **sublinear sumcheck theorem** showing that if one has suitable PCPs / IOPPs of proximity for certain code constraints, then one can obtain a public-coin IOP for sumchecks over $H^m$ for $C^{\otimes m}$ with verifier complexity inherited from those proximity systems rather than paying linear dependence on the code block length (Section 1.5, pp. 7–8).

## Methods and Proof Techniques

### 1. Interactive proof composition

The paper develops an IOP analogue of proof composition. The key observation is that after the prover sends the outer proof, the verifier may reveal the outer randomness without harming soundness, so the prover only needs to generate one inner proof for the chosen randomness, not one for every possible randomness string (Section 1.5, pp. 6–7).

### 2. Sublinear sumcheck

The classical [[Sum-check Protocol]] gives strong algebraic checking power but can force verifier work linear in the code block length or in degree-related parameters. The paper replaces explicit linear-time checking steps with proximity proofs, thereby reducing verifier work to the complexity of those proximity testers (Section 1.5, pp. 7–8).

### 3. Code-focused IOPP constructions

The Reed–Solomon and tensor-product-code results are obtained by combining the new interactive composition theorem with prior robust PCP / local-testing ingredients and PCPs of proximity for nondeterministic computation (Section 1.5, p. 8).

### 4. Circuit satisfiability via algebraic coding tools without heavy routing

For circuit satisfiability, the paper avoids the heavier routing machinery common in PCP constructions and instead uses one round of interaction to reduce circuit satisfiability directly to a sumcheck instance over a suitably chosen code family, followed by the new sumcheck and proximity-testing tools (Section 1.5, pp. 8–10).

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The headline complexity profile stated in Section 1.4 is:

- **Circuit satisfiability:** 3 rounds, linear proof length, constant query complexity, soundness error $1/2$ (Theorem 1.1, p. 5).
- **Reed–Solomon IOPP:** 2 rounds, linear proof length, constant query complexity, constant proximity parameter, soundness error $1/2$ (Theorem 1.2, p. 5).
- **Tensor product code IOPP:** 1 round, sublinear proof length, constant query complexity, constant proximity parameter, soundness error $1/2$ (Theorem 1.3, p. 6).

For the composition theorem, the central performance improvement is that proof length becomes additive:
$$
\ell = \ell_{\mathrm{out}} + \ell_{\mathrm{in}},
$$
instead of paying an exponential factor in the outer verifier’s randomness (Section 1.5, pp. 6–7).

For the sublinear sumcheck theorem, the verifier time becomes roughly
$$
m\cdot t_v^{\mathrm{SC}} + O(m),
$$
with query complexity
$$
m\cdot q_{\mathrm{SC}} + m + 1,
$$
so the verifier inherits sublinear dependence on code block length from the underlying proximity proof system rather than scanning full codewords (Section 1.5, pp. 7–8).

## Why It Matters

This paper matters because it makes the case that IOPs are not just a cleaner abstraction — they are a **strictly more productive parameter-design space** than the currently known PCP or IP constructions.

In the current wiki, it deepens several themes at once:
- the distinction between static PCPs and interactive oracle models,
- the importance of [[Sum-check Protocol]] as a reusable algebraic backbone,
- the bridge from PCP/MIP history into oracle/proximity-based modern proof systems,
- and the specific route from IOPs toward RS-proximity and STARK-era thinking.

This paper is also especially helpful after [[PCP vs MIP vs IOP Lineage]], because it supplies a concrete example of *why* IOPs deserve to be treated as more than just "PCPs with rounds".

## Connections to the Wiki

This paper should strengthen:
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Sum-check Protocol]]
- the later RS/IOPP / STARK branch through [[FRI]] and [[Reed-Solomon Proximity Testing]]

It is one of the clearest current sources showing the IOP model paying off in actual proof parameters rather than only conceptual cleanliness.

## Open Questions / Limitations

- The current note now captures the formal theorem statements and the two main technical tools from the introduction, but a future pass could still extract more theorem detail from the later technical sections.
- It would be useful to compare these Reed–Solomon IOPP results more explicitly against the later FRI/WHIR-style proximity-testing branch.
- A future synthesis may want to explain more systematically when IOPs outperform known PCPs because of interaction itself versus because of the associated coding-theoretic tooling.

## Suggested Next Reading

- [[Interactive Oracle Proofs]]
- [[PCP vs MIP vs IOP Lineage]]
- [[FRI]]
- [[Reed-Solomon Proximity Testing]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]

## Related
- [[Interactive Oracle Proofs (IOPs)]]
- [[Interactive Oracle Proofs]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Sum-check Protocol]]
