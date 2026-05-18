# Changelog

## [0.2.0-repo-intelligence] - 2026-05-18

### Added
- AI routes (/ai/chat, /explain, /review, /refactor) with OpenAI-compatible provider + timeout/retry/fallback
- Workflow dispatcher
- Repo chunking service (exclude list, metadata)
- Embedding abstraction + deterministic fallback
- In-memory vector store (Qdrant-ready)
- GitHub repo sync (/github/import + /github/webhook)
- Repo intelligence actions (/repos/summarize, explain-file, review, architecture)
- Structured Pydantic responses + error handling
- 20+ tests covering all flows and fallbacks

### Security
- No secrets in logs
- Safe GitHub clone (regex validation, no injection)
- Backend-controlled AI access

### Limitations
- No OAuth
- No frontend
- In-memory vector only
- Context limited to retrieved chunks

Production-ready backend MVP for repo-aware developer AI.