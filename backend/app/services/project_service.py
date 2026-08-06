class ProjectService:
    """Service helpers for project-oriented business logic."""

    @staticmethod
    def summarize(project_name: str, description: str | None) -> str:
        """Build a simple summary of a project."""
        return f"Project {project_name}: {description or 'No description provided'}"
