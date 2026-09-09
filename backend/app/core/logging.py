"""
MedPredict AI — Structured Logging Engine
Provides contextual logging with correlation IDs, levels, and JSON/text formatters.
"""

import sys
import logging
from typing import Optional
from contextvars import ContextVar

# Context variable for request correlation tracking
correlation_id_ctx: ContextVar[Optional[str]] = ContextVar("correlation_id", default=None)

class StructuredLogFormatter(logging.Formatter):
    """Formats log records with correlation ID and service context."""
    
    def format(self, record: logging.LogRecord) -> str:
        corr_id = correlation_id_ctx.get()
        record.correlation_id = corr_id if corr_id else "-"
        return super().format(record)

def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configures root logger with structured formatting."""
    log_format = "[%(asctime)s] [%(levelname)s] [%(name)s] [corr_id:%(correlation_id)s] %(message)s"
    formatter = StructuredLogFormatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger("medpredict")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    
    # Avoid duplicate handlers on re-initialization
    if not logger.handlers:
        logger.addHandler(handler)
        logger.propagate = False

    return logger

logger = setup_logging()
