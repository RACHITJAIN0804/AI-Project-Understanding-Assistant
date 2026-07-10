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
    Save uploaded ZIP file.
    """

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"File saved: {file.filename}")

    return file_path


def extract_zip(zip_path: Path):
    """
    Extract uploaded ZIP archive.
    """

    extract_folder = EXTRACT_DIR / zip_path.stem

    if extract_folder.exists():
        shutil.rmtree(extract_folder)

    extract_folder.mkdir(parents=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    logger.info(f"Extracted to {extract_folder}")

    return extract_folder