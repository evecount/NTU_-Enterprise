import csv
import importlib.util
import json
from pathlib import Path
import pytest

TRACK_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = TRACK_DIR / "data" / "synthetic"


def _load_mod(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, TRACK_DIR / "src" / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_synthetic_legacy_db_counts():
    crm_path = DATA_DIR / "legacy_crm_customers.csv"
    orders_path = DATA_DIR / "legacy_workshop_orders.csv"
    clusters_path = DATA_DIR / "ground_truth_clusters.json"
    assert crm_path.exists()
    assert orders_path.exists()
    assert clusters_path.exists()

    with crm_path.open(encoding="utf-8") as f:
        crm_rows = list(csv.DictReader(f))
    with orders_path.open(encoding="utf-8") as f:
        order_rows = list(csv.DictReader(f))
    clusters = json.loads(clusters_path.read_text(encoding="utf-8"))

    assert len(crm_rows) == 500
    assert len(order_rows) == 1200
    assert len(clusters) == 320


def test_phone_normalizer_starter():
    norm = _load_mod("t3_norm", "normalizer.py")
    assert norm.normalize_sg_phone("+65 9123 4567") == "+6591234567"
    assert norm.normalize_sg_phone("8234-5678") == "+6582345678"


@pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="TODO: learner implements deduplicate_customers")
def test_deduplicator_clusters_entities():
    dedup = _load_mod("t3_dedup", "deduplicator.py")
    result = dedup.deduplicate_customers(DATA_DIR / "legacy_crm_customers.csv")
    assert "master_records" in result
