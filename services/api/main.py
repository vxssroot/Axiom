from fastapi import FastAPI
from app.routes.ai import router as ai_router

app = FastAPI(
    title="Axiom API",
    version="1.0.0",
    description="Backend API for Axiom AI Developer Assistant"
)

app.include_router(ai_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "axiom-api",
        "version": "1.0.0"
    }
