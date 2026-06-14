from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from ..services.vector_store import VECTOR_STORE
from ..orchestrator.workflows import WORKFLOWS
import uuid
import json

router = APIRouter(prefix='/repos', tags=['Repo Intelligence'])

class RepoRequest(BaseModel):
    repo_id: str = Field(..., min_length=1)
    query: Optional[str] = None
    file_path: Optional[str] = None
    k: int = Field(8, ge=1, le=20)

class BlastRadiusRequest(BaseModel):
    repo_id: str = Field(..., min_length=1)
    target: str = Field(..., min_length=1)

class RepoResponse(BaseModel):
    content: str
    provider: str
    fallback: bool
    repo_id: str
    chunks_used: int
    request_id: str

class DependentItem(BaseModel):
    file: str
    relationship: str
    confidence: float

class ChangeHistoryItem(BaseModel):
    date: str
    author: str
    summary: str

class HistoricalIncident(BaseModel):
    description: str
    severity: str

class BlastRadiusResponse(BaseModel):
    target: str
    risk_score: str
    risk_reasoning: str
    dependents: List[DependentItem]
    change_history: List[ChangeHistoryItem]
    historical_incidents: List[HistoricalIncident]
    recommendation: str

@router.post('/summarize', response_model=RepoResponse)
async def summarize(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, req.query or 'overview architecture modules', req.k)
    context = '\n'.join([c.get('preview', c.get('content', ''))[:300] for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No indexed context for this repo. Index first via /github/import or /repos/index.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Summarize this repository at high level (modules, purpose, key files):\n{context}'
    result = await WORKFLOWS['chat']({'prompt': prompt})
    return RepoResponse(content=result, provider='gpt-4o-mini', fallback=False, repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

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
    return RepoResponse(content=result, provider='gpt-4o-mini', fallback=False, repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/review', response_model=RepoResponse)
async def review(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, req.query or 'code quality bugs security', req.k)
    context = '\n'.join([c.get('preview', '') for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No context for review. Index repo first.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Provide structured code review (bugs, security, improvements):\n{context}'
    result = await WORKFLOWS['review']({'prompt': prompt})
    return RepoResponse(content=result, provider='gpt-4o-mini', fallback=False, repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/architecture', response_model=RepoResponse)
async def architecture(req: RepoRequest):
    rid = str(uuid.uuid4())[:8]
    chunks = VECTOR_STORE.search(req.repo_id, 'architecture modules layers dependencies', req.k)
    context = '\n'.join([c.get('preview', '') for c in chunks])
    if not context:
        return RepoResponse(content='[FALLBACK] No architecture context. Index repo first.', provider='stub', fallback=True, repo_id=req.repo_id, chunks_used=0, request_id=rid)
    prompt = f'Generate architecture overview (modules, layers, dependencies, risks, missing pieces):\n{context}'
    result = await WORKFLOWS['chat']({'prompt': prompt})
    return RepoResponse(content=result, provider='gpt-4o-mini', fallback=False, repo_id=req.repo_id, chunks_used=len(chunks), request_id=rid)

@router.post('/blast-radius', response_model=BlastRadiusResponse)
async def blast_radius(req: BlastRadiusRequest):
    """
    Analyze the blast radius for a specific target (file path or function name).
    Returns risk assessment, dependents, change history, and recommendations.
    """
    target = req.target
    chunks = VECTOR_STORE.search(req.repo_id, target, k=20)
    
    # Build dependency context from chunks
    context = '\n'.join([c.get('content', '')[:500] for c in chunks])
    
    if not context:
        # Return minimal fallback response
        return BlastRadiusResponse(
            target=target,
            risk_score='low',
            risk_reasoning='No indexed context available for this target.',
            dependents=[],
            change_history=[],
            historical_incidents=[],
            recommendation='Index the repository to enable blast radius analysis.'
        )
    
    # Call the blast_radius workflow
    result_json = await WORKFLOWS['blast_radius']({
        'target': target,
        'context': context
    })
    
    try:
        # Parse the JSON response from the workflow
        result_data = json.loads(result_json)
        
        # Convert dependents list
        dependents = [
            DependentItem(
                file=d.get('file', ''),
                relationship=d.get('relationship', ''),
                confidence=float(d.get('confidence', 0.0))
            )
            for d in result_data.get('dependents', [])
        ]
        
        # Convert change history list
        change_history = [
            ChangeHistoryItem(
                date=ch.get('date', ''),
                author=ch.get('author', ''),
                summary=ch.get('summary', '')
            )
            for ch in result_data.get('change_history', [])
        ]
        
        # Convert historical incidents list
        historical_incidents = [
            HistoricalIncident(
                description=hi.get('description', ''),
                severity=hi.get('severity', 'low')
            )
            for hi in result_data.get('historical_incidents', [])
        ]
        
        return BlastRadiusResponse(
            target=target,
            risk_score=result_data.get('risk_score', 'low'),
            risk_reasoning=result_data.get('risk_reasoning', ''),
            dependents=dependents,
            change_history=change_history,
            historical_incidents=historical_incidents,
            recommendation=result_data.get('recommendation', '')
        )
    except (json.JSONDecodeError, ValueError, KeyError) as e:
        # Fallback if parsing fails
        return BlastRadiusResponse(
            target=target,
            risk_score='medium',
            risk_reasoning='Analysis completed but response parsing failed.',
            dependents=[],
            change_history=[],
            historical_incidents=[],
            recommendation='Retry the analysis or contact support.'
        )
