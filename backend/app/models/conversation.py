from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.project import Project
    from app.models.prompt import Prompt
    from app.models.generated_code import GeneratedCode


class Conversation(Base):
    """A chat thread tied to a project."""

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    project: Mapped["Project"] = relationship(back_populates="conversations")
    prompts: Mapped[list["Prompt"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan",
    )
    generated_codes: Mapped[list["GeneratedCode"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan",
    )
