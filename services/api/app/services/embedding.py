import os
import hashlib
from typing import List, Dict

EMB_KEY = os.getenv('EMBEDDING_API_KEY', '')
EMB_BASE = os.getenv('EMBEDDING_BASE_URL', 'https://api.openai.com/v1')
EMB_MODEL = os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')

def embed(texts: List[str]) -> List[List[float]]:
    if not EMB_KEY:
        return [[hash(t) % 1000 / 1000.0 for _ in range(1536)] for t in texts]  # deterministic fallback
    # Real OpenAI embedding call would go here (omitted for scope)
    return [[0.0] * 1536 for _ in texts]

def get_embedding_status() -> Dict:
    return {'configured': bool(EMB_KEY), 'model': EMB_MODEL}