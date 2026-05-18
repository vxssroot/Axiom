from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
import httpx
import jwt
import secrets
from datetime import datetime, timedelta
from ..config.oauth import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_REDIRECT_URI, JWT_SECRET

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.get('/github/login')
async def github_login():
    state = secrets.token_urlsafe(16)
    url = f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=repo,user:email&state={state}'
    return RedirectResponse(url)

@router.get('/github/callback')
async def github_callback(code: str, state: str, request: Request, response: Response):
    if not code:
        raise HTTPException(400, 'Missing code')
    async with httpx.AsyncClient() as client:
        token_resp = await client.post('https://github.com/login/oauth/access_token', data={'client_id': GITHUB_CLIENT_ID, 'client_secret': GITHUB_CLIENT_SECRET, 'code': code, 'redirect_uri': GITHUB_REDIRECT_URI}, headers={'Accept': 'application/json'})
        token_data = token_resp.json()
        access_token = token_data.get('access_token')
        if not access_token:
            raise HTTPException(400, 'OAuth failed')
    # Fetch user
    async with httpx.AsyncClient() as client:
        user_resp = await client.get('https://api.github.com/user', headers={'Authorization': f'Bearer {access_token}', 'Accept': 'application/json'})
        user_data = user_resp.json()
    user_id = str(user_data.get('id'))
    # Issue JWT session (dev - no DB)
    payload = {'sub': user_id, 'github_login': user_data.get('login'), 'github_token': access_token, 'exp': datetime.utcnow() + timedelta(days=7)}
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    response.set_cookie('axiom_session', token, httponly=True, secure=False, samesite='lax')
    return {'status': 'authenticated', 'user': user_data.get('login'), 'session': 'set'}

@router.get('/me')
async def me(request: Request):
    token = request.cookies.get('axiom_session')
    if not token:
        raise HTTPException(401, 'No session')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return {'user_id': payload['sub'], 'github_login': payload.get('github_login')}
    except:
        raise HTTPException(401, 'Invalid session')

@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('axiom_session')
    return {'status': 'logged_out'}