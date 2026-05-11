# Axiom

<p align="center">
  <strong>AI Developer Assistant for serious engineering workflows.</strong>
</p>

<p align="center">
  Explain code. Fix bugs. Refactor safely. Generate tests. Review security. Search repositories with context.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active_development-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/product-AI_Developer_Assistant-111827?style=for-the-badge" />
  <img src="https://img.shields.io/badge/stack-web_first-1f2937?style=for-the-badge" />
  <img src="https://img.shields.io/badge/architecture-backend_controlled-374151?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/frontend-React_/_Next.js-000000?style=flat-square" />
  <img src="https://img.shields.io/badge/backend-FastAPI_/_Node.js-111827?style=flat-square" />
  <img src="https://img.shields.io/badge/vector_db-Qdrant_/_pgvector-1f2937?style=flat-square" />
  <img src="https://img.shields.io/badge/AI-LangGraph_Ready-374151?style=flat-square" />
  <img src="https://img.shields.io/badge/license-private-red?style=flat-square" />
</p>

---

## Overview

**Axiom** is an AI Developer Assistant designed to help developers understand, improve, and ship code faster.

The product starts as a web-first MVP, then expands into a CLI tool and VS Code extension using the same backend infrastructure.

Axiom is not intended to be a basic chatbot wrapper.

It is designed as a serious developer workflow platform with:

- project-aware AI responses
- repository context retrieval
- structured code analysis
- AI workflow orchestration
- secure backend-controlled model access
- scalable product architecture

Design inspiration:

> Linear + Vercel + Notion + Cursor

Clean. Minimal. Developer-native. Enterprise-grade.

---

## Core Principle

> The frontend must never talk directly to the AI model.

All AI requests must go through the backend.

This protects:

- API keys
- user data
- model costs
- rate limits
- logs
- prompt logic
- security rules
- product stability

---

## Architecture

```txt
[ Frontend Layer ]
Web App / CLI / VS Code Extension
        ↓
[ Backend Layer ]
API Gateway / Auth / Rate Limits / Logging
        ↓
[ Intelligence Layer ]
AI Models / LangGraph / Vector DB / Storage
Main Features
Explain Code
Understand unfamiliar code clearly.
Fix Bug
Analyze issues and generate safer fixes.
Refactor
Improve structure and maintainability.
Generate Tests
Create meaningful test cases automatically.
Security Review
Review code for vulnerabilities and risky patterns.
Repository Search
Ask questions across an entire codebase intelligently.

axiom/
├── apps/
│   ├── web/
│   │   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   ├── styles/
│   │   └── package.json
│   │
│   ├── cli/
│   │   ├── src/
│   │   └── package.json
│   │
│   └── vscode-extension/
│       ├── src/
│       └── package.json
│
├── services/
│   ├── api/
│   │   ├── app/
│   │   ├── routes/
│   │   ├── middleware/
│   │   ├── schemas/
│   │   └── main.py
│   │
│   ├── ai-orchestrator/
│   │   ├── workflows/
│   │   ├── agents/
│   │   ├── prompts/
│   │   └── graph.py
│   │
│   ├── repo-indexer/
│   │   ├── chunkers/
│   │   ├── parsers/
│   │   ├── embeddings/
│   │   └── indexer.py
│   │
│   └── worker/
│       ├── jobs/
│       └── queue.py
│
├── packages/
│   ├── shared-types/
│   ├── config/
│   └── ui/
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── roadmap.md
│   └── contribution.md
│
├── infra/
│   ├── docker/
│   ├── railway/
│   ├── vercel/
│   └── scripts/
│
├── .github/
│   └── workflows/
│
├── .env.example
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── docker-compose.yml


