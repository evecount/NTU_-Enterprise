import importlib.util
import json
from pathlib import Path
import pytest

TRACK_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = TRACK_DIR / "data" / "synthetic"


def _load_pipeline():
    spec = importlib.util.spec_from_file_location("t1_pipeline", TRACK_DIR / "src" / "pipeline.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_synthetic_fixtures_exist_and_match_counts():
    payloads_path = DATA_DIR / "raw_workflow_payloads.jsonl"
    contract_path = DATA_DIR / "expected_schema_contract.json"
    assert payloads_path.exists()
    assert contract_path.exists()

    lines = [ln for ln in payloads_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(lines) == 250

    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert "required_fields" in contract


@pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="TODO: learner implements parse_and_quarantine")
def test_pipeline_parses_and_quarantines():
    pipeline = _load_pipeline()
    valid, quarantine = pipeline.parse_and_quarantine(DATA_DIR / "raw_workflow_payloads.jsonl")
    assert len(valid) == 200
    assert len(quarantine) == 50
