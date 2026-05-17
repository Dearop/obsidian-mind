---
date: 2026-05-09
description: "Formal verification of DeFi protocols using the Lean 4 theorem prover — research direction surfaced at ZKProof 8."
tags:
  - brain
  - research
---

# DeFi Lean Verification

Formal verification of DeFi protocols using **Lean 4** (the theorem prover/proof assistant). Surfaced as a research direction at ZKProof 8, Rome, May 2026.

## What it is

Lean 4 is a formal proof assistant that can mechanically verify mathematical properties of programs and protocols. Applied to DeFi, it means proving correctness of on-chain logic — AMMs, lending protocols, settlement mechanisms — at the mathematical level, not just via testing or audits.

## State of the art

- **AMM verification**: Constant-product AMMs (Uniswap-style) have been mechanized in Lean, combining dependent types with domain-specific proof APIs.
- **Veil framework**: Open-source multi-modal verification for distributed protocols embedded in Lean. Combines symbolic/concrete model checking, SMT-based proofs, and interactive theorem proving. Found a bug in a prior Rabia consensus verification that two other tools missed.
- **Blockchain consensus in Lean 4**: Active work on formally verifying blockchain protocol proofs — addressing the gap between "manually proved in natural language" and machine-verified correctness.
- **AI-assisted proving**: DeepSeek-Prover-V2 (Apr 2025) enables AI-driven Lean 4 theorem proving via recursive informal→formal reasoning. Mathlib now has 210K+ theorems and 100K+ definitions formalized.

## Why it matters for Ethereum/DeFi

Manual audits and fuzzing catch bugs but cannot prove absence of bugs. Lean verification provides correctness *guarantees*. As DeFi protocols handle billions in TVL, formal verification is the only credible path to "verified correct" smart contracts.

## Potential directions

- Lean 4 formalization of a specific DeFi primitive (AMM, lending, ZK verifier)
- Lean proofs for EVM semantics / EIP correctness
- Enterprise angle: regulated DeFi requiring provably correct execution (links to [[Adrian (Miden)]] master's thesis context)

## Related

- [[Justin Drake]] — EIP-level correctness, formal verification of ZKVMs
- [[Antonio Tolas]] — PQ precompile correctness
- [[Adrian (Miden)]] — enterprise thesis angle
- [[Paul Quesnot]]
