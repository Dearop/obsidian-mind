---
date: 2026-04-10
type: log
created: 2026-04-10
updated: 2026-04-15
tags:
  - wiki
  - changelog
description: "Log — research wiki page"
---

# Log

## [2026-04-10] setup | Initialized research wiki scaffold
- Replaced the empty/default `AGENTS.md` with an operating schema for an LLM-maintained research wiki.
- Confirmed the vault already had top-level `raw/` and `wiki/` directories plus Obsidian configuration.
- Observed that the previous wiki state was mostly uninitialized: empty `AGENTS.md`, minimal `Index.md`, empty `Log.md`, and no source notes.
- Added raw source subfolders:
  - `raw/inbox/`
  - `raw/papers/`
  - `raw/articles/`
  - `raw/books/`
  - `raw/assets/`
- Added starter wiki pages:
  - [[Overview]]
  - [[Research Agenda]]
  - [[Intake Questions]]
- Rewrote [[Index]] to serve as a compact navigation map.
- Established conventions for ingest, query, lint, indexing, and logging in `AGENTS.md` (repo root).
- Remaining work:
  - clarify the user's actual interests and study priorities
  - add representative raw sources
  - ingest the first real source
  - evolve concept/entity/synthesis pages from real material

## [2026-04-10] ingest | Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup
- Ingested `raw/papers/SNARKs & STARKs/Spartan.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]].
- Created related entity pages:
  - [[Spartan]]
  - [[Srinath Setty]]
- Created related concept pages:
  - [[zkSNARKs]]
  - [[Transparent zkSNARKs]]
  - [[Rank-1 Constraint Satisfiability (R1CS)]]
  - [[Polynomial Commitments]]
  - [[Computation Commitments]]
  - [[SPARK]]
  - [[Sum-check Protocol]]
- Updated [[Index]] to reflect the first processed source and the emerging proof-systems topic cluster.
- Updated [[Research Agenda]] to reflect an initial focus on transparent SNARK/STARK-adjacent papers.
- Remaining work:
  - ingest the next papers in the `SNARKs & STARKs` folder
  - refine comparative pages as more systems are added
  - decide whether to add dedicated pages for [[Trusted Setup]] and [[Fiat-Shamir Transform]] next

## [2026-04-10] query | Mapped SNARKs & STARKs paper collection
- Scanned the `raw/papers/SNARKs & STARKs/` folder to identify the paper set.
- Extracted titles and first-page metadata from the PDFs where possible using PDFKit.
- Created synthesis page: [[SNARKs and STARKs Reading Map]].
- Organized the collection into four main clusters:
  - classical algebraic / PCP foundations
  - PCP / IOP / Reed–Solomon / STARK substrate
  - transparent SNARK and succinct-proof-system design
  - accumulation / folding / recursion / IVC
- Added suggested reading paths for:
  - modern systems understanding
  - theory-to-systems understanding
  - recursion / accumulation focus
- Assessed collection size as manageable for the persistent-wiki workflow, provided ingest happens incrementally rather than all at once.
- Flagged `3-540-44693-1.pdf` as likely a proceedings/container artifact rather than a single target paper.
- Remaining work:
  - ingest the next anchor paper (`WHIR.pdf` or `Warp.pdf`)
  - create comparison pages once a few more anchors are processed
  - decide whether to split future syntheses into SNARK-focused vs STARK-focused maps

## [2026-04-10] ingest | WHIR Reed-Solomon Proximity Testing with Super-Fast Verification
- Ingested `raw/papers/SNARKs & STARKs/WHIR.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]].
- Created related entity pages:
  - [[WHIR]]
  - [[Gal Arnon]]
  - [[Alessandro Chiesa]]
  - [[Giacomo Fenzi]]
  - [[Eylon Yogev]]
- Created related concept pages:
  - [[Interactive Oracle Proofs (IOPs)]]
  - [[Reed-Solomon Proximity Testing]]
  - [[Constrained Reed-Solomon Codes]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to reflect WHIR as the next processed anchor on the STARK/IOPP side of the corpus.
- Strengthened the wiki's emerging contrast between:
  - Spartan-style multilinear/sum-check transparent SNARK design
  - WHIR-style Reed–Solomon / IOPP / hash-based SNARG compilation
- Remaining work:
  - ingest `Warp.pdf` next for the accumulation / recursion branch
  - ingest `2016-116.pdf` next for the canonical IOP foundation page
  - later create a synthesis comparing multilinear SNARK systems against RS/FRI/IOPP systems

## [2026-04-10] ingest | WARP Linear-Time Accumulation Schemes
- Ingested `raw/papers/SNARKs & STARKs/Warp.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[WARP Linear-Time Accumulation Schemes]].
- Created related entity pages:
  - [[WARP]]
  - [[Benedikt Bünz]]
  - [[William Wang]]
- Reused and strengthened recurring entity pages:
  - [[Alessandro Chiesa]]
  - [[Giacomo Fenzi]]
- Created related concept pages:
  - [[Accumulation Schemes]]
  - [[Proof-Carrying Data (PCD)]]
  - [[Incrementally Verifiable Computation (IVC)]]
  - [[Interactive Oracle Reductions (IORs)]]
  - [[Polynomial Equation Satisfiability (PESAT)]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to reflect WARP as the recursion / accumulation anchor in the corpus.
- Strengthened the wiki's emerging three-way comparison between:
  - Spartan-style multilinear / transparent SNARK systems
  - WHIR-style Reed–Solomon / IOPP / hash-based verifier-centric systems
  - WARP-style accumulation / recursion / composition systems
- Remaining work:
  - ingest `2016-116.pdf` next to solidify the canonical IOP foundation page
  - later create a synthesis comparing accumulation/folding systems against direct recursive-SNARK approaches
  - later create a synthesis comparing multilinear SNARK systems against RS/FRI/IOPP systems

## [2026-04-10] ingest | Interactive Oracle Proofs
- Ingested `raw/papers/SNARKs & STARKs/2016-116.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[Interactive Oracle Proofs]].
- Created related entity pages:
  - [[Eli Ben-Sasson]]
  - [[Nicholas Spooner]]
- Reused and strengthened recurring entity page:
  - [[Alessandro Chiesa]]
- Created related concept pages:
  - [[Fiat-Shamir Transform]]
  - [[State Restoration Attacks]]
- Upgraded [[Interactive Oracle Proofs (IOPs)]] from a WHIR-driven stub into a canonical foundational concept page backed by the original IOP paper.
- Created synthesis page: [[Interactive Oracle Proofs (IOPs) vs Interactive Oracle Reductions (IORs)]].
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to place the original IOP paper into the core reading sequence.
- Remaining work:
  - ingest `TR17-134.pdf` next to ground the FRI / RS-proximity branch
  - later create a synthesis comparing multilinear SNARK systems against RS/FRI/IOPP systems
  - later create a synthesis comparing IOP/IOPP systems against IOR/accumulation systems more fully

## [2026-04-10] ingest | Fast Reed-Solomon Interactive Oracle Proofs of Proximity
- Ingested `raw/papers/SNARKs & STARKs/TR17-134.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]].
- Created related entity pages:
  - [[Iddo Bentov]]
  - [[Ynon Horesh]]
  - [[Michael Riabzev]]
- Reused and strengthened recurring entity page:
  - [[Eli Ben-Sasson]]
- Created related concept page:
  - [[FRI]]
- Upgraded [[Reed-Solomon Proximity Testing]] from a WHIR-centered stub into a broader comparison-oriented concept page anchored by both FRI and WHIR.
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to place FRI as the canonical historical anchor for the RS/IOPP/STARK branch.
- Strengthened the wiki's historical bridge from:
  - [[Interactive Oracle Proofs]] as the model-level foundation
  - [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]] as the key RS/IOPP engine
  - [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]] as a later verifier-optimized refinement in the same ecosystem
- Remaining work:
  - create a synthesis comparing [[FRI]] and [[WHIR]] directly
  - later create a synthesis comparing multilinear SNARK systems against RS/FRI/IOPP systems
  - later ingest additional STARK-substrate papers as needed

## [2026-04-10] query | Created FRI vs WHIR synthesis
- Reviewed the existing source and concept pages for [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]], [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]], [[FRI]], and [[Reed-Solomon Proximity Testing]].
- Created synthesis page: [[FRI vs WHIR]].
- Framed the comparison around the most useful durable distinction:
  - [[FRI]] as the canonical historical Reed–Solomon / IOPP foundation
  - [[WHIR]] as a later verifier-optimized constrained-Reed–Solomon refinement and replacement candidate
- Added practical reading guidance about when to treat FRI as the baseline and when to read WHIR as the modern systems optimization layer.
- Updated [[Index]] so the comparison is discoverable from the top-level catalog.
- Remaining work:
  - later create a broader synthesis comparing RS/FRI/IOPP systems against multilinear / sum-check systems
  - later compare FRI and STIR directly once the relevant source is ingested
  - continue ingesting additional STARK-substrate papers as needed

## [2026-04-10] ingest | Quasar Sublinear Accumulation Schemes for Multiple Instances
- Ingested `raw/papers/SNARKs & STARKs/Quasar.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[Quasar Sublinear Accumulation Schemes for Multiple Instances]].
- Created related entity pages:
  - [[Quasar]]
  - [[Tianyu Zheng]]
  - [[Shang Gao]]
  - [[Yu Guo]]
  - [[Bin Xiao]]
- Linked Quasar into the existing recursion / accumulation graph around:
  - [[Accumulation Schemes]]
  - [[Incrementally Verifiable Computation (IVC)]]
  - [[Proof-Carrying Data (PCD)]]
  - [[Polynomial Commitments]]
  - [[WARP]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to reflect Quasar as a processed recursion / accumulation source.
- Strengthened the contrast inside the recursion branch between:
  - [[WARP]] as a linear-time hash-based accumulation anchor
  - [[Quasar]] as a multi-instance accumulation / IVC anchor targeting sublinear verifier dependence on accumulated instances
- Remaining work:
  - create a dedicated synthesis comparing [[Quasar]] and [[WARP]]
  - continue ingesting recursion / folding papers such as `Symphony.pdf`
  - later compare accumulation-based recursion against folding-based recursion more explicitly

## [2026-04-10] query | Created Quasar vs WARP synthesis
- Reviewed the existing source and concept pages for [[Quasar Sublinear Accumulation Schemes for Multiple Instances]], [[WARP Linear-Time Accumulation Schemes]], [[Accumulation Schemes]], and [[Incrementally Verifiable Computation (IVC)]].
- Created synthesis page: [[Quasar vs WARP]].
- Framed the comparison around the most useful durable distinction:
  - [[WARP]] as the broad, foundational hash-based accumulation framework optimizing linear-time proving
  - [[Quasar]] as the more targeted multi-instance IVC construction optimizing verifier-side dependence on the number of accumulated instances
- Added practical reading guidance about when to treat WARP as the accumulation foundation and when to treat Quasar as the recursion-overhead optimization paper.
- Updated [[Index]] so the comparison is discoverable from the top-level catalog.
- Remaining work:
  - ingest `Symphony.pdf` to add a folding-oriented contrast point in the recursion branch
  - later create a broader synthesis comparing accumulation-based recursion against folding-based recursion
  - continue refining the recursion branch as more papers are ingested

## [2026-04-10] ingest | Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding
- Ingested `raw/papers/SNARKs & STARKs/Symphony.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]].
- Created related entity pages:
  - [[Symphony]]
  - [[Binyi Chen]]
- Created related concept pages:
  - [[Folding Schemes]]
  - [[High-Arity Folding]]
  - [[Commit-and-Prove SNARKs]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to reflect Symphony as the main folding-oriented recursion anchor in the corpus.
- Strengthened the recursion branch into a clearer three-way comparison between:
  - [[WARP]] as a foundational hash-based accumulation framework
  - [[Quasar]] as a multi-instance IVC / sublinear-verifier accumulation design
  - [[Symphony]] as a high-arity folding-based SNARK avoiding Fiat–Shamir logic inside recursive statements
- Remaining work:
  - create a broader synthesis comparing accumulation-based recursion against folding-based recursion
  - possibly create a focused synthesis comparing [[Symphony]] and [[Quasar]]
  - continue ingesting remaining recursion / transparent-system papers as needed

## [2026-04-10] query | Created Accumulation vs Folding in Recursive Proof Systems synthesis
- Reviewed the existing recursion-branch source and concept pages for [[WARP Linear-Time Accumulation Schemes]], [[Quasar Sublinear Accumulation Schemes for Multiple Instances]], [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]], [[Accumulation Schemes]], [[Folding Schemes]], and [[Incrementally Verifiable Computation (IVC)]].
- Created synthesis page: [[Accumulation vs Folding in Recursive Proof Systems]].
- Organized the recursion branch around a durable three-way map:
  - [[WARP]] as foundational accumulation
  - [[Quasar]] as recursion-overhead-optimized accumulation / multi-instance IVC
  - [[Symphony]] as high-arity folding-based recursion
- Framed the key distinction around **which bottleneck is being optimized**:
  - accumulation prover cost
  - accumulation verifier cost inside recursion
  - folding depth / Fiat–Shamir circuit overhead
- Updated [[Index]] so the new synthesis is discoverable from the top-level catalog.
- Remaining work:
  - possibly create a focused synthesis comparing [[Symphony]] and [[Quasar]]
  - continue ingesting remaining recursion / transparent-system papers as needed
  - revisit this synthesis after more folding-oriented papers are ingested

## [2026-04-10] ingest | Fractal Post-Quantum and Transparent Recursive Proofs from Holography
- Ingested `raw/papers/SNARKs & STARKs/2019-1076.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]].
- Created related entity pages:
  - [[Fractal]]
  - [[Dev Ojha]]
- Created related concept pages:
  - [[Holographic Proofs]]
  - [[Preprocessing SNARKs]]
- Reused and strengthened recurring entity/concept pages:
  - [[Alessandro Chiesa]]
  - [[Nicholas Spooner]]
  - [[Proof-Carrying Data (PCD)]]
  - [[Incrementally Verifiable Computation (IVC)]]
  - [[Interactive Oracle Proofs (IOPs)]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to place Fractal as the bridge between the IOP/holography branch and the recursion branch.
- Strengthened the wiki's transparent-recursion storyline around:
  - holographic IOPs
  - preprocessing SNARKs
  - transparent/post-quantum recursive composition
- Remaining work:
  - compare [[Fractal]] directly against later accumulation- and folding-based recursion systems
  - ingest remaining transparent-system papers such as `veil.pdf`
  - continue refining bridge pages between the IOP, STARK-substrate, and recursion branches

## [2026-04-10] ingest | VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems
- Ingested `raw/papers/SNARKs & STARKs/veil.pdf`.
- Extracted metadata and readable text from the PDF using PDFKit.
- Created source page: [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]].
- Created related entity pages:
  - [[VEIL]]
  - [[Rahul Dalal]]
  - [[Tamir Hemo]]
  - [[Eugene Rabinovich]]
  - [[Ron D. Rothblum]]
- Created related concept page:
  - [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- Strengthened recurring concept pages:
  - [[Transparent zkSNARKs]]
  - [[Polynomial Commitments]]
- Updated [[Index]], [[Research Agenda]], and [[SNARKs and STARKs Reading Map]] to reflect VEIL as a processed source.
- Strengthened the wiki's understanding of the zero-knowledge compiler layer for hash-based multilinear systems, especially as a contrast to built-in zk system design and recursion-based wrapping.
- Remaining work:
  - create a synthesis comparing VEIL with native zk-ification approaches and recursive wrapping approaches
  - compare VEIL more directly against [[Spartan]] and [[Fractal]] as different routes to transparent zero knowledge
  - continue refining the transparent / multilinear / recursion bridge pages

## [2026-04-10] query | Created VEIL vs Spartan vs Fractal synthesis
- Reviewed the existing source and concept pages for [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]], [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]], [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]], and [[Transparent zkSNARKs]].
- Created synthesis page: [[VEIL vs Spartan vs Fractal]].
- Framed the comparison around the most useful durable distinction:
  - [[Spartan]] as native transparent zkSNARK design
  - [[Fractal]] as transparent recursive architecture from holography and preprocessing
  - [[VEIL]] as lightweight zk compilation for multilinear hash-based systems
- Added practical reading guidance about when to treat Spartan as the base transparent-zk anchor, Fractal as the recursion bridge, and VEIL as the low-overhead zk retrofit paper.
- Updated [[Index]] so the new comparison is discoverable from the top-level catalog.
- Remaining work:
  - later create a broader synthesis spanning direct zkSNARK design, STARK/IOPP pipelines, preprocessing recursion, and zk wrappers
  - continue refining the transparent / multilinear / recursion bridge pages as more sources are ingested
  - revisit this synthesis after more multilinear and zk-compiler papers are added

## [2026-04-11] lint | SNARK/STARK wiki health pass
- Audited the current SNARK/STARK branch for missing links, stale scaffold text, weak navigation, and missing hub pages.
- Found two concrete structural issues:
  - links to the old vault's `AGENTS.md` did not resolve inside the wiki graph
  - repeated references to `[[Trusted Setup]]` pointed to a missing concept page
- Created missing concept page: [[Trusted Setup]].
- Updated [[Overview]] to reflect that the wiki has moved beyond scaffold mode into a real SNARK/STARK study branch.
- Updated [[Research Agenda]] to replace placeholder study-thread text with actual active themes and recurring concepts drawn from the ingested corpus.
- Updated [[SNARKs and STARKs Reading Map]] to replace stale “future page” placeholders with links to now-existing canonical pages and more realistic next-step syntheses.
- Updated [[Index]] so [[Trusted Setup]] is discoverable from the top-level catalog.
- Lint findings summary:
  - no true orphan markdown pages were found in the current wiki graph
  - the biggest remaining weakness is not broken links but uneven page maturity, especially among entity stubs and some broad concept hubs
  - the most valuable remaining missing synthesis is a page comparing **multilinear / sum-check systems** against **RS / FRI / IOPP systems**
- Remaining work:
  - strengthen a few broad hub pages such as [[zkSNARKs]], [[Transparent zkSNARKs]], and [[Reed-Solomon Proximity Testing]] as the next canonical comparison layer
  - optionally prune or consolidate very small entity stubs if the vault becomes cluttered
  - continue periodic lint passes as more papers are ingested

## [2026-04-11] query | Created multilinear vs RS/FRI/IOPP synthesis
- Reviewed the existing multilinear/sum-check and RS/FRI/IOPP anchor pages, especially [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]], [[Sum-check Protocol]], [[Interactive Oracle Proofs (IOPs)]], [[FRI]], [[Reed-Solomon Proximity Testing]], and [[FRI vs WHIR]].
- Created synthesis page: [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]].
- Framed the comparison around the most useful durable distinction:
  - multilinear / sum-check systems as **relation-centric**
  - RS / FRI / IOPP systems as **code-centric / proximity-centric**
- Positioned [[Spartan]] as the main multilinear anchor, [[FRI]] as the main RS-proximity anchor, [[WHIR]] as the modern constrained-RS refinement, and [[Fractal]] / [[VEIL]] as bridge papers that mix ideas across the boundary.
- Updated [[Index]] so the new comparison is discoverable from the top-level catalog.
- Remaining work:
  - strengthen [[zkSNARKs]] and [[Reed-Solomon Proximity Testing]] so they point to this comparison more explicitly
  - later create a broader synthesis spanning transparent, trusted-setup, and pairing-based system families
  - revisit this page after more STARK-substrate and multilinear-system papers are ingested

## [2026-04-11] refactor | Hub strengthening and mathematical-background pass on concept pages
- Audited the concept layer and identified the broadest navigation hubs to strengthen first:
  - [[zkSNARKs]]
  - [[Transparent zkSNARKs]]
  - [[Polynomial Commitments]]
  - [[Interactive Oracle Proofs (IOPs)]]
  - [[Reed-Solomon Proximity Testing]]
  - [[Accumulation Schemes]]
  - [[Folding Schemes]]
- Added a new **Mathematical background / formulae** section to every current page in `wiki/concepts/`.
- Added explicit formulae / formal schemata across the concept layer, including examples such as:
  - R1CS constraint equations
  - polynomial-commitment commit/open/verify interfaces
  - sum-check recurrence equations
  - Reed–Solomon code definitions and proximity distance
  - Fiat–Shamir challenge derivation
  - accumulation / folding / IVC / PCD update schemata
- Strengthened hub pages by adding explicit “Current map in this wiki” sections where most useful, so major concept pages now point more clearly into the comparison syntheses.
- In particular, strengthened these hubs to route readers into the new synthesis pages:
  - [[zkSNARKs]]
  - [[Transparent zkSNARKs]]
  - [[Polynomial Commitments]]
  - [[Interactive Oracle Proofs (IOPs)]]
  - [[Reed-Solomon Proximity Testing]]
  - [[Accumulation Schemes]]
  - [[Folding Schemes]]
- Result of the pass:
  - all 25 concept pages now include mathematical background
  - the top-level hub layer is materially better connected to the current family-comparison syntheses
- Remaining work:
  - continue enriching weaker concept pages with more detailed examples and derivations as the corpus grows
  - consider a later pass splitting especially broad pages such as [[Polynomial Commitments]] if the topic cluster becomes much denser
  - optionally add worked examples to a few core pages like [[Sum-check Protocol]], [[FRI]], and [[Rank-1 Constraint Satisfiability (R1CS)]]

## [2026-04-11] refactor | Added worked examples to core mathematical concept pages
- Added worked-example sections to several of the highest-value mathematical concept pages:
  - [[Sum-check Protocol]]
  - [[Rank-1 Constraint Satisfiability (R1CS)]]
  - [[FRI]]
  - [[Polynomial Commitments]]
  - [[Reed-Solomon Proximity Testing]]
- The examples were chosen to be small, concrete, and readable enough for study use:
  - explicit Boolean-hypercube summation for sum-check
  - a single multiplication constraint for R1CS
  - a simple even/odd polynomial decomposition for FRI folding
  - a one-point opening example for polynomial commitments
  - a tiny Reed–Solomon codeword/proximity example
- Result of the pass:
  - the main mathematically dense hub pages now contain both formal definitions and at least one concrete toy example
  - the concept layer is better suited for incremental study rather than only high-level orientation
- Remaining work:
  - continue adding worked examples to additional concept pages where helpful
  - optionally create a dedicated mathematical preliminaries / toy examples synthesis page later

## [2026-04-11] query | Created Mathematical Preliminaries for SNARKs and STARKs
- Created synthesis page: [[Mathematical Preliminaries for SNARKs and STARKs]].
- Organized the current SNARK/STARK branch into a compact mathematical study guide covering:
  - finite-field arithmetic
  - arithmetization and [[Rank-1 Constraint Satisfiability (R1CS)]]
  - multilinear extensions
  - [[Sum-check Protocol]]
  - [[Polynomial Commitments]]
  - [[Interactive Oracle Proofs (IOPs)]]
  - Reed–Solomon codes and [[Reed-Solomon Proximity Testing]]
  - [[FRI]]-style folding
  - non-interactivity via [[Fiat-Shamir Transform]]
  - recursion through accumulation / folding / preprocessing
- Included small formulas and miniature examples so the page works as a study-oriented bridge into the more detailed concept notes.
- Updated [[Index]] so the preliminaries page is discoverable from the top-level syntheses list.
- Remaining work:
  - later add a dedicated page for finite-field / coding-theory preliminaries if the mathematical layer grows much deeper
  - optionally create a companion page of worked toy examples only

## [2026-04-11] refactor | Second-tier concept enrichment pass
- Enriched a second tier of concept pages with additional mathematical intuition and worked examples, focusing on compiler, oracle, and recursion-architecture concepts.
- Added worked examples to:
  - [[Fiat-Shamir Transform]]
  - [[Interactive Oracle Proofs (IOPs)]]
  - [[Accumulation Schemes]]
  - [[Folding Schemes]]
  - [[Preprocessing SNARKs]]
  - [[Proof-Carrying Data (PCD)]]
  - [[Holographic Proofs]]
  - [[Interactive Oracle Reductions (IORs)]]
  - [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- Strengthened navigation on selected concept hubs by adding or expanding “Current map in this wiki” sections where useful, especially around:
  - compiler concepts
  - recursion concepts
  - oracle-proof abstractions
- Result of the pass:
  - the concept layer now has broader coverage of worked examples beyond the first math-heavy core pages
  - more second-tier concepts now point clearly into the synthesis layer and study-guide pages
- Remaining work:
  - continue enriching additional concept pages opportunistically as new papers are ingested
  - optionally standardize “Current map in this wiki” sections across even more concept pages if the graph grows denser

## [2026-04-13] ingest | Algebraic Methods for Interactive Proof Systems
- Ingested `raw/papers/SNARKs & STARKs/146585.146605.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Algebraic Methods for Interactive Proof Systems]].
- Positioned the paper as a classical algebraic-IP foundation for the current SNARK/STARK branch, especially for the historical lineage behind [[Sum-check Protocol]].
- Updated [[Sum-check Protocol]] to cite this paper as a foundational source and to frame its importance more explicitly in relation to the classical algebraic worldview.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - interactive-proof verification of the permanent via low-degree polynomial consistency checks
  - derivation that languages in the polynomial-time hierarchy admit interactive proofs
  - clear historical bridge from algebraic IP techniques to later sum-check-centered and arithmetized proof-system design
- Remaining work:
  - eventually compare this permanent-based algebraic IP style more directly against the oracle-centric viewpoint in [[Interactive Oracle Proofs]]

## [2026-04-13] ingest | Fast Probabilistic Algorithms for Verification of Polynomial Identities
- Ingested `raw/papers/SNARKs & STARKs/322217.322225.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Fast Probabilistic Algorithms for Verification of Polynomial Identities]].
- Created concept page: [[Polynomial Identity Testing]].
- Positioned the paper as the clearest classical anchor for the randomized "why random evaluation works" intuition underlying later algebraic-verification techniques.
- Updated [[Index]] so both the new source and the new concept are discoverable from the top-level catalog.
- Main takeaways captured in the source and concept pages:
  - nonzero multivariate polynomials vanish on only a bounded fraction of points in a large enough testing domain
  - random evaluation can replace expensive symbolic expansion for high-confidence identity checking
  - the same probabilistic algebraic style extends to divisibility, ideal membership, and related polynomial properties
  - this classical PIT worldview forms part of the conceptual path toward [[Algebraic Methods for Interactive Proof Systems]] and later [[Sum-check Protocol]]-centered systems
- Remaining work:
  - connect [[Polynomial Identity Testing]] more explicitly into one or two synthesis pages such as [[Mathematical Preliminaries for SNARKs and STARKs]] or the reading map if the classical branch grows further

## [2026-04-13] ingest | Delegating Computation Interactive Proofs for Muggles
- Ingested `raw/papers/SNARKs & STARKs/2699436.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Delegating Computation Interactive Proofs for Muggles]].
- Positioned the paper as a bridge from classical interactive-proof complexity results toward the modern verifiable-computation / delegation viewpoint.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - public-coin interactive proofs for log-space uniform Boolean-circuit computations of depth $d$
  - efficient honest provers together with super-efficient verifiers and low communication
  - strong motivation for proof systems as tools for outsourcing and verifying tractable computation, not only for complexity-class separations
  - conceptual linkage from classical algebraic IPs toward later succinct-verification and delegation-oriented systems
- Remaining work:
  - decide whether to create a dedicated concept or synthesis page for verifiable computation / delegation if more bridge papers are ingested
  - connect this source more explicitly into recursion-oriented pages such as [[Proof-Carrying Data (PCD)]] or [[Incrementally Verifiable Computation (IVC)]] if that branch becomes more central

## [2026-04-13] ingest | Checking Computations in Polylogarithmic Time
- Ingested `raw/papers/SNARKs & STARKs/103418.103428.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Checking Computations in Polylogarithmic Time]].
- Positioned the paper as a classical bridge from interactive-proof complexity toward transparent verification and verifiable computation.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - nondeterministic tasks can be transformed so that witness checking becomes polylogarithmic-time Monte Carlo verification
  - deterministic proof systems can be extended so ordinary proofs become transparent proofs checkable in polylogarithmic randomized time
  - error-correcting encodings are essential because ultra-fast checkers cannot afford to read everything exhaustively
  - the paper articulates an early strong asymmetry goal that anticipates later succinct-verification and delegation-oriented systems
- Remaining work:
  - if the bridge branch keeps growing, create a dedicated synthesis on transparent verification / verifiable computation
  - later compare this paper more explicitly with [[Delegating Computation Interactive Proofs for Muggles]] and PCP/IOP-style representations

## [2026-04-13] lint | Research wiki maintenance pass after classical-foundations expansion
- Ran a research lint pass across `research/` focusing on link health, orphans, index coverage, contradictions, and near-duplicate concepts.
- Verified index coverage:
  - all current source, concept, entity, synthesis, and open-question pages are represented in [[Index]]
  - the only research page without an inbound link across the vault was [[Index]], which is expected because it is primarily a top-level navigation hub embedded from [[Home]]
- Fixed small issues found during lint:
  - removed placeholder example wikilinks `Source A` and `Source B` from [[Contradictions]] and replaced them with inline code so the template no longer creates false broken links
  - removed premature links to the not-yet-ingested PCP theorem page from [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]
  - normalized one future reference in [[Log]] so the not-yet-created PCP theorem page is mentioned as plain text rather than a live broken wikilink
- Structural findings:
  - no true research-page orphans besides the expected top-level [[Index]] hub
  - no missing pages in [[Index]]
  - no active contradictions recorded yet in [[Contradictions]]
  - a few concept pairs are adjacent but not duplicates, especially [[zkSNARKs]] vs [[Transparent zkSNARKs]] and [[Interactive Oracle Proofs (IOPs)]] vs [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- Remaining work:

## [2026-04-13] ingest | Proof Verification and the Hardness of Approximation Problems
- Ingested `raw/papers/SNARKs & STARKs/278298.278306.pdf` as the PCP-theorem anchor after the earlier Arora–Safra PDF proved too extraction-poor for reliable use.
- Extracted readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Proof Verification and the Hardness of Approximation Problems]].
- Created concept page: [[Probabilistically Checkable Proofs (PCPs)]].
- Positioned the paper as the main PCP theorem / approximation-hardness anchor currently available in the wiki.
- Updated [[Index]] so the new source and PCP concept are discoverable from the top-level catalog.
- Main takeaways captured in the new pages:
  - the PCP theorem viewpoint that $NP = PCP(O(\log n), O(1))$
  - the role of PCPs as a canonical local-checking proof model between MIP-style and IOP-style viewpoints
  - major hardness-of-approximation consequences, especially for MAX-SNP-hard problems
- Remaining work:
  - revisit the original Arora–Safra paper if a cleaner extract becomes available

## [2026-04-13] synthesis | Added PCP vs MIP vs IOP Lineage
- Created synthesis page: [[PCP vs MIP vs IOP Lineage]].
- Synthesized the conceptual evolution from:
  - multi-prover interactive proofs,
  - to static probabilistically checkable proofs,
  - to interactive oracle proofs as the model closest to many modern oracle-based systems.
- Positioned the page as the canonical lineage explainer connecting:
  - [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]
  - [[Probabilistically Checkable Proofs (PCPs)]]
  - [[Interactive Oracle Proofs (IOPs)]]
- Updated [[Index]] so the new synthesis is discoverable from the top-level catalog.
- Result of the pass:
  - the PCP layer now has a synthesis page rather than only separate concept/source anchors
  - the research wiki now explains both the motivation axis ([[Transparent Verification and Verifiable Computation]]) and the formal-model axis ([[PCP vs MIP vs IOP Lineage]])
- Remaining work:
  - revisit the Arora–Safra paper if a higher-quality extract becomes available
  - later compare PCP / MIP / IOP lineage more explicitly against the RS/IOPP / STARK lineage in a dedicated synthesis if needed

## [2026-04-13] ingest | Interactive Oracle Proofs with Constant Rate and Query Complexity
- Ingested `raw/papers/SNARKs & STARKs/2016-324.pdf`.
- Extracted readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Interactive Oracle Proofs with Constant Rate and Query Complexity]].
- Updated [[Interactive Oracle Proofs (IOPs)]] to reflect this paper as the main parameter-improvement and construction-oriented IOP anchor alongside the original model paper.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - constant-round IOPs can achieve proof-length / query-complexity tradeoffs not known for PCPs or IPs alone
  - circuit satisfiability admits 3-round IOPs with linear proof length and constant query complexity
  - Reed–Solomon codes admit 2-round IOPPs with linear proof length and constant query complexity
  - the paper introduces IOP composition and sublinear-sumcheck tools that help explain later oracle-based proof-system efficiency gains
- Remaining work:
  - consider adding a dedicated concept page for IOPPs if the RS/IOPP branch grows denser
  - connect this paper more explicitly into [[FRI]], [[Reed-Solomon Proximity Testing]], and any future RS/IOPP / STARK-lineage synthesis

## [2026-04-13] ingest | A PCP Theorem for Interactive Proofs and Applications
- Ingested `raw/papers/SNARKs & STARKs/2021-915.pdf`.
- Extracted readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[A PCP Theorem for Interactive Proofs and Applications]].
- Updated [[Probabilistically Checkable Proofs (PCPs)]], [[Interactive Oracle Proofs (IOPs)]], and [[PCP vs MIP vs IOP Lineage]] so the paper is reflected as a theorem-level bridge from PCP-style local checking to interactive settings.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - any language with a public-coin $k$-round IP has a $k$-round IOP where the verifier reads only $O(1)$ bits from each prover and verifier message and uses $O(\log n)$ decision randomness
  - the paper extends the PCP theorem viewpoint from static NP proofs to interactive proofs
  - index-decodable PCPs provide a bridge to commit-and-prove SNARKs in the random oracle model
  - the result strengthens the conceptual status of IOPs beyond mere hybrid convenience
- Remaining work:
  - consider adding a dedicated concept page for index-decodable PCPs if the commit-and-prove branch grows

## [2026-04-14] synthesis | Added RS IOPP and STARK Lineage
- Created synthesis page: [[RS IOPP and STARK Lineage]].
- Synthesized the internal historical development of the Reed–Solomon / oracle-proof branch from:
  - local-checking foundations,
  - to IOP abstractions,
  - to IOPPs,
  - to [[FRI]] as the foundational practical engine,
  - to [[WHIR]] as a verifier-optimized constrained-RS refinement.
- Positioned the page as complementary to:
  - [[PCP vs MIP vs IOP Lineage]] for model evolution,
  - and [[Multilinear and Sum-check Systems vs RS FRI and IOPP Systems]] for family-level comparison.
- Updated [[Index]] so the new synthesis is discoverable from the top-level catalog.
- Result of the pass:
  - the STARK-substrate side of the wiki now has a dedicated historical synthesis rather than only local comparisons such as [[FRI vs WHIR]]
  - the overall map is more balanced across classical foundations, formal model evolution, and transparent-proof substrate evolution
- Remaining work:
  - later connect this synthesis more explicitly into [[FRI]], [[Reed-Solomon Proximity Testing]], and the reading map if desired

## [2026-04-14] concept | Added Interactive Oracle Proofs of Proximity (IOPPs)
- Created concept page: [[Interactive Oracle Proofs of Proximity (IOPPs)]].
- Positioned the page as the model-layer bridge between generic [[Interactive Oracle Proofs (IOPs)]] and the RS / STARK substrate centered on [[Reed-Solomon Proximity Testing]].
- Updated nearby concept pages to point to the new hub, especially:
  - [[Interactive Oracle Proofs (IOPs)]]
  - [[Reed-Solomon Proximity Testing]]
- Updated [[Index]] so the new concept is discoverable from the top-level catalog.
- Result of the pass:
  - the RS/IOPP branch now has a clearer concept layer rather than jumping directly from generic IOPs to FRI/WHIR
  - the distinction between IOPs and IOPPs is now explicit in the wiki graph
- Remaining work:
  - choose the next best RS/STARK-adjacent remaining raw paper and ingest it one-by-one
  - update related RS/IOPP/STARK pages plus [[Index]] and [[Log]]

## [2026-04-14] ingest | Probabilistic checking of proofs; a new characterization of NP
- Ingested `raw/papers/SNARKs & STARKs/Probabilistic_checking_of_proofs_a_new_characterization_of_NP.pdf` as a historical PCP milestone, despite poor local text extraction quality.
- Created source page: [[Probabilistic checking of proofs; a new characterization of NP]].
- Treated the page as a provisional historical-summary note rather than a full theorem-detail note, because the extracted PDF text is largely obscured by licensing overlays.
- Updated [[Probabilistically Checkable Proofs (PCPs)]], [[PCP vs MIP vs IOP Lineage]], and [[Index]] so the Arora–Safra milestone now appears explicitly in the PCP branch.
- Main takeaways captured in the source page:
  - this paper is a major PCP-theorem milestone
  - it is the historical predecessor to [[Proof Verification and the Hardness of Approximation Problems]]
  - it fills an important gap between MIP/local-checking intuition and the later constant-query PCP theorem anchor
- Remaining work:
  - strengthen the page if a cleaner extract or alternative source copy becomes available
  - later compare it more explicitly against the later constant-query PCP theorem paper

## [2026-04-14] lint | Focused research pass after PCP / IOPP / STARK updates
- Ran a focused research lint pass after the recent PCP, IOPP, RS/STARK, and delegation updates.
- Verified link health across `research/`:
  - no true missing research links remain
  - placeholder broken-link mentions in prior lint notes are now fully normalized
- Verified catalog coverage:
  - all current research sources, concepts, entities, syntheses, and open questions are represented in [[Index]]
  - current counts are 20 source pages, 28 concept pages, 7 entity pages, 12 synthesis pages, and 1 open-question page
- Verified graph hygiene:
  - the only research page without an inbound link across the vault is [[Index]], which remains expected because it is the top-level catalog hub
  - no obvious true duplicates were found beyond already-known valid adjacent pairs such as [[zkSNARKs]] vs [[Transparent zkSNARKs]] and [[Interactive Oracle Proofs (IOPs)]] vs [[Multilinear Interactive Oracle Proofs (MIOPs)]]
- Fixed small issues found during lint:
  - normalized old lint wording in [[Log]] so removed placeholder examples no longer appear as live broken-link text
  - replaced shorthand references `[[IVC]]` and `[[PCD]]` in [[Transparent Verification and Verifiable Computation]] with their canonical full note titles
- Result of the pass:
  - the research graph is currently clean on missing-link and index-coverage checks
  - the recent PCP / IOPP / STARK additions appear to be well integrated into the broader wiki structure

## [2026-04-14] refactor | Targeted cross-link pass for classical, PCP/IOP, and delegation/RS branches
- Ran a focused cross-link pass on the newly expanded research graph.
- Strengthened the classical spine:
  - linked [[Polynomial Identity Testing]], [[Sum-check Protocol]], and [[Algebraic Methods for Interactive Proof Systems]] more explicitly to each other
  - made PIT more visible as the randomized-algebraic precursor to sum-check-style reasoning
- Strengthened PCP/IOP synthesis connections:
  - linked [[Probabilistically Checkable Proofs (PCPs)]] more explicitly to [[PCP vs MIP vs IOP Lineage]]
  - linked the lineage synthesis back to [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]] and [[Interactive Oracle Proofs of Proximity (IOPPs)]]
  - updated [[Interactive Oracle Proofs (IOPs)]] and [[Interactive Oracle Proofs of Proximity (IOPPs)]] to surface the delegation-oriented IOP bridge
- Strengthened delegation ↔ IOP ↔ RS/IOPP links:
  - updated [[Transparent Verification and Verifiable Computation]] to point more directly to [[Linear-Size Constant-Query IOPs for Delegating Computation]], [[Interactive Oracle Proofs of Proximity (IOPPs)]], and [[RS IOPP and STARK Lineage]]
  - updated [[RS IOPP and STARK Lineage]] to treat [[Linear-Size Constant-Query IOPs for Delegating Computation]] as a useful boundary case between delegation and RS/IOPP substrate design
- Result of the pass:
  - the research graph now has a cleaner flow from classical algebraic checking → PCP/IOP formal models → delegation-oriented oracle proofs → RS/IOPP/STARK substrate design
  - the newly added syntheses and concept hubs are better integrated into older foundational pages

## [2026-04-14] ingest | Linear-Size Constant-Query IOPs for Delegating Computation
- Ingested `raw/papers/SNARKs & STARKs/2019-1230.pdf`.
- Extracted readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Linear-Size Constant-Query IOPs for Delegating Computation]].
- Updated [[Transparent Verification and Verifiable Computation]] and [[Interactive Oracle Proofs (IOPs)]] so the paper is reflected as a modern delegation-oriented IOP bridge.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - rich classes of algebraic computations admit constant-query IOPs with linear-size proofs and polylogarithmic verifier time
  - prover arithmetic complexity is $O(T\log T)$, making the construction close to an ideal delegation-oriented IOP
  - the proof is built from a constant number of Reed–Solomon codewords, tying the delegation branch back to the RS / oracle-proof substrate
  - the result connects classical delegation motivation to modern oracle-proof realizations
- Remaining work:
  - consider connecting this paper more explicitly into [[RS IOPP and STARK Lineage]] if desired

## [2026-04-14] ingest | On the Concrete Efficiency of Probabilistically-Checkable Proofs
- Ingested `raw/papers/SNARKs & STARKs/2488608.2488681.pdf`.
- Extracted readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]].
- Updated [[Probabilistically Checkable Proofs (PCPs)]] to reflect this paper as the main practicality / threshold-oriented counterpart to the theorem-level PCP anchors.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - first PCP with quasi-optimal prover and verifier time up to polylogarithmic factors for RAM computations
  - introduction of a concrete-efficiency threshold measuring when PCP use beats naive verification
  - Reed–Solomon PCP-of-proximity threshold improved from about `2^683` to about `2^43`
  - strong reminder that positive PCP applications live or die on concrete efficiency, not only asymptotic verifier locality
- Remaining work:
  - connect this paper more explicitly into [[Transparent Verification and Verifiable Computation]] and possibly the RS / IOPP branch if desired

## [2026-04-14] refactor | Wired IOPP concept into STARK-substrate pages
- Continued integrating [[Interactive Oracle Proofs of Proximity (IOPPs)]] into the STARK-substrate branch.
- Updated:
  - [[FRI]] to frame FRI explicitly as an IOPP-level engine and to add a current-map section pointing into the RS substrate synthesis
  - [[WHIR]] to point more directly at the new IOPP hub and the RS-lineage synthesis
  - [[SNARKs and STARKs Reading Map]] to explicitly name [[Interactive Oracle Proofs of Proximity (IOPPs)]] and [[RS IOPP and STARK Lineage]] inside the PCP / IOP / RS / STARK substrate cluster
- Result of the pass:
  - the STARK-substrate graph now has a cleaner progression from [[Interactive Oracle Proofs (IOPs)]] to [[Interactive Oracle Proofs of Proximity (IOPPs)]] to [[FRI]] / [[WHIR]]
  - the reading map now points more directly to the dedicated historical synthesis for the RS branch

## [2026-04-13] synthesis | Added Transparent Verification and Verifiable Computation
- Created synthesis page: [[Transparent Verification and Verifiable Computation]].
- Synthesized the branch linking:
  - classical algebraic checking
  - transparent proof / local-checking ambitions
  - delegation-oriented interactive proofs
  - recursive proof-carrying models such as [[Incrementally Verifiable Computation (IVC)]] and [[Proof-Carrying Data (PCD)]]
- Positioned the page as the canonical hub for the verification-asymmetry story that runs across several previously separate source and concept pages.
- Updated [[Index]] so the new synthesis is discoverable from the top-level catalog.
- Result of the pass:
  - the bridge branch now has a proper synthesis layer rather than only individual source notes
  - the research wiki better explains why classical transparent-proof and delegation papers belong in the same long arc as modern recursive proof systems
- Remaining work:
  - connect this synthesis more explicitly into future PCP/IOP coverage once the PCP theorem branch is ingested
  - decide later whether this page should split into separate delegation and recursion syntheses if the branch becomes much denser

## [2026-04-13] ingest | Non-deterministic Exponential Time Has Two-Prover Interactive Protocols
- Ingested `raw/papers/SNARKs & STARKs/BF01200056.pdf`.
- Extracted metadata and readable text from the PDF using a PDFKit-based Swift script.
- Created source page: [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]].
- Positioned the paper as a classical MIP landmark linking algebraic interactive proofs to the later PCP/MIP/IOP local-checking lineage.
- Updated [[Index]] so the new source is discoverable from the top-level catalog.
- Main takeaways captured in the source page:
  - two-prover interactive proofs characterize nondeterministic exponential time
  - the proof combines algebraic extrapolation ideas with a multilinearity-verification scheme for oracle-held functions
  - the paper is a key historical bridge from algebraic IPs toward local-consistency and multi-prover proof models
  - it motivates future wiki coverage of MIP / PCP concepts more explicitly
- Remaining work:
  - ingest one of the PCP-theorem anchors next, especially `Probabilistic checking of proofs; a new characterization of NP` if extraction quality can be made acceptable
  - consider adding a dedicated concept page for multi-prover interactive proofs once the PCP branch is denser

## [2026-04-13] refactor | Adjusted agenda and overview from resolved intake questions
- Re-read [[Intake Questions]] after resolution and propagated the user's preferences into the research planning pages.
- Updated [[Research Agenda]] to reflect:
  - four long-term domains: Mathematics, Cryptography, Computer Science, and AI
  - the current cryptography branch as primary, but not exclusive
  - stronger emphasis on concept-first organization
  - one-source-at-a-time ingest expectations
  - rigorous formal treatment for papers and lighter workflows for non-paper sources
  - maintenance expectations around [[Contradictions]], lint rhythm, and active next-source suggestions
  - clearer articulation of open branches for Mathematics, CS, and AI
- Updated [[Overview]] to reflect the resolved workflow decisions and the expanded current state of the SNARK/STARK branch.
- Result of the pass:
  - the planning/docs layer now better matches the user's stated breadth, rigor expectations, and maintenance preferences
  - the research wiki is no longer framed as SNARK/STARK-only, but as a broader multi-domain system with one mature branch so far
- Remaining work:
  - optionally propagate the same planning assumptions into any future dedicated synthesis for verifiable computation / transparent verification
  - start the first non-cryptography branch once the user drops sources for Mathematics, CS, or AI

## [2026-04-15] lint | Research source paper-standard audit
- Audited all pages in `research/sources/` against the paper-note standard in [[CLAUDE]] and `templates/Research Source.md`.
- Verified that all 20 source pages now share the required source frontmatter fields and canonical section order:
  - `Summary`
  - `Key Claims`
  - `Formal Definitions and Results`
  - `Methods and Proof Techniques`
  - `Complexity and Performance`
  - `Why It Matters`
  - `Connections to the Wiki`
  - `Open Questions / Limitations`
  - `Suggested Next Reading`
  - `Related`
- Normalized the one structurally non-compliant page:
  - [[Proof Verification and the Hardness of Approximation Problems]]
    - renamed `Key Claims / Findings` to `Key Claims`
    - removed the duplicate `Why It Matters` split and merged its content into the canonical section
    - refreshed `updated` to `2026-04-15`
    - tightened suggested-reading links
- Validation result: no remaining source pages with missing required frontmatter or non-canonical section ordering.
- Remaining work:
  - many source pages still need a deeper substantive upgrade to fully satisfy the strongest paper standard in [[CLAUDE]]: explicit section/page citations, more theorem-level detail, and more precise complexity bounds drawn directly from the raw papers
  - current environment lacks PDF-text extraction tooling, so those deeper upgrades should be done from extracted text or with PDF/OCR access rather than by guessing from existing summaries

## [2026-04-15] refactor | Deepened weakest research source notes with direct PDF-backed detail
- Restored local PDF extraction capability using a small Swift + PDFKit script against files in `raw/papers/SNARKs & STARKs/`.
- Ranked source pages by substantive rigor and selected four weak notes for immediate upgrade:
  - [[Checking Computations in Polylogarithmic Time]]
  - [[Non-deterministic Exponential Time Has Two-Prover Interactive Protocols]]
  - [[Proof Verification and the Hardness of Approximation Problems]]
  - [[Interactive Oracle Proofs with Constant Rate and Query Complexity]]
- Refreshed those pages to paper standard by adding:
  - theorem-level statements tied to the paper openings
  - explicit section / page citations
  - sharper complexity claims drawn from the papers rather than from prior summaries
  - stronger methods sections grounded in the stated technical contributions
- Verified after editing that all four upgraded pages still match the canonical source-note section order and now contain many explicit citation markers.
- Remaining work:
  - continue the same PDF-backed upgrade pass across the remaining weakest source notes, especially [[Probabilistic checking of proofs; a new characterization of NP]], which still depends on a poor source extract
  - decide whether to archive or commit the temporary local PDF extraction helper outside the vault, since it was used ad hoc for this pass rather than added as a tracked project script

## [2026-04-15] refactor | Deepened second batch of research source notes with direct PDF-backed detail
- Continued the PDF-backed paper-standard pass and upgraded the next batch of weak source notes:
  - [[A PCP Theorem for Interactive Proofs and Applications]]
  - [[Algebraic Methods for Interactive Proof Systems]]
  - [[Delegating Computation Interactive Proofs for Muggles]]
  - [[Fast Probabilistic Algorithms for Verification of Polynomial Identities]]
  - [[Interactive Oracle Proofs]]
  - [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]
  - [[WARP Linear-Time Accumulation Schemes]]
  - [[WHIR Reed-Solomon Proximity Testing with Super-Fast Verification]]
  - [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]
- For each page, replaced summary-only theorem claims with direct source-backed statements from the paper openings and added explicit citations to abstracts, theorems, definitions, lemmas, and page ranges.
- Revalidated the whole `research/sources/` directory after the pass:
  - no source pages with missing required frontmatter
  - no source pages with non-canonical section ordering
- Remaining weak notes after re-ranking are now concentrated in:
  - [[Probabilistic checking of proofs; a new characterization of NP]] (still blocked by poor source extract)
  - [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]
  - [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
  - [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
  - [[Linear-Size Constant-Query IOPs for Delegating Computation]]
  - [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]]

## [2026-04-15] refactor | Deepened final planned weak batch of research source notes
- Continued the PDF-backed paper-standard pass and upgraded the next targeted weak batch:
  - [[Symphony Scalable SNARKs in the Random Oracle Model from Lattice-Based High-Arity Folding]]
  - [[Fast Reed-Solomon Interactive Oracle Proofs of Proximity]]
  - [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
  - [[Linear-Size Constant-Query IOPs for Delegating Computation]]
  - [[On the Concrete Efficiency of Probabilistically-Checkable Proofs]]
- For each page, replaced high-level summary-only claims with front-matter theorem statements, concrete asymptotic bounds, and explicit citations to abstract / theorems / definitions / tables / page ranges.
- Re-ranked `research/sources/` after the pass. Remaining structurally compliant but relatively weaker notes are now mainly:
  - [[Probabilistic checking of proofs; a new characterization of NP]] — still limited by poor source extraction quality
  - [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]] — structurally solid, but still lighter on explicit citations than the upgraded cohort
- Result of the pass:
  - the planned weakest-source batch has been completed
  - most research source pages now have theorem-level and citation-backed front sections rather than only narrative summaries

## [2026-04-15] refactor | Final cleanup pass on VEIL and Arora–Safra
- Upgraded [[VEIL Lightweight Zero-Knowledge for Hash-Based Multilinear Proof Systems]] using direct PDF-backed detail from the abstract and introduction:
  - added explicit citations for the compiler goal, MIOP structural abstraction, zk-code padding, extra-column blinding, and reported concrete overheads
  - grounded the page more directly in the paper's front-matter definitions and quantitative claims
- Tried a stronger extraction strategy for [[Probabilistic checking of proofs; a new characterization of NP]] by rendering PDF pages to images and running OCR.
- Result of the stronger extraction pass:
  - the PDF remains heavily degraded by IEEE overlay text, so most details are still unrecoverable with confidence
  - however, OCR did recover the explicit main-theorem line `NP = PCP(O(log n), O(log n))` and some supporting fragments about recursive proof checking and the algebraic 3SAT view
- Updated the Arora–Safra note accordingly:
  - preserved the strong source-quality caveat
  - replaced purely indirect theorem claims with the limited theorem statement now recoverable locally
  - kept all unrecoverable deeper details marked as provisional rather than guessed
- End state after cleanup:
  - `research/sources/` remains structurally consistent
  - VEIL is no longer among the notably weak citation-light notes
  - Arora–Safra remains the only source note still meaningfully constrained by source-quality limitations, but it is now stronger than before and locally grounded where possible

## [2026-04-30] ingest | Added Zero-Knowledge IOPPs for Constrained Interleaved Codes paper
- Ingested paper from raw/papers/SNARKs & STARKs/2026-391.pdf via pdftotext
- Created source note: research/sources/Zero-Knowledge IOPPs for Constrained Interleaved Codes.md
- Paper presents IOP of proximity for constrained interleaved linear codes with honest-verifier zero-knowledge
- Key contributions: zero-knowledge sumcheck IOR and zero-knowledge code-switching IOR
- Added to research wiki with proper frontmatter and links to [[Interactive Oracle Proofs (IOPs)]] and [[Zero-Knowledge Proofs]]
