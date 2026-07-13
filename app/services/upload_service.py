from pathlib import Path
import shutil
import zipfile
import logging

from app.core.custom_exceptions import (
    FileSaveError,
    FileExtractionError,
)

logger = logging.getLogger(__name__)

UPLOAD_DIR = Path("uploads")
EXTRACT_DIR = Path("extracted")

UPLOAD_DIR.mkdir(exist_ok=True)
EXTRACT_DIR.mkdir(exist_ok=True)


def save_uploaded_file(file) -> Path:
    file_path = UPLOAD_DIR / file.filename

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"File saved: {file.filename}")
        return file_path

    except Exception as e:
        logger.exception("Failed to save uploaded file.")
        raise FileSaveError(f"Failed to save uploaded file: {e}")


def extract_zip(zip_path: Path) -> Path:
    extract_folder = EXTRACT_DIR / zip_path.stem

    try:
        if extract_folder.exists():
            shutil.rmtree(extract_folder)
            logger.info(f"Removed old extracted folder: {extract_folder}")

        extract_folder.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_folder)

        logger.info(f"Repository extracted to: {extract_folder}")

        return extract_folder

    except PermissionError as e:
        logger.exception("Permission denied while deleting extraction folder.")
        raise FileExtractionError(
            "Permission denied while deleting old extracted repository. Close any programs using the folder and try again."
        )

    except zipfile.BadZipFile:
        logger.exception("Invalid ZIP archive.")
        raise FileExtractionError("The uploaded file is not a valid ZIP archive.")

    except Exception as e:
        logger.exception("Repository extraction failed.")
        raise FileExtractionError(f"Failed to extract repository: {e}")