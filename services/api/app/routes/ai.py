from fastapi import APIRouter, HTTPException, Request
from ..schemas.ai import AIRequest, AIResponse
from ..orchestrator.workflows import WORKFLOWS
from ..services.vector_store import VECTOR_STORE
import uuid

router = APIRouter(prefix='/ai', tags=['AI'])

@router.post('/chat', response_model=AIResponse)
async def chat(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    context = ''
    if hasattr(req, 'repo_id') and req.repo_id:
        results = VECTOR_STORE.search(req.repo_id, req.prompt or req.context or '', 3)
        context = '\n'.join([r.get('preview', '') for r in results])
    prompt = (req.prompt or '') + (f'\nContext:\n{context}' if context else '')
    result = await WORKFLOWS['chat']({'prompt': prompt})
    return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)

@router.post('/explain', response_model=AIResponse)
async def explain(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    context = ''
    if hasattr(req, 'repo_id') and req.repo_id:
        results = VECTOR_STORE.search(req.repo_id, req.prompt or '', 3)
        context = '\n'.join([r.get('preview', '') for r in results])
    prompt = (req.prompt or '') + (f'\nContext:\n{context}' if context else '')
    result = await WORKFLOWS['explain']({'prompt': prompt})
    return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)

@router.post('/review', response_model=AIResponse)
async def review(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    result = await WORKFLOWS['review']({'prompt': req.prompt})
    return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)

@router.post('/refactor', response_model=AIResponse)
async def refactor(req: AIRequest, request: Request):
    rid = str(uuid.uuid4())[:8]
    result = await WORKFLOWS['refactor']({'prompt': req.prompt})
    return AIResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], request_id=rid)
