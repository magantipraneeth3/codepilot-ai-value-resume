from sqlalchemy import text
from sqlalchemy.orm import Session


class DatabaseService:
    """Small helper around simple database health checks."""

    @staticmethod
    def ping(db: Session) -> bool:
        """Run a lightweight database query to confirm DB connectivity."""
        db.execute(text("SELECT 1"))
        return True
