# Track 4 (Bonus): Agentic Enterprise Q&A & Workflow Assistant

**Client Case:** Cybrdeck & SME Operations | **Duration:** 4 Weeks (Two 2-Week Cycles)

## Cycle Gates
- **Cycle 1 (Weeks 1–2):** Index `unified_sme_master.json` & `workshop_sops.md`, build deterministic/hybrid retriever (`src/retriever.py`).
- **Cycle 2 (Weeks 3–4):** Add citation grounding & `ESCALATE_TO_HUMAN` refusal guardrails (`src/assistant.py`), run `eval_qa_pairs.json` evals.

## Synthetic Fixtures
- `data/synthetic/unified_sme_master.json`
- `data/synthetic/workshop_sops.md`
- `data/synthetic/eval_qa_pairs.json` (25 QA pairs: 20 answerable + 5 out-of-scope refusals)
