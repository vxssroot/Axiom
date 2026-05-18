# Axiom (v0.9 - Production Deploy)

## Docker Production
```bash
docker compose up --build
```

## Deploy
- Railway: Backend (Dockerfile.backend) + Frontend (Dockerfile.frontend) + Postgres
- Fly.io: fly launch --dockerfile Dockerfile.backend

## Env
DATABASE_URL (Postgres)
NEXT_PUBLIC_API_URL
GITHUB_CLIENT_ID/SECRET
JWT_SECRET/ENCRYPTION_SECRET

## Health
curl /health

SQLite dev only. Secure cookies in prod.