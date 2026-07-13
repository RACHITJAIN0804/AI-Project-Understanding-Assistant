from pathlib import Path
import logging

from app.core.custom_exceptions import RepositoryReadError
from app.utils.file_filters import (
    IGNORED_DIRECTORIES,
    SUPPORTED_EXTENSIONS,
)

logger = logging.getLogger(__name__)


def read_repository(repository_path: Path):
    project_files = []

    try:
        for file_path in repository_path.rglob("*"):

            if file_path.is_dir():
                continue

            if any(part in IGNORED_DIRECTORIES for part in file_path.parts):
                continue

            if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            try:
                content = file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                project_files.append(
                    {
                        "name": file_path.name,
                        "path": str(file_path.relative_to(repository_path)),
                        "extension": file_path.suffix,
                        "content": content,
                    }
                )

            except Exception as e:
                logger.warning(f"Could not read {file_path}: {e}")

        if not project_files:
            raise RepositoryReadError(
                "No supported project files were found in the uploaded repository."
            )

        logger.info(f"Read {len(project_files)} files.")

        return project_files

    except RepositoryReadError:
        raise

    except Exception as e:
        logger.exception("Failed to read repository.")
        raise RepositoryReadError(f"Failed to read repository: {e}")