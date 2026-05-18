Production Deployment

Docker: docker compose up --build

Railway: Connect repo, add Backend (Dockerfile.backend), Frontend (Dockerfile.frontend), Postgres. Set DATABASE_URL, NEXT_PUBLIC_API_URL, GITHUB_CLIENT_ID/SECRET, JWT_SECRET, ENCRYPTION_SECRET.

Fly.io: fly launch --dockerfile Dockerfile.backend

Health: curl /health

Notes: SQLite dev only. Secure cookies in prod. No secrets committed.