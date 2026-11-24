# Track 2: Anomaly Triage Pipeline for Enterprise Workflow Automation

**Client Case:** Cybrdeck Workflow Systems | **Duration:** 4 Weeks (Two 2-Week Cycles)

## Cycle Gates
- **Cycle 1 (Weeks 1–2):** Ingest telemetry, profile normal operating bounds, implement baseline detectors (`src/detector.py`).
- **Cycle 2 (Weeks 3–4):** Implement severity scoring & deterministic routing (`src/router.py`), structured audit logs, and live demo.

## Synthetic Fixtures
- `data/synthetic/baseline_telemetry.csv` (1,000 normal operating records)
- `data/synthetic/fault_injected_stream.csv` (300 records with 45 seeded anomalies)
