from typing import Dict, Any
from .ai_provider import call_provider

async def run_chat(req: Dict[str, Any]) -> Dict[str, Any]:
    prompt = req.get('prompt', '')
    return await call_provider(prompt, 'You are a helpful engineering assistant.')

async def run_explain(req: Dict[str, Any]) -> Dict[str, Any]:
    code = req.get('prompt', '')
    return await call_provider(f'Explain this code clearly:\n{code}', 'You are a senior engineer explaining code.')

async def run_review(req: Dict[str, Any]) -> Dict[str, Any]:
    code = req.get('prompt', '')
    return await call_provider(f'Review this code for bugs, security, and improvements:\n{code}', 'You are a strict code reviewer.')

async def run_refactor(req: Dict[str, Any]) -> Dict[str, Any]:
    code = req.get('prompt', '')
    return await call_provider(f'Refactor this code for clarity and performance:\n{code}', 'You are an expert refactoring engineer.')

WORKFLOWS = {'chat': run_chat, 'explain': run_explain, 'review': run_review, 'refactor': run_refactor}