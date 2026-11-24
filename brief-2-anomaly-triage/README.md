# Brief 2: Anomaly Triage Pipeline for Enterprise Workflow Automation

**Track:** Operations & Decision Intelligence  
**Duration:** 4 Weeks (Two 2-Week Sprints)

## Objective
Build an operational triage engine that monitors workflow telemetry streams, detects anomalies (duplicate transactions, dropped webhooks, latency spikes, stalled sequences), scores incident severity, and routes actions (`Auto-Resolve`, `Human Review`, `Immediate Escalation`) with an audit trail.

## Starter Data
- `data/sample_telemetry.jsonl` — Synthetic multi-department workflow events with seeded duplicate transactions, latency spikes, and stalled workflows.

## Milestones
- **Weeks 1–2:** Ingest telemetry, establish baseline operating bounds, and implement rule-based + statistical anomaly detectors.
- **Weeks 3–4:** Build multi-factor severity scoring, deterministic routing matrix, deployable API/service, and live demo.
