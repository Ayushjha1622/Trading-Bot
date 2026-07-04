from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

from core.config import settings

# Create logs directory if it doesn't exist
log_path = Path(settings.log_file)
log_path.parent.mkdir(parents=True, exist_ok=True)


class Logger:

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)

        # Prevent duplicate handlers
        if logger.handlers:
            return logger

        logger.setLevel(settings.log_level.upper())

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        # File Handler
        file_handler = RotatingFileHandler(
            filename=settings.log_file,
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=5,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.propagate = False

        return logger