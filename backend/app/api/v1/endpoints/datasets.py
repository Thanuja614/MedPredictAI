"""
MedPredict AI — Dataset Ingestion & Quality Profile Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form, status
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.dataset import DatasetRead, DatasetVersionRead
from backend.app.services.dataset_service import DatasetService
from backend.app.security.deps import (
    get_current_active_user,
    require_roles
)
from backend.app.core.errors import EntityNotFoundError
from backend.app.models.user import User

router = APIRouter(prefix="/datasets", tags=["Datasets & Quality"])

@router.post(
    "/upload",
    response_model=DatasetVersionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Upload & Profile Dataset (Data Scientist & Admin Only)",
    dependencies=[Depends(require_roles("DATA_SCIENTIST", "ADMIN"))]
)
def upload_dataset(
    disease_id: str = Form(..., description="Target disease UUID"),
    dataset_name: Optional[str] = Form(None, description="Custom dataset name"),
    file: UploadFile = File(..., description="Tabular data file (CSV, XLSX, Parquet)"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Ingests tabular dataset, calculates SHA-256 checksum, and generates an automated data quality score.
    """
    return DatasetService.upload_dataset(
        db=db,
        file=file,
        disease_id=disease_id,
        user_id=current_user.id,
        dataset_name=dataset_name
    )

@router.get(
    "/",
    response_model=List[DatasetRead],
    summary="List Datasets",
    dependencies=[Depends(require_roles("DATA_SCIENTIST", "ADMIN", "DOCTOR", "AUDITOR"))]
)
def list_datasets(
    disease_id: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Retrieves all registered datasets and their version histories."""
    return DatasetService.list_datasets(db, disease_id=disease_id)

@router.get(
    "/versions/{version_id}",
    response_model=DatasetVersionRead,
    summary="Get Dataset Version & Quality Report",
    dependencies=[Depends(require_roles("DATA_SCIENTIST", "ADMIN", "AUDITOR"))]
)
def get_dataset_version(
    version_id: str,
    db: Session = Depends(get_db)
):
    """Retrieves dataset version metadata and automated quality audit report."""
    ver = DatasetService.get_version(db, version_id)
    if not ver:
        raise EntityNotFoundError(f"Dataset version '{version_id}' not found")
    return ver
