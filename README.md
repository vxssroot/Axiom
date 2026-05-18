# Axiom (v0.3 - Vector Retrieval)

## New Endpoints
POST /repos/index  (chunk + embed + upsert)
POST /repos/search (semantic via fallback)

/ai/chat and /ai/explain now accept optional repo_id for context.

## Env
EMBEDDING_API_KEY=... (optional)
QDRANT_URL=... (future)

## Test
pytest services/api/tests/test_vector.py

No real Qdrant yet - in-memory fallback only.