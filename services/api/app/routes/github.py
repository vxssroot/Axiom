from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Optional
from ..services.github_client import clone_or_fetch, get_github_status, validate_repo_url
from ..services.chunker import chunk_repo
from ..services.embedding import embed
from ..services.vector_store import VECTOR_STORE

router = APIRouter(prefix='/github', tags=['GitHub'])

class ImportRequest(BaseModel):
    repo_url: HttpUrl
    repo_id: Optional[str] = None
    branch: str = 'main'

@router.post('/import')
async def import_repo(req: ImportRequest):
    if not validate_repo_url(str(req.repo_url)):
        raise HTTPException(400, 'Invalid GitHub repo URL')
    try:
        local_path = clone_or_fetch(str(req.repo_url), req.branch)
        chunks = chunk_repo(local_path)
        if chunks:
            embs = embed([c['content'] for c in chunks])
            for c, e in zip(chunks, embs):
                c['embedding'] = e
            rid = req.repo_id or str(req.repo_url).split('/')[-1].replace('.git', '')
            VECTOR_STORE.upsert(rid, chunks)
            return {'status': 'imported', 'repo_id': rid, 'files': len(set(c['file'] for c in chunks)), 'chunks': len(chunks), 'github': get_github_status()}
        return {'status': 'no_chunks', 'repo_id': req.repo_id}
    except Exception as e:
        raise HTTPException(500, f'Import failed: {str(e)[:200]}')

@router.post('/webhook')
async def github_webhook(payload: dict):
    event = payload.get('event') or payload.get('action', 'unknown')
    if 'push' in str(event).lower() or 'pull_request' in str(event).lower():
        return {'status': 'accepted', 'event': event, 'note': 'logged - auto-index TODO'}
    return {'status': 'ignored', 'event': event}