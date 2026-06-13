import os
from typing import Dict, Any
from openai import AsyncOpenAI

async def call_provider(prompt: str, system_prompt: str) -> str:
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY missing.")
    client = AsyncOpenAI(api_key=api_key)
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

async def run_chat(req: Dict[str, Any]) -> str:
    return await call_provider(
        req.get('prompt', ''),
        'You are a helpful engineering assistant.'
    )

async def run_explain(req: Dict[str, Any]) -> str:
    return await call_provider(
        f"Explain this code clearly:\n{req.get('prompt', '')}",
        'You are a senior engineer explaining code.'
    )

async def run_review(req: Dict[str, Any]) -> str:
    return await call_provider(
        f"Review this code for bugs, security, improvements:\n{req.get('prompt', '')}",
        'You are a strict code reviewer.'
    )

async def run_refactor(req: Dict[str, Any]) -> str:
    return await call_provider(
        f"Refactor this code for clarity and performance:\n{req.get('prompt', '')}",
        'You are an expert refactoring engineer.'
    )

WORKFLOWS = {
    'chat': run_chat,
    'explain': run_explain,
    'review': run_review,
    'refactor': run_refactor
}