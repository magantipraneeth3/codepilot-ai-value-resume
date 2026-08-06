class ChatService:
    """Utility service for formatting chat messages and history."""

    @staticmethod
    def format_history(messages: list[dict[str, str]]) -> str:
        """Build a textual history from message payloads."""
        return "\n".join(f"{item['role']}: {item['content']}" for item in messages)
