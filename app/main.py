from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.rest import router as rest_router
from app.api.routes.websocket import router as websocket_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rest_router, prefix="/api", tags=["REST"])
app.include_router(websocket_router, prefix="/ws", tags=["WebSocket"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Market Data API"}