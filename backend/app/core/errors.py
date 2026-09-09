"""
MedPredict AI — Error Envelopes & Central Exception Handlers
Provides uniform, safe API error responses across the platform.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from backend.app.core.logging import logger

class MedPredictAPIException(Exception):
    """Base exception for application domain errors."""
    def __init__(self, message: str, code: str = "APPLICATION_ERROR", status_code: int = 400, details: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or []

class EntityNotFoundError(MedPredictAPIException):
    def __init__(self, message: str, details: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message, code="NOT_FOUND", status_code=status.HTTP_404_NOT_FOUND, details=details)

class ResourceNotFoundError(EntityNotFoundError):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(f"{resource} '{identifier}' not found")

class BusinessRuleViolationError(MedPredictAPIException):
    def __init__(self, message: str, details: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message, code="BUSINESS_RULE_VIOLATION", status_code=status.HTTP_400_BAD_REQUEST, details=details)

class AuthorizationError(MedPredictAPIException):
    def __init__(self, message: str = "Access denied: insufficient permissions"):
        super().__init__(message, code="FORBIDDEN", status_code=status.HTTP_403_FORBIDDEN)

class AuthenticationError(MedPredictAPIException):
    def __init__(self, message: str = "Invalid authentication credentials"):
        super().__init__(message, code="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)

class DataValidationError(MedPredictAPIException):
    def __init__(self, message: str, details: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message, code="VALIDATION_ERROR", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, details=details)


def format_error_response(code: str, message: str, details: Optional[List[Any]] = None, status_code: int = 400) -> JSONResponse:
    """Generates standardized error envelope."""
    payload = {
        "success": False,
        "error": {
            "code": code,
            "message": message,
            "details": details or []
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    return JSONResponse(status_code=status_code, content=payload)

async def app_exception_handler(request: Request, exc: MedPredictAPIException) -> JSONResponse:
    logger.warning(f"Handled MedPredictAPIException [{exc.code}] on {request.url.path}: {exc.message}")
    return format_error_response(code=exc.code, message=exc.message, details=exc.details, status_code=exc.status_code)

async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    code = "HTTP_ERROR"
    if exc.status_code == 404:
        code = "RESOURCE_NOT_FOUND"
    elif exc.status_code == 401:
        code = "UNAUTHORIZED"
    elif exc.status_code == 403:
        code = "FORBIDDEN"
    return format_error_response(code=code, message=str(exc.detail), status_code=exc.status_code)

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    details = []
    for err in exc.errors():
        details.append({
            "field": ".".join(str(loc) for loc in err.get("loc", [])),
            "issue": err.get("msg", "Invalid value"),
            "type": err.get("type", "value_error")
        })
    return format_error_response(
        code="REQUEST_VALIDATION_ERROR",
        message="Request payload failed schema validation",
        details=details,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )

async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.critical(f"Unhandled internal server error on {request.url.path}: {exc}", exc_info=True)
    return format_error_response(
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected internal server error occurred. Please contact the administrator.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
