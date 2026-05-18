from fastapi import APIRouter, HTTPException, Request, Response, Depends
from fastapi.responses import RedirectResponse
import httpx
import jwt
import secrets
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..config.oauth import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_REDIRECT_URI, JWT_SECRET
from ..db.database import get_db
from ..db.models import User, GitHubToken, AuditLog
from ..services.token_encryption import encrypt_token, decrypt_token

router = APIRouter(prefix='/auth', tags=['Auth'])

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('axiom_session')
    if not token:
        return None
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return {'sub': payload['sub'], 'github_login': payload.get('github_login')}
    except:
        return None

@router.get('/github/login')
async def github_login():
    state = secrets.token_urlsafe(16)
    url = f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=repo,user:email&state={state}'
    return RedirectResponse(url)

@router.get('/github/callback')
async def github_callback(code: str, state: str, request: Request, response: Response, db: Session = Depends(get_db)):
    if not code:
        raise HTTPException(400, 'Missing code')
    async with httpx.AsyncClient() as client:
        token_resp = await client.post('https://github.com/login/oauth/access_token', data={'client_id': GITHUB_CLIENT_ID, 'client_secret': GITHUB_CLIENT_SECRET, 'code': code, 'redirect_uri': GITHUB_REDIRECT_URI}, headers={'Accept': 'application/json'})
        token_data = token_resp.json()
        access_token = token_data.get('access_token')
        if not access_token:
            raise HTTPException(400, 'OAuth failed')
    async with httpx.AsyncClient() as client:
        user_resp = await client.get('https://api.github.com/user', headers={'Authorization': f'Bearer {access_token}', 'Accept': 'application/json'})
        user_data = user_resp.json()
    github_id = str(user_data.get('id'))
    login = user_data.get('login')
    # Create/update user
    user = db.query(User).filter(User.github_id == github_id).first()
    if not user:
        user = User(github_id=github_id, login=login, email=user_data.get('email'))
        db.add(user)
        db.commit()
        db.refresh(user)
    # Store encrypted token
    encrypted = encrypt_token(access_token)
    token_record = db.query(GitHubToken).filter(GitHubToken.user_id == user.id).first()
    if token_record:
        token_record.encrypted_token = encrypted
    else:
        token_record = GitHubToken(user_id=user.id, encrypted_token=encrypted)
        db.add(token_record)
    db.commit()
    # Audit
    db.add(AuditLog(event='login', user_id=user.id, details=f'github:{login}'))
    db.commit()
    # JWT session
    payload = {'sub': str(user.id), 'github_login': login, 'exp': datetime.utcnow() + timedelta(days=7)}
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    response.set_cookie('axiom_session', token, httponly=True, secure=False, samesite='lax')
    return {'status': 'authenticated', 'user': login}

@router.get('/me')
async def me(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('axiom_session')
    if not token:
        raise HTTPException(401, 'No session')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = db.query(User).filter(User.id == int(payload['sub'])).first()
        return {'user_id': payload['sub'], 'github_login': user.login if user else payload.get('github_login')}
    except:
        raise HTTPException(401, 'Invalid session')

@router.post('/logout')
async def logout(response: Response, request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('axiom_session')
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            db.add(AuditLog(event='logout', user_id=int(payload['sub'])))
            db.commit()
        except: pass
    response.delete_cookie('axiom_session')
    return {'status': 'logged_out'}