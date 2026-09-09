"""
MedPredict AI — Dataset & Quality Schemas
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class DataQualityReportRead(BaseModel):
    id: str
    dataset_version_id: str
    quality_score: float
    missing_cell_count: int
    duplicate_row_count: int
    metrics_json: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DatasetVersionRead(BaseModel):
    id: str
    dataset_id: str
    version_tag: str
    file_path: str
    file_format: str
    row_count: int
    column_count: int
    checksum_sha256: str
    uploaded_by_user_id: Optional[str] = None
    created_at: datetime
    quality_report: Optional[DataQualityReportRead] = None

    model_config = ConfigDict(from_attributes=True)

class DatasetRead(BaseModel):
    id: str
    name: str
    disease_id: str
    source_description: Optional[str] = None
    is_synthetic: bool
    created_at: datetime
    versions: List[DatasetVersionRead] = []

    model_config = ConfigDict(from_attributes=True)
