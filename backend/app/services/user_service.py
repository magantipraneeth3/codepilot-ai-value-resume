class UserService:
    """Service helpers for user-facing operations."""

    @staticmethod
    def profile_label(username: str) -> str:
        """Build a display label for a username."""
        return f"User:{username}"
