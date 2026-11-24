"""Starter schema contract definitions for Track 1."""

from pydantic import BaseModel, Field


class WorkflowPayload(BaseModel):
    event_id: str
    client_id: str
    source: str
    timestamp: str
    service_type: str
    amount_sgd: float = Field(ge=0.0)
    priority: str = "normal"
