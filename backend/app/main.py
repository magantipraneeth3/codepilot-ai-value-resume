from fastapi import FastAPI

from app.api.ai import router as ai_router
from app.api.auth import router as auth_router
from app.api.projects import router as project_router
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="CodePilot AI API",
    version="1.0.0",
    description="Backend foundation for the CodePilot AI assistant.",
)

register_exception_handlers(app)

# Include the authentication and domain routes.
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(ai_router)


@app.get("/", tags=["health"])
def root() -> dict[str, str]:
    """Simple health endpoint for the backend service."""
    return {"message": "CodePilot AI Backend Running"}
