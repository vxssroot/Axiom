from fastapi import APIRouter, HTTPException, Request
from ..schemas.ai import AIRequest, AIResponse, ErrorResponse
from ..orchestrator.workflows import WORKFLOWS
import uuid

router = APIRouter(prefix='/ai', tags=['AI'])

@router.post('/chat', response_model=AIResponse)
async def chat(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    try:
        result = await WORKFLOWS['chat']({'prompt': req.prompt})
        return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)
    except Exception as e:
        raise HTTPException(500, detail=ErrorResponse(error='chat_failed', detail=str(e)[:100], request_id=rid).dict())

@router.post('/explain', response_model=AIResponse)
async def explain(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    try:
        result = await WORKFLOWS['explain']({'prompt': req.prompt})
        return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)
    except Exception as e:
        raise HTTPException(500, detail=ErrorResponse(error='explain_failed', detail=str(e)[:100], request_id=rid).dict())

@router.post('/review', response_model=AIResponse)
async def review(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    try:
        result = await WORKFLOWS['review']({'prompt': req.prompt})
        return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)
    except Exception as e:
        raise HTTPException(500, detail=ErrorResponse(error='review_failed', detail=str(e)[:100], request_id=rid).dict())

@router.post('/refactor', response_model=AIResponse)
async def refactor(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    try:
        result = await WORKFLOWS['refactor']({'prompt': req.prompt})
        return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)
    except Exception as e:
        raise HTTPException(500, detail=ErrorResponse(error='refactor_failed', detail=str(e)[:100], request_id=rid).dict())
