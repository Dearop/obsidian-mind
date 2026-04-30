---
date: 2026-04-10
type: synthesis
status: stable
created: 2026-04-10
updated: 2026-04-10
tags:
  - quasar
  - warp
  - comparison
  - accumulation
  - ivc
related:
  - "[[Quasar Sublinear Accumulation Schemes for Multiple Instances]]"
  - "[[WARP Linear-Time Accumulation Schemes]]"
  - "[[Quasar]]"
  - "[[WARP]]"
  - "[[Accumulation Schemes]]"
  - "[[Incrementally Verifiable Computation (IVC)]]"
description: "Comparison of linear-time hash-based accumulation against sublinear-verifier multi-instance accumulation"
---

# Quasar vs WARP

## Thesis / purpose

This page compares two important anchors in the wiki's recursion / accumulation branch:
- [[WARP]] — a broad hash-based accumulation framework whose headline result is **linear-time accumulation proving**,
- [[Quasar]] — a multi-instance accumulation / IVC construction whose headline result is **sublinear verifier dependence on the number of accumulated instances**.

The most useful durable summary is:

> **WARP optimizes the accumulation prover in a very general framework; Quasar optimizes recursion overhead by reducing verifier-side dependence on the number of accumulated instances.**

So these papers are close enough to compare directly, but they are not trying to win on the exact same axis.

## Main takeaways

- WARP is the better paper if your question is: *can accumulation itself be made broadly efficient and linear-time to prove in a transparent, hash-based setting?*
- Quasar is the better paper if your question is: *can recursive circuits avoid paying verifier cost that scales linearly with the number of accumulated instances?*
- WARP is more framework-heavy and more general in its coding-theoretic / compiler setup.
- Quasar is more targeted at practical recursive proving overhead in **multi-instance IVC**.
- WARP emphasizes **general linear codes**, **IORs**, and **straightline extraction**.
- Quasar emphasizes **polynomial commitments**, **partial evaluation**, and reducing expensive **CRC** operations.
- WARP feels like a foundational accumulation paper.
- Quasar feels like an optimization-oriented recursion paper built on top of an already mature accumulation perspective.

## Asymptotic complexity comparison

Both systems are accumulation schemes, but they target different scaling axes. Let $\ell$ denote the number of accumulated instances, $N$ the constraint system size, $\lambda$ the security parameter, and $\rho$ the rate parameter for code-based variants.

| Metric | WARP | Quasar (curve variant) | Quasar (code variant) |
|--------|------|-----------------------|----------------------|
| **Accumulation prover** | $O(\ell \cdot \lvert \hat{p} \rvert)$ (linear in instance size) | $O(\ell \cdot \mathsf{polylog}(N))$ MSMs | $O(\ell \cdot \mathsf{polylog}(N))$ field ops |
| **Accumulation verifier** | $O(\ell \cdot (\log N + \lambda))$ | $O(\log \ell)$ group operations | $O\bigl((\lambda / \log(1/\rho)) \cdot (\log N + \log \ell)\bigr)$ |
| **Decider (final check)** | One SNARK verification | One SNARK verification | One SNARK verification |
| **Proof size per instance** | $O(\lambda)$ hash digests | $O(\log \ell)$ group elements | $O(\lambda \log N)$ field/hash elements |
| **Post-quantum** | Yes (hash-based) | No (pairing / discrete-log) | Plausibly (hash-based) |
| **Security model** | ROM, general linear codes | Generic/algebraic group model | ROM, coding-theoretic |

**The key asymptotic distinction.** WARP's verifier cost grows **linearly** in $\ell$ — each accumulated instance adds proportional verifier work. Quasar's curve variant achieves **logarithmic** dependence on $\ell$: doubling the number of accumulated instances adds only a constant number of group operations to the verifier. For applications accumulating many instances (large $\ell$), this is a dramatic practical improvement.

**Tradeoff.** Quasar pays for its verifier sublinearity with more complex polynomial-commitment machinery and, in the curve variant, loss of post-quantum security. WARP's hash-based design gives up verifier sublinearity in $\ell$ in exchange for simpler, transparent, plausibly post-quantum compilation.

## Comparison / synthesis

| Axis | WARP | Quasar |
|---|---|---|
| Historical role in this corpus | Foundational accumulation anchor | Optimization-oriented recursion / multi-instance accumulation follow-up |
| Primary goal | Linear-time accumulation prover | Sublinear verifier dependence on number of accumulated instances `ℓ` |
| Main application framing | Accumulation, PCD, recursive composition broadly | Multi-instance IVC and recursion-overhead reduction |
| Core technical language | IORs, general linear codes, constrained-code batching | PCS-based accumulation, partial evaluation, multi-cast + 2-to-1 fold reductions |
| Security flavor | Hash-based, ROM, plausibly post-quantum, transparent | Curve-based and code-based variants; code-based gives post-quantum plausibility |
| Main asymptotic story | Linear prover, logarithmic verifier | Sublinear verifier in `ℓ`; can also get linear prover with suitable PCS |
| Practical bottleneck addressed | Prover overhead in accumulation itself | Recursive-circuit overhead from verifier-side commitment combination work |
| Relation to recursion | General recursion / PCD substrate | More directly tuned to multi-instance IVC |

## What WARP contributes that Quasar contrasts with

### 1. A very general accumulation framework
WARP's strongest identity is not just one asymptotic point, but the *kind* of framework it builds:
- accumulation from **IORs**,
- over **general linear codes**,
- with a hash-based ROM compilation story,
- and with a new straightline-extraction notion that does not require efficient error-tolerant decoding.

This gives WARP a strong “foundational substrate” feel.

### 2. Linear-time proving as the central victory
WARP's headline is simple and important:
- the first accumulation scheme with **linear prover time** and **logarithmic verifier time**.

That matters because recursive pipelines repeatedly invoke the accumulation prover, so prover superlinearity compounds badly.

### 3. A transparent / hash-based stance
WARP is especially notable for getting these properties in a **hash-based**, **transparent**, **plausibly post-quantum** setting rather than leaning on group-based accumulation.

## What Quasar adds beyond WARP

### 1. A different bottleneck diagnosis
Quasar starts from a more specific complaint:
- even with accumulation, the **verifier** may still do work linear in the number of accumulated instances `ℓ`.

That verifier cost then gets embedded into recursive circuits, creating large recursion overhead.

This is a narrower but very practical target.

### 2. Sublinear verifier dependence on accumulated instances
Quasar's central claim is that a multi-instance accumulation scheme can be built where verifier complexity is **sublinear in `ℓ`**.

This is the paper's defining contrast against many prior approaches, including how it positions itself relative to WARP.

### 3. Partial evaluation instead of standard random linear combination
The main technical optimization is to replace the usual random-linear-combination pattern with **partial evaluation of polynomials**, reducing the number of expensive **CRC** operations the verifier must perform.

This makes Quasar feel more PCS- and recursion-engineering-centric than WARP.

## Where WARP feels stronger

WARP feels stronger when the question is:
- can we build a broadly applicable accumulation scheme from clean foundations,
- over general linear codes,
- with transparent hash-based compilation,
- and with strong extraction properties?

It also feels stronger as a canonical paper for understanding **what accumulation schemes are** at a high level.

## Where Quasar feels stronger

Quasar feels stronger when the question is:
- how do we reduce practical recursive overhead in a multi-instance setting,
- especially when verifier-side commitment combination dominates,
- and when polynomial-commitment structure is available and central?

It is the more direct “recursion engineering” paper of the two.

## Framework contrast

### WARP worldview
- Start from IORs.
- Work over general linear codes.
- Build a ROM accumulation scheme with strong extraction and batching machinery.
- Treat accumulation as a general proof-composition primitive.

### Quasar worldview
- Start from a recursion bottleneck in multi-instance IVC.
- Use polynomial-commitment structure heavily.
- Redesign the accumulation framework to reduce verifier-side commitment-combination work.
- Treat accumulation as something that should be optimized for recursive deployment.

## Evidence and citations

### WARP
From [[WARP Linear-Time Accumulation Schemes]]:
- first linear-time accumulation prover,
- logarithmic verifier,
- hash-based / ROM / general-linear-code framework,
- and a strong emphasis on straightline extraction and unbounded accumulation.

### Quasar
From [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]:
- sublinear verifier complexity in `ℓ`,
- multi-instance IVC,
- partial evaluation to reduce CRC operations,
- and PCS-based curve/code instantiations with explicit comparison against [[WARP]].

## Tensions / contradictions

### Generality vs specialization
- WARP is more general and foundational.
- Quasar is more specialized toward a recursion bottleneck that matters in practice.

### Prover optimization vs verifier optimization
- WARP's identity centers on **prover linearity**.
- Quasar's identity centers on **verifier sublinearity in `ℓ`**.

### Hash-based code framework vs PCS-heavy recursion engineering
- WARP is more about code-based accumulation architecture.
- Quasar is more about exploiting PCS structure to reduce recursive overhead.

## Reading advice

### Read WARP first if:
- you want to understand accumulation as a primitive,
- you care about transparency / post-quantum plausibility,
- you want the cleaner foundational accumulation paper.

### Read Quasar next if:
- you care about recursive prover engineering,
- you care about multi-instance IVC,
- you want to understand how verifier-side accumulation cost becomes the next bottleneck after accumulation itself becomes viable.

## Provisional conclusion

A good durable summary for the wiki is:

> **WARP makes hash-based accumulation broadly efficient; Quasar makes multi-instance recursive accumulation more verifier-efficient.**

Or even shorter:

> **WARP optimizes the accumulation prover; Quasar optimizes recursion overhead from the accumulation verifier.**

That is the clearest way to remember why both papers matter.

## Next steps

- Eventually compare [[WARP]] and [[Quasar]] against folding-oriented papers such as `Symphony.pdf`.
- Create a broader synthesis on **accumulation vs folding vs direct recursive verification**.
- If more recursion papers are added, split this branch into:
  - general accumulation frameworks,
  - multi-instance IVC systems,
  - folding-based recursive systems.
