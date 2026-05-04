---
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

- **2026-04-15** — Unify whir-p3 benchmarks behind a single `whir-bench` crate whose schemes are thin wrappers over `warp_ivc` recursive IVC paths. Legacy `warp_bench`, `pipeline_bench`, `accumulation_bench`, and older `compare_bench` removed after parity validation. See [[whir-bench Crate Migration]] and [[whir-bench Scheme Mapping]].

- **2026-05-01** — Keep WHIR typed output non-authoritative until the verifier proof relation enforces the full typed folded-output semantics. Direct typed hooks and prover-side validation are useful scaffolding, but `verify_v2` must remain fail-closed. See [[Symphony WHIR Public Verifier]] and [[rules]].

- **2026-05-01** — Treat `prove_public` / `verify_public` and `PublicProofBundle` / `PublicSymphonyProof` as the product-facing public verifier API. `prove_v2` / `verify_v2` remain compatibility names. See [[Symphony WHIR Public Verifier]] and [[rules]].
