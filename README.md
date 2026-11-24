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

Full specifications are in [`NTU PaCE x Cybrdeck - Applied Industry Project Briefs (4-Week Sprint Track).md`](./NTU%20PaCE%20x%20Cybrdeck%20-%20Applied%20Industry%20Project%20Briefs%20(4-Week%20Sprint%20Track).md) and [`SPRINT_PLAYBOOK.md`](./SPRINT_PLAYBOOK.md).

---

## How to Fork & Submit Your Squad's Work

1. **Fork this repository**
   - Click **Fork** in the top-right corner of [`evecount/NTU_-Enterprise`](https://github.com/evecount/NTU_-Enterprise) to create your squad's copy under your GitHub account.
2. **Clone your fork locally**
   ```bash
   git clone https://github.com/<your-username>/NTU_-Enterprise.git
   cd NTU_-Enterprise
   git remote add upstream https://github.com/evecount/NTU_-Enterprise.git
   ```
3. **Create a branch for your track**
   ```bash
   git checkout -b squad/<track-number>-<your-team-name>
   ```
4. **Set up Python & run the smoke tests**
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate  |  macOS/Linux: source .venv/bin/activate
   pip install -e .
   python -m pytest -v
   ```
5. **Explore & build**
   - Open `track-<n>-.../notebooks/01_explore.ipynb` to inspect the synthetic dataset, then implement your solution in `src/` and update `tests/`.
   - Follow [`SPRINT_PLAYBOOK.md`](./SPRINT_PLAYBOOK.md) for Cycle 1 (Weeks 1–2) and Cycle 2 (Weeks 3–4) gates.
6. **Commit, push, and open a Pull Request**
   ```bash
   git add -A
   git commit -m "Cycle 1: <your squad summary>"
   git push -u origin squad/<track-number>-<your-team-name>
   ```
   - On GitHub, click **Compare & pull request** targeting `evecount/NTU_-Enterprise:main` and fill out the PR checklist.

> **Zero Real PII:** All fixtures in `*/data/synthetic/` are 100% synthetically generated (`seed=42`). Never commit real customer records, phone numbers, or API keys. Full SME datasets are unlocked only after squad opt-in.
