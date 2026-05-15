import hashlib
import hmac

from fastapi import HTTPException, Request

from .config import GitHubAppConfig


async def verify_github_signature(request: Request) -> bytes:
    """
    Verify the X-Hub-Signature-256 header on incoming GitHub webhook requests.

    Returns raw request body if signature is valid.
    Raises HTTP 401 if signature is missing or does not match.
    Uses hmac.compare_digest for constant-time comparison
    to prevent timing attacks.
    """
    body = await request.body()
    sig_header = request.headers.get("X-Hub-Signature-256", "")

    if not sig_header.startswith("sha256="):
        raise HTTPException(status_code=401, detail="Missing webhook signature")

    expected = hmac.new(
        GitHubAppConfig.WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(f"sha256={expected}", sig_header):
        raise HTTPException(status_code=401, detail="Invalid webhook signature")

    return body
