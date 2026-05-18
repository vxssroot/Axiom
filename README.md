# Axiom (v0.2 - Core AI Orchestrator)

## New AI Routes (POST)
- /ai/chat
- /ai/explain
- /ai/review
- /ai/refactor

All use OpenAI-compatible provider with timeout/retry/fallback.

## Run
cd services/api && uvicorn main:app --reload

## Test
pytest services/api/tests/test_ai.py

## Env
AI_API_KEY=sk-... (optional for real calls)