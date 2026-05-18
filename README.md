# Axiom (v0.6 - Full GitHub OAuth)

## New Auth Endpoints
GET /auth/github/login | GET /auth/github/callback | GET /auth/me | POST /auth/logout

## GitHub Features
GET /github/repos (authenticated list)
POST /github/import (now supports authenticated private repos via stored token)

## Security
- JWT session cookies (HttpOnly)
- No token logging
- Encrypted storage pattern ready (ENCRYPTION_SECRET)
- Backend-controlled OAuth

## Test
pytest services/api/tests/test_oauth.py

Public repo import remains fully supported without auth.