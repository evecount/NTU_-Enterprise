"""Starter statistical/heuristic anomaly detector skeleton for Track 2."""

from pathlib import Path
from typing import Any


def detect_anomalies(stream_csv: Path, baseline_csv: Path) -> list[dict[str, Any]]:
    """TODO (Cycle 1): Detect duplicate tx_ids, sequence gaps, p99 latency spikes, and stalled states."""
    raise NotImplementedError("TODO: Implement detect_anomalies in Cycle 1")
