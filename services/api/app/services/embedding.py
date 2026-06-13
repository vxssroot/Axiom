import os
from typing import List, Dict
from openai import AsyncOpenAI

EMB_KEY = os.getenv('OPENAI_API_KEY')
EMB_MODEL = 'text-embedding-3-small'

async def embed(texts: List[str]) -> List[List[float]]:
    if not EMB_KEY:
        raise ValueError("OPENAI_API_KEY environment variable is missing.")
    client = AsyncOpenAI(api_key=EMB_KEY)
    response = await client.embeddings.create(
        input=texts,
        model=EMB_MODEL,
        dimensions=1536
    )
    return [data.embedding for data in response.data]

def get_embedding_status() -> Dict:
    return {'configured': bool(EMB_KEY), 'model': EMB_MODEL}