import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize_fallback():
    r = client.post('/repos/summarize', json={'repo_id': 'nonexistent'})
    assert r.status_code == 200
    assert r.json()['fallback'] is True

def test_explain_file_fallback():
    r = client.post('/repos/explain-file', json={'repo_id': 'nonexistent', 'file_path': 'main.py'})
    assert r.status_code == 200
    assert r.json()['fallback'] is True

def test_review_fallback():
    r = client.post('/repos/review', json={'repo_id': 'nonexistent'})
    assert r.status_code == 200
    assert r.json()['fallback'] is True

def test_architecture_fallback():
    r = client.post('/repos/architecture', json={'repo_id': 'nonexistent'})
    assert r.status_code == 200
    assert r.json()['fallback'] is True

def test_missing_repo_id():
    r = client.post('/repos/summarize', json={'repo_id': ''})
    assert r.status_code == 422

def test_with_indexed_context():
    from app.services.vector_store import VECTOR_STORE
    VECTOR_STORE.upsert('test-intel', [{'content': 'FastAPI backend with AI routes', 'preview': 'FastAPI backend'}])
    r = client.post('/repos/summarize', json={'repo_id': 'test-intel'})
    assert r.status_code == 200
    assert r.json()['chunks_used'] > 0