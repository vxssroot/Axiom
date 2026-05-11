from fastapi import APIRouter
from app.schemas.ai import ExplainCodeRequest, ExplainCodeResponse

router = APIRouter()


@router.post("/api/v1/ai/explain", response_model=ExplainCodeResponse)
def explain_code(payload: ExplainCodeRequest):
    return ExplainCodeResponse(
        summary="Code explanation placeholder",
        explanation="This endpoint will process code explanation requests.",
        important_logic="The backend receives code input and prepares structured AI responses.",
        possible_issues="AI model integration is not connected yet.",
        suggested_improvements="Connect LangGraph workflow and model provider next."
    )
