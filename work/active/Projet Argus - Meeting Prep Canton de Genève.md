---
date: 2026-05-20
description: "Meeting preparation for the Canton of Geneva call on Projet Argus — 700h AI agent security incident detection estimate"
tags:
  - work-note
  - meeting-prep
status: active
quarter: Q2-2026
---

# Projet Argus — Meeting Prep: Canton de Genève

**Date**: 2026-05-20
**Context**: Initial call with the Canton of Geneva security team to discuss the [[Estimation Horaire Argus]] (700h estimate submitted 2026-05-11). Goal: align on scope, validate assumptions, gauge budget fit, define next steps.

---

## What You're Walking In With

You submitted a **700-hour estimate** for an AI agent-based system that automates security incident detection and response for the État de Genève's internal security team. The solution uses existing AI models (API or local) + orchestration, with **mandatory human validation** on all remediation actions — no autonomous execution.

Timeline: **~8–9 months**. Variable consultant availability (10–15h/week month 1, full-time months 2–4, then part-time).

---

## Phase Summary (know this cold)

| Phase | Description | Hours | When |
|-------|-------------|-------|------|
| 1 | Discovery, scoping, specifications | 55h | Month 1 |
| 2 | Technical architecture, security & AI governance | 85h | Month 2 |
| 3 | Log source integration & pipeline | 90h | Month 2–3 |
| 4 | AI agents: analysis, correlation, recommendation | 125h | Month 3 |
| 5 | *(Phase 5 — verify in full doc)* | ~70h | Month 3–4 |
| 6 | UI, human validation & traceability | 90h | Month 4 |
| 7 | Tests, validation, robustness & security | 95h | Months 5–8 |
| 8 | Documentation, training & handover | 60h | Months 8–9 |
| — | Project management (continuous) | 30h | All |

**Key deliverable**: a working detection → recommendation → human validation → remediation pipeline with audit trail and engineer dashboard.

---

## Critical Assumptions to Validate in This Call

These are the hidden risks in the estimate. If any are wrong, scope or timeline changes.

- **H6 — Existing tooling**: The estimate assumes a SIEM (ELK, Splunk, or equivalent) is already in place and accessible. **Ask if they have one and which.** If they don't, that's a scope expansion.
- **H7 — Access provisioning**: Logs, APIs, and test environments need to be available within reasonable time. Delays here directly push the calendar.
- **H8 — Availability constraint**: The estimate is built around 10–15h/week in month 1, then full-time months 2–4. If their timeline is tighter, this needs renegotiating.

---

## What's Explicitly Out of Scope (protect yourself)

Be ready to state these clearly — they prevent scope creep:

- No production SLA or long-term support after handover
- No SIEM replacement or setup from scratch
- No from-scratch AI/LLM model training
- No fully autonomous remediation (human approval always required)
- No regulatory audit or formal compliance certification (NIS2, ISO, etc.)
- No complete infrastructure build if cloud/on-premise doesn't exist yet
- No long-term corrective maintenance post-transfer

> Frame it as: "These are not limitations — they're what keep the estimate honest. Extensions possible via avenant."

---

## Questions to Ask Them

1. **What SIEM/log tooling do you currently have?** (ELK, Splunk, Graylog, other?) — Critical for H6
2. **What incident types matter most?** (Intrusion, data exfiltration, lateral movement?) — Prioritizes Phase 4 agent design
3. **Who is the technical point of contact on your side?** — You need an internal security engineer for feedback loops
4. **Is there a deadline driving this?** — Affects H8 availability negotiation
5. **What's the budget envelope?** — 700h × your rate = the number. Are they aligned?
6. **Where will the solution run?** — On-premise (Geneva datacenter)? Cloud (which provider)? Both?
7. **Any compliance constraints?** — LPD (Swiss data protection), NIS2, cantonal IT policy?
8. **What does success look like in 6 months for your team?** — Anchors the conversation in their pain, not your deliverable

---

## Likely Objections & Responses

**"700 hours is a lot."**
→ "Phase 1 alone is 55h — we could start there and validate the approach before committing to the full roadmap. It's designed to be incremental."

**"Why isn't the remediation automatic?"**
→ "For a public institution, autonomous execution on production infrastructure is a liability question, not a technical one. Human validation is a feature — it keeps your team in control and gives you the audit trail compliance requires."

**"Can this integrate with our current SIEM?"**
→ "Yes, that's exactly what Phase 3 covers. I'd need to know which one — the integration approach differs significantly between ELK and Splunk."

**"What happens after the handover?"**
→ "The estimate ends with a full handover and 2–3 training sessions. Ongoing maintenance or evolution can be scoped as a separate engagement."

---

## What You Want to Leave With

- [ ] Confirmed: they have existing log infrastructure (or know they need Phase 0 first)
- [ ] Confirmed: budget range is aligned with the estimate
- [ ] Named: the internal technical contact for the project
- [ ] Agreed: next step (kick off Phase 1? Revise scope? Sign?)
- [ ] Flagged: any regulatory constraints that affect design

---

## Related

- [[Paul Quesnot]]
- [[North Star]]
