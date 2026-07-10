from fastapi import APIRouter

from app.api.endpoints.health import router as health_router
from app.api.endpoints.upload import router as upload_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(upload_router)