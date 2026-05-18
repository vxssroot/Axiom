from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel, HttpUrl
from typing import Optional
import httpx
from ..services.github_client import clone_or_fetch, get_github_status, validate_repo_url
from ..services.chunker import chunk_repo
from ..services.embedding import embed
from ..services.vector_store import VECTOR_STORE

router = APIRouter(prefix='/github', tags=['GitHub'])

class ImportRequest(BaseModel):
    repo_url: HttpUrl
    repo_id: Optional[str] = None
    branch: str = 'main'

def get_current_user(request: Request):
    token = request.cookies.get('axiom_session')
    if not token:
        return None
    # Simplified - in prod validate JWT
    return {'github_token': 'from-session'}  # placeholder

@router.get('/repos')
async def list_repos(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(401, 'Auth required for private repos')
    # In real: use stored token to call GitHub /user/repos
    return {'repos': ['user/repo1', 'user/repo2'], 'note': 'mocked - real GitHub call in prod'}

@router.post('/import')
async def import_repo(req: ImportRequest, request: Request):
    if not validate_repo_url(str(req.repo_url)):
        raise HTTPException(400, 'Invalid URL')
    user = get_current_user(request)
    token = user.get('github_token') if user else None
    try:
        local_path = clone_or_fetch(str(req.repo_url), req.branch)
        chunks = chunk_repo(local_path)
        if chunks:
            embs = embed([c['content'] for c in chunks])
            for c, e in zip(chunks, embs):
                c['embedding'] = e
            rid = req.repo_id or str(req.repo_url).split('/')[-1].replace('.git', '')
            VECTOR_STORE.upsert(rid, chunks)
            return {'status': 'imported', 'repo_id': rid, 'files': len(set(c['file'] for c in chunks)), 'chunks': len(chunks)}
        return {'status': 'no_chunks'}
    except Exception as e:
        raise HTTPException(500, f'Import failed: {str(e)[:200]}')

@router.post('/webhook')
async def github_webhook(payload: dict):
    event = payload.get('event') or payload.get('action', 'unknown')
    if 'push' in str(event).lower() or 'pull_request' in str(event).lower():
        return {'status': 'accepted', 'event': event}
    return {'status': 'ignored', 'event': event}