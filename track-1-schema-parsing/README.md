# Track 1: Schema Parsing Pipeline for Enterprise Workflow Automation

**Client Case:** Cybrdeck Workflow Systems | **Duration:** 4 Weeks (Two 2-Week Cycles)

## Cycle Gates
- **Cycle 1 (Weeks 1–2):** Define schema contracts (`src/models.py`), implement ingestion & validation (`src/pipeline.py`), reject malformed payloads.
- **Cycle 2 (Weeks 3–4):** Implement dead-letter quarantine routing with diagnostic logs, edge-case tests, and live demo.

## Synthetic Fixtures
- `data/synthetic/raw_workflow_payloads.jsonl` (250 records: 80% valid, 20% seeded anomalies)
- `data/synthetic/expected_schema_contract.json`
