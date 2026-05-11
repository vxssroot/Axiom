from fastapi import APIRouter
from app.schemas.ai import ExplainCodeRequest, ExplainCodeResponse
from app.core.ai_client import explain_code_with_ai

router = APIRouter()


@router.post("/api/v1/ai/explain", response_model=ExplainCodeResponse)
def explain_code(payload: ExplainCodeRequest):
    result = explain_code_with_ai(
        code=payload.code,
        language=payload.language,
        user_prompt=payload.user_prompt
    )

    return ExplainCodeResponse(
        summary=result["summary"],
        explanation=result["explanation"],
        important_logic=result["important_logic"],
        possible_issues=result["possible_issues"],
        suggested_improvements=result["suggested_improvements"]
    )
