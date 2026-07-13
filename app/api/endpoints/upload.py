from fastapi import APIRouter, UploadFile, File, HTTPException
import logging

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
    """
    Upload a repository, analyze it, generate an AI prompt,
    and return the AI explanation.
    """

    if not file.filename.endswith(".zip"):
        logger.warning("Non-ZIP file uploaded.")

        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are allowed.",
        )

    # Save uploaded ZIP
    saved_file = save_uploaded_file(file)

    # Extract ZIP
    extracted_path = extract_zip(saved_file)

    # Read project files
    project_files = read_repository(extracted_path)

    # Analyze repository
    analysis = analyze_repository(
        extracted_path,
        project_files,
    )

    # Build AI prompt
    prompt = build_project_prompt(analysis)

    logger.info("Prompt generated successfully.")

    # Get AI explanation
    explanation = explain_project(prompt)

    logger.info("AI explanation generated successfully.")

    return {
        "analysis": analysis,
        "explanation": explanation,
    }