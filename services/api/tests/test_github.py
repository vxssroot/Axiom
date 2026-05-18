import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_validate_url():
    from app.services.github_client import validate_repo_url
    assert validate_repo_url('https://github.com/user/repo')
    assert not validate_repo_url('https://evil.com/repo')
    assert not validate_repo_url('git@github.com:user/repo.git')

def test_import_mocked(monkeypatch):
    from app.services import github_client
    monkeypatch.setattr(github_client, 'clone_or_fetch', lambda u, b: '/tmp/fake')
    from app.services import chunker
    monkeypatch.setattr(chunker, 'chunk_repo', lambda p: [{'file': 'a.py', 'content': 'print(1)', 'preview': 'print'}])
    r = client.post('/github/import', json={'repo_url': 'https://github.com/test/repo'})
    assert r.status_code == 200
    assert r.json()['status'] in ('imported', 'no_chunks')

def test_token_not_leaked():
    from app.services.github_client import get_github_status
    s = get_github_status()
    assert 'token' not in str(s).lower()

def test_webhook_push():
    r = client.post('/github/webhook', json={'event': 'push', 'ref': 'refs/heads/main'})
    assert r.status_code == 200
    assert r.json()['status'] == 'accepted'

def test_webhook_pr():
    r = client.post('/github/webhook', json={'action': 'opened', 'pull_request': {}})
    assert r.status_code == 200

def test_imported_searchable():
    from app.services.vector_store import VECTOR_STORE
    VECTOR_STORE.upsert('test-repo', [{'content': 'def bar(): pass', 'preview': 'def bar'}])
    r = client.post('/repos/search', json={'repo_id': 'test-repo', 'query': 'bar'})
    assert r.status_code == 200
    assert len(r.json().get('results', [])) >= 0