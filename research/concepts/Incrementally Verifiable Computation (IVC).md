---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - ivc
  - recursion
  - proof-systems
related:
  - "[[Proof-Carrying Data (PCD)]]"
  - "[[Accumulation Schemes]]"
  - "[[WARP]]"
description: "Stepwise proof-carrying computation model closely tied to recursion"
---

# Incrementally Verifiable Computation (IVC)

## Definition / framing

Incrementally verifiable computation (IVC) is a setting in which a long computation is broken into steps and each step updates a proof state that certifies the correctness of the computation so far.

## Why it matters

IVC is one of the main reasons the recursion / accumulation branch of the proof-systems literature matters in practice.

In *[[WARP Linear-Time Accumulation Schemes]]*, IVC appears as part of the motivating family of recursive proof applications that benefit from better accumulation schemes.

## Key distinctions

- IVC is closely related to recursive proof composition and often overlaps conceptually with PCD.
- The practical cost of each step is heavily influenced by the efficiency of the underlying accumulation / folding / recursive-verification machinery.
- Some papers target the IVC substrate directly, while others target one of its key building blocks.


## Mathematical background / formulae

IVC can be viewed as a sequence of state/proof pairs
$$
(s_0,\pi_0),(s_1,\pi_1),\dots,(s_T,\pi_T),
$$
where each step certifies a transition relation such as
$$
T(s_t,s_{t+1},u_t)=1.
$$
The key property is that $\pi_{t+1}$ certifies not just the newest step, but also the correctness of all prior steps summarized by $\pi_t$.

### Formal IVC definition

An IVC scheme for a step function $F: S \times X \to S$ consists of two algorithms:
- $\mathsf{IVC.Prove}(i, s_i, x_i, \pi_{i-1}) \to \pi_i$ — given the step index, current state, current input, and the proof from the previous step, produce an updated proof.
- $\mathsf{IVC.Verify}(i, s_0, s_i, \pi_i) \to \{0, 1\}$ — given the step count, initial state, claimed final state, and proof, accept or reject.

The scheme must satisfy three properties:

**Correctness.** If $s_j = F(s_{j-1}, x_j)$ for all $j \in [1, i]$, and each $\pi_j$ is honestly computed via $\mathsf{IVC.Prove}$, then
$$\mathsf{IVC.Verify}(i, s_0, s_i, \pi_i) = 1.$$

**Soundness.** For all PPT adversaries $\mathcal{A}$:
$$\Pr[\mathsf{IVC.Verify}(i, s_0, s_i^*, \pi^*) = 1 \;\wedge\; s_i^* \neq F^{(i)}(s_0, \vec{x})] \leq \mathsf{negl}(\lambda)$$
where $F^{(i)}$ denotes $i$-fold sequential application, i.e., $F^{(i)}(s_0, (x_1, \dots, x_i)) = F(\cdots F(F(s_0, x_1), x_2) \cdots, x_i)$. In words, no efficient adversary can produce a convincing proof for a final state that is not the honest result of applying $F$ step by step.

**Succinctness.** The proof size $|\pi_i|$ and the verification time $T_{\mathsf{Verify}}$ are independent of $i$ (or at most polylogarithmic in $i$). This is the crucial efficiency property: no matter how many steps have been executed, the proof remains short and fast to check.

### Key property — proof of all prior steps

$\pi_i$ attests not just to step $i$, but to the entire chain of computation:
$$\pi_i \;\Rightarrow\; \bigwedge_{j=1}^{i} \bigl(s_j = F(s_{j-1}, x_j)\bigr).$$
This is what distinguishes IVC from simply producing independent proofs for each step. The single proof $\pi_i$ is a certificate for the full history, yet its size does not grow with $i$.

### Worked example: 3-step summation

Let $F(s, x) = s + x$ over $\mathbb{Z}$, with initial state $s_0 = 0$ and inputs $x_1 = 3, x_2 = 5, x_3 = 2$.

| Step $j$ | Input $x_j$ | State $s_j = F(s_{j-1}, x_j)$ | Proof produced |
|-----------|-------------|-------------------------------|----------------|
| 1 | 3 | $s_1 = 0 + 3 = 3$ | $\pi_1 = \mathsf{IVC.Prove}(1, s_1, x_1, \pi_0)$ |
| 2 | 5 | $s_2 = 3 + 5 = 8$ | $\pi_2 = \mathsf{IVC.Prove}(2, s_2, x_2, \pi_1)$ |
| 3 | 2 | $s_3 = 8 + 2 = 10$ | $\pi_3 = \mathsf{IVC.Prove}(3, s_3, x_3, \pi_2)$ |

At the end, a verifier checks $\mathsf{IVC.Verify}(3, 0, 10, \pi_3) \stackrel{?}{=} 1$. If it accepts, the verifier is convinced that:
- $s_1 = 0 + 3 = 3$
- $s_2 = 3 + 5 = 8$
- $s_3 = 8 + 2 = 10$

All three transitions are certified by the single proof $\pi_3$, whose size is independent of the number of steps. An adversary who tries to claim $s_3^* = 11$ (or any value other than $10$) cannot produce a valid $\pi^*$ except with negligible probability.

## Evidence / sources

- [[WARP Linear-Time Accumulation Schemes]]
- [[Quasar Sublinear Accumulation Schemes for Multiple Instances]]
- [[Fractal Post-Quantum and Transparent Recursive Proofs from Holography]]

## Related entities

- [[WARP]]
- [[Quasar]]
- [[Fractal]]
- [[Benedikt Bünz]]

## Open questions

- How do multi-instance IVC approaches like [[Quasar]] compare with preprocessing-recursion approaches like [[Fractal]] in terms of concrete efficiency and generality?

## Wiki development

- This page should compare IVC with PCD and direct recursive SNARK verification more explicitly as the corpus grows.
