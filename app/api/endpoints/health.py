from fastapi import APIRouter
import logging

from app.core.settings import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", tags=["Root"])
def root():
    logger.info("Root endpoint accessed.")

    return {
        "message": f"Welcome to {settings.app_name}"
    }


@router.get("/health", tags=["Health"])
def health_check():
    logger.info("Health endpoint accessed.")

    return {
        "status": "healthy"
    }