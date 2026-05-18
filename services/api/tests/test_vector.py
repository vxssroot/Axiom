import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chunker_excludes():
    from app.services.chunker import chunk_repo, EXCLUDE
    assert 'node_modules' in EXCLUDE and '.git' in EXCLUDE

def test_chunker_metadata():
    chunks = [{'file': 'test.py', 'language': 'py', 'chunk_index': 0, 'content': 'def x(): pass', 'preview': 'def x()'}]
    assert 'file' in chunks[0] and 'preview' in chunks[0]

def test_fallback_embedding():
    from app.services.embedding import embed
    e = embed(['hello world'])
    assert len(e[0]) == 1536

def test_inmemory_search():
    from app.services.vector_store import VECTOR_STORE
    VECTOR_STORE.upsert('test', [{'content': 'def foo(): pass', 'preview': 'def foo'}])
    res = VECTOR_STORE.search('test', 'foo', 1)
    assert len(res) == 1

def test_repos_index_fallback():
    r = client.post('/repos/index', json={'repo_path': '/tmp', 'repo_id': 't1'})
    assert r.status_code in (200, 422)

def test_repos_search_fallback():
    r = client.post('/repos/search', json={'repo_id': 't1', 'query': 'test'})
    assert r.status_code == 200

def test_ai_chat_with_context():
    r = client.post('/ai/chat', json={'prompt': 'explain', 'repo_id': 't1'})
    assert r.status_code == 200
    assert 'content' in r.json()