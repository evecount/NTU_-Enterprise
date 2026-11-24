# Track 3: SME Legacy Database Modernization & Record Unification

**Sector Case:** SME Digital Transformation | **Duration:** 4 Weeks (Two 2-Week Cycles)

## Cycle Gates
- **Cycle 1 (Weeks 1–2):** Load & profile legacy CRM/order tables, standardize SG postal codes & `+65` phones (`src/normalizer.py`), design unified schema.
- **Cycle 2 (Weeks 3–4):** Implement fuzzy entity resolution (`src/deduplicator.py`), migrate to unified SQL model, output data-quality scorecard.

## Synthetic Fixtures
- `data/synthetic/legacy_crm_customers.csv` (500 messy SME client profiles)
- `data/synthetic/legacy_workshop_orders.csv` (1,200 historical orders with orphaned FKs)
- `data/synthetic/ground_truth_clusters.json` (canonical entity cluster key map)
