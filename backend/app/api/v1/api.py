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
    predictions,
    analytics,
    governance,
    reports,
    jobs,
    notifications,
    audit,
    settings
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

# Longitudinal Risk Analytics & Population Cohort
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

# Model Governance & Drift Detection
api_router.include_router(governance.router, prefix="/governance", tags=["Model Governance"])

# Clinical & Diagnostic Reports
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])

# Background Jobs
api_router.include_router(jobs.router, prefix="/jobs", tags=["Background Jobs"])

# In-App Notifications
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

# Security & Compliance Audit Trail
api_router.include_router(audit.router, prefix="/audit", tags=["Audit Trail"])

# Dynamic System Settings
api_router.include_router(settings.router, prefix="/settings", tags=["System Settings"])

