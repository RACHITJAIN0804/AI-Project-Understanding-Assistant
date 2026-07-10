from pathlib import Path
import shutil
import zipfile
import logging

logger = logging.getLogger(__name__)

UPLOAD_DIR = Path("uploads")
EXTRACT_DIR = Path("extracted")

UPLOAD_DIR.mkdir(exist_ok=True)
EXTRACT_DIR.mkdir(exist_ok=True)


def save_uploaded_file(file) -> Path:
    """
    Save the uploaded ZIP file to the uploads directory.
    """

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"File saved: {file.filename}")

    return file_path


def extract_zip(zip_path: Path) -> Path:
    """
    Extract the uploaded ZIP archive.
    """

    extract_folder = EXTRACT_DIR / zip_path.stem

    # Remove old extracted folder if it exists
    if extract_folder.exists():
        try:
            shutil.rmtree(extract_folder)
            logger.info(f"Removed old extracted folder: {extract_folder}")
        except PermissionError:
            logger.error(
                f"Permission denied while deleting '{extract_folder}'. "
                "Close any programs using this folder and try again."
            )
            raise

    # Create a fresh extraction directory
    extract_folder.mkdir(parents=True, exist_ok=True)

    # Extract ZIP
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    logger.info(f"Repository extracted to: {extract_folder}")

    return extract_folder