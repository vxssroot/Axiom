from fastapi import APIRouter
from ..schemas.ai import ExplainCodeRequest, ExplainCodeResponse
from ..core.ai_client import explain_code_with_ai

router = APIRouter(prefix="/api/v1/ai", tags=["ai"])


@router.post("/explain", response_model=ExplainCodeResponse)
async def explain_code(payload: ExplainCodeRequest):
    """Explain code using AI orchestration."""
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