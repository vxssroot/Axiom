# Axiom (v0.7 - Persistent Storage)

## New
- SQLAlchemy + SQLite/Postgres support
- Users, GitHub tokens (encrypted), Repositories, Audit logs
- OAuth now persists user + encrypted token
- Repo import persists metadata + audit
- /auth/me reads from DB

## Env
DATABASE_URL=sqlite:///./axiom.db (or postgres://...)
ENCRYPTION_SECRET=32-byte-key

## Test
pytest services/api/tests/test_persistent.py

SQLite fallback for dev/tests. Production: use Postgres + Alembic.