from fastapi import FastAPI

app = FastAPI(
    title="Axiom API",
    version="1.0.0",
    description="Backend API for Axiom AI Developer Assistant"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "axiom-api",
        "version": "1.0.0"
    }
