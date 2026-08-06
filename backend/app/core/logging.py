import logging


def configure_logging() -> None:
    """Configure application logging for the API service."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
