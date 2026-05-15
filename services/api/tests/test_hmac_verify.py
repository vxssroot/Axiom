import hashlib
import hmac
import os

from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

from app.core.hmac_verify import verify_github_signature


os.environ.setdefault("GITHUB_APP_ID", "123456")
os.environ.setdefault("GITHUB_PRIVATE_KEY", "placeholder")
os.environ.setdefault("GITHUB_WEBHOOK_SECRET", "test-secret")


TEST_SECRET = "test-secret"


def make_signature(body: bytes) -> str:
    digest = hmac.new(
        TEST_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    return f"sha256={digest}"


app = FastAPI()


@app.post("/test-webhook")
async def test_webhook(
    body: bytes = Depends(verify_github_signature)
):
    return {"status": "ok"}


client = TestClient(app)


def test_valid_signature_passes():
    body = b'{"action": "created"}'

    response = client.post(
        "/test-webhook",
        content=body,
        headers={
            "X-Hub-Signature-256": make_signature(body)
        }
    )

    assert response.status_code == 200


def test_invalid_signature_rejected():
    body = b'{"action": "created"}'

    response = client.post(
        "/test-webhook",
        content=body,
        headers={
            "X-Hub-Signature-256": "sha256=invalidsignature"
        }
    )

    assert response.status_code == 401


def test_missing_signature_rejected():
    body = b'{"action": "created"}'

    response = client.post(
        "/test-webhook",
        content=body
    )

    assert response.status_code == 401
