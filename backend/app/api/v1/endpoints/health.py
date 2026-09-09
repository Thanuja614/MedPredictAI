"""
MedPredict AI — Health & Observability Endpoints
Provides liveness, readiness, and system uptime diagnostic probes.
"""

from datetime import datetime, timezone
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from backend.app.core.config import settings
from backend.app.core.database import check_db_health

router = APIRouter(tags=["Health & Observability"])

START_TIME = datetime.now(timezone.utc)

@router.get("/health", summary="Liveness Probe", status_code=status.HTTP_200_OK)
def liveness_check():
    """
    Kubernetes / Docker liveness probe confirming the web server process is responsive.
    """
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.PROJECT_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@router.get("/ready", summary="Readiness Probe")
def readiness_check():
    """
    Readiness probe verifying downstream database and infrastructure connectivity.
    """
    db_ok = check_db_health()
    uptime_seconds = (datetime.now(timezone.utc) - START_TIME).total_seconds()
    
    is_ready = db_ok
    status_code = status.HTTP_200_OK if is_ready else status.HTTP_503_SERVICE_UNAVAILABLE

    payload = {
        "status": "ready" if is_ready else "degraded",
        "uptime_seconds": round(uptime_seconds, 2),
        "components": {
            "database": "connected" if db_ok else "disconnected",
            "redis": "available" if settings.CACHE_ENABLED else "disabled"
        },
        "disclaimer_enforced": settings.SYSTEM_DISCLAIMER_ENFORCED,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    return JSONResponse(status_code=status_code, content=payload)
