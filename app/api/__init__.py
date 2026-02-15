from fastapi import APIRouter

from app.api.attrazione import router as attrazione_router
from app.api.famiglia import router as famiglia_router
from app.api.visitatore import router as visitatore_router
from app.api.giro import router as giro_router

api_router = APIRouter()
api_router.include_router(attrazione_router)
api_router.include_router(famiglia_router)
api_router.include_router(visitatore_router)
api_router.include_router(giro_router)
