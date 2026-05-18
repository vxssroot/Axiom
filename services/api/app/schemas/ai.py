from pydantic import BaseModel, Field
from typing import Optional, Literal

class AIRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)
    context: Optional[str] = None
    temperature: float = Field(0.2, ge=0.0, le=1.0)

class AIResponse(BaseModel):
    content: str
    provider: str
    fallback: bool
    request_id: Optional[str] = None

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    request_id: Optional[str] = None