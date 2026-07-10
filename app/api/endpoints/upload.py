from fastapi import APIRouter, UploadFile, File, HTTPException
import logging

from app.services.upload_service import (
    save_uploaded_file,
    extract_zip,
)

from app.services.file_reader import read_repository

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_repository(file: UploadFile = File(...)):

    if not file.filename.endswith(".zip"):

        logger.warning("Non-ZIP file uploaded.")

        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are allowed.",
        )

    saved_file = save_uploaded_file(file)

    extracted_path = extract_zip(saved_file)

    project_files = read_repository(extracted_path)

    logger.info("Repository processed successfully.")

    return {
        "message": "Repository uploaded successfully.",
        "repository": saved_file.name,
        "files_found": len(project_files),
        "files": [
            file["path"]
            for file in project_files
        ]
    }