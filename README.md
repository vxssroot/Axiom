# Axiom (v0.5 - Repo Intelligence Actions)

## New Endpoints (POST /repos)
- /summarize (high-level repo overview)
- /explain-file (target file explanation)
- /review (structured code review)
- /architecture (modules/layers/dependencies/risks)

All use indexed context from vector store + AI workflow.

## Test
pytest services/api/tests/test_intelligence.py

Requires prior /github/import or /repos/index for real context.