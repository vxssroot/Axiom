from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from ..services.vector_store import VECTOR_STORE
from ..orchestrator.workflows import WORKFLOWS
import uuid

router = APIRouter(prefix='/repos', tags=['Repo Intelligence'])

class RepoRequest(BaseModel):
    repo_id: str = Field(..., min_length=1)
    query: Optional[str] = None
    file_path: Optional[str] = None
    k: int = Field(8, ge=1, le=20)

class RepoResponse(BaseModel):
    content: str
    provider: str
    fallback: bool
    repo_id: str
    chunks_used: int
    request_id: str

@router.post('/summarize', response_model=RepoResponse)
async def summarize(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, req.query or 'overview architecture modules', req.k)
    context = '\n'.join([c.get('preview', c.get('content', ''))[:300] for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No indexed context for this repo. Index first via /github/import or /repos/index.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Summarize this repository at high level (modules, purpose, key files):\n{context}'
    result = await WORKFLOWS['chat']({'prompt': prompt})
    return RepoResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/explain-file', response_model=RepoResponse)
async def explain_file(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    q = req.file_path or req.query or ''
    chunks = VECTOR_STORE.search(req.repo_id, q, req.k)
    context = '\n'.join([c.get('content', '')[:400] for c in chunks if req.file_path in c.get('file', '')] or [c.get('preview', '') for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No chunks for this file. Index the repo first.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Explain this file in detail:\n{context}'
    result = await WORKFLOWS['explain']({'prompt': prompt})
    return RepoResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/review', response_model=RepoResponse)
async def review(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, req.query or 'code quality bugs security', req.k)
    context = '\n'.join([c.get('preview', '') for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No context for review. Index repo first.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Provide structured code review (bugs, security, improvements):\n{context}'
    result = await WORKFLOWS['review']({'prompt': prompt})
    return RepoResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/architecture', response_model=RepoResponse)
async def architecture(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, 'architecture modules layers dependencies', req.k)
    context = '\n'.join([c.get('preview', '') for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No architecture context. Index repo first.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Generate architecture overview (modules, layers, dependencies, risks, missing pieces):\n{context}'
    result = await WORKFLOWS['chat']({'prompt': prompt})
    return RepoResponse(content=result['content'], provider=result['provider'], fallback=result['fallback'], repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)
