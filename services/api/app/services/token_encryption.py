import os
import base64
from cryptography.fernet import Fernet

ENCRYPTION_SECRET = os.getenv('ENCRYPTION_SECRET', 'dev-32-byte-key-for-token-encryption!!')
if len(ENCRYPTION_SECRET) < 32:
    ENCRYPTION_SECRET = ENCRYPTION_SECRET.ljust(32, '0')
key = base64.urlsafe_b64encode(ENCRYPTION_SECRET[:32].encode())
fernet = Fernet(key)

def encrypt_token(token: str) -> str:
    return fernet.encrypt(token.encode()).decode()

def decrypt_token(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()