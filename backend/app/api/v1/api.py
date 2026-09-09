"""
MedPredict AI — API v1 Master Router
Aggregates all domain routes under the /api/v1 prefix.
"""

from fastapi import APIRouter
from backend.app.api.v1.endpoints import (
    health,
    auth,
    users,
    patients,
    diseases,
    datasets,
    predictions
)

api_router = APIRouter()

# Core health & diagnostics
api_router.include_router(health.router)

# Authentication & Access Control
api_router.include_router(auth.router)

# Users & Profile Management
api_router.include_router(users.router)

# Patients & Clinical Encounters
api_router.include_router(patients.router)

# Disease Framework & Symptom Screening
api_router.include_router(diseases.router)

# Dataset Ingestion & Data Quality
api_router.include_router(datasets.router)

# ML Predictions & Explainability
api_router.include_router(predictions.router)
