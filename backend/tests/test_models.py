"""
MedPredict AI — Database ORM Models Test Suite
Validates relational schema, constraints, relationships, and queries across all domains.
"""

from datetime import date
from backend.app.models.user import User, Role, Permission
from backend.app.models.patient import Patient, MedicalProfile, Assessment
from backend.app.models.disease import Disease, DiseaseFeature
from backend.app.models.dataset import Dataset, DatasetVersion, DataQualityReport
from backend.app.models.model import MLModel, Experiment, TrainingRun, ModelVersion
from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.audit import AuditLog, SystemEvent, SecurityEvent
from backend.app.models.job import Job, Notification
from backend.app.models.report import Report
from backend.app.models.setting import SystemSetting

def test_user_and_role_models(db_session):
    # Create Role
    role = Role(name="PATIENT", description="Patient user role")
    db_session.add(role)
    db_session.flush()

    # Create User
    user = User(
        email="patient.test@medpredict.ai",
        hashed_password="mock_hashed_password",
        first_name="Jane",
        last_name="Doe",
        is_active=True,
        is_verified=True
    )
    user.roles.append(role)
    db_session.add(user)
    db_session.flush()

    # Verify query and property
    retrieved = db_session.query(User).filter_by(email="patient.test@medpredict.ai").first()
    assert retrieved is not None
    assert retrieved.full_name == "Jane Doe"
    assert retrieved.has_role("PATIENT") is True
    assert retrieved.has_role("ADMIN") is False

def test_patient_and_clinical_models(db_session):
    user = User(
        email="patient.clinical@medpredict.ai",
        hashed_password="mock_hashed_password",
        first_name="John",
        last_name="Smith"
    )
    db_session.add(user)
    db_session.flush()

    patient = Patient(
        user_id=user.id,
        date_of_birth=date(1985, 5, 20),
        gender="Male",
        blood_group="O+",
        emergency_contact="555-0199"
    )
    db_session.add(patient)
    db_session.flush()

    med_profile = MedicalProfile(
        patient_id=patient.id,
        allergies="Penicillin",
        chronic_conditions="Hypertension",
        family_history="Type 2 Diabetes in maternal grandfather"
    )
    db_session.add(med_profile)
    db_session.flush()

    assert patient.medical_profile is not None
    assert patient.medical_profile.allergies == "Penicillin"

def test_disease_and_features_models(db_session):
    disease = Disease(
        name="Diabetes",
        slug="diabetes",
        category="Endocrine",
        description="Type 2 Diabetes risk assessment"
    )
    db_session.add(disease)
    db_session.flush()

    feature = DiseaseFeature(
        disease_id=disease.id,
        name="glucose",
        data_type="numeric",
        unit="mg/dL",
        min_value=40.0,
        max_value=300.0,
        is_required=True
    )
    db_session.add(feature)
    db_session.flush()

    assert len(disease.features) == 1
    assert disease.features[0].name == "glucose"

def test_prediction_and_explanation_models(db_session):
    # Setup disease, user, model
    disease = Disease(name="Heart Disease", slug="heart_disease", category="Cardiovascular")
    db_session.add(disease)
    db_session.flush()

    dataset = Dataset(name="Cleveland Heart Demo", disease_id=disease.id)
    db_session.add(dataset)
    db_session.flush()

    ds_ver = DatasetVersion(
        dataset_id=dataset.id,
        version_tag="1.0.0",
        file_path="/data/datasets/heart.csv",
        file_format="csv",
        row_count=303,
        column_count=14,
        checksum_sha256="abc123hash"
    )
    db_session.add(ds_ver)
    db_session.flush()

    experiment = Experiment(name="Heart Logistic Baseline", disease_id=disease.id)
    db_session.add(experiment)
    db_session.flush()

    run = TrainingRun(
        experiment_id=experiment.id,
        dataset_version_id=ds_ver.id,
        algorithm="LogisticRegression",
        status="completed"
    )
    db_session.add(run)
    db_session.flush()

    ml_model = MLModel(name="Heart Disease Risk Model", disease_id=disease.id)
    db_session.add(ml_model)
    db_session.flush()

    m_ver = ModelVersion(
        model_id=ml_model.id,
        training_run_id=run.id,
        version_tag="1.0.0",
        artifact_path="/models/heart_v1.joblib",
        artifact_hash_sha256="modelhash123",
        status="active"
    )
    db_session.add(m_ver)
    db_session.flush()

    # Create Prediction
    prediction = Prediction(
        model_version_id=m_ver.id,
        disease_id=disease.id,
        probability=0.78,
        risk_level="HIGH"
    )
    db_session.add(prediction)
    db_session.flush()

    p_input = PredictionInput(
        prediction_id=prediction.id,
        input_features_json='{"age": 62, "cholesterol": 280}'
    )
    db_session.add(p_input)

    explanation = Explanation(
        prediction_id=prediction.id,
        method="SHAP_TREE",
        feature_contributions_json='{"cholesterol": +0.22, "age": +0.15}',
        base_value=0.41
    )
    db_session.add(explanation)
    db_session.flush()

    # Assert relationships
    assert prediction.input_data is not None
    assert prediction.explanation is not None
    assert prediction.explanation.base_value == 0.41
    assert prediction.risk_level == "HIGH"
