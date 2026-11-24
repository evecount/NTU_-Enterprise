# **NTU PaCE x Cybrdeck Systems — Applied Industry Project Briefs (4-Week Sprint Track) Proposal** 

DRAFT 13 November 2026 

## **Programme Overview & Administration Metadata**

| Metadata Dimension | Detail Specification |
| :---- | :---- |
| **Programme Track** | SkillsFuture Career Transition Programme (SCTP) — Data Science & AI (3 Core Tracks \+ 1 Optional/Bonus Track) |
| **Industry Partner** | Cybrdeck Systems |
| **Engagement Format** | 4-Week Applied Sprint (Two 2-Week Iterative Cycles) |
| **Target Virtual Briefing Window** | 1–3 December 2026 |
| **Starter Repository Hub** | [https\://github.com/evecount/NTU\_-Enterprise](https://github.com/evecount/NTU_-Enterprise) |
| **Team Structure** | Recommended Squads of 2–3 Builders |
| **Learner Commitment** | \~8 hours/week per learner (\~65 total man-hours per 2-person squad):• 1.5 hours/week — Live weekly technical standup & code review• 5.0 hours/week — Asynchronous engineering & implementation• 1.5 hours/week — Asynchronous PR review, feedback, & documentation |
| **Mentor Commitment** | Capped at \~3–4 hours/week total across the cohort (shared across Gwendalynn Lim & Benjamin Lim)—covering the weekly 1.5-hour live cohort standup/code review plus asynchronous GitHub PR reviews (not 8 hours per learner) |
| **Lead Mentors** | Gwendalynn Lim (Tech Lead / Quantum Systems Architect), Benjamin Lim (Co-Founder) |

# **Brief 1: Schema Parsing Pipeline for Enterprise Workflow Automation**

**Track:** Ingestion & Data Engineering  
**Client Case:** Cybrdeck Workflow Systems

# **1\. Executive Context & Problem Statement**

Cybrdeck operates workflow automation across heterogeneous, semi-structured inputs—intake forms, community registers, operational notes, and system event logs. Upstream data frequently arrives with missing keys, inconsistent structural nesting, and type ambiguity. Before downstream automation or analytical services can trigger, this data must pass through an automated ingestion boundary that enforces data integrity and quarantines malformed inputs without breaking system availability.

# **2\. Core Functional Deliverables (4-Week MVP Scope)**

Learners design and implement a core ingestion and validation pipeline that:

* **Ingests Raw Workflow Payloads:** Parses multi-format, semi-structured operational records.  
* **Enforces Invariant Data Contracts:** Validates structural schemas, field types, and required attributes.  
* **Executes Dead-Letter Quarantine:** Automatically catches malformed, missing, or corrupted records, routing them to an isolated quarantine store with explainable diagnostic logs.  
* **Outputs Normalized Records:** Exposes clean, structured outputs ready for downstream consumption.

# **3\. Bi-Weekly Delivery Rhythm**

* **Cycle 1 (Weeks 1–2) — Ingestion & Schema Contracts:** Establish baseline data contracts; implement automated parsing and type-validation logic; verify rejection handling against malformed test payloads.  
* **Cycle 2 (Weeks 3–4) — Quarantine Routing, Hardening & Demo:** Implement dead-letter quarantine routing and diagnostic logging; complete edge-case test coverage and README documentation; deliver a live end-to-end technical demonstration.

# **4\. Technical Governance & Definition of Done**

* **Environment & Stack:** Open-standard scripting language, modern schema-validation libraries, and production-grade version control (tooling aligned with learner competency).  
* **Provided Scaffolding:** Synthetic enterprise workflow datasets, schema test cases, and reference delivery criteria.  
* **Definition of Done:** A working, version-controlled codebase with automated validation tests, documented schema rules, clean quarantine error logs, and a live demonstration parsing raw input into validated structures.

# **Brief 2: Anomaly Triage Pipeline for Enterprise Workflow Automation**

**Track:** Operations & Decision Intelligence  
**Client Case:** Cybrdeck Workflow Systems

# **1\. Executive Context & Problem Statement**

In live automated operations, exceptions inevitably occur—duplicate transactions, dropped webhook events, out-of-range system latencies, and stalled operational sequences. Without automated triage, operators face severe alert fatigue. Cybrdeck requires a core triage engine that monitors workflow telemetry, detects operational deviations, evaluates severity, and routes incidents into deterministic resolution tiers.

# **2\. Core Functional Deliverables (4-Week MVP Scope)**

Learners design and implement an operational triage engine that:

* **Monitors Telemetry Streams:** Ingests batch or streaming event logs and transaction records from automated workflows.  
* **Detects Deviations & Faults:** Applies statistical and heuristic detectors to identify operational anomalies against normal system baselines.  
* **Automates Severity Scoring:** Prioritizes incidents using multi-factor scoring (operational impact, frequency, risk).  
* **Routes Triage Actions:** Categorizes incidents into deterministic outcomes (Auto-Resolve, Human Review, Immediate Escalation) with a clear audit trail.

# **3\. Bi-Weekly Delivery Rhythm**

* **Cycle 1 (Weeks 1–2) — Baseline Modeling & Signal Extraction:** Ingest synthetic telemetry; profile normal operating bounds; implement baseline rule-based and statistical anomaly detectors.  
* **Cycle 2 (Weeks 3–4) — Triage Scoring, Routing & Demo:** Build severity-scoring logic and routing rules to filter false-positive noise; generate structured incident audit logs; deliver a live end-to-end incident handling demonstration.

# **4\. Technical Governance & Definition of Done**

* **Environment & Stack:** Open-standard numerical/statistical libraries, lightweight service/CLI interfaces, and production-grade version control (tooling aligned with learner competency).  
* **Provided Scaffolding:** Synthetic telemetry and transaction event logs with seeded fault scenarios, plus reference architectural rubrics.  
* **Definition of Done:** A functional triage pipeline that reliably isolates seeded operational faults, outputs clear human-readable diagnostic reasons, passes automated verification tests, and is demonstrated live.

# **Brief 3: SME Legacy Database Modernization & Record Unification**

**Track:** Data Engineering & Database Modernization  
**Sector Case:** SME Digital Transformation

# **1\. Executive Context & Problem Statement**

Traditional small-to-medium enterprises (SMEs) frequently operate on legacy relational databases, exported accounting spreadsheets, and fragmented CRM archives accumulated over decades. These stores suffer from severe data degradation: duplicate client profiles, missing postal codes, unstandardized corporate entity names, and orphaned transaction logs. Before an enterprise can adopt modern CRM tools or business intelligence reporting, the legacy records must be audited, deduplicated, and consolidated into a unified customer master table.

# **2\. Core Functional Deliverables (4-Week MVP Scope)**

Learners design and implement a data modernization and entity-resolution pipeline that:

* **Ingests Multi-Source Legacy Extracts:** Ingests legacy relational dumps (CSV/SQL/tabular records) representing historical customer accounts and transactions.  
* **Executes Fuzzy Matching & Deduplication:** Identifies and clusters duplicate customer records across conflicting spellings, registration variations, and phone/email discrepancies.  
* **Performs Address & Profile Normalization:** Standardizes localization formats (e.g., postal codes, regional phone dialing prefixes, currency formatting).  
* **Generates a Unified Customer Master Model:** Outputs clean, unified client entity tables linked to historical transactions, alongside an automated data-quality scorecard quantifying deduplication gains.

# **3\. Bi-Weekly Delivery Rhythm**

* **Cycle 1 (Weeks 1–2) — Ingestion, Profiling & Target Schema:** Load legacy database extracts; profile completeness, null-rates, and schema anomalies; design the target unified client schema.  
* **Cycle 2 (Weeks 3–4) — Entity Resolution, Migration & Demo:** Implement rule-based and fuzzy matching deduplication logic; migrate cleaned records into the unified relational model; generate before-and-after quality audit logs and deliver a live walkthrough.

# **4\. Technical Governance & Definition of Done**

* **Environment & Stack:** Open-standard relational database (SQL) and scripting language, modern data manipulation libraries, and version-controlled scripts (tooling aligned with learner competency).  
* **Provided Scaffolding:** Fully synthetic, masked benchmark datasets exhibiting classic legacy data anomalies (duplicate entities, inconsistent schema keys, unnormalized fields). Zero proprietary or personally identifiable information (PII) is utilized.  
* **Definition of Done:** A functional migration and deduplication pipeline that resolves conflicting client entities, outputs a clean unified relational store, and produces an auditable data-quality report demonstrating measurable deduplication accuracy.

# **Brief 4 (Optional / Bonus Challenge): Agentic Enterprise Q\&A & Workflow Assistant**

**Track:** Applied AI & Agentic Orchestration (Bonus Extension / Track 4\)  
**Client Case:** Cybrdeck & SME Operations

# **1\. Executive Context & Problem Statement**

Once raw operational records, telemetry logs, and legacy client databases have been cleaned and unified (via Briefs 1–3), frontline staff—such as customer service receptionists, workshop coordinators, and account managers—still face high friction looking up client histories, inventory status, or standard operating protocols during live inquiries. Rather than replacing frontline staff, organizations need a grounded, hallucination-safe AI assistant that queries unified records and SOPs to give staff immediate, verifiable answers.

# **2\. Core Functional Deliverables (4-Week MVP / Bonus Scope)**

Learners design and implement a grounded Q\&A and workflow assistant (either as a standalone Track 4 build or as a bonus extension atop Briefs 1–3) that:

* **Indexes Clean Enterprise Knowledge:** Ingests normalized client records, inventory catalogs, and SOP documents into a structured retrieval index.  
* **Executes Grounded Retrieval & Tool Lookup:** Answers frontline staff queries (e.g., customer history lookup, part availability, resolution protocol) with explicit source citations and zero hallucinated records.  
* **Enforces Safe Escalation Boundaries:** Detects out-of-scope or ambiguous queries and routes them cleanly to human escalation rather than guessing.  
* **Exposes a Lightweight Frontline Interface:** Provides a clean chat/CLI or web UI suitable for rapid frontline lookup.

# **3\. Bi-Weekly Delivery Rhythm**

* **Cycle 1 (Weeks 1–2) — Knowledge Ingestion & Retrieval Baseline:** Ingest normalized SME datasets and SOP fixtures; implement deterministic search/RAG indexing and baseline query answering.  
* **Cycle 2 (Weeks 3–4) — Guardrails, Citation Verification & Demo:** Add citation grounding, refusal/escalation rules for missing data, automated evaluation tests, and deliver a live frontline Q\&A walkthrough.

# **4\. Technical Governance & Definition of Done**

* **Environment & Stack:** Open-standard scripting language, retrieval/orchestration libraries, and version-controlled scripts (tooling aligned with learner competency).  
* **Provided Scaffolding:** Synthetic unified SME client tables, mock SOP documents, evaluation Q\&A test pairs, and starter templates at [https\://github.com/evecount/NTU\_-Enterprise](https://github.com/evecount/NTU_-Enterprise).  
* **Definition of Done:** A working, grounded Q\&A assistant that accurately retrieves client/operational facts with citations, safely refuses unanswerable queries, passes automated evaluation checks, and is demonstrated live.

