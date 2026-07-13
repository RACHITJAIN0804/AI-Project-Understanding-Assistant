from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from app.core.settings import settings
from app.core.logging import configure_logging
from app.core.custom_exceptions import (
    InvalidFileError,
    FileExtractionError,
    RepositoryReadError,
    PromptGenerationError,
    AIServiceError,
)
from app.api.router import api_router

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.exception_handler(InvalidFileError)
async def invalid_file_exception_handler(
    request: Request,
    exc: InvalidFileError,
):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )


@app.exception_handler(FileExtractionError)
async def file_extraction_exception_handler(
    request: Request,
    exc: FileExtractionError,
):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )


@app.exception_handler(RepositoryReadError)
async def repository_read_exception_handler(
    request: Request,
    exc: RepositoryReadError,
):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )


@app.exception_handler(PromptGenerationError)
async def prompt_generation_exception_handler(
    request: Request,
    exc: PromptGenerationError,
):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )


@app.exception_handler(AIServiceError)
async def ai_service_exception_handler(
    request: Request,
    exc: AIServiceError,
):
    return JSONResponse(
        status_code=503,
        content={"detail": str(exc)},
    )


app.include_router(api_router)

logger.info("Application started successfully.")