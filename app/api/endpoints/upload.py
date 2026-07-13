from fastapi import APIRouter, UploadFile, File
import logging

from app.core.custom_exceptions import InvalidFileError
from app.services.upload_service import (
    save_uploaded_file,
    extract_zip,
)
from app.services.file_reader import read_repository
from app.services.analyzer import analyze_repository
from app.services.prompt_builder import build_project_prompt
from app.services.ai.gemini_service import explain_project

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_repository(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".zip"):
        logger.warning("Non-ZIP file uploaded.")
        raise InvalidFileError("Only ZIP files are allowed.")

    saved_file = save_uploaded_file(file)

    extracted_path = extract_zip(saved_file)

    project_files = read_repository(extracted_path)

    analysis = analyze_repository(
        extracted_path,
        project_files,
    )

    prompt = build_project_prompt(analysis)

    logger.info("Prompt generated successfully.")

    explanation = explain_project(prompt)

    logger.info("AI explanation generated successfully.")

    return {
        "analysis": analysis,
        "explanation": explanation,
    }