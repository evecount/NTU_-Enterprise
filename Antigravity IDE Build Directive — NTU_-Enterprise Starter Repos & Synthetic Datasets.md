# **Antigravity IDE Build Directive — NTU\_-Enterprise Starter Repos & Synthetic Datasets**

**Technical Scaffolding & Synthetic Data Engineering Plan**

---

## **Execution Metadata**

| Parameter | Configuration Value |
| :---- | :---- |
| **Target Environment** | Antigravity IDE (Local Workstation) |
| **Target Repository** | [https\://github.com/evecount/NTU\_-Enterprise](https://github.com/evecount/NTU_-Enterprise) |
| **Branch / Tag** | `main` (`v1.0-seed`) |
| **Project Leads** | Gwen Lim & Benjamin Lim (Cybrdeck Systems) |
| **Target Completion** | Before Wednesday, 25 November 2026 (Morning SGT) |

---

# **1\. Objective & Architectural Guardrails**

Scaffold the turnkey starter repository structure and 100% synthetic sample datasets inside `https://github.com/evecount/NTU_-Enterprise` for the NTU PaCE x Cybrdeck 4-Week Applied Sprint Track (two 2-week iterative cycles, \~8 hrs/week per learner, 2–3 person squads).

## **Critical Engineering Guardrails**

* **Zero Real PII / Zero Proprietary Data:** Every fixture in `data/synthetic/` must be 100% synthetically generated using deterministic random seeds (`seed=42`). Never commit real Singapore SME customer records, phone numbers, NRICs, or proprietary Cybrdeck internal business logic.  
* **Tool-Agnostic & Python-First:** Provide clean Python 3.11+ scaffolding (`pyproject.toml` / `requirements.txt`, `pytest` smoke tests, and standard CLI entrypoints) while allowing squads to substitute libraries (e.g., Pydantic, Pandera, Great Expectations, DuckDB, SQLite, Polars, Pandas) as long as the automated acceptance tests pass.  
* **4-Week MVP Scope Discipline (2 Cycles):** Every track README and acceptance test suite must explicitly enforce the **4-week (two 2-week cycle) MVP boundary**—focusing on core parsing, anomaly triage, entity deduplication, and grounded Q\&A verification rather than heavy Kubernetes/microservice deployment overhead.

---

# **2\. Target Monorepo Directory Structure (`NTU_-Enterprise`)**

Generate and verify the following directory layout inside `https://github.com/evecount/NTU_-Enterprise`:

```
NTU_-Enterprise/
├── README.md                                  # Master cohort overview, 4-week cadence, PR workflow & rubric
├── pyproject.toml                             # Shared Python 3.11+ dependencies (pytest, pydantic, duckdb, rapidfuzz)
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md               # Cycle 1 & Cycle 2 self-check checklist for async PR reviews
│   └── workflows/
│       └── ci-smoke.yml                       # Automated pytest verification on every squad PR
│
├── track-1-schema-parsing/
│   ├── README.md                              # Brief 1 spec, Cycle 1 & Cycle 2 gates, Definition of Done
│   ├── data/
│   │   └── synthetic/
│   │       ├── raw_workflow_payloads.jsonl    # 250 mixed semi-structured intake, register & event records (~20% seeded faults)
│   │       └── expected_schema_contract.json  # Reference invariant schema rules & required field definitions
│   ├── src/
│   │   ├── __init__.py
│   │   ├── pipeline.py                        # Starter ingestion, validation & dead-letter quarantine skeleton
│   │   └── models.py                          # Starter schema contract definitions
│   └── tests/
│       └── test_schema_pipeline.py            # Smoke tests verifying valid normalization & quarantine error logs
│
├── track-2-anomaly-triage/
│   ├── README.md                              # Brief 2 spec, Cycle 1 & Cycle 2 gates, Definition of Done
│   ├── data/
│   │   └── synthetic/
│   │       ├── baseline_telemetry.csv         # 1,000 normal operating event & webhook latency records
│   │       └── fault_injected_stream.csv      # 300 mixed records with seeded duplicates, dropped webhooks & latency spikes
│   ├── src/
│   │   ├── __init__.py
│   │   ├── detector.py                        # Starter statistical/heuristic anomaly detector skeleton
│   │   └── router.py                          # Starter severity scoring & tier routing (Auto-Resolve / Review / Escalate)
│   └── tests/
│       └── test_triage_engine.py              # Smoke tests verifying fault isolation & audit trail output
│
├── track-3-sme-db-modernization/
│   ├── README.md                              # Brief 3 spec, Cycle 1 & Cycle 2 gates, Definition of Done
│   ├── data/
│   │   └── synthetic/
│   │       ├── legacy_crm_customers.csv       # 500 messy SME client profiles (fuzzy name typos, +65/65 phone variants, missing postal codes)
│   │       ├── legacy_workshop_orders.csv     # 1,200 historical service/parts transactions with orphaned & duplicate foreign keys
│   │       └── ground_truth_clusters.json     # Evaluation key mapping synthetic duplicates to canonical entity IDs
│   ├── src/
│   │   ├── __init__.py
│   │   ├── normalizer.py                      # Starter SG postal code, +65 phone & entity name standardization
│   │   └── deduplicator.py                    # Starter fuzzy matching, master table unification & quality scorecard
│   └── tests/
│       └── test_db_modernization.py           # Smoke tests verifying deduplication precision/recall & relational integrity
│
└── track-4-bonus-agentic-qa/
    ├── README.md                              # Optional Track 4 / Bonus Challenge spec (standalone or atop Tracks 1–3)
    ├── data/
    │   └── synthetic/
    │       ├── unified_sme_master.json        # Clean normalized SME customer & parts catalog fixture
    │       ├── workshop_sops.md               # Synthetic SOP manual (warranty rules, part lookup, escalation policy)
    │       └── eval_qa_pairs.json             # 25 grounded Q&A test pairs (including 5 unanswerable refusal test cases)
    ├── src/
    │   ├── __init__.py
    │   ├── retriever.py                       # Starter deterministic/hybrid retrieval & citation formatter
    │   └── assistant.py                       # Starter grounded Q&A loop with human-escalation guardrails
    └── tests/
        └── test_grounded_qa.py                # Smoke tests verifying citation accuracy & zero-hallucination refusals
```

---

# **3\. Synthetic Dataset Generation Specifications**

Instruct Antigravity IDE to run a deterministic generator script (`scripts/generate_synthetic_datasets.py`, `seed=42`) that populates all fixtures across Tracks 1–4 according to these specifications:

## **Track Breakdown & Dataset Constraints**

| Track | Dataset / File Name | Count | Structural Parameters & Synthetic Noise |
| :---- | :---- | :---- | :---- |
| **Track 1** | `raw_workflow_payloads.jsonl` | 250 records | **80% Valid:** Heterogeneous JSON simulating SME service intake, workshop job sheets, webhooks.**20% Anomalies (50 records):** Missing `client_id` or `timestamp`, string amounts where floats are expected (e.g., `"SGD 1,200.00"`), malformed ISO-8601 dates, nested null arrays. |
|  | `expected_schema_contract.json` | 1 contract | Invariant field definitions, strict type constraints, and valid enum ranges for pipeline assertion. |
| **Track 2** | `baseline_telemetry.csv` | 1,000 records | **Normal Operating Baseline:** Latency `45ms–180ms`, HTTP `200`, monotonic sequence IDs across 4 SME departments (Sales, Service, Admin, Distribution). |
|  | `fault_injected_stream.csv` | 300 records | **Fault Injected (45 anomalies):** Duplicate transaction IDs within 5s windows, dropped sequence gaps, p99 latency spikes (`>2,500ms`), stalled state transitions. |
| **Track 3** | `legacy_crm_customers.csv` | 500 records | **Singapore SME Noise Profile:** Duplicate corporate/individual entries (e.g., `"Tan Ah Kow Motor Pte Ltd"` vs `"TAN A.K. MOTOR PTE. LTD."`), inconsistent SG phone prefixes (`"91234567"`, `"+65 9123 4567"`, `"65-91234567"`), missing/truncated postal codes. |
|  | `legacy_workshop_orders.csv` | 1,200 records | Historical service & parts orders containing orphaned foreign keys and duplicate booking records. |
|  | `ground_truth_clusters.json` | Key map | Evaluation mapping synthetic fuzzy duplicate profiles to canonical entity IDs. |
| **Track 4** | `unified_sme_master.json` | 1 fixture | Normalized customer history and European automotive parts catalog. |
|  | `workshop_sops.md` | 1 document | Standard Operating Manual covering warranty terms, parts lookup logic, and human escalation rules. |
|  | `eval_qa_pairs.json` | 25 QA pairs | **20 Answerable:** Frontline queries requiring exact markdown source citations.**5 Unanswerable:** Out-of-scope/refusal queries that must return an explicit `ESCALATE_TO_HUMAN` action. |

---

# **4\. Antigravity Execution Sequence**

Execute the following sequential operations within Antigravity IDE to build, validate, and publish release tag `v1.0-seed`:

1. **Clone & Initialize Repository Structure**  
   Open `https://github.com/evecount/NTU_-Enterprise` in Antigravity IDE and create the directory tree, master `README.md`, `pyproject.toml`, and GitHub Actions workflow configuration.  
2. **Generate & Audit Synthetic Fixtures**  
   Execute `python scripts/generate_synthetic_datasets.py` with `seed=42`. Verify zero PII inclusion, valid formatting, and exact target record counts across all `data/synthetic/` directories.  
3. **Verify Baseline CI Smoke Tests**  
   Run `pytest -v` across all four track test suites (`test_schema_pipeline.py`, `test_triage_engine.py`, `test_db_modernization.py`, `test_grounded_qa.py`). Confirm starter stubs run cleanly and fail only on expected unimplemented `TODO` assertions designed for learner implementation.  
4. **Tag & Push `v1.0-seed`**  
   Commit all scaffolding, push to `main`, tag the repository with `v1.0-seed`, and confirm public read permissions so learner squads can immediately fork the starter repository.

