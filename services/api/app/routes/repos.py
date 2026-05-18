from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ..services.chunker import chunk_repo
from ..services.embedding import embed, get_embedding_status
from ..services.vector_store import VECTOR_STORE, get_vector_status

router = APIRouter(prefix='/repos', tags=['Repos'])

class IndexRequest(BaseModel):
    repo_path: str
    repo_id: str = 'default'

class SearchRequest(BaseModel):
    repo_id: str = 'default'
    query: str
    k: int = 5

@router.post('/index')
async def index(req: IndexRequest):
    chunks = chunk_repo(req.repo_path)
    if not chunks:
        return {'status': 'empty', 'repo_id': req.repo_id}
    emb = embed([c['content'] for c in chunks])
    for c, e in zip(chunks, emb):
        c['embedding'] = e
    VECTOR_STORE.upsert(req.repo_id, chunks)
    return {'status': 'indexed', 'chunks': len(chunks), 'repo_id': req.repo_id, 'embedding': get_embedding_status()}

@router.post('/search')
async def search(req: SearchRequest):
    results = VECTOR_STORE.search(req.repo_id, req.query, req.k)
    return {'results': results, 'vector': get_vector_status()}