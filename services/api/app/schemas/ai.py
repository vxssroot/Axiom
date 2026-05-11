from pydantic import BaseModel
from typing import Optional


class ExplainCodeRequest(BaseModel):
    code: str
    language: str
    user_prompt: Optional[str] = None


class ExplainCodeResponse(BaseModel):
    summary: str
    explanation: str
    important_logic: str
    possible_issues: str
    suggested_improvements: str
