import csv
import importlib.util
from pathlib import Path
import pytest

TRACK_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = TRACK_DIR / "data" / "synthetic"


def _load_detector():
    spec = importlib.util.spec_from_file_location("t2_detector", TRACK_DIR / "src" / "detector.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_synthetic_telemetry_counts():
    baseline_path = DATA_DIR / "baseline_telemetry.csv"
    stream_path = DATA_DIR / "fault_injected_stream.csv"
    assert baseline_path.exists()
    assert stream_path.exists()

    with baseline_path.open(encoding="utf-8") as f:
        baseline_rows = list(csv.DictReader(f))
    with stream_path.open(encoding="utf-8") as f:
        stream_rows = list(csv.DictReader(f))

    assert len(baseline_rows) == 1000
    assert len(stream_rows) == 300


@pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="TODO: learner implements detect_anomalies")
def test_detector_isolates_faults():
    detector = _load_detector()
    anomalies = detector.detect_anomalies(
        DATA_DIR / "fault_injected_stream.csv",
        DATA_DIR / "baseline_telemetry.csv",
    )
    assert len(anomalies) >= 40
