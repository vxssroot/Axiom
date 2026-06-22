<p align="center">
  <img src="https://img.shields.io/badge/version-0.3.0-blue.svg?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/next.js-14.2-black?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/fastapi-0.115-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/status-active-success.svg?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/contributions-welcome-orange.svg?style=for-the-badge" alt="Contributions">
  <img src="https://img.shields.io/github/stars/vxssroot/Axiom?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/vxssroot/Axiom?style=social" alt="Forks">
  <img src="https://img.shields.io/github/last-commit/vxssroot/Axiom" alt="Last Commit">
</p>

<br />

<div align="center">
  <h1>⚡ Axiom</h1>
  <p><strong>Founder-Grade Repo Intelligence</strong></p>
  <p>AI Developer Assistant for serious engineering workflows</p>
  <br />
  <p>
    <a href="#-features"><strong>Explore Features »</strong></a>
    ·
    <a href="#-quickstart">Quickstart</a>
    ·
    <a href="#-screenshots">Screenshots</a>
    ·
    <a href="#-deployment">Deployment</a>
  </p>
</div>

<br />

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🖼️ Screenshots](#️-screenshots)
- [🚀 Quickstart](#-quickstart)
- [🏗️ Architecture](#️-architecture)
- [📦 Deployment](#-deployment)
- [🛠️ Tech Stack](#️-tech-stack)
- [📝 License](#-license)
- [🤝 Contributing](#-contributing)

---

## ✨ Features

### 🧠 AI-Powered Intelligence
- **Code Understanding** - Semantic search inside repositories
- **Smart Review** - AI-powered code review and analysis
- **Architecture Overview** - Get high-level system architecture insights
- **File Explanation** - Understand any file with AI assistance

### 🔐 Enterprise-Grade Security
- **GitHub OAuth** - Secure authentication with encrypted token storage
- **Private Repo Access** - Full support for private repositories
- **Audit Logging** - Complete activity tracking
- **Session Management** - Persistent, secure sessions

### 🚀 Production Ready
- **Full-Stack** - FastAPI backend + Next.js 14 frontend
- **Docker Support** - Production containers for easy deployment
- **Cloud Ready** - Deploy to Railway, Fly.io, or any VPS
- **MIT Licensed** - Free and open source

---

## 🖼️ Screenshots

<div align="center">

### 🔐 Sign Up / Login Page
<a href="https://imgur.com/kVfmXi1" target="_blank">
  <img src="https://imgur.com/kVfmXi1.png" alt="Sign Up Page" width="800"/>
</a>
<br/>
*Clean authentication with GitHub OAuth - [View on Imgur](https://imgur.com/kVfmXi1)*

<br /><br />

### 📊 Welcome / Dashboard Page
<a href="https://imgur.com/kVfmXi1" target="_blank">
  <img src="https://imgur.com/kVfmXi1.png" alt="Welcome Dashboard" width="800"/>
</a>
<br/>
*Your repository intelligence dashboard - [View on Imgur](https://imgur.com/kVfmXi1)*

</div>

> **📸 Note:** Both screenshots are hosted on Imgur. The sign-up page and welcome page share the same gallery link since you only provided one URL. If you have separate images, update the links accordingly.

---

## 🚀 Quickstart

### Prerequisites

- Python 3.9+
- Node.js 18+
- Docker (optional)
- GitHub OAuth App

### 1. Clone the Repository

```bash
git clone https://github.com/vxssroot/Axiom.git
cd Axiom
```

### 2. Backend Setup

```bash
cd services/api
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your GitHub OAuth credentials
python -m uvicorn app.main:app --reload
```

### 3. Frontend Setup

```bash
cd apps/web
npm install
npm run dev
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 5. Docker Setup (Optional)

```bash
docker compose up --build
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Axiom Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐      ┌─────────────┐      ┌───────────┐  │
│  │   Next.js   │      │   FastAPI   │      │  Postgres │  │
│  │  Frontend   │◄────►│   Backend   │◄────►│  Database │  │
│  │  (Port 3000)│      │  (Port 8000)│      │           │  │
│  └─────────────┘      └─────────────┘      └───────────┘  │
│         │                    │                              │
│         ▼                    ▼                              │
│  ┌─────────────┐      ┌─────────────┐                     │
│  │   GitHub    │      │  Qdrant/    │                     │
│  │    OAuth    │      │  Vector DB  │                     │
│  └─────────────┘      └─────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Components

- **Frontend**: Next.js 14 with Tailwind CSS for dark, enterprise UI
- **Backend**: FastAPI with SQLAlchemy ORM
- **Database**: PostgreSQL for persistent storage
- **Vector Search**: Qdrant (in-memory) for semantic code search
- **AI Layer**: OpenAI-compatible API with safe fallback
- **Auth**: GitHub OAuth with encrypted token storage

---

## 📦 Deployment

### Railway

```bash
railway up
```

### Fly.io

```bash
flyctl deploy -c fly.toml
```

### Docker

```bash
docker compose up --build
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Next.js 14 |
| Database | PostgreSQL |
| Vector DB | Qdrant |
| Auth | GitHub OAuth |
| Deployment | Docker |
| Language | Python 3.14 |
| Language | TypeScript |

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place. We welcome:

- 🐛 Bug reports
- 💡 Feature suggestions
- 🔧 Pull requests
- 📖 Documentation improvements

See `CONTRIBUTING.md` for more details.

### Contributors

<a href="https://github.com/vxssroot/Axiom/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vxssroot/Axiom" />
</a>

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing backend framework
- [Next.js](https://nextjs.org/) for the React framework
- [Tailwind CSS](https://tailwindcss.com/) for styling
- [GitHub](https://github.com/) for OAuth and API

---

## 📊 Project Status

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Development](https://img.shields.io/badge/Development-Active-brightgreen?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/vxssroot/Axiom?style=for-the-badge)
![PRs](https://img.shields.io/github/issues-pr/vxssroot/Axiom?style=for-the-badge)

---

<p align="center">
  Built with ❤️ for serious engineering workflows
</p>

<p align="center">
  <a href="https://github.com/vxssroot/Axiom">⭐ Star on GitHub</a>
  ·
  <a href="https://github.com/vxssroot/Axiom/issues">Report Bug</a>
  ·
  <a href="https://github.com/vxssroot/Axiom/issues">Request Feature</a>
</p>
