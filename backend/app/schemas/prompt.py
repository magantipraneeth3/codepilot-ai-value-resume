from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PromptRequest(BaseModel):
    """Schema for creating a prompt entry."""

    content: str


class PromptResponse(BaseModel):
    """Schema for returning a prompt entry."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    content: str
    created_at: datetime
