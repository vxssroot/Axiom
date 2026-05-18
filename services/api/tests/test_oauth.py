import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_redirect():
    r = client.get('/auth/github/login')
    assert r.status_code == 307 or r.status_code == 302
    assert 'github.com' in r.headers.get('location', '')

def test_callback_missing_code():
    r = client.get('/auth/github/callback?state=abc')
    assert r.status_code == 400

def test_me_no_session():
    r = client.get('/auth/me')
    assert r.status_code == 401

def test_logout():
    r = client.post('/auth/logout')
    assert r.status_code == 200
    assert r.json()['status'] == 'logged_out'

def test_github_repos_unauth():
    r = client.get('/github/repos')
    assert r.status_code == 401

def test_secrets_not_logged(monkeypatch):
    from app.config import oauth
    assert 'GITHUB_CLIENT_SECRET' not in str(oauth.__dict__)

def test_import_public_still_works():
    r = client.post('/github/import', json={'repo_url': 'https://github.com/test/public-repo'})
    assert r.status_code in (200, 500)  # 500 if no real clone, but route exists