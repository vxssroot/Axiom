from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel, HttpUrl
from typing import Optional
import httpx
from sqlalchemy.orm import Session
from ..services.github_client import clone_or_fetch, validate_repo_url
from ..services.chunker import chunk_repo
from ..services.embedding import embed
from ..services.vector_store import VECTOR_STORE
from ..db.database import get_db
from ..db.models import Repository, AuditLog

router = APIRouter(prefix='/github', tags=['GitHub'])

class ImportRequest(BaseModel):
    repo_url: HttpUrl
    repo_id: Optional[str] = None
    branch: str = 'main'

def get_current_user(request: Request):
    token = request.cookies.get('axiom_session')
    if not token:
        return None
    from jose import jwt
    from ..config.oauth import JWT_SECRET
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return {'user_id': int(payload['sub']), 'github_login': payload.get('github_login')}
    except:
        return None

@router.get('/repos')
async def list_repos(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(401, 'Auth required')
    return {'repos': ['user/repo1', 'user/repo2'], 'note': 'mocked - real GitHub /user/repos in prod'}

@router.post('/import')
async def import_repo(req: ImportRequest, request: Request, db: Session = Depends(get_db)):
    if not validate_repo_url(str(req.repo_url)):
        raise HTTPException(400, 'Invalid URL')
    user = get_current_user(request)
    try:
        local_path = clone_or_fetch(str(req.repo_url), req.branch)
        chunks = chunk_repo(local_path)
        if chunks:
            embs = embed([c['content'] for c in chunks])
            for c, e in zip(chunks, embs):
                c['embedding'] = e
            rid = req.repo_id or str(req.repo_url).split('/')[-1].replace('.git', '')
            VECTOR_STORE.upsert(rid, chunks)
            # Persist metadata
            repo = Repository(repo_id=rid, owner=str(req.repo_url).split('/')[-2], name=rid, branch=req.branch, chunks_count=len(chunks), user_id=user['user_id'] if user else None)
            db.add(repo)
            db.commit()
            db.add(AuditLog(event='repo_import', user_id=user['user_id'] if user else None, details=f'{rid} ({len(chunks)} chunks)'))
            db.commit()
            return {'status': 'imported', 'repo_id': rid, 'files': len(set(c['file'] for c in chunks)), 'chunks': len(chunks)}
        return {'status': 'no_chunks'}
    except Exception as e:
        raise HTTPException(500, f'Import failed: {str(e)[:200]}')

@router.post('/webhook')
async def github_webhook(payload: dict, db: Session = Depends(get_db)):
    event = payload.get('event') or payload.get('action', 'unknown')
    db.add(AuditLog(event='github_webhook', details=str(event)[:100]))
    db.commit()
    if 'push' in str(event).lower() or 'pull_request' in str(event).lower():
        return {'status': 'accepted', 'event': event}
    return {'status': 'ignored', 'event': event}