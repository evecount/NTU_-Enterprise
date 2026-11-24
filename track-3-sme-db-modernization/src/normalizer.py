"""Starter SG postal code, +65 phone & entity name standardization for Track 3."""

import re


def normalize_sg_phone(raw_phone: str) -> str:
    """TODO (Cycle 1): Normalize Singapore phone variants into canonical +65XXXXXXXX."""
    digits = re.sub(r"\D", "", raw_phone or "")
    if digits.startswith("65") and len(digits) == 10:
        return f"+{digits}"
    if len(digits) == 8:
        return f"+65{digits}"
    return ""


def normalize_sg_postal(raw_postal: str) -> str:
    """TODO (Cycle 1): Extract valid 6-digit Singapore postal code or return empty string."""
    raise NotImplementedError("TODO: Implement normalize_sg_postal in Cycle 1")
