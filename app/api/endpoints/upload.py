from fastapi import APIRouter, UploadFile, File, HTTPException
import logging

from app.services.upload_service import (
    save_uploaded_file,
    extract_zip,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_repository(file: UploadFile = File(...)):
    """
    Upload and extract a ZIP repository.
    """

    if not file.filename.endswith(".zip"):
        logger.warning("Non-ZIP file uploaded.")

        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are allowed."
        )

    saved_file = save_uploaded_file(file)

    extracted_path = extract_zip(saved_file)

    logger.info("Repository uploaded successfully.")

    return {
        "message": "Repository uploaded successfully.",
        "repository": saved_file.name,
        "location": str(extracted_path)
    }