"""Starter ingestion, validation & dead-letter quarantine skeleton for Track 1."""

from pathlib import Path
from typing import Any


def parse_and_quarantine(input_jsonl: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """TODO (Cycle 1-2): Parse JSONL records, validate against WorkflowPayload,
    and return (valid_records, quarantined_records_with_reasons)."""
    raise NotImplementedError("TODO: Implement parse_and_quarantine in Cycle 1")
