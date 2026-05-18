import os

GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', '')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '')
GITHUB_REDIRECT_URI = os.getenv('GITHUB_REDIRECT_URI', 'http://localhost:8000/auth/github/callback')
JWT_SECRET = os.getenv('JWT_SECRET', 'dev-secret-change-in-prod')
ENCRYPTION_SECRET = os.getenv('ENCRYPTION_SECRET', 'dev-32-byte-key-for-token-encryption!!')

if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET:
    print('[WARN] GitHub OAuth not fully configured - set CLIENT_ID/SECRET')