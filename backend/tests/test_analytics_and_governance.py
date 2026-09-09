"""
MedPredict AI — Analytics, Governance, Reports, Jobs & Audit Integration Tests
"""

import pytest
import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.core.database import SessionLocal
from backend.app.models.user import User
from backend.app.models.patient import Patient
from backend.app.models.disease import Disease
from backend.app.models.model import MLModel, ModelVersion, TrainingRun, Experiment
from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.dataset import Dataset, DatasetVersion
from backend.app.ml.monitoring.drift_detector import DriftDetector
from backend.app.services.analytics_service import AnalyticsService
from backend.app.services.governance_service import GovernanceService
from backend.app.services.report_service import ReportService
from backend.app.services.job_service import JobService
from backend.app.services.notification_service import NotificationService
from backend.app.services.audit_service import AuditService

client = TestClient(app)

def test_drift_detector_psi_and_ks():
    """Verify authentic statistical calculations for KS test and PSI."""
    np.random.seed(42)
    ref_data = np.random.normal(loc=50.0, scale=10.0, size=200)
    
    # Identical distribution -> zero PSI
    same_data = ref_data.copy()
    psi_zero = DriftDetector.calculate_psi(ref_data, same_data)
    assert psi_zero < 0.01, f"Expected near zero PSI for identical distribution, got {psi_zero}"

    # Shifted distribution -> high PSI
    shifted_data = ref_data + 25.0
    psi_high = DriftDetector.calculate_psi(ref_data, shifted_data)
    assert psi_high > 0.2, f"Expected high PSI for shifted distribution, got {psi_high}"

    ref_df = pd.DataFrame({"glucose": ref_data, "age": np.random.randint(20, 80, 200)})
    curr_df = pd.DataFrame({"glucose": shifted_data, "age": np.random.randint(20, 80, 200)})

    res = DriftDetector.evaluate_feature_drift(ref_df, curr_df, ["glucose", "age"])
    assert res["overall_drift_detected"] is True
    assert "glucose" in res["drifted_features"]
    assert res["feature_metrics"]["glucose"]["severity"] == "SIGNIFICANT"

def test_fairness_metrics():
    """Verify disparate impact and demographic parity calculations."""
    preds = [1, 1, 0, 1, 0, 0, 1, 0]
    sens = ["M", "M", "M", "M", "F", "F", "F", "F"]

    fairness = DriftDetector.evaluate_fairness(
        predictions=preds,
        sensitive_attribute=sens,
        privileged_value="M",
        unprivileged_value="F"
    )
    assert fairness["valid"] is True
    assert "disparate_impact_ratio" in fairness
    assert "demographic_parity_difference" in fairness

def test_analytics_and_reporting_lifecycle(db_session):
    """Test longitudinal trajectory calculation and authentic PDF report generation."""
    db = db_session
    try:
        # Create a test user and patient
        import datetime as dt
        test_user = User(
            email="eleanor.test@medpredict.local",
            hashed_password="dummy_password_hash",
            first_name="Eleanor",
            last_name="Vance",
            is_active=True
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)

        patient = Patient(
            user_id=test_user.id,
            date_of_birth=dt.date(1980, 4, 12),
            gender="female",
            blood_group="A+"
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)

        # Get or create disease
        disease = db.query(Disease).filter_by(slug="diabetes").first()
        if not disease:
            disease = Disease(
                name="Diabetes Mellitus",
                slug="diabetes",
                category="Endocrine & Metabolic",
                description="Chronic metabolic disease characterized by elevated blood glucose.",
                version="1.0.0"
            )

            db.add(disease)
            db.commit()
            db.refresh(disease)


        # Create or fetch MLModel and version
        ml_model = db.query(MLModel).filter_by(disease_id=disease.id).first()
        if not ml_model:
            ml_model = MLModel(name="Diabetes Gradient Boosted Classifier", disease_id=disease.id)
            db.add(ml_model)
            db.commit()
            db.refresh(ml_model)

        version = db.query(ModelVersion).filter_by(model_id=ml_model.id).first()
        if not version:
            # Need experiment and training run
            exp = Experiment(name="Baseline Experiment", disease_id=disease.id)
            db.add(exp)
            db.commit()
            db.refresh(exp)

            ds = db.query(Dataset).filter_by(disease_id=disease.id).first()
            if not ds:
                ds = Dataset(name="Diabetes Data", disease_id=disease.id)
                db.add(ds)
                db.commit()
            ds_ver = db.query(DatasetVersion).filter_by(dataset_id=ds.id).first()
            if not ds_ver:
                ds_ver = DatasetVersion(

                    dataset_id=ds.id,
                    version_tag="v1.0",
                    file_path="data/datasets/diabetes/diabetes.csv",
                    file_format="csv",
                    row_count=400,
                    column_count=9,
                    checksum_sha256="dummy_sha256_checksum"
                )
                db.add(ds_ver)
                db.commit()
                db.refresh(ds_ver)


            tr = TrainingRun(experiment_id=exp.id, dataset_version_id=ds_ver.id, algorithm="RandomForest", status="completed")
            db.add(tr)
            db.commit()
            db.refresh(tr)

            version = ModelVersion(model_id=ml_model.id, training_run_id=tr.id, version_tag="v1.0.0", artifact_path="models/artifacts/diabetes/v1.0.0", artifact_hash_sha256="abc12345", status="active")
            db.add(version)
            db.commit()
            db.refresh(version)

        # Insert 2 sequential predictions to test timeline
        p1 = Prediction(
            patient_id=patient.id,
            disease_id=disease.id,
            model_version_id=version.id,
            probability=0.32,
            risk_level="LOW"
        )
        db.add(p1)
        db.flush()

        inp1 = PredictionInput(prediction_id=p1.id, input_features_json='{"Glucose": 110, "BMI": 26.5}')
        expl1 = Explanation(prediction_id=p1.id, feature_contributions_json='{"Glucose": 0.05, "BMI": -0.02}')
        db.add_all([inp1, expl1])

        p2 = Prediction(
            patient_id=patient.id,
            disease_id=disease.id,
            model_version_id=version.id,
            probability=0.68,
            risk_level="HIGH"
        )
        db.add(p2)
        db.flush()

        inp2 = PredictionInput(prediction_id=p2.id, input_features_json='{"Glucose": 165, "BMI": 32.1}')
        expl2 = Explanation(prediction_id=p2.id, feature_contributions_json='{"Glucose": 0.25, "BMI": 0.12}')
        db.add_all([inp2, expl2])
        db.commit()

        # 1. Test Analytics Service
        timeline = AnalyticsService.get_patient_timeline(db, patient.id, disease.id)
        assert timeline["total_assessments"] >= 2
        assert len(timeline["timeline"]) >= 2
        assert "disclaimer" in timeline

        dist = AnalyticsService.get_population_risk_distribution(db, disease.id)
        assert dist["total_inferences"] >= 2
        assert "percentages" in dist

        stats = AnalyticsService.get_system_overview(db)
        assert stats["total_patients"] >= 1
        assert stats["total_predictions"] >= 2

        # 2. Test Report Service (PDF generation + SHA-256 integrity verification)
        report = ReportService.generate_clinical_pdf_report(db, p2.id)
        assert report.id is not None
        assert report.format == "pdf"
        
        verification = ReportService.verify_report_file(db, report.id)
        assert verification["verified"] is True
        assert len(verification["sha256_digest"]) == 64

        # 3. Test Jobs Service
        job = JobService.create_job(db, "model_training", {"disease": "diabetes"})
        assert job.status == "pending"
        JobService.update_job_progress(db, job.id, 50, "running")
        updated_job = JobService.get_job(db, job.id)
        assert updated_job.progress_percent == 50
        assert updated_job.status == "running"

        # 4. Test Notification Service
        notif_user = db.query(User).filter_by(email="doctor@medpredict.local").first() or test_user
        notif = NotificationService.create_notification(db, notif_user.id, "High Risk Alert", "Patient Eleanor scored HIGH risk", "alert")
        assert notif.id is not None
        notifs = NotificationService.get_user_notifications(db, notif_user.id, unread_only=True)
        assert any(n["id"] == notif.id for n in notifs)

        # 5. Test Audit Service
        audit = AuditService.log(db, "TEST_ACTION", "Patient", patient.id, details={"flag": "ok"})
        assert audit.id is not None
        logs = AuditService.query_logs(db, action="TEST_ACTION")
        assert logs["total_returned"] >= 1
        csv_data = AuditService.export_csv(db)
        assert "TEST_ACTION" in csv_data
    finally:
        pass


