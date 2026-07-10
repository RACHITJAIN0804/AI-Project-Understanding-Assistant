import logging
import logging.config
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def configure_logging() -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,

            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                }
            },

            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": "INFO",
                },

                "file": {
                    "class": "logging.FileHandler",
                    "filename": str(LOG_FILE),
                    "formatter": "standard",
                    "level": "INFO",
                },
            },

            "root": {
                "handlers": ["console", "file"],
                "level": "INFO",
            },
        }
    )