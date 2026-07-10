from fastapi import FastAPI
from app.core.settings import settings
from app.core.logging import configure_logging

import logging

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

logger.info("Application started successfully.")

@app.get("/")
def root():
    logger.info("Root endpoint accessed.")

    return {
        "message": f"Welcome to {settings.app_name}"
    }


@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed.")

    return {
        "status": "healthy"
    }