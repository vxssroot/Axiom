import os
import asyncio
from typing import Dict, Any
import httpx

AI_KEY = os.getenv('AI_API_KEY', '')
AI_BASE = os.getenv('AI_BASE_URL', 'https://api.openai.com/v1')
AI_MODEL = os.getenv('AI_MODEL', 'gpt-4o-mini')

async def call_provider(prompt: str, system: str = 'You are a precise engineering assistant.') -> Dict[str, Any]:
    if not AI_KEY:
        return {'content': f'[STUB] {prompt[:100]}...', 'provider': 'stub', 'fallback': True}
    headers = {'Authorization': f'Bearer {AI_KEY}', 'Content-Type': 'application/json'}
    payload = {'model': AI_MODEL, 'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}], 'max_tokens': 800}
    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=12.0) as client:
                r = await client.post(f'{AI_BASE}/chat/completions', json=payload, headers=headers)
                r.raise_for_status()
                data = r.json()
                return {'content': data['choices'][0]['message']['content'], 'provider': 'openai', 'fallback': False}
        except Exception as e:
            if attempt == 2:
                return {'content': f'[FALLBACK] Provider error: {str(e)[:50]}', 'provider': 'fallback', 'fallback': True}
            await asyncio.sleep(0.5 * (attempt + 1))
    return {'content': '[ERROR] Max retries', 'provider': 'error', 'fallback': True}

def get_provider_status() -> Dict[str, Any]:
    return {'configured': bool(AI_KEY), 'model': AI_MODEL, 'base': AI_BASE}