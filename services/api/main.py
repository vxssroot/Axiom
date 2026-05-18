from fastapi import FastAPI
from app.routes.ai import router as ai_router

app = FastAPI(title='Axiom API', version='0.2.0')
app.include_router(ai_router)

@app.get('/health')
async def health():
    return {'status': 'ok', 'service': 'axiom-api', 'version': '0.2.0'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)