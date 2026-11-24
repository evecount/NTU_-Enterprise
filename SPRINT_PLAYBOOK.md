# 4-Week Sprint Playbook & Submission Guide

Welcome to the **NTU PaCE × Cybrdeck Systems Applied Industry Project Sprints**.  
Use this checklist to stay aligned across the 4-week sprint (~8 hours/week per learner, 2–3 builders per squad).

---

## Weekly Rhythm

### Cycle 1 (Weeks 1–2) — Exploration, Contracts & Baseline Logic
- **Week 1:**
  - Fork/branch `evecount/NTU_-Enterprise` and pick your track (`track-1` through `track-4`).
  - Open `notebooks/01_explore.ipynb` in your track to inspect the synthetic dataset (`data/synthetic/`).
  - Profile edge cases, missing fields, or baseline distributions.
- **Week 2:**
  - Implement Cycle 1 core functions in `src/` (schema contracts, baseline anomaly detector, SG normalizer, or retriever).
  - Run `python -m pytest -v` locally and remove the `@pytest.mark.xfail` marker on the tests you've implemented.
  - Open a **Cycle 1 Draft PR** before your weekly 90-minute standup.

### Cycle 2 (Weeks 3–4) — Resiliency, Auditability & Live Demo
- **Week 3:**
  - Implement Cycle 2 logic (dead-letter quarantine + diagnostics, severity scoring + routing matrix, fuzzy deduplication + quality scorecard, or grounded citations + `ESCALATE_TO_HUMAN`).
  - Add unit tests for edge cases in `tests/`.
- **Week 4:**
  - Package a clean CLI or lightweight API/UI entrypoint and update your track's `README.md` with run instructions.
  - Verify `python -m pytest -v` passes 100% with **zero real PII** committed.
  - Deliver your end-to-end live technical demo!

---

## Local Setup & Verification

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate  |  macOS/Linux: source .venv/bin/activate
pip install -e .
python -m pytest -v
```
