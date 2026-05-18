# Axiom (v0.4 - GitHub Repo Sync)

## New Endpoints
POST /github/import (clone + chunk + index)
POST /github/webhook (push/PR events logged)

After import, /repos/search and /ai/* work with the repo_id.

## Env
GITHUB_TOKEN=ghp_... (for private repos)
GITHUB_CLONE_BASE_DIR=/tmp/axiom-repos

## Test
pytest services/api/tests/test_github.py

Safe clone, no command injection, secrets not logged.