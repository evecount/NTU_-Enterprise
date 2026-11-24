# NTU PaCE × Cybrdeck Systems — Applied Industry Project Sprints (4-Week Track)

**Programme:** SkillsFuture Career Transition Programme (SCTP) — Data Science & AI (DSAI)  
**Industry Partner:** Cybrdeck Systems  
**Format:** 4-Week Applied Sprint (Two 2-Week Iterative Cycles, ~8 hrs/week per learner)  
**Squad Size:** 2–3 Builders per Track  
**Mentorship:** Weekly 90-minute live technical standups & code reviews (Gwendalynn Lim & Benjamin Lim) + async PR feedback  

---

## Project Tracks

| Track | Title | Focus | Starter Folder |
| :--- | :--- | :--- | :--- |
| **Track 1 (Brief 1)** | **Schema Parsing Pipeline** | Semi-structured ingestion, invariant data contracts, dead-letter quarantine | [`track-1-schema-parsing/`](./track-1-schema-parsing/) |
| **Track 2 (Brief 2)** | **Anomaly Triage Pipeline** | Telemetry monitoring, duplicate/latency/stall detection, severity scoring & routing | [`track-2-anomaly-triage/`](./track-2-anomaly-triage/) |
| **Track 3 (Brief 3)** | **SME Legacy DB Modernization** | Multi-source legacy extracts, fuzzy entity resolution, unified customer master & scorecard | [`track-3-sme-db-modernization/`](./track-3-sme-db-modernization/) |
| **Track 4 (Bonus)** | **Agentic Enterprise Q&A** | Grounded RAG/lookup assistant over cleaned SME datasets with human escalation | [`track-4-bonus-agentic-qa/`](./track-4-bonus-agentic-qa/) |

Full specifications are in [`NTU PaCE x Cybrdeck - Applied Industry Project Briefs (4-Week Sprint Track).md`](./NTU%20PaCE%20x%20Cybrdeck%20-%20Applied%20Industry%20Project%20Briefs%20(4-Week%20Sprint%20Track).md) and [`PROJECT_BRIEFS_4_WEEK.md`](./PROJECT_BRIEFS_4_WEEK.md).

---

## Quick Start

```bash
python -m venv .venv
pip install -e .
pytest -v
```

> **Zero Real PII:** All fixtures in `*/data/synthetic/` are 100% synthetically generated (`seed=42`). Full SME datasets are unlocked only after squad opt-in.
