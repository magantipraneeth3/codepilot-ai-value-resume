from typing import Generator
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings

# SQLAlchemy engine configured from the environment database URL.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Session factory used by FastAPI dependency injection.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models.
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Provide a database session for each request and close it afterward."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Depends(get_db)
