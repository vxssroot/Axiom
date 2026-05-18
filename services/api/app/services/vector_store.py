from typing import List, Dict, Any

class InMemoryStore:
    def __init__(self):
        self.data: Dict[str, List[Dict]] = {}
    def upsert(self, repo_id: str, chunks: List[Dict]):
        self.data[repo_id] = chunks
    def search(self, repo_id: str, query: str, k: int = 5) -> List[Dict]:
        chunks = self.data.get(repo_id, [])
        q = query.lower()
        scored = sorted(chunks, key=lambda c: sum(1 for w in q.split() if w in c.get('content', '').lower()), reverse=True)
        return scored[:k]

VECTOR_STORE = InMemoryStore()

def get_vector_status() -> Dict:
    return {'type': 'in-memory', 'repos': list(VECTOR_STORE.data.keys())}