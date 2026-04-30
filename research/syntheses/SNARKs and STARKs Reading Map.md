---
date: 2026-04-10
type: synthesis
status: stable
created: 2026-04-10
updated: 2026-04-10
tags:
  - snarks
  - starks
  - reading-map
  - proof-systems
related:
  - "[[Research Agenda]]"
  - "[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]"
  - "[[zkSNARKs]]"
  - "[[Transparent zkSNARKs]]"
  - "[[Sum-check Protocol]]"
  - "[[Polynomial Commitments]]"
description: "Topic clusters, reading paths, and ingest strategy for the SNARK/STARK paper collection"
---

# SNARKs and STARKs Reading Map

## Thesis / purpose

This page maps the current `raw/papers/SNARKs & STARKs/` collection into a few coherent study threads rather than treating it as one undifferentiated pile.

The collection is **not too large for the wiki workflow**. It is, however, too large to deeply ingest in a single pass without losing structure. The right approach is:
- map first,
- then ingest in themed waves,
- and let concept/entity/synthesis pages grow incrementally.

This map is based on a **title/metadata/first-page scan**, not a full read of every paper yet.

## Collection scope

The collection contains roughly **20 papers**, spanning classical proof-complexity foundations through modern recursive/folding systems, with a clear topical center around SNARKs, STARKs, PCP/IOP machinery, and accumulation.

This is a manageable size for a focused reading program. The set works best when approached in themed waves (1 anchor paper at a time, or 2-3 from the same cluster) rather than as a single pass. The clusters and reading paths below are designed for that kind of incremental study.

## What is in the collection?

Broadly, the collection appears to cover four layers:

1. **Classical proof-complexity / interactive-proof foundations**
2. **PCP / IOP / Reed–Solomon / STARK substrate**
3. **Transparent SNARK and succinct-proof system design**
4. **Accumulation / folding / recursion / IVC direction**

That is a healthy shape. It means the folder is not random; it already forms a curriculum.

## Cluster 1 — Classical algebraic and PCP foundations

These papers explain where the modern machinery comes from.

### Core papers
- `322217.322225.pdf` — **Fast Probabilistic Algorithms for Verification of Polynomial Identities**
  - Early randomized algebraic verification.
  - Good for the "why random evaluation works" background.
- `146585.146605.pdf` — **Algebraic Methods for Interactive Proof Systems**
  - Key historical anchor for algebraic IP techniques and the sum-check worldview.
- `103418.103428.pdf` — **Checking Computations in Polylogarithmic Time**
  - Early delegation / proof-checking perspective.
- `BF01200056.pdf` — **Non-deterministic Exponential Time Has Two-Prover Interactive Protocols**
  - Multi-prover lineage and complexity backdrop.
- `278298.278306.pdf` — **Proof Verification and the Hardness of Approximation Problems**
  - PCP-era landmark and complexity framing.
- `Probabilistic_checking_of_proofs_a_new_characterization_of_NP.pdf` — **Probabilistic checking of proofs; a new characterization of NP**
  - Arora–Safra PCP theorem anchor.
- `2699436.pdf` — **Delegating Computation: Interactive Proofs for Muggles**
  - Connects foundational theory to verifiable computation more directly.

### What this cluster teaches
- why low-degree / algebraic checks matter,
- where sum-check-style reasoning comes from,
- why probabilistic proof verification became possible,
- and how modern succinct proof systems inherit old IP/PCP ideas.

### Notes
This cluster is intellectually important, but it is easy to get buried in it. For many practical reading goals, it should be sampled strategically rather than exhausted first.

## Cluster 2 — PCP / IOP / Reed–Solomon / STARK substrate

This is the main bridge from classical proof complexity to modern transparent proof systems.

### Core papers
- `2016-116.pdf` — **Interactive Oracle Proofs**
  - Foundational IOP model paper.
- `2016-324.pdf` — **Interactive Oracle Proofs with Constant Rate and Query Complexity**
  - Refines the IOP design space.
- [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
  - FRI anchor; central for understanding STARK-family ideas.
- `2019-1230.pdf` — **Linear-Size Constant-Query IOPs for Delegating Computation**
  - Important efficiency direction for computation delegation.
- `2021-915.pdf` — **A PCP Theorem for Interactive Proofs and Applications**
  - Higher-level structural understanding of IOP power.
- `2488608.2488681.pdf` — **On the Concrete Efficiency of Probabilistically-Checkable Proofs**
  - Useful reality check on concrete overheads.
- `WHIR.pdf` — **WHIR: Reed–Solomon Proximity Testing with Super-Fast Verification**
  - Modern verifier-speed advance in the Reed–Solomon / IOPP direction.

### What this cluster teaches
- how PCP-style verification becomes practical enough to matter for cryptographic proof systems,
- why Reed–Solomon testing matters so much in STARK-like systems,
- how modern transparent arguments often depend more on [[Interactive Oracle Proofs of Proximity (IOPPs)]] / [[FRI]] machinery than on older pairing-based SNARK intuition,
- and how the RS substrate evolves from generic oracle-proof abstractions into a dedicated transparent-proof compiler layer (see [[RS IOPP and STARK Lineage]]).

### Notes
If your goal is to understand **STARKs seriously**, this cluster is probably more important than many of the classical PCP papers.

## Cluster 3 — Transparent SNARKs and succinct-proof-system design

This is where high-level cryptographic system design becomes concrete.

### Core papers
- `Spartan.pdf` — **Spartan: Efficient and general-purpose zkSNARKs without trusted setup**
  - Current first ingested anchor in the wiki.
  - Emphasizes arbitrary R1CS, sub-linear verification, computation commitments, and SPARK.
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
  - Important transparent recursive-proof direction.
- [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]
  - Zero-knowledge compiler lens for hash-based multilinear systems.

### What this cluster teaches
- the trusted-setup vs transparency trade-off,
- how proof systems are assembled from lower-level subcomponents,
- and how modern systems differ in arithmetization, commitment choices, recursion strategy, and zero-knowledge add-ons.

### Notes
This is probably the best cluster for building an actual systems-level mental model.

## Cluster 4 — Accumulation, folding, recursion, and IVC

This is the more recent scaling / composition frontier.

### Core papers
- [[WARP Linear-Time Accumulation Schemes]]
  - Accumulation as a primitive for proof-carrying data and recursive composition.
- `Quasar.pdf` — **Quasar: Sublinear Accumulation Schemes for Multiple Instances**
  - Multi-instance accumulation direction.
- `Symphony.pdf` — **Symphony: Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding**
  - Folding-focused, modern, plausibly post-quantum direction.

### What this cluster teaches
- how modern recursive systems avoid naive recursive verification,
- why accumulation/folding now sits near the center of scalable proof design,
- and how the field is shifting from just "one-shot succinct proofs" toward composable proof pipelines.

### Notes
This cluster makes the most sense after you have at least one solid anchor in transparent SNARKs and one solid anchor in IOP/FRI-style systems.

## One suspicious / likely non-core item

- `3-540-44693-1.pdf`
  - This appears to be a large conference proceedings volume rather than a single SNARK/STARK paper.
  - It may still contain something relevant, but as currently identified it looks more like a container artifact than a paper to ingest directly.
  - Unless you know the exact target paper inside it, this should probably be treated as **low priority / maybe ignore**.

## Suggested reading orders

## Path A — Minimal modern systems path

If you want to understand the field quickly without doing a full theory deep dive:

1. [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
2. [[Interactive Oracle Proofs]]
3. [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
4. [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
5. [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
6. [[WARP Linear-Time Accumulation Schemes]]
7. `Symphony.pdf`
8. [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

This is the best path if your goal is **modern proof-system architecture**.

## Path B — Theory-to-systems path

If you want the conceptual lineage:

1. `322217.322225.pdf` — polynomial identity testing background
2. `146585.146605.pdf` — algebraic interactive proofs / sum-check worldview
3. `Probabilistic_checking_of_proofs_a_new_characterization_of_NP.pdf`
4. `2016-116.pdf` — IOPs
5. `TR17-134.pdf` — FRI
6. `Spartan.pdf`
7. [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
8. `WHIR.pdf`
9. [[WARP Linear-Time Accumulation Schemes]]
10. `Symphony.pdf`

This is the best path if your goal is **deep explanatory understanding**.

## Path C — Recursion / accumulation / folding path

If your main interest is where the field is going now:

1. `Spartan.pdf`
2. `WHIR.pdf`
3. [[WARP Linear-Time Accumulation Schemes]]
4. [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
5. [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]
6. [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]
7. [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

This is the best path if your goal is **recursive systems, IVC, and composition**.

## Suggested ingest order for this wiki

For the wiki specifically, a good next ingest sequence is:

1. [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]] — already done
2. [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
3. [[WARP Linear-Time Accumulation Schemes]]
4. [[Interactive Oracle Proofs]]
5. [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
6. [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
7. [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
8. [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]
9. [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]]

Then optionally backfill the classical theory papers as needed.

Why this order:
- it establishes one SNARK anchor,
- then one modern RS/IOPP anchor,
- then one accumulation anchor,
- then fills in the conceptual substrate.

## Practical recommendation

Do **not** try to ingest all of these immediately.

Instead:
- keep this reading map as the canonical overview,
- ingest one anchor at a time,
- and let concept pages become more precise as repeated themes appear.

Likely durable canonical pages to keep strengthening:
- [[Polynomial Commitments]]
- [[Sum-check Protocol]]
- [[Transparent zkSNARKs]]
- [[Interactive Oracle Proofs (IOPs)]]
- [[Reed-Solomon Proximity Testing]]
- [[Accumulation vs Folding in Recursive Proof Systems]]

## Tensions / contradictions to track later

As more papers are ingested, the wiki should explicitly compare:
- trusted setup vs transparency,
- sum-check/multilinear style systems vs Reed–Solomon/FRI style systems,
- proof size vs verifier time vs prover time,
- recursion via SNARK verification vs accumulation/folding,
- standard-model vs random-oracle security framing,
- and concrete practicality vs asymptotic elegance.

## Next steps

- Create a synthesis page comparing **SNARK-style multilinear systems** against **FRI/IOPP-style systems**.
- Create a synthesis page comparing **transparent recursive architectures** against **direct transparent zk system design**.
- Continue backfilling classical theory papers only where they materially improve the current system-level map.
