from fastapi import FastAPI
import logging

from app.core.settings import settings
from app.core.logging import configure_logging
from app.api.router import api_router

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

logger.info("Application started successfully.")

app.include_router(api_router)