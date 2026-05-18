import os
from typing import List, Dict, Any

EXCLUDE = {'node_modules', '.git', 'dist', 'build', '__pycache__', '.venv', 'target', '.next', 'out'}

def chunk_repo(repo_path: str, max_lines: int = 50) -> List[Dict[str, Any]]:
    chunks = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        for f in files:
            if f.endswith(('.py', '.ts', '.js', '.tsx', '.go', '.rs', '.java')):
                full = os.path.join(root, f)
                try:
                    with open(full, 'r', errors='ignore') as fh:
                        lines = fh.readlines()
                    for i in range(0, len(lines), max_lines):
                        chunk = ''.join(lines[i:i+max_lines])
                        chunks.append({
                            'file': full.replace(repo_path, ''), 'language': f.split('.')[-1],
                            'chunk_index': i // max_lines, 'content': chunk[:2000],
                            'preview': chunk[:200].replace('\n', ' ')
                        })
                except: pass
    return chunks