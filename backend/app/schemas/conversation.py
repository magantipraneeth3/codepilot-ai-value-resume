from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ConversationCreate(BaseModel):
    """Schema for creating a conversation."""

    title: str = Field(..., min_length=1, max_length=100)


class ConversationResponse(BaseModel):
    """Schema for returning conversation data."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    project_id: int
    created_at: datetime
    updated_at: datetime
