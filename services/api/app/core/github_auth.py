import time

import httpx
import jwt

from .config import GitHubAppConfig


def generate_app_jwt() -> str:
    """
    Generate a short-lived JWT signed with the GitHub App private key.

    Authenticates Axiom as the registered GitHub App.
    Backdated 60s on iat to tolerate clock skew between servers.
    Valid for 9 minutes — GitHub hard ceiling is 10.
    """
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + 540,
        "iss": GitHubAppConfig.APP_ID,
    }
    return jwt.encode(payload, GitHubAppConfig.PRIVATE_KEY, algorithm="RS256")


async def get_installation_token(installation_id: int) -> str:
    """
    Exchange a GitHub App JWT for a scoped installation access token.

    Tokens are valid for 60 minutes.
    Never cache beyond 55 minutes.
    Used by the ingestion pipeline to clone repos and call GitHub API
    on behalf of a specific user or org installation.
    """
    app_jwt = generate_app_jwt()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://api.github.com/app/installations/{installation_id}/access_tokens",
            headers={
                "Authorization": f"Bearer {app_jwt}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        response.raise_for_status()
        return response.json()["token"]
