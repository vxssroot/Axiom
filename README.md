# Axiom — AI Developer Assistant (v0.2.0-repo-intelligence)

**Production-ready backend milestone for repo-aware AI engineering workflows.**

## Real Capabilities
- FastAPI backend with /health, /metrics
- AI routes: /ai/chat, /explain, /review, /refactor (OpenAI-compatible + safe stub)
- Workflow dispatcher (chat/explain/review/refactor)
- Repo chunking (local path, exclude common dirs, metadata preserved)
- Embedding abstraction (OpenAI + deterministic fallback)
- Vector store (in-memory fallback, Qdrant-ready interface)
- GitHub repo import (/github/import: clone + chunk + embed + index; supports token for private)
- /github/webhook (push/PR logging)
- Repo search (/repos/search)
- Repo intelligence actions: /repos/summarize, /explain-file (file_path filter), /review, /architecture
- Structured responses with chunks_used, provider, fallback, request_id
- Tests for all core flows

## Setup
cd services/api && pip install -r requirements.txt && uvicorn main:app --reload

## Key Endpoints
POST /github/import | POST /repos/index | POST /repos/search | POST /repos/summarize | POST /repos/explain-file | POST /repos/review | POST /repos/architecture | POST /ai/*

## Limitations (Current)
- No GitHub OAuth yet
- No frontend/dashboard
- Qdrant optional/not fully wired (in-memory only)
- Fallback embeddings dev/test only
- Context limited to retrieved chunks (k=8 default)
- No persistent auth/workspaces
- No PR automation or audit logs

## Screenshots
Coming soon (backend API + Postman collection)

## Test
pytest services/api/tests/ -q

Safety: Backend-controlled AI only. No direct model access from client.