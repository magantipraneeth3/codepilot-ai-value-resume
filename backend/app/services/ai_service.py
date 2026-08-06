class AIService:
    """A lightweight AI service interface for chat and code generation."""

    @staticmethod
    def generate_response(message: str) -> str:
        """Return a deterministic assistive response for the provided prompt."""
        return f"Assistant response to: {message}"

    @staticmethod
    def generate_code(prompt: str) -> str:
        """Return a simple code stub based on the prompt."""
        return f"# Generated from prompt: {prompt}\nprint('Hello from CodePilot AI')"
