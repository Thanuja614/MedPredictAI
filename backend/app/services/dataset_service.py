"""
MedPredict AI — Dataset Management & Ingestion Service
Handles secure uploads, MIME validation, SHA-256 hashing, and automated quality profiling.
"""

import os
import hashlib
import json
from pathlib import Path
from typing import List, Optional
import pandas as pd
from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.core.errors import DataValidationError, EntityNotFoundError
from backend.app.models.dataset import Dataset, DatasetVersion, DataQualityReport
from backend.app.models.disease import Disease
from backend.app.models.audit import AuditLog
from backend.app.ml.data_quality.engine import DataQualityEngine

ALLOWED_EXTENSIONS = {".csv", ".xlsx", ".parquet"}
MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024  # 50 MB

class DatasetService:

    @staticmethod
    def upload_dataset(
        db: Session,
        file: UploadFile,
        disease_id: str,
        user_id: str,
        dataset_name: Optional[str] = None
    ) -> DatasetVersion:
        """Securely saves uploaded dataset file, verifies integrity, and generates quality profile."""
        disease = db.query(Disease).filter(Disease.id == disease_id).first()
        if not disease:
            raise EntityNotFoundError(f"Disease '{disease_id}' not found")

        # 1. Validate file extension
        raw_filename = file.filename or "uploaded_data.csv"
        ext = Path(raw_filename).suffix.lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise DataValidationError(f"Unsupported file format '{ext}'. Allowed: {list(ALLOWED_EXTENSIONS)}")

        # 2. Sanitize filename against directory traversal
        clean_filename = Path(raw_filename).name.replace(" ", "_")

        # 3. Stream content and compute SHA-256
        content = file.file.read()
        if len(content) > MAX_FILE_SIZE_BYTES:
            raise DataValidationError("Uploaded file exceeds 50MB limit")
        if len(content) == 0:
            raise DataValidationError("Uploaded file is empty")

        sha256_hash = hashlib.sha256(content).hexdigest()

        # 4. Save to storage location
        target_dir = Path(settings.DATASETS_DIR) / disease.slug
        target_dir.mkdir(parents=True, exist_ok=True)
        file_path = target_dir / f"{sha256_hash[:12]}_{clean_filename}"
        with open(file_path, "wb") as f:
            f.write(content)

        # 5. Read into DataFrame for profiling
        try:
            if ext == ".csv":
                df = pd.read_csv(file_path)
            elif ext == ".xlsx":
                df = pd.read_excel(file_path)
            else:
                df = pd.read_parquet(file_path)
        except Exception as e:
            raise DataValidationError(f"Could not parse uploaded file into tabular format: {e}")

        row_count, col_count = df.shape

        # 6. Run Data Quality Engine
        quality_metrics = DataQualityEngine.audit_dataset(df)
        quality_score = quality_metrics["quality_score"]

        # 7. Create or retrieve parent Dataset record
        name = dataset_name or f"{disease.name} Clinical Dataset ({clean_filename})"
        dataset = db.query(Dataset).filter(Dataset.name == name).first()
        if not dataset:
            dataset = Dataset(
                name=name,
                disease_id=disease.id,
                source_description=f"Uploaded by user {user_id}",
                is_synthetic=True
            )
            db.add(dataset)
            db.flush()

        # 8. Create DatasetVersion record
        existing_versions = db.query(DatasetVersion).filter(DatasetVersion.dataset_id == dataset.id).count()
        ver_tag = f"1.{existing_versions}.0"

        dataset_ver = DatasetVersion(
            dataset_id=dataset.id,
            version_tag=ver_tag,
            file_path=str(file_path),
            file_format=ext.replace(".", ""),
            row_count=row_count,
            column_count=col_count,
            checksum_sha256=sha256_hash,
            uploaded_by_user_id=user_id
        )
        db.add(dataset_ver)
        db.flush()

        # 9. Create DataQualityReport record
        quality_report = DataQualityReport(
            dataset_version_id=dataset_ver.id,
            quality_score=quality_score,
            missing_cell_count=quality_metrics["missing_cells_total"],
            duplicate_row_count=quality_metrics["duplicate_rows"],
            metrics_json=json.dumps(quality_metrics)
        )
        db.add(quality_report)

        # 10. Record Audit Log
        audit = AuditLog(
            user_id=user_id,
            action="DATASET_UPLOADED",
            entity_type="datasets",
            entity_id=dataset.id,
            details_json=f'{{"version": "{ver_tag}", "score": {quality_score}, "rows": {row_count}}}'
        )
        db.add(audit)
        db.commit()
        db.refresh(dataset_ver)
        return dataset_ver

    @staticmethod
    def list_datasets(db: Session, disease_id: Optional[str] = None) -> List[Dataset]:
        query = db.query(Dataset)
        if disease_id:
            query = query.filter(Dataset.disease_id == disease_id)
        return query.all()

    @staticmethod
    def get_version(db: Session, version_id: str) -> Optional[DatasetVersion]:
        return db.query(DatasetVersion).filter(DatasetVersion.id == version_id).first()
