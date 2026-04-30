---
date: 2026-04-10
type: concept
created: 2026-04-10
updated: 2026-04-11
tags:
  - cryptography
  - arithmetization
  - r1cs
related:
  - "[[zkSNARKs]]"
  - "[[Spartan]]"
  - "[[Polynomial Commitments]]"
description: "Core arithmetization target used by Spartan"
---

# Rank-1 Constraint Satisfiability (R1CS)

## Definition / framing

R1CS is an NP-complete language and a standard arithmetized representation of computation used in many zkSNARK systems.

In the framing emphasized by *[[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]*, R1CS generalizes arithmetic circuit satisfiability and serves as the target language for which Spartan constructs succinct arguments.

## Why it matters

R1CS is a key interface layer between high-level programs and proof systems.

If a proof system is built for R1CS, then practical usability depends on both:
- the efficiency of compiling applications into R1CS,
- and the efficiency of proving/verifying satisfiability of the resulting instance.

## Key distinctions

- R1CS is more of an **arithmetized statement format** than an end-user programming model.
- Different proof systems support different computational models directly; supporting arbitrary R1CS often signals broad generality.
- One of Spartan's major claims is that it achieves sub-linear verification for **arbitrary R1CS instances**, not just highly structured special cases.


## Mathematical background / formulae

An R1CS instance is specified by matrices $A,B,C$ over a field and asks for a vector
$$
z=(1,x,w)
$$
such that for every constraint index $i$,
$$
\langle A_i,z\rangle \cdot \langle B_i,z\rangle = \langle C_i,z\rangle.
$$
This compactly represents multiplication-gate consistency across an arithmetized computation.

## Worked example

Suppose we want to encode the statement
$$
z = x\cdot y
$$
with public inputs $x,y,z$ and no additional witness. One R1CS constraint is enough:
$$
\langle A_1,(1,x,y,z)\rangle \cdot \langle B_1,(1,x,y,z)\rangle = \langle C_1,(1,x,y,z)\rangle,
$$
with rows chosen so that
$$
\langle A_1,(1,x,y,z)\rangle = x,
\qquad
\langle B_1,(1,x,y,z)\rangle = y,
\qquad
\langle C_1,(1,x,y,z)\rangle = z.
$$
For example, if $(x,y,z)=(3,5,15)$ then the constraint checks
$$
3\cdot 5 = 15.
$$
More complicated computations are encoded by introducing intermediate variables into the vector $z=(1,x,w)$ and writing one multiplicative consistency equation per gate/constraint.

## Evidence / sources

- [[Spartan Efficient and General-Purpose zkSNARKs without Trusted Setup]]

## Related entities

- [[Spartan]]

## Open questions

- Which of the other papers in the SNARKs/STARKs folder reuse R1CS versus moving to a different algebraic model?

## Wiki development

- What is the right page in this wiki to compare R1CS with QAPs, AIR, Plonkish arithmetizations, and related representations?
