from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

from core.config import settings

# Create log directory if it doesn't exist
log_path = Path(settings.log_file)
log_path.parent.mkdir(parents=True, exist_ok=True)

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)

# File Handler
file_handler = RotatingFileHandler(
    filename=settings.log_file,
    maxBytes=1_000_000,  # 1 MB
    backupCount=5,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Root Logger
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    handlers=[
        file_handler,
        console_handler,
    ],
)

logger = logging.getLogger("TradingBot")