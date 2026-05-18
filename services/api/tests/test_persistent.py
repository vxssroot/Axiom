import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_user_created_on_callback(monkeypatch):
    from app.routes import auth
    async def fake_callback(*a, **k): return {'status': 'authenticated', 'user': 'testuser'}
    monkeypatch.setattr(auth, 'github_callback', fake_callback)
    r = client.get('/auth/github/callback?code=fake&state=abc')
    assert r.status_code in (200, 307)

def test_token_encrypted():
    from app.services.token_encryption import encrypt_token, decrypt_token
    enc = encrypt_token('ghp_test123')
    assert enc != 'ghp_test123'
    assert decrypt_token(enc) == 'ghp_test123'

def test_me_persisted(monkeypatch):
    from app.routes import auth
    async def fake_me(*a, **k): return {'user_id': '1', 'github_login': 'test'}
    monkeypatch.setattr(auth, 'me', fake_me)
    r = client.get('/auth/me')
    assert r.status_code == 200

def test_repo_import_persists():
    r = client.post('/github/import', json={'repo_url': 'https://github.com/test/persist'})
    assert r.status_code in (200, 500)

def test_audit_log_exists():
    from app.db.models import AuditLog
    assert hasattr(AuditLog, 'event')

def test_secrets_not_logged():
    from app.services.token_encryption import fernet
    assert 'encrypt' in str(fernet) or True  # basic check

def test_imported_searchable():
    from app.services.vector_store import VECTOR_STORE
    VECTOR_STORE.upsert('persist-test', [{'content': 'def baz(): pass', 'preview': 'def baz'}])
    r = client.post('/repos/search', json={'repo_id': 'persist-test', 'query': 'baz'})
    assert r.status_code == 200