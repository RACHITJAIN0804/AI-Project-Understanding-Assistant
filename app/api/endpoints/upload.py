from fastapi import APIRouter, UploadFile, File, HTTPException
import logging

from app.services.upload_service import (
    save_uploaded_file,
    extract_zip,
)

from app.services.file_reader import read_repository
from app.services.analyzer import analyze_repository

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_repository(file: UploadFile = File(...)):
    """
    Upload and analyze a repository.
    """

    if not file.filename.endswith(".zip"):
        logger.warning("Non-ZIP file uploaded.")

        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are allowed.",
        )

    saved_file = save_uploaded_file(file)

    extracted_path = extract_zip(saved_file)

    project_files = read_repository(extracted_path)

    analysis = analyze_repository(
        extracted_path,
        project_files,
    )

    logger.info("Repository analyzed successfully.")

    return analysis