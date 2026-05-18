# Contributing to Axiom

## Local Setup
```bash
# Backend
git clone https://github.com/er4700345-coder/Axiom.git
cd Axiom/services/api
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd ../apps/web
npm install
npm run dev

# Full stack
docker compose up --build
```

## Branch Naming
- feature/xxx (new capability)
- fix/xxx (bug fix)
- docs/xxx (documentation)

## PR Expectations
- Small, focused changes
- Tests for new functionality
- Clear description of what/why
- No fake data or logic

## Testing
- Backend: pytest services/api/tests/
- Frontend: npm test (when added)
- Full stack: docker compose up --build + manual verification

Thank you for contributing to serious engineering AI.