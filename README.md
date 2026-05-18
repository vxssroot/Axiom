# Axiom — Founder-Grade Repo Intelligence

**Production-ready full-stack AI for serious engineering workflows.**

Axiom gives engineers and teams a secure, backend-controlled AI layer that understands entire repositories — not just snippets.

## Architecture
- FastAPI backend (Python) with SQLAlchemy + Postgres
- Next.js 14 frontend (dark, minimal, enterprise UI)
- GitHub OAuth + encrypted token storage
- Repo chunking + embedding + vector retrieval (in-memory + Qdrant-ready)
- AI orchestration (OpenAI-compatible + safe fallback)
- Repo intelligence actions (summarize, explain-file, review, architecture)

## Real Features (v0.3.0-foundation)
- GitHub OAuth login + private repo access
- One-click repo import + indexing
- Semantic search inside repos
- AI-powered code review, architecture overview, file explanation
- Full audit logging + persistent sessions
- Production Docker + Railway/Fly.io deployment ready

## Quickstart
```bash
docker compose up --build
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
```

## Deployment
- Railway: Backend + Frontend + Postgres
- Fly.io: Backend (Dockerfile.backend)
- See DEPLOY.md for full checklist

## Screenshots
Coming soon (clean dark UI with repo intelligence panels)

## License
MIT (see LICENSE)

## Contributing
See CONTRIBUTING.md

Founder-grade. No toy features. No fake claims.