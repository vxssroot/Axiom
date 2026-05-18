import os
import re
import subprocess
from typing import Dict, Any

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
CLONE_BASE = os.getenv('GITHUB_CLONE_BASE_DIR', '/tmp/axiom-repos')
os.makedirs(CLONE_BASE, exist_ok=True)

SAFE_URL = re.compile(r'^https://github\.com/[\w.-]+/[\w.-]+(?:\.git)?$')

def validate_repo_url(url: str) -> bool:
    return bool(SAFE_URL.match(url))

def clone_or_fetch(repo_url: str, branch: str = 'main') -> str:
    if not validate_repo_url(repo_url):
        raise ValueError('Invalid GitHub URL')
    repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
    target = os.path.join(CLONE_BASE, repo_name)
    env = os.environ.copy()
    if GITHUB_TOKEN:
        env['GIT_ASKPASS'] = 'echo'
        env['GIT_USERNAME'] = 'oauth2'
        env['GIT_PASSWORD'] = GITHUB_TOKEN
    try:
        if os.path.exists(target):
            subprocess.check_call(['git', '-C', target, 'fetch', 'origin', branch], env=env, timeout=60)
            subprocess.check_call(['git', '-C', target, 'checkout', branch], env=env, timeout=30)
        else:
            clone_url = repo_url
            if GITHUB_TOKEN and 'github.com' in repo_url:
                clone_url = repo_url.replace('https://', f'https://oauth2:{GITHUB_TOKEN}@')
            subprocess.check_call(['git', 'clone', '--depth', '1', '--branch', branch, clone_url, target], env=env, timeout=120)
        return target
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Clone/fetch failed: {e}')

def get_github_status() -> Dict[str, Any]:
    return {'token_configured': bool(GITHUB_TOKEN), 'clone_base': CLONE_BASE}