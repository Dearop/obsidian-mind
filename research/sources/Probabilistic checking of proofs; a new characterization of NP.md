---
date: 2026-04-14
type: source
status: processed
source_kind: paper
created: 2026-04-14
updated: 2026-04-15
raw_path: raw/papers/SNARKs & STARKs/Probabilistic_checking_of_proofs_a_new_characterization_of_NP.pdf
authors:
  - Sanjeev Arora
  - Shmuel Safra
year: 1992
tags:
  - pcp
  - approximation-hardness
  - classical-foundations
  - local-checking
related:
  - "[[Probabilistically Checkable Proofs (PCPs)]]"
  - "[[Proof Verification and the Hardness of Approximation Problems]]"
  - "[[PCP vs MIP vs IOP Lineage]]"
  - "[[SNARKs and STARKs Reading Map]]"
  - "[[Checking Computations in Polylogarithmic Time]]"
description: "Arora–Safra PCP-theorem landmark, treated here as a historically important predecessor to the later constant-query PCP theorem paper"
---

# Probabilistic checking of proofs; a new characterization of NP

## Summary

This paper is the Arora–Safra PCP-theorem landmark: a historically central result giving a new probabilistic characterization of NP and helping establish the modern PCP worldview.

In the current wiki, its main role is as a **predecessor anchor** to [[Proof Verification and the Hardness of Approximation Problems]]. The later paper explicitly states that it builds on and improves the Arora–Safra result by reducing the number of queried proof bits to a constant, whereas the Arora–Safra verifiers still read a nonconstant — though very slowly growing — number of bits (as quoted in [[Proof Verification and the Hardness of Approximation Problems]] and consistent with OCR-recoverable text from the local PDF).

So this paper is best understood here as:
- a major PCP-theorem milestone,
- a key step in the hardness-of-approximation story,
- and an important bridge between earlier local-checking proof ideas and the later constant-query PCP formulation that became canonical.

## Key Claims

- The paper gives a new probabilistic characterization of NP (OCR-recoverable front-matter text, pp. 3–4).
- It proves the theorem statement
  $$
  NP = PCP(O(\log n), O(\log n))
  $$
  in the OCR-recoverable local extract (Theorem 1, OCR of p. 4).
- It is historically upstream of [[Proof Verification and the Hardness of Approximation Problems]], which later improves the query complexity to a constant.
- It is part of the proof-complexity route by which local proof checking becomes central to approximation hardness.

## Formal Definitions and Results

> [!important] Note on source quality
> The locally extracted PDF text for this file is heavily obscured by IEEE licensing overlays. This page therefore relies on a combination of: (1) PDF metadata, (2) OCR-recoverable fragments from rendered page images, and (3) cross-reference evidence from later papers in the corpus. Statements below are limited to claims that can be supported by that evidence.

The strongest theorem-level statement recoverable from the local OCR pass is the explicit main-theorem line:
$$
NP = PCP(O(\log n), O(\log n)).
$$
This appears in the OCR output for the page containing “A New Characterization of NP” and “Theorem 1 (Main)” (local OCR of the rendered PDF, corresponding to the early theorem page).

The same OCR-recoverable section also states that the paper is answering the open characterization question left by earlier PCP work and positions the result as a sharp characterization of NP in terms of verifier randomness and query access.

Beyond this, later ingested corpus evidence gives a reliable historical comparison point: [[Proof Verification and the Hardness of Approximation Problems]] states that Arora–Safra achieved logarithmic randomness with a **nonconstant** number of queried proof bits, and that the later work improved this to a constant (see that source note's citations to pp. 502 and 506 of the 1998 paper).

Accordingly, the safest current formal takeaway is:
- Arora–Safra proves a PCP characterization of NP with logarithmic randomness and logarithmic query complexity;
- this became a major intermediate milestone before the later constant-query PCP theorem formulation.

## Methods and Proof Techniques

### 1. Recursive proof checking

The OCR-recoverable portions of the paper explicitly mention **recursive proof checking** and derive a recurrence for verifier query complexity (local OCR of middle theorem pages). This aligns with how later papers describe the Arora–Safra framework.

### 2. Algebraic view of 3SAT

The OCR-recoverable text includes a lemma labeled **“Algebraic View of 3SAT”**, describing a polynomial encoding of satisfiability constraints over a low-degree extension. This strongly supports reading the paper as a key step in the algebraization route from NP witnesses to locally checkable proof objects.

### 3. Sum-check and low-degree testing ingredients

The OCR-recoverable discussion around verifier runtime and low-degree extensions explicitly references sum-check and small-degree testing ideas. Even though the current extract quality is poor, this is consistent with the known historical role of the paper and with later PCP literature.

### 4. Local proof access as the core design target

The paper's method is clearly aimed at reducing verifier randomness and proof-query complexity while preserving correctness. This is the design axis that later became the standard PCP theorem viewpoint.

## Complexity and Performance

> Prover time, verifier time, proof size, communication complexity, assumptions — whatever applies.

The strongest parameter statement recoverable from the local source is the main theorem:
$$
NP = PCP(O(\log n), O(\log n)).
$$
Thus the verifier uses:
- **randomness:**
  $$
  O(\log n),
  $$
- **query complexity:**
  $$
  O(\log n).
  $$

The OCR-recovered middle pages also indicate a recurrence whose conclusion is
$$
C(n) = O(\log^2 n)
$$
for an intermediate verifier-query parameter inside the recursive proof-checking analysis. Because the extract quality is imperfect, this note treats that recurrence evidence as suggestive support for the paper's internal technique rather than as the headline external theorem.

Historically, the right high-level performance interpretation is:
- stronger than earlier polylog/polylog-style PCP formulations,
- weaker than the later constant-query PCP theorem,
- but sufficient to establish PCP-style local checking as a central complexity-theoretic phenomenon.

## Why It Matters

This paper matters because it fills an important historical gap in the PCP branch.

Without it, the graph jumps too quickly from MIP/local-checking intuition to the later constant-query PCP theorem. With it, the wiki can represent the more realistic progression:
- early local-checking and multi-prover ideas,
- Arora–Safra PCP theorem milestone,
- later constant-query PCP theorem refinements,
- then oracle-based models such as IOPs.

It is also helpful because the current raw collection explicitly contains this paper, making it worth cataloging even in partially recovered form.

## Connections to the Wiki

This paper should strengthen:
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Proof Verification and the Hardness of Approximation Problems]]
- [[PCP vs MIP vs IOP Lineage]]
- [[SNARKs and STARKs Reading Map]]

It is especially useful as the missing historical intermediate node between:
- [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]
- and the later constant-query PCP theorem anchor.

## Open Questions / Limitations

- The local PDF remains badly degraded by licensing overlays; even after OCR, only fragments are recoverable with confidence.
- The theorem line
  $$
  NP = PCP(O(\log n), O(\log n))
  $$
  is now locally source-backed, but many deeper construction details still need a cleaner scan or alternate copy.
- If a better source copy becomes available, this page should be upgraded from partial-recovery mode to normal theorem-detail mode.

## Suggested Next Reading

- [[Proof Verification and the Hardness of Approximation Problems]]
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[PCP vs MIP vs IOP Lineage]]
- [[Checking Computations in Polylogarithmic Time]]

## Related
- [[Probabilistically Checkable Proofs (PCPs)]]
- [[Proof Verification and the Hardness of Approximation Problems]]
- [[PCP vs MIP vs IOP Lineage]]
- [[SNARKs and STARKs Reading Map]]
