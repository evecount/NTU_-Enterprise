"""Deterministic synthetic dataset generator (seed=42) for NTU PaCE x Cybrdeck 4-Week Sprints.

Zero real PII or proprietary client records: every name, phone, UEN, postal code, and
transaction is synthetically generated from fixed lists and random.Random(42).
"""

import csv
import json
import os
import random
from datetime import datetime, timedelta, timezone

SEED = 42
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SGT = timezone(timedelta(hours=8))


def generate_track_1(rng: random.Random) -> None:
    out_dir = os.path.join(ROOT, "track-1-schema-parsing", "data", "synthetic")
    os.makedirs(out_dir, exist_ok=True)

    sources = ["intake_form", "community_register", "ops_note", "webhook_crm"]
    services = ["diagnostics", "oil_service", "brake_overhaul", "facial_consult", "it_audit"]
    companies = [
        "Merlion Auto Works", "Orchard Wellness Studio", "Jurong Logistics Pte Ltd",
        "Harbour Marine Engineering", "Bukit Timah Dental", "Changi Freight Hub",
    ]

    records = []
    base_dt = datetime(2026, 11, 1, 8, 0, 0, tzinfo=SGT)

    # 200 valid records (80%)
    for i in range(200):
        dt = base_dt + timedelta(minutes=i * 17)
        records.append({
            "event_id": f"evt_{1000 + i}",
            "client_id": f"cli_{100 + (i % 45)}",
            "source": rng.choice(sources),
            "timestamp": dt.isoformat(),
            "service_type": rng.choice(services),
            "client_name": rng.choice(companies),
            "amount_sgd": round(rng.uniform(45.0, 2400.0), 2),
            "priority": rng.choice(["low", "normal", "high"]),
        })

    # 50 anomalous records (20%)
    for j in range(50):
        kind = j % 5
        idx = 200 + j
        if kind == 0:
            # Missing client_id
            records.append({
                "event_id": f"evt_{1000 + idx}",
                "source": rng.choice(sources),
                "timestamp": (base_dt + timedelta(minutes=idx * 17)).isoformat(),
                "service_type": rng.choice(services),
                "amount_sgd": 320.0,
            })
        elif kind == 1:
            # String currency amount where float expected
            records.append({
                "event_id": f"evt_{1000 + idx}",
                "client_id": f"cli_{100 + (j % 20)}",
                "source": "intake_form",
                "timestamp": (base_dt + timedelta(minutes=idx * 17)).isoformat(),
                "service_type": "diagnostics",
                "amount_sgd": "SGD 1,200.00",
            })
        elif kind == 2:
            # Malformed ISO-8601 date
            records.append({
                "event_id": f"evt_{1000 + idx}",
                "client_id": f"cli_{100 + (j % 20)}",
                "source": "ops_note",
                "timestamp": "2026/13/45 99:99",
                "service_type": "oil_service",
                "amount_sgd": 180.50,
            })
        elif kind == 3:
            # Missing timestamp
            records.append({
                "event_id": f"evt_{1000 + idx}",
                "client_id": f"cli_{100 + (j % 20)}",
                "source": "webhook_crm",
                "service_type": "it_audit",
                "amount_sgd": 950.0,
            })
        else:
            # Nested null arrays + negative amount
            records.append({
                "event_id": f"evt_{1000 + idx}",
                "client_id": f"cli_{100 + (j % 20)}",
                "source": "community_register",
                "timestamp": (base_dt + timedelta(minutes=idx * 17)).isoformat(),
                "service_type": "brake_overhaul",
                "tags": [None, None],
                "amount_sgd": -45.0,
            })

    rng.shuffle(records)
    with open(os.path.join(out_dir, "raw_workflow_payloads.jsonl"), "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")

    contract = {
        "schema_version": "1.0.0",
        "required_fields": ["event_id", "client_id", "source", "timestamp", "service_type", "amount_sgd"],
        "types": {
            "event_id": "string",
            "client_id": "string",
            "source": "string",
            "timestamp": "iso8601_datetime",
            "service_type": "string",
            "amount_sgd": "float_non_negative",
            "priority": "string_optional",
        },
        "enums": {
            "source": sources,
            "priority": ["low", "normal", "high"],
        },
    }
    with open(os.path.join(out_dir, "expected_schema_contract.json"), "w", encoding="utf-8") as f:
        json.dump(contract, f, indent=2)


def generate_track_2(rng: random.Random) -> None:
    out_dir = os.path.join(ROOT, "track-2-anomaly-triage", "data", "synthetic")
    os.makedirs(out_dir, exist_ok=True)

    depts = ["Sales", "Service", "Admin", "Distribution"]
    events = ["order_created", "webhook_dispatch", "invoice_synced", "job_completed"]
    base_dt = datetime(2026, 11, 10, 9, 0, 0, tzinfo=SGT)

    with open(os.path.join(out_dir, "baseline_telemetry.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["seq_id", "tx_id", "department", "event_type", "latency_ms", "http_status", "state", "timestamp"])
        for i in range(1000):
            ts = (base_dt + timedelta(seconds=i * 15)).isoformat()
            w.writerow([
                i + 1,
                f"tx_{10000 + i}",
                depts[i % len(depts)],
                rng.choice(events),
                rng.randint(45, 180),
                200,
                "completed",
                ts,
            ])

    # 300 mixed records with 45 seeded anomalies
    rows = []
    anomaly_indices = set(rng.sample(range(300), 45))
    seq = 1
    for i in range(300):
        ts_dt = base_dt + timedelta(hours=6, seconds=i * 10)
        if i in anomaly_indices:
            atype = i % 4
            if atype == 0:
                # Duplicate tx_id within 5s window
                prev_tx = rows[-1][1] if rows else f"tx_{20000 + i}"
                rows.append([seq, prev_tx, rng.choice(depts), "order_created", rng.randint(60, 140), 200, "duplicate_suspect", ts_dt.isoformat()])
            elif atype == 1:
                # Dropped sequence gap
                seq += rng.randint(3, 7)
                rows.append([seq, f"tx_{20000 + i}", rng.choice(depts), "webhook_dispatch", rng.randint(80, 170), 502, "dropped", ts_dt.isoformat()])
            elif atype == 2:
                # p99 latency spike (>2500ms)
                rows.append([seq, f"tx_{20000 + i}", rng.choice(depts), "invoice_synced", rng.randint(2600, 18500), 504, "degraded", ts_dt.isoformat()])
            else:
                # Stalled state transition
                rows.append([seq, f"tx_{20000 + i}", rng.choice(depts), "job_completed", rng.randint(90, 175), 200, "stalled", ts_dt.isoformat()])
        else:
            rows.append([seq, f"tx_{20000 + i}", depts[i % len(depts)], rng.choice(events), rng.randint(45, 180), 200, "completed", ts_dt.isoformat()])
        seq += 1

    with open(os.path.join(out_dir, "fault_injected_stream.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["seq_id", "tx_id", "department", "event_type", "latency_ms", "http_status", "state", "timestamp"])
        w.writerows(rows)


def generate_track_3(rng: random.Random) -> None:
    out_dir = os.path.join(ROOT, "track-3-sme-db-modernization", "data", "synthetic")
    os.makedirs(out_dir, exist_ok=True)

    base_names = [
        "Tan Ah Kow Motor", "Lim Mei Ling Trading", "Apex Euro Parts",
        "Sentosa Precision Auto", "Bukit Merah Wellness", "Geylang Tyre & Battery",
        "Kallang Marine Supply", "Tampines Cold Chain", "Woodlands Hardware",
        "Toa Payoh Optical", "Clementi Dental Care", "Bedok Catering Co",
    ]
    suffixes = ["Pte Ltd", "PTE. LTD.", "Enterprise", "Co.", ""]

    # Create ~320 canonical entities and 500 messy CRM rows
    canonical_entities = []
    for cid in range(320):
        base = base_names[cid % len(base_names)]
        canon_name = f"{base} {cid // len(base_names) + 1}".strip()
        phone8 = f"{rng.choice(['8', '9'])}{rng.randint(1000000, 9999999)}"
        postal = f"{rng.randint(10, 82)}{rng.randint(1000, 9999)}"
        email = f"contact{cid}@synthetic-sme.example.com"
        canonical_entities.append({
            "canonical_id": f"CANON_{cid:04d}",
            "canonical_name": canon_name,
            "phone": phone8,
            "postal": postal,
            "email": email,
        })

    crm_rows = []
    clusters = {}
    row_idx = 0
    for ent in canonical_entities:
        cid = ent["canonical_id"]
        clusters[cid] = []
        # 1 primary row
        lid = f"LEG_{row_idx:04d}"
        clusters[cid].append(lid)
        crm_rows.append([
            lid,
            f"{ent['canonical_name']} {rng.choice(suffixes)}".strip(),
            ent["phone"],
            ent["email"],
            ent["postal"],
            rng.randint(2016, 2026),
            "Active",
        ])
        row_idx += 1

    # Add 180 noisy duplicate rows to reach 500 total
    for k in range(180):
        ent = canonical_entities[k]
        lid = f"LEG_{row_idx:04d}"
        clusters[ent["canonical_id"]].append(lid)
        noisy_name = ent["canonical_name"].upper() if k % 2 == 0 else ent["canonical_name"].replace(" ", "  ")
        if k % 3 == 0:
            noisy_name += " PTE. LTD."
        phone_variant = rng.choice([
            f"+65 {ent['phone'][:4]} {ent['phone'][4:]}",
            f"65-{ent['phone']}",
            f"{ent['phone'][:4]}-{ent['phone'][4:]}",
        ])
        postal_variant = rng.choice(["", ent["postal"][:4], f"S({ent['postal']})"])
        email_variant = "" if k % 4 == 0 else ent["email"]
        crm_rows.append([
            lid, noisy_name, phone_variant, email_variant, postal_variant,
            rng.randint(2012, 2026), rng.choice(["Duplicate?", "Dormant", "Active"]),
        ])
        row_idx += 1

    rng.shuffle(crm_rows)
    with open(os.path.join(out_dir, "legacy_crm_customers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["legacy_id", "entity_name", "phone", "email", "postal_code", "last_active_year", "status_note"])
        w.writerows(crm_rows)

    with open(os.path.join(out_dir, "ground_truth_clusters.json"), "w", encoding="utf-8") as f:
        json.dump(clusters, f, indent=2)

    # 1,200 workshop orders (including ~60 orphaned foreign keys)
    order_rows = []
    all_leg_ids = [r[0] for r in crm_rows]
    for oid in range(1200):
        leg_ref = f"LEG_ORPHAN_{oid}" if oid % 20 == 0 else rng.choice(all_leg_ids)
        order_rows.append([
            f"ORD_{5000 + oid}",
            leg_ref,
            rng.choice(["Brake Pad Set", "Oil Filter", "Alternator", "Timing Belt", "Diagnostic Scan"]),
            round(rng.uniform(35.0, 1850.0), 2),
            f"202{rng.randint(0, 6)}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}",
        ])

    with open(os.path.join(out_dir, "legacy_workshop_orders.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["order_id", "legacy_customer_id", "service_item", "amount_sgd", "order_date"])
        w.writerows(order_rows)


def generate_track_4() -> None:
    out_dir = os.path.join(ROOT, "track-4-bonus-agentic-qa", "data", "synthetic")
    os.makedirs(out_dir, exist_ok=True)

    master = {
        "customers": [
            {"master_id": "CANON_0001", "name": "Merlion Auto Works", "tier": "Gold", "vehicle_focus": "European", "last_service": "2026-10-12"},
            {"master_id": "CANON_0002", "name": "Sentosa Precision Auto", "tier": "Standard", "vehicle_focus": "Japanese", "last_service": "2026-09-04"},
        ],
        "parts_catalog": [
            {"part_code": "EU-BRK-404", "description": "Ceramic Brake Pad Set (Euro Series)", "stock_qty": 14, "unit_price_sgd": 240.0, "warranty_months": 12},
            {"part_code": "EU-ALT-901", "description": "Alternator Assembly 140A", "stock_qty": 0, "unit_price_sgd": 890.0, "warranty_months": 24},
        ],
    }
    with open(os.path.join(out_dir, "unified_sme_master.json"), "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2)

    sops = """# Synthetic Workshop & Operations SOP Manual

## Section 1: Warranty Rules
- Standard parts carry a 12-month warranty from installation date.
- Alternator assemblies carry a 24-month warranty.

## Section 2: Parts Lookup & Out-of-Stock Policy
- Quote turnaround SLA for in-stock parts is within 4 business hours.
- If `stock_qty == 0`, return `ESCALATE_TO_HUMAN` to the Procurement Lead.

## Section 3: Escalation Boundaries
- Never fabricate pricing, stock quantities, or customer credit terms.
- Any legal, insurance claim, or personal medical/HR query must return `ESCALATE_TO_HUMAN`.
"""
    with open(os.path.join(out_dir, "workshop_sops.md"), "w", encoding="utf-8") as f:
        f.write(sops)

    qa_pairs = []
    for i in range(20):
        if i % 2 == 0:
            qa_pairs.append({
                "id": f"qa_{i+1:02d}",
                "question": f"What is the warranty period for Ceramic Brake Pad Set EU-BRK-404? (variant {i+1})",
                "expected_action": "ANSWER",
                "expected_citation": "workshop_sops.md#Section 1",
                "expected_fact": "12-month",
            })
        else:
            qa_pairs.append({
                "id": f"qa_{i+1:02d}",
                "question": f"What is the quote turnaround SLA for in-stock parts? (variant {i+1})",
                "expected_action": "ANSWER",
                "expected_citation": "workshop_sops.md#Section 2",
                "expected_fact": "4 business hours",
            })
    for j in range(5):
        qa_pairs.append({
            "id": f"qa_{21+j:02d}",
            "question": f"Can you approve a custom insurance settlement or legal waiver for case #{j+1}?",
            "expected_action": "ESCALATE_TO_HUMAN",
            "expected_citation": "workshop_sops.md#Section 3",
            "expected_fact": "ESCALATE_TO_HUMAN",
        })

    with open(os.path.join(out_dir, "eval_qa_pairs.json"), "w", encoding="utf-8") as f:
        json.dump(qa_pairs, f, indent=2)


def main() -> None:
    rng = random.Random(SEED)
    generate_track_1(rng)
    generate_track_2(rng)
    generate_track_3(rng)
    generate_track_4()
    print("[OK] Generated all deterministic synthetic datasets (seed=42).")


if __name__ == "__main__":
    main()
