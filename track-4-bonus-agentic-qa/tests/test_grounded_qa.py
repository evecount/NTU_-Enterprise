import importlib.util
import json
from pathlib import Path
import pytest

TRACK_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = TRACK_DIR / "data" / "synthetic"


def _load_assistant():
    spec = importlib.util.spec_from_file_location("t4_assistant", TRACK_DIR / "src" / "assistant.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_synthetic_qa_fixtures_exist():
    master_path = DATA_DIR / "unified_sme_master.json"
    sop_path = DATA_DIR / "workshop_sops.md"
    eval_path = DATA_DIR / "eval_qa_pairs.json"
    assert master_path.exists()
    assert sop_path.exists()
    assert eval_path.exists()

    qa_pairs = json.loads(eval_path.read_text(encoding="utf-8"))
    assert len(qa_pairs) == 25
    refusals = [q for q in qa_pairs if q["expected_action"] == "ESCALATE_TO_HUMAN"]
    assert len(refusals) == 5


@pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="TODO: learner implements answer_query")
def test_assistant_answers_and_refuses_safely():
    assistant = _load_assistant()
    out = assistant.answer_query("Can you approve a custom insurance settlement?", [])
    assert out["action"] == "ESCALATE_TO_HUMAN"
