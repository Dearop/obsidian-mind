---
date: 2026-04-11
type: synthesis
status: stable
created: 2026-04-11
updated: 2026-04-11
tags:
  - mathematics
  - preliminaries
  - snarks
  - starks
  - study-guide
related:
  - "[[zkSNARKs]]"
  - "[[Rank-1 Constraint Satisfiability (R1CS)]]"
  - "[[Sum-check Protocol]]"
  - "[[Polynomial Commitments]]"
  - "[[Interactive Oracle Proofs (IOPs)]]"
  - "[[FRI]]"
  - "[[Reed-Solomon Proximity Testing]]"
  - "[[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]"
description: "Compact study guide to the main algebraic objects, proof templates, and formulae used across the current SNARK/STARK branch"
---

# Mathematical Preliminaries for SNARKs and STARKs

## Thesis / purpose

This page is a compact mathematical study guide for the current SNARK/STARK branch of the wiki.

It is not meant to replace the concept pages. Instead, it gives a **minimal common language** for reading the current corpus, especially papers like:
- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
- [[Interactive Oracle Proofs]]
- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
- [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
- [[WARP Linear-Time Accumulation Schemes]]
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
- [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

The shortest durable summary is:

> **Most of the current branch is about encoding computation algebraically, then checking that encoding efficiently using either multilinear/sum-check machinery or oracle/proximity machinery.**

## Main takeaways

- The current branch relies heavily on **finite-field algebra**.
- Two recurring polynomial worlds are:
  - **multilinear extensions** over the Boolean hypercube,
  - **low-degree / Reed–Solomon codewords** over larger evaluation domains.
- Two recurring proof templates are:
  - **sum-check-style reduction** of algebraic sums,
  - **FRI / proximity-style reduction** of low-degree claims.
- A large amount of proof-system engineering is really about choosing the right:
  - arithmetization,
  - commitment layer,
  - and recursion / composition strategy.

## 1. Finite fields as the ambient arithmetic

Most of the objects in this branch live over a finite field $\mathbb{F}$.

The important point is that addition, subtraction, multiplication, and division by nonzero elements all happen **inside** $\mathbb{F}$.

### Tiny example
If we work over $\mathbb{F}_7$, then
$$
3+6 \equiv 2 \pmod 7,
\qquad
5\cdot 5 \equiv 4 \pmod 7.
$$

Why this matters:
- circuit constraints are evaluated over fields,
- polynomials are defined over fields,
- codewords and proximity tests are field-valued,
- verifier challenges are field elements.

## 2. Arithmetizing computation

A core move in SNARK/STARK design is to turn a computational claim into algebra.

### Generic viewpoint
Start with a relation
$$
R(x,w)=1,
$$
where:
- $x$ is the public statement,
- $w$ is the witness.

The proof system does not usually reason about the original program directly. Instead, it reasons about an **algebraic encoding** of the claim.

In the current wiki, the most important encoding is:
- [[Rank-1 Constraint Satisfiability (R1CS)]].

## 3. R1CS

R1CS represents a computation using multiplicative constraints of the form
$$
\langle A_i,z\rangle \cdot \langle B_i,z\rangle = \langle C_i,z\rangle,
$$
where
$$
z=(1,x,w)
$$
contains constants, public inputs, and witness coordinates.

### Why it matters here
- [[Spartan]] is directly built for arbitrary R1CS.
- [[Fractal]] also targets R1CS through holographic proof machinery.
- Later recursion papers often compare themselves to or generalize beyond R1CS-like relations.

### Tiny example
To encode
$$
z = x\cdot y,
$$
one constraint can enforce exactly:
$$
x\cdot y = z.
$$
This is the basic pattern from which large arithmetized computations are built.

For details, see [[Rank-1 Constraint Satisfiability (R1CS)]].

## 4. Multilinear extensions

A function on the Boolean hypercube,
$$
f:\{0,1\}^n \to \mathbb{F},
$$
can be uniquely extended to a multilinear polynomial
$$
\widetilde{f}(X_1,\dots,X_n)=\sum_{b\in\{0,1\}^n} f(b)\prod_{i=1}^n \big(b_iX_i+(1-b_i)(1-X_i)\big).
$$

This is one of the central algebraic objects in the current branch.

### Why it matters here
- [[Spartan]] works heavily with multilinear structure.
- [[SPARK]] is about efficient commitment support for sparse multilinear polynomials.
- [[VEIL]] abstracts many practical systems as multilinear interactive oracle proofs.

### Intuition
Multilinear extensions are useful because they let a proof system:
- reason about Boolean-table data as a polynomial,
- interpolate that data consistently,
- and reduce correctness to evaluation claims at random points.

## 5. Sum-check

Given a low-degree polynomial $g(X_1,\dots,X_n)$ and a claimed sum
$$
S = \sum_{b\in\{0,1\}^n} g(b),
$$
the sum-check protocol reduces this large claim to a sequence of smaller ones.

### First round
The prover sends
$$
g_1(X)=\sum_{x_2,\dots,x_n\in\{0,1\}^{n-1}} g(X,x_2,\dots,x_n),
$$
and the verifier checks
$$
g_1(0)+g_1(1)=S.
$$
Then the verifier samples a random challenge $r_1$ and continues recursively.

### Why it matters here
This is the core algebraic reduction pattern in the multilinear branch, especially for [[Spartan]].

See also:
- [[Sum-check Protocol]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## 6. Polynomial commitments

A polynomial commitment scheme provides an interface like
$$
c \leftarrow \mathsf{Commit}(f),
\qquad
\pi \leftarrow \mathsf{Open}(f,z),
$$
with verification condition
$$
\mathsf{Verify}(c,z,v,\pi)=1 \iff f(z)=v.
$$

### Why it matters here
This is one of the most reused abstractions in the entire branch.

It lets a protocol:
- commit to a polynomial once,
- later prove evaluations succinctly,
- and modularize the connection between algebra and succinct verification.

It is central to:
- [[Spartan]]
- [[WHIR]]
- [[Quasar]]
- [[VEIL]]

## 7. Oracle proofs and IOPs

In an interactive oracle proof, the prover sends large oracle-accessible messages
$$
O_1,O_2,\dots,O_r,
$$
and the verifier checks only a small number of locations.

This changes the proof-system mindset from:
- “read the whole proof”

to:
- “query a few positions of a structured object and rely on algebraic consistency.”

### Why it matters here
This is the main language of the STARK / RS-proximity side of the branch:
- [[Interactive Oracle Proofs]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[FRI]]
- [[WHIR]]
- parts of [[Fractal]]

## 8. Reed–Solomon codes and low-degree testing

For a domain $D \subseteq \mathbb{F}$ and degree bound $d$, the Reed–Solomon code is
$$
RS_{D,d}=\{(f(\alpha))_{\alpha\in D}: \deg f < d\}.
$$

A proximity test asks whether a word $w$ is close to this code:
$$
\operatorname{dist}(w,RS_{D,d})=\min_{c\in RS_{D,d}} \frac{\Delta(w,c)}{|D|}.
$$

### Tiny example
If
$$
f(X)=1+2X
$$
on the domain $D=\{0,1,2\}$, then the codeword is
$$
(1,3,5).
$$
A nearby word such as
$$
(1,3,8)
$$
is not exactly the same codeword, but differs only in one position.

### Why it matters here
This is the central mathematical substrate for:
- [[FRI]]
- [[WHIR]]
- the broader RS / FRI / IOPP branch

See:
- [[Reed-Solomon Proximity Testing]]
- [[FRI vs WHIR]]

## 9. FRI-style reduction

FRI repeatedly reduces a low-degree claim to a smaller one by splitting a polynomial into even and odd parts:
$$
f(X)=f_0(X^2)+Xf_1(X^2),
$$
then folding to
$$
g(Y)=f_0(Y)+\beta f_1(Y)
$$
for random challenge $\beta$.

### Why it matters here
This is the main engine that made RS-proximity-based transparent proof systems practical.

In the current branch:
- [[FRI]] is the canonical foundation,
- [[WHIR]] is the later verifier-optimized constrained-RS refinement,
- [[Fractal]] uses FRI-style verifier infrastructure inside a larger recursive architecture.

## 10. Two family lenses: multilinear vs RS/FRI

One of the main organizing principles of the branch is:

### Multilinear / sum-check lens
- start from the algebraic relation directly,
- represent computation via multilinear structure,
- reduce with sum-check,
- end with evaluation/commitment checks.

Main anchor:
- [[Spartan]]

### RS / FRI / IOPP lens
- start from oracle-accessible structured codewords,
- check low-degree or proximity structure,
- use sparse query access,
- compile to transparent arguments.

Main anchors:
- [[FRI]]
- [[WHIR]]
- [[Interactive Oracle Proofs]]

This comparison is developed in:
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]

## 11. Non-interactivity and Fiat–Shamir

Many systems in this branch start from an interactive protocol and become non-interactive via Fiat–Shamir:
$$
\rho_i = H(x,m_1,\rho_1,\dots,m_i),
$$
where $H$ is modeled as a random oracle.

This is one of the main bridges from:
- interactive proofs,
- sum-check protocols,
- IOPs / IOPPs,

to practical non-interactive proof systems.

See [[Fiat-Shamir Transform]].

## 12. Recursion, accumulation, and folding

After the base proof layer, the next mathematical question is how to **compose proofs recursively**.

The current branch has three main routes:
- [[Fractal]] — preprocessing/holography route to transparent recursion
- [[WARP]] and [[Quasar]] — accumulation-oriented recursion
- [[Symphony]] — folding-oriented recursion

The main comparison page is:
- [[Accumulation vs Folding in Recursive Proof Systems]]

## Suggested reading order from this page

If you want the most useful mathematical path through the current wiki, a good order is:

1. [[Rank-1 Constraint Satisfiability (R1CS)]]
2. [[Sum-check Protocol]]
3. [[Polynomial Commitments]]
4. [[Interactive Oracle Proofs (IOPs)]]
5. [[Reed-Solomon Proximity Testing]]
6. [[FRI]]
7. [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]
8. [[Accumulation vs Folding in Recursive Proof Systems]]

## Provisional conclusion

A durable summary for this page is:

> **The mathematical core of the current SNARK/STARK branch is: arithmetize computation over a finite field, then verify the resulting algebra either through multilinear/sum-check reductions or through Reed–Solomon / proximity-testing reductions, and finally compile or compose those checks into a practical proof system.**

## Related pages

- [[zkSNARKs]]
- [[Rank-1 Constraint Satisfiability (R1CS)]]
- [[Sum-check Protocol]]
- [[Polynomial Commitments]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[FRI]]
- [[Reed-Solomon Proximity Testing]]
- [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]]
- [[Accumulation vs Folding in Recursive Proof Systems]]
