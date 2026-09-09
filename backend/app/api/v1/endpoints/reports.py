"""
MedPredict AI — Clinical & Diagnostic Report Endpoints
"""

from typing import Dict, Any, List
from pathlib import Path
from fastapi import APIRouter, Depends, Path as FPath, Response
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.security.deps import get_current_active_user
from backend.app.services.report_service import ReportService

router = APIRouter()

@router.post("/generate/{prediction_id}")
def generate_prediction_report(
    prediction_id: str = FPath(..., description="Target Prediction ID"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Generates an authentic PDF clinical summary report for the given prediction."""
    report = ReportService.generate_clinical_pdf_report(
        db=db,
        prediction_id=prediction_id,
        user_id=current_user.id
    )
    return {
        "report_id": report.id,
        "title": report.title,
        "format": report.format,
        "download_url": f"/api/v1/reports/{report.id}/download",
        "created_at": report.created_at.isoformat() if report.created_at else None
    }

@router.get("/{report_id}/download")
def download_report(
    report_id: str = FPath(..., description="Report ID to download"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Downloads the generated PDF report."""
    report = ReportService.get_report_by_id(db, report_id)
    file_path = Path(report.file_path)
    
    return FileResponse(
        path=str(file_path),
        filename=file_path.name,
        media_type="application/pdf"
    )

@router.get("/{report_id}/verify")
def verify_report(
    report_id: str = FPath(..., description="Report ID to verify"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Dict[str, Any]:
    """Computes SHA-256 verification digest to guarantee document authenticity and integrity."""
    return ReportService.verify_report_file(db, report_id)

@router.get("")
def list_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[Dict[str, Any]]:
    """Lists recent generated reports."""
    reports = db.execute(
        select(Report).order_by(desc(Report.created_at)).limit(50)
    ).scalars().all()
    
    return [
        {
            "id": r.id,
            "title": r.title,
            "report_type": r.report_type,
            "format": r.format,
            "created_at": r.created_at.isoformat() if r.created_at else None
        }
        for r in reports
    ]
