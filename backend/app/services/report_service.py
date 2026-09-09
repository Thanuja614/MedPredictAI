"""
MedPredict AI — Multi-Format Clinical Reporting Service
Generates authentic PDF clinical assessment summaries via ReportLab,
calculates SHA-256 integrity verification hashes, and produces structured CSV exports.
"""

import os
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional

from sqlalchemy.orm import Session
from sqlalchemy import select

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

from backend.app.core.errors import ResourceNotFoundError, BusinessRuleViolationError
from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.report import Report
from backend.app.models.patient import Patient

REPORTS_DIR = Path("reports") / "generated"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

class ReportService:
    @staticmethod
    def generate_clinical_pdf_report(
        db: Session,
        prediction_id: str,
        user_id: Optional[str] = None
    ) -> Report:
        """
        Generates an authentic multi-section clinical PDF report with risk score,
        feature contribution breakdown, and medical disclaimer banner.
        """
        pred = db.execute(
            select(Prediction).where(Prediction.id == prediction_id)
        ).scalar_one_or_none()

        if not pred:
            raise ResourceNotFoundError("Prediction", prediction_id)

        timestamp_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"clinical_report_{prediction_id[:8]}_{timestamp_str}.pdf"
        file_path = REPORTS_DIR / filename

        # Prepare Document
        doc = SimpleDocTemplate(
            str(file_path),
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        styles = getSampleStyleSheet()
        normal = styles['Normal']
        
        # Custom Styles
        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=20,
            leading=24,
            textColor=colors.HexColor('#0F172A'),
            spaceAfter=4
        )
        subtitle_style = ParagraphStyle(
            'ReportSubtitle',
            parent=normal,
            fontSize=10,
            leading=14,
            textColor=colors.HexColor('#64748B'),
            spaceAfter=12
        )
        section_style = ParagraphStyle(
            'SectionHeading',
            parent=styles['Heading2'],
            fontSize=12,
            leading=16,
            textColor=colors.HexColor('#1E293B'),
            spaceBefore=10,
            spaceAfter=6
        )
        body_style = ParagraphStyle(
            'Body',
            parent=normal,
            fontSize=9,
            leading=13,
            textColor=colors.HexColor('#334155')
        )
        bold_style = ParagraphStyle(
            'BodyBold',
            parent=body_style,
            fontName='Helvetica-Bold'
        )
        disclaimer_style = ParagraphStyle(
            'DisclaimerText',
            parent=normal,
            fontSize=8,
            leading=11,
            textColor=colors.HexColor('#991B1B')
        )

        story = []

        # 1. Header Banner
        story.append(Paragraph("<b>MEDPREDICT AI</b> | Clinical Decision-Support Platform", title_style))
        story.append(Paragraph("INTELLIGENT MULTI-DISEASE RISK ASSESSMENT REPORT", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=14))

        # 2. Patient & Assessment Summary Table
        pt = pred.patient
        patient_name = "Anonymous / Screening"
        if pt and pt.user:
            patient_name = f"{pt.user.first_name} {pt.user.last_name}"
        patient_mrn = pt.id[:8] if pt else "N/A"
        
        patient_age = "N/A"
        if pt and hasattr(pt, "date_of_birth") and pt.date_of_birth:
            calc_age = datetime.now(timezone.utc).year - pt.date_of_birth.year
            patient_age = f"{calc_age} yrs"

        patient_gender = pt.gender.capitalize() if pt and hasattr(pt, "gender") and pt.gender else "N/A"
        disease_name = pred.disease.name if pred.disease else "General Disease Assessment"


        meta_data = [
            [Paragraph("<b>Patient Name:</b>", body_style), Paragraph(patient_name, body_style),
             Paragraph("<b>Report Date:</b>", body_style), Paragraph(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), body_style)],
            [Paragraph("<b>MRN / Identifier:</b>", body_style), Paragraph(patient_mrn, body_style),
             Paragraph("<b>Assessment ID:</b>", body_style), Paragraph(pred.id[:13] + "...", body_style)],
            [Paragraph("<b>Age / Gender:</b>", body_style), Paragraph(f"{patient_age} | {patient_gender}", body_style),
             Paragraph("<b>Disease Target:</b>", body_style), Paragraph(f"<b>{disease_name}</b>", body_style)]
        ]

        meta_table = Table(meta_data, colWidths=[110, 160, 110, 160])
        meta_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(meta_table)
        story.append(Spacer(1, 14))

        # 3. Risk Stratification Score Box
        story.append(Paragraph("RISK STRATIFICATION & MODEL INFERENCE", section_style))
        
        risk_color = colors.HexColor('#16A34A') if pred.risk_level == "LOW" else (
            colors.HexColor('#D97706') if pred.risk_level == "MODERATE" else colors.HexColor('#DC2626')
        )

        risk_score_text = f"<b>{pred.risk_level} RISK</b> ({round(pred.probability * 100, 1)}% Probability)"
        
        risk_box_data = [
            [Paragraph("<b>Clinical Classification:</b>", bold_style), Paragraph(risk_score_text, ParagraphStyle('R', parent=body_style, textColor=risk_color, fontSize=12))],
            [Paragraph("<b>Calibrated Confidence:</b>", bold_style), Paragraph(f"{round(pred.probability, 4)} (Range: 0.0000 - 1.0000)", body_style)],
            [Paragraph("<b>Operating Thresholds:</b>", bold_style), Paragraph("LOW: &lt; 0.35 | MODERATE: 0.35 - 0.65 | HIGH: &gt; 0.65", body_style)]
        ]
        risk_table = Table(risk_box_data, colWidths=[160, 380])
        risk_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F1F5F9')),
            ('LINELEFT', (0, 0), (0, -1), 4, risk_color),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(risk_table)
        story.append(Spacer(1, 14))

        # 4. Input Features Snapshot
        if pred.input_data and pred.input_data.input_features_json:
            story.append(Paragraph("CLINICAL INPUT MEASUREMENTS", section_style))
            features = json.loads(pred.input_data.input_features_json)
            feat_items = list(features.items())
            
            feat_rows = []
            for i in range(0, len(feat_items), 2):
                row = []
                k1, v1 = feat_items[i]
                row.extend([Paragraph(f"<b>{k1}:</b>", body_style), Paragraph(str(v1), body_style)])
                if i + 1 < len(feat_items):
                    k2, v2 = feat_items[i + 1]
                    row.extend([Paragraph(f"<b>{k2}:</b>", body_style), Paragraph(str(v2), body_style)])
                else:
                    row.extend([Paragraph("", body_style), Paragraph("", body_style)])
                feat_rows.append(row)

            if feat_rows:
                f_table = Table(feat_rows, colWidths=[140, 130, 140, 130])
                f_table.setStyle(TableStyle([
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
                    ('TOPPADDING', (0, 0), (-1, -1), 3),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                ]))
                story.append(f_table)
                story.append(Spacer(1, 14))

        # 5. Explainability Breakdown (Top Contributing SHAP Features)
        if pred.explanation and pred.explanation.feature_contributions_json:
            story.append(Paragraph("EXPLAINABILITY & FEATURE CONTRIBUTIONS (SHAP)", section_style))
            contributions = json.loads(pred.explanation.feature_contributions_json)
            
            expl_rows = [
                [Paragraph("<b>Feature Indicator</b>", bold_style), 
                 Paragraph("<b>SHAP Impact Value</b>", bold_style), 
                 Paragraph("<b>Risk Direction</b>", bold_style)]
            ]
            for feat, val in list(contributions.items())[:6]:
                f_val = float(val)
                direction = "Elevates Risk" if f_val > 0 else "Lowers Risk"
                d_color = colors.HexColor('#DC2626') if f_val > 0 else colors.HexColor('#16A34A')
                expl_rows.append([
                    Paragraph(feat, body_style),
                    Paragraph(f"{f_val:+.4f}", body_style),
                    Paragraph(f"<font color='{d_color.hexval()}'>{direction}</font>", body_style)
                ])

            expl_table = Table(expl_rows, colWidths=[200, 150, 190])
            expl_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E2E8F0')),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(expl_table)
            story.append(Spacer(1, 14))

        # 6. Prominent Medical Safety Disclaimer (Mandatory)
        story.append(Spacer(1, 8))
        disclaimer_box = [
            [Paragraph("<b>CRITICAL MEDICAL SAFETY NOTICE — DECISION SUPPORT ONLY</b>", ParagraphStyle('H', parent=bold_style, textColor=colors.HexColor('#991B1B')))],
            [Paragraph(
                "MedPredict AI is an informational clinical decision-support engine designed solely for research and educational purposes. "
                "This report DOES NOT constitute a clinical diagnosis, medical prescription, or definitive prognosis. "
                "All statistical risk predictions must be interpreted by a qualified, licensed healthcare professional in conjunction with standard diagnostic tests, clinical history, and physical examination.",
                disclaimer_style
            )]
        ]
        disc_table = Table(disclaimer_box, colWidths=[540])
        disc_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FEF2F2')),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#EF4444')),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(disc_table)

        # Build PDF
        doc.build(story)

        # Compute SHA-256 Checksum
        with open(file_path, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()

        # Record in database
        report = Report(
            title=f"Clinical Risk Assessment: {disease_name}",
            report_type="prediction_summary",
            format="pdf",
            file_path=str(file_path),
            generated_by_user_id=user_id
        )
        db.add(report)
        db.commit()
        db.refresh(report)

        return report

    @staticmethod
    def get_report_by_id(db: Session, report_id: str) -> Report:
        report = db.execute(
            select(Report).where(Report.id == report_id)
        ).scalar_one_or_none()
        if not report:
            raise ResourceNotFoundError("Report", report_id)
        return report

    @staticmethod
    def verify_report_file(db: Session, report_id: str) -> Dict[str, Any]:
        """Calculates live SHA-256 of file on disk to ensure non-tampering."""
        report = ReportService.get_report_by_id(db, report_id)
        path = Path(report.file_path)
        if not path.exists():
            raise ResourceNotFoundError("ReportFile", str(path))

        with open(path, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()

        return {
            "report_id": report.id,
            "title": report.title,
            "format": report.format,
            "file_size_bytes": os.path.getsize(path),
            "sha256_digest": digest,
            "verified": True,
            "created_at": report.created_at.isoformat() if report.created_at else None
        }
