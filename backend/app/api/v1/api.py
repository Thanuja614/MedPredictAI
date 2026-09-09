"""
MedPredict AI — API v1 Master Router
Aggregates all domain routes under the /api/v1 prefix.
"""

from fastapi import APIRouter
from backend.app.api.v1.endpoints import health

api_router = APIRouter()

# Core health & diagnostics
api_router.include_router(health.router)
