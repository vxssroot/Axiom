from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import logging
from .core.config import settings

app = FastAPI(title="Axiom API", version="0.1.0", debug=settings.DEBUG)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logging.info(f"{request.method} {request.url.path} - {response.status_code} - {process_time:.4f}s")
    return response

# Placeholder tenant middleware (non-production)
@app.middleware("http")
async def tenant_middleware(request: Request, call_next):
    # TODO: Implement real tenant resolution from JWT / workspace header
    request.state.tenant_id = "default"  # Placeholder only
    return await call_next(request)

# Health route
@app.get("/health")
async def health():
    return {"status": "healthy", "environment": settings.ENVIRONMENT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
