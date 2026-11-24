# NTU PaCE × Cybrdeck Systems — Applied Industry Project Sprints (4-Week Track)

**Programme:** SkillsFuture Career Transition Programme (SCTP) — Data Science & AI (DSAI)  
**Industry Partner:** Cybrdeck Systems  
**Format:** 4-Week Applied Sprint (Two 2-Week Iterative Cycles)  
**Squad Size:** 2–3 Builders per Track  
**Mentorship:** Weekly 90-minute live technical standups & code reviews (Gwendalynn Lim & Benjamin Lim) + asynchronous repo feedback  

---

## Overview

This repository houses the starter briefs, synthetic sample datasets, and technical standards for the **NTU PaCE × Cybrdeck 4-Week Applied Industry Project Sprints**.

Instead of toy classroom exercises, squads tackle **real Singapore SME operational bottlenecks**—starting with the synthetic, masked datasets in this repo and unlocking full production/SME datasets upon formal squad opt-in.

---

## Project Tracks

| Track | Title | Focus | Starter Folder |
| :--- | :--- | :--- | :--- |
| **Brief 1** | **Schema Parsing Pipeline** | Multi-format ingestion, invariant data contracts, dead-letter quarantine, normalized outputs | [`brief-1-schema-parsing/`](./brief-1-schema-parsing/) |
| **Brief 2** | **Anomaly Triage Pipeline** | Telemetry stream monitoring, statistical/heuristic fault detection, severity scoring & routing | [`brief-2-anomaly-triage/`](./brief-2-anomaly-triage/) |
| **Brief 3** | **SME Legacy DB Modernization & Record Unification** | Multi-source legacy extracts, fuzzy entity resolution/deduplication, unified customer master model | [`brief-3-legacy-db-unification/`](./brief-3-legacy-db-unification/) |
| **Track 4 (Bonus)** | **Agentic Q&A / Operations Assistant** | Internal/customer-service RAG & protocol agent built over cleaned enterprise datasets | [`bonus-track-4-agentic-qa/`](./bonus-track-4-agentic-qa/) |

Full specifications, deliverables, and 4-week sprint milestones are in [`PROJECT_BRIEFS_4_WEEK.md`](./PROJECT_BRIEFS_4_WEEK.md).

---

## 4-Week Sprint Cadence

- **Sprint 1 (Weeks 1–2) — Foundation, Ingestion & Baseline Logic:**  
  Establish data contracts / unified schema, build core ingestion & baseline parsing/detection/profiling pipelines, and verify against synthetic test cases.
- **Sprint 2 (Weeks 3–4) — Resiliency, Service Encapsulation & Live Showcase:**  
  Implement dead-letter quarantine / severity routing / entity resolution & audit scorecards, package as an isolated deployable service/pipeline, and deliver an end-to-end live technical demo.

---

## Getting Started

1. **Join the NTU DSAI Alumni Builders Discord channel** (link shared in your cohort briefing email).
2. **Fork or branch** this repository for your squad.
3. **Explore the synthetic datasets** in your chosen track's `data/` folder before the live briefing session.
4. **Opt in** within 3 days post-briefing to lock your squad and unlock the full project dataset.
