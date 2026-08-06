from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GeneratedCodeResponse(BaseModel):
    """Schema for returning generated code payloads."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    language: str
    code: str
    explanation: str | None
    created_at: datetime
