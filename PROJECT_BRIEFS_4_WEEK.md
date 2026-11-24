# NTU PaCE × Cybrdeck — Applied Industry Project Briefs (4-Week Sprint Edition)

- **Programme Track:** SkillsFuture Career Transition Programme (SCTP) — Data Science & AI (Learner Sprints)
- **Industry Partner:** Cybrdeck Systems
- **Engagement Format:** 4-Week Applied Sprint (Two 2-Week Iterative Cycles)
- **Team Structure:** Squads of 2–3 Builders
- **Mentorship Cadence:** Weekly 90-minute technical standup / code review + asynchronous repository feedback
- **Lead Mentors:** Gwendalynn Lim (Tech Lead / Quantum Systems Architect), Benjamin Lim (Co-Founder)

---

## Brief 1: Schema Parsing Pipeline for Enterprise Workflow Automation

**Track:** Ingestion & Data Engineering | **Client Case:** Cybrdeck Workflow Systems

### 1. Executive Context & Problem Statement
Cybrdeck operates workflow automation across heterogeneous, semi-structured inputs—intake forms, community registers, operational notes, and system event logs. Upstream data frequently arrives with missing keys, inconsistent structural nesting, and type ambiguity. Before downstream automation or analytical services can trigger, this data must pass through an automated ingestion boundary that guarantees data integrity and quarantines anomalies without breaking system availability.

### 2. Core Functional Deliverables
Learners design and deploy an automated ingestion pipeline that:
- **Ingests Raw Workflow Payloads:** Parses multi-format, semi-structured operational records.
- **Enforces Invariant Data Contracts:** Validates structural schemas, field types, and required attributes.
- **Executes Dead-Letter Quarantine:** Automatically catches malformed, missing, or corrupted records, routing them to an isolated quarantine with explainable diagnostic logs.
- **Exposes Structured Data Endpoints:** Delivers normalized, queryable outputs consumable by downstream reporting and automation engines.

### 3. 4-Week Delivery Rhythm
- **Sprint 1 (Weeks 1–2) — Ingestion & Schema Contracts:** Establish baseline data contracts; implement automated parsing and validation logic; verify rejection handling for malformed test payloads.
- **Sprint 2 (Weeks 3–4) — Quarantine Routing, Service Packaging & Showcase:** Implement dead-letter triage and diagnostic logs; package the pipeline into an isolated, deployable service; write architecture documentation; deliver an end-to-end live technical demonstration.

### 4. Technical Governance & Standards
- **Environment & Stack:** Open-standard scripting language (e.g., Python), modern schema-validation libraries (e.g., Pydantic / JSON Schema), and version control.
- **Provided Scaffolding:** Synthetic enterprise workflow payloads (`brief-1-schema-parsing/data/sample_payloads.jsonl`) and reference delivery criteria.
- **Definition of Done:** A working codebase with automated test verification, documented schema validation rules, an isolated runtime packaging setup, and a live demonstration parsing raw input into validated, queryable structures.

---

## Brief 2: Anomaly Triage Pipeline for Enterprise Workflow Automation

**Track:** Operations & Decision Intelligence | **Client Case:** Cybrdeck Workflow Systems

### 1. Executive Context & Problem Statement
In live automated operations across disconnected departments (sales, service repair, telemarketing, admin, distribution), exceptions inevitably occur—duplicate transactions, dropped webhook events, out-of-range system latencies, and stalled operational sequences. Without automated triage, teams face severe alert fatigue. Cybrdeck requires an intelligent triage engine that monitors workflow telemetry, detects operational anomalies, evaluates severity, and routes incidents to appropriate resolution tiers.

### 2. Core Functional Deliverables
Learners design and deploy an operational triage engine that:
- **Monitors Telemetry Streams:** Ingests continuous event logs and transaction records from automated workflows.
- **Detects Deviations & Faults:** Applies statistical and heuristic detectors to identify operational anomalies against normal system baselines.
- **Automates Severity Scoring:** Prioritizes incidents using multi-factor scoring (business impact, frequency, operational risk).
- **Routes Triage Actions:** Categorizes incidents into deterministic outcomes (`Auto-Resolve`, `Human Review`, `Immediate Escalation`) with a clear audit trail.

### 3. 4-Week Delivery Rhythm
- **Sprint 1 (Weeks 1–2) — Baseline Modeling & Signal Extraction:** Ingest synthetic telemetry; analyze normal operating bounds; implement baseline rule-based and statistical anomaly detectors.
- **Sprint 2 (Weeks 3–4) — Triage Scoring, Service Packaging & Showcase:** Build severity-scoring algorithms and routing rules to filter false-positive noise; wrap triage logic into an isolated, deployable service with structured audit trails; deliver an end-to-end incident handling demonstration.

### 4. Technical Governance & Standards
- **Environment & Stack:** Open-standard numerical/statistical libraries, modern web service frameworks (e.g., FastAPI), and version control.
- **Provided Scaffolding:** Synthetic telemetry and transaction event logs with seeded fault scenarios (`brief-2-anomaly-triage/data/sample_telemetry.jsonl`).
- **Definition of Done:** A functional triage pipeline that reliably isolates seeded operational faults, outputs clear human-readable diagnostic reasons, runs in an isolated environment, and is verified through a live incident response demonstration.

---

## Brief 3: SME Legacy Database Modernization & Record Unification

**Track:** Data Engineering & Database Modernization | **Sector Case:** SME Digital Transformation

### 1. Executive Context & Problem Statement
Traditional small-to-medium enterprises (SMEs) frequently operate on legacy relational databases, exported accounting spreadsheets, paper/sticker inventory logs, and fragmented CRM archives accumulated over decades (e.g., 40-year-old Singaporean SMEs with 55,000+ client records). These stores suffer from severe data degradation: duplicate client profiles, dormant/deceased contacts, missing postal codes, unstandardized corporate entity names, and orphaned transaction logs. Before the enterprise can adopt modern CRM tools, automated outreach, or BI dashboards, the legacy store must be audited, deduplicated, and transformed into a unified customer master record.

### 2. Core Functional Deliverables
Learners design and implement a data modernization and deduplication pipeline that:
- **Ingests Multi-Source Legacy Extracts:** Ingests legacy relational dumps (CSV/SQL/tabular records) representing historical customer accounts and transactions.
- **Executes Fuzzy Matching & Deduplication:** Identifies and clusters duplicate customer records across conflicting spellings, variations in business registration numbers, and phone/email discrepancies.
- **Performs Address & Profile Normalization:** Standardizes localization formats (e.g., Singapore 6-digit postal codes, `+65` phone dialing codes, currency formatting).
- **Generates a Unified Customer Master Model:** Outputs clean, unified client entity tables with relationship links to past transaction histories, alongside an automated data-quality report quantifying deduplication gains.

### 3. 4-Week Delivery Rhythm
- **Sprint 1 (Weeks 1–2) — Ingestion, Profiling & Entity Resolution:** Load legacy tables; profile data completeness, null-rates, and schema anomalies; design the target unified client schema; prototype fuzzy matching and deterministic conflict-resolution rules (e.g., newest timestamp vs. most complete record).
- **Sprint 2 (Weeks 3–4) — Target Schema Migration & Quality Audit:** Migrate cleaned records into the unified relational structure; generate automated before-and-after audit logs and data-quality scorecard; deliver a technical walkthrough comparing legacy fragmentation against modern queryable records.

### 4. Technical Governance & Standards
- **Environment & Stack:** Open-standard relational database (SQL / SQLite / DuckDB / PostgreSQL) and Python data manipulation libraries, with version-controlled scripts.
- **Provided Scaffolding:** Fully synthetic, masked benchmark datasets exhibiting classic legacy data anomalies (`brief-3-legacy-db-unification/data/sample_legacy_clients.csv`). Zero proprietary or real PII is included in the public repo.
- **Definition of Done:** A functional migration and deduplication pipeline that successfully ingests legacy data, resolves conflicting client entities, outputs a clean unified relational database, and produces an auditable data-quality scorecard demonstrating measurable deduplication accuracy.

---

## Track 4 (Bonus Challenge): Agentic Q&A / Operations Assistant

**Track:** Applied GenAI & RAG | **Client Case:** Post-Cleanup SME Operations

### 1. Executive Context & Problem Statement
Once an SME's messy client records, inventory logs, or SOPs have been cleaned (Briefs 1–3), non-technical staff (e.g., front-desk receptionists or customer service reps) still need an instant way to query that knowledge without touching SQL or spreadsheets.

### 2. Core Functional Deliverables
- **Grounded Retrieval / Query Layer:** Connects safely to the cleaned structured database and SOP documents.
- **Human-in-the-Loop Assistant:** Answers staff queries (e.g., *"Look up client history or protocol for issue X"*) with citations, confidence/grounding checks, and zero fabricated records.
- **Evaluation Harness:** Basic test suite verifying factual accuracy and refusal on out-of-scope queries.

### 3. 4-Week Delivery Rhythm
- **Sprint 1 (Weeks 1–2):** Index cleaned sample records + SOP markdown; build baseline Q&A endpoint with strict citation/grounding prompts.
- **Sprint 2 (Weeks 3–4):** Add structured lookup tools, evaluation test cases, and a lightweight web/chat UI for live demo.
