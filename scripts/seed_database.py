#!/usr/bin/env python3
"""
MedPredict AI — Database Seeding Engine
Populates system roles, permissions, development accounts, and 10 core disease schemas.
Strictly creates SYNTHETIC DEMONSTRATION DATA for development and testing.
"""

import sys
import os
from pathlib import Path
from datetime import date, datetime, timezone

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Ensure workspace root is in path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Allow CLI flag or environment fallback for local standalone seeding
if "--sqlite" in sys.argv or not os.getenv("DATABASE_URL"):
    if not os.getenv("DATABASE_URL") or os.getenv("DATABASE_URL").startswith("postgresql"):
        # If postgres is not running locally, use sqlite for standalone seed verification
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', 5432))
        sock.close()
        if result != 0:
            os.environ["DATABASE_URL"] = "sqlite:///./medpredict_dev.db"

from backend.app.core.database import SessionLocal, engine, Base
from backend.app.core.security import get_password_hash
from backend.app.models.user import User, Role, Permission, UserRole, RolePermission
from backend.app.models.patient import Patient, Doctor, MedicalProfile
from backend.app.models.disease import Disease, DiseaseFeature
from backend.app.models.setting import SystemSetting

ROLES_DATA = [
    {"name": "PATIENT", "description": "Patient user with access to self-assessments and prediction history"},
    {"name": "DOCTOR", "description": "Healthcare provider with clinical decision support access"},
    {"name": "DATA_SCIENTIST", "description": "Data scientist with dataset management and ML model training access"},
    {"name": "ADMIN", "description": "System administrator with user governance and health monitoring access"},
    {"name": "AUDITOR", "description": "Compliance auditor with read-only audit trail and security log access"}
]

PERMISSIONS_DATA = [
    {"name": "users:read", "module": "users", "description": "View user accounts"},
    {"name": "users:write", "module": "users", "description": "Manage user accounts"},
    {"name": "roles:assign", "module": "roles", "description": "Assign user roles"},
    {"name": "patients:read", "module": "patients", "description": "View patient clinical records"},
    {"name": "patients:write", "module": "patients", "description": "Create and update patient profiles"},
    {"name": "assessments:create", "module": "assessments", "description": "Create clinical assessment"},
    {"name": "predictions:evaluate", "module": "predictions", "description": "Run ML disease predictions"},
    {"name": "predictions:batch", "module": "predictions", "description": "Execute batch prediction jobs"},
    {"name": "datasets:manage", "module": "datasets", "description": "Upload and validate datasets"},
    {"name": "models:train", "module": "models", "description": "Train and register ML models"},
    {"name": "models:promote", "module": "models", "description": "Promote model to production"},
    {"name": "audit:read", "module": "audit", "description": "View immutable audit logs"},
    {"name": "system:manage", "module": "system", "description": "Configure system settings and view health"}
]

SAMPLE_USERS = [
    {
        "email": "admin@medpredict.ai",
        "password": "AdminPassword123!",
        "first_name": "Admin",
        "last_name": "User",
        "roles": ["ADMIN"]
    },
    {
        "email": "doctor@medpredict.ai",
        "password": "DoctorPassword123!",
        "first_name": "Sarah",
        "last_name": "Chen",
        "roles": ["DOCTOR"],
        "license": "MD-987654",
        "specialization": "Cardiology & Internal Medicine",
        "hospital": "Metropolitan Medical Center"
    },
    {
        "email": "datascientist@medpredict.ai",
        "password": "ScientistPassword123!",
        "first_name": "Alex",
        "last_name": "Rivers",
        "roles": ["DATA_SCIENTIST"]
    },
    {
        "email": "patient@medpredict.ai",
        "password": "PatientPassword123!",
        "first_name": "John",
        "last_name": "Doe",
        "roles": ["PATIENT"],
        "dob": date(1980, 4, 15),
        "gender": "Male",
        "blood_group": "A+",
        "emergency": "Jane Doe (555-0144)"
    },
    {
        "email": "auditor@medpredict.ai",
        "password": "AuditorPassword123!",
        "first_name": "Marcus",
        "last_name": "Vance",
        "roles": ["AUDITOR"]
    }
]

DISEASES_CATALOG = [
    {
        "name": "Diabetes",
        "slug": "diabetes",
        "category": "Endocrine & Metabolic",
        "description": "Risk prediction of Type-2 diabetes based on glycemic, anthropometric and clinical markers.",
        "features": [
            {"name": "pregnancies", "data_type": "numeric", "unit": "count", "min_value": 0, "max_value": 20, "is_required": True, "description": "Number of times pregnant"},
            {"name": "glucose", "data_type": "numeric", "unit": "mg/dL", "min_value": 40, "max_value": 300, "is_required": True, "description": "Plasma glucose concentration at 2 hours in an oral glucose tolerance test"},
            {"name": "blood_pressure", "data_type": "numeric", "unit": "mmHg", "min_value": 40, "max_value": 200, "is_required": True, "description": "Diastolic blood pressure"},
            {"name": "skin_thickness", "data_type": "numeric", "unit": "mm", "min_value": 5, "max_value": 100, "is_required": True, "description": "Triceps skin fold thickness"},
            {"name": "insulin", "data_type": "numeric", "unit": "mu U/ml", "min_value": 10, "max_value": 900, "is_required": True, "description": "2-Hour serum insulin"},
            {"name": "bmi", "data_type": "numeric", "unit": "kg/m^2", "min_value": 15.0, "max_value": 60.0, "is_required": True, "description": "Body Mass Index"},
            {"name": "diabetes_pedigree", "data_type": "numeric", "unit": "score", "min_value": 0.05, "max_value": 2.5, "is_required": True, "description": "Diabetes pedigree function (genetic score)"},
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 18, "max_value": 100, "is_required": True, "description": "Age in years"}
        ]
    },
    {
        "name": "Heart Disease",
        "slug": "heart_disease",
        "category": "Cardiovascular",
        "description": "Detection of coronary artery and cardiovascular risk indicators.",
        "features": [
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 20, "max_value": 100, "is_required": True, "description": "Age in years"},
            {"name": "sex", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 1, "is_required": True, "description": "Sex (1 = male; 0 = female)"},
            {"name": "chest_pain_type", "data_type": "categorical", "unit": "type", "min_value": 0, "max_value": 3, "is_required": True, "description": "Chest pain type (0-3)"},
            {"name": "resting_bp", "data_type": "numeric", "unit": "mmHg", "min_value": 80, "max_value": 220, "is_required": True, "description": "Resting blood pressure on admission"},
            {"name": "cholesterol", "data_type": "numeric", "unit": "mg/dL", "min_value": 100, "max_value": 600, "is_required": True, "description": "Serum cholesterol"},
            {"name": "fasting_blood_sugar", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)"},
            {"name": "resting_ecg", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 2, "is_required": True, "description": "Resting electrocardiographic results (0-2)"},
            {"name": "max_hr", "data_type": "numeric", "unit": "bpm", "min_value": 60, "max_value": 220, "is_required": True, "description": "Maximum heart rate achieved"},
            {"name": "exercise_angina", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "Exercise induced angina (1 = yes; 0 = no)"},
            {"name": "st_depression", "data_type": "numeric", "unit": "mm", "min_value": 0.0, "max_value": 7.0, "is_required": True, "description": "ST depression induced by exercise relative to rest"},
            {"name": "st_slope", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 2, "is_required": True, "description": "The slope of the peak exercise ST segment (0-2)"}
        ]
    },
    {
        "name": "Liver Disease",
        "slug": "liver_disease",
        "category": "Gastroenterology & Hepatology",
        "description": "Evaluation of hepatic biomarkers and enzymatic activity for liver impairment risk.",
        "features": [
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 10, "max_value": 95, "is_required": True, "description": "Age of the patient"},
            {"name": "gender", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 1, "is_required": True, "description": "Gender (1 = Male, 0 = Female)"},
            {"name": "total_bilirubin", "data_type": "numeric", "unit": "mg/dL", "min_value": 0.2, "max_value": 30.0, "is_required": True, "description": "Total Bilirubin"},
            {"name": "direct_bilirubin", "data_type": "numeric", "unit": "mg/dL", "min_value": 0.1, "max_value": 15.0, "is_required": True, "description": "Direct Bilirubin"},
            {"name": "alkaline_phosphatase", "data_type": "numeric", "unit": "IU/L", "min_value": 50, "max_value": 2000, "is_required": True, "description": "Alkaline Phosphatase"},
            {"name": "alamine_aminotransferase", "data_type": "numeric", "unit": "IU/L", "min_value": 5, "max_value": 1500, "is_required": True, "description": "Alamine Aminotransferase (ALT)"},
            {"name": "aspartate_aminotransferase", "data_type": "numeric", "unit": "IU/L", "min_value": 5, "max_value": 1500, "is_required": True, "description": "Aspartate Aminotransferase (AST)"},
            {"name": "total_proteins", "data_type": "numeric", "unit": "g/dL", "min_value": 2.0, "max_value": 10.0, "is_required": True, "description": "Total Proteins"},
            {"name": "albumin", "data_type": "numeric", "unit": "g/dL", "min_value": 1.0, "max_value": 6.0, "is_required": True, "description": "Albumin"},
            {"name": "ag_ratio", "data_type": "numeric", "unit": "ratio", "min_value": 0.2, "max_value": 3.0, "is_required": True, "description": "Albumin and Globulin Ratio"}
        ]
    },
    {
        "name": "Kidney Disease",
        "slug": "kidney_disease",
        "category": "Nephrology",
        "description": "Chronic kidney disease (CKD) risk evaluation from renal biochemical markers.",
        "features": [
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 10, "max_value": 95, "is_required": True, "description": "Age"},
            {"name": "blood_pressure", "data_type": "numeric", "unit": "mmHg", "min_value": 50, "max_value": 200, "is_required": True, "description": "Blood Pressure"},
            {"name": "specific_gravity", "data_type": "numeric", "unit": "sg", "min_value": 1.005, "max_value": 1.030, "is_required": True, "description": "Specific Gravity"},
            {"name": "albumin", "data_type": "categorical", "unit": "grade", "min_value": 0, "max_value": 5, "is_required": True, "description": "Albumin levels (0-5)"},
            {"name": "sugar", "data_type": "categorical", "unit": "grade", "min_value": 0, "max_value": 5, "is_required": True, "description": "Sugar levels (0-5)"},
            {"name": "blood_urea", "data_type": "numeric", "unit": "mg/dL", "min_value": 10, "max_value": 300, "is_required": True, "description": "Blood Urea"},
            {"name": "serum_creatinine", "data_type": "numeric", "unit": "mg/dL", "min_value": 0.4, "max_value": 15.0, "is_required": True, "description": "Serum Creatinine"},
            {"name": "sodium", "data_type": "numeric", "unit": "mEq/L", "min_value": 100, "max_value": 170, "is_required": True, "description": "Sodium"},
            {"name": "potassium", "data_type": "numeric", "unit": "mEq/L", "min_value": 2.0, "max_value": 8.0, "is_required": True, "description": "Potassium"},
            {"name": "hemoglobin", "data_type": "numeric", "unit": "g/dL", "min_value": 3.0, "max_value": 18.0, "is_required": True, "description": "Hemoglobin"}
        ]
    },
    {
        "name": "Breast Cancer",
        "slug": "breast_cancer",
        "category": "Oncology",
        "description": "Risk assessment for breast malignancy using cellular morphology descriptors.",
        "features": [
            {"name": "radius_mean", "data_type": "numeric", "unit": "mm", "min_value": 5.0, "max_value": 35.0, "is_required": True, "description": "Mean of distances from center to points on the perimeter"},
            {"name": "texture_mean", "data_type": "numeric", "unit": "score", "min_value": 8.0, "max_value": 45.0, "is_required": True, "description": "Standard deviation of gray-scale values"},
            {"name": "perimeter_mean", "data_type": "numeric", "unit": "mm", "min_value": 40.0, "max_value": 200.0, "is_required": True, "description": "Mean size of the core tumor"},
            {"name": "area_mean", "data_type": "numeric", "unit": "mm^2", "min_value": 100.0, "max_value": 2600.0, "is_required": True, "description": "Mean area of the core tumor"},
            {"name": "smoothness_mean", "data_type": "numeric", "unit": "score", "min_value": 0.05, "max_value": 0.20, "is_required": True, "description": "Mean of local variation in radius lengths"},
            {"name": "compactness_mean", "data_type": "numeric", "unit": "score", "min_value": 0.01, "max_value": 0.35, "is_required": True, "description": "Mean perimeter^2 / area - 1.0"},
            {"name": "concavity_mean", "data_type": "numeric", "unit": "score", "min_value": 0.0, "max_value": 0.45, "is_required": True, "description": "Mean severity of concave portions of the contour"}
        ]
    },
    {
        "name": "Stroke",
        "slug": "stroke",
        "category": "Neurology & Cerebrovascular",
        "description": "Cerebrovascular accident risk estimation based on vascular and systemic indicators.",
        "features": [
            {"name": "gender", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 1, "is_required": True, "description": "1 = Male, 0 = Female"},
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 18, "max_value": 100, "is_required": True, "description": "Age of the patient"},
            {"name": "hypertension", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "0 = no, 1 = yes"},
            {"name": "heart_disease", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "0 = no, 1 = yes"},
            {"name": "ever_married", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "0 = no, 1 = yes"},
            {"name": "avg_glucose_level", "data_type": "numeric", "unit": "mg/dL", "min_value": 50, "max_value": 300, "is_required": True, "description": "Average blood glucose level"},
            {"name": "bmi", "data_type": "numeric", "unit": "kg/m^2", "min_value": 12.0, "max_value": 65.0, "is_required": True, "description": "Body Mass Index"}
        ]
    },
    {
        "name": "Hypertension",
        "slug": "hypertension",
        "category": "Cardiovascular",
        "description": "Essential hypertension risk calculation from hemodynamic and lifestyle indicators.",
        "features": [
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 18, "max_value": 100, "is_required": True, "description": "Age in years"},
            {"name": "systolic_bp", "data_type": "numeric", "unit": "mmHg", "min_value": 80, "max_value": 240, "is_required": True, "description": "Systolic Blood Pressure"},
            {"name": "diastolic_bp", "data_type": "numeric", "unit": "mmHg", "min_value": 50, "max_value": 140, "is_required": True, "description": "Diastolic Blood Pressure"},
            {"name": "heart_rate", "data_type": "numeric", "unit": "bpm", "min_value": 45, "max_value": 180, "is_required": True, "description": "Resting Heart Rate"},
            {"name": "bmi", "data_type": "numeric", "unit": "kg/m^2", "min_value": 15.0, "max_value": 55.0, "is_required": True, "description": "Body Mass Index"},
            {"name": "cholesterol", "data_type": "numeric", "unit": "mg/dL", "min_value": 100, "max_value": 400, "is_required": True, "description": "Total Cholesterol"}
        ]
    },
    {
        "name": "Anemia",
        "slug": "anemia",
        "category": "Hematology",
        "description": "Erythrocyte and hemoglobin deficiency screening from complete blood count metrics.",
        "features": [
            {"name": "gender", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 1, "is_required": True, "description": "0 = Female, 1 = Male"},
            {"name": "hemoglobin", "data_type": "numeric", "unit": "g/dL", "min_value": 4.0, "max_value": 20.0, "is_required": True, "description": "Hemoglobin concentration"},
            {"name": "mch", "data_type": "numeric", "unit": "pg", "min_value": 12.0, "max_value": 40.0, "is_required": True, "description": "Mean Corpuscular Hemoglobin"},
            {"name": "mchc", "data_type": "numeric", "unit": "g/dL", "min_value": 20.0, "max_value": 40.0, "is_required": True, "description": "Mean Corpuscular Hemoglobin Concentration"},
            {"name": "mcv", "data_type": "numeric", "unit": "fL", "min_value": 50.0, "max_value": 120.0, "is_required": True, "description": "Mean Corpuscular Volume"}
        ]
    },
    {
        "name": "Thyroid Disease",
        "slug": "thyroid",
        "category": "Endocrine",
        "description": "Thyroid functional impairment (hypothyroidism / hyperthyroidism) risk detection.",
        "features": [
            {"name": "age", "data_type": "numeric", "unit": "years", "min_value": 10, "max_value": 100, "is_required": True, "description": "Age of the patient"},
            {"name": "sex", "data_type": "categorical", "unit": "code", "min_value": 0, "max_value": 1, "is_required": True, "description": "0 = Female, 1 = Male"},
            {"name": "on_thyroxine", "data_type": "categorical", "unit": "flag", "min_value": 0, "max_value": 1, "is_required": True, "description": "Patient currently on thyroxine (0 = no, 1 = yes)"},
            {"name": "tsh", "data_type": "numeric", "unit": "mIU/L", "min_value": 0.01, "max_value": 50.0, "is_required": True, "description": "Thyroid Stimulating Hormone"},
            {"name": "t3", "data_type": "numeric", "unit": "nmol/L", "min_value": 0.1, "max_value": 10.0, "is_required": True, "description": "Triiodothyronine level"},
            {"name": "tt4", "data_type": "numeric", "unit": "nmol/L", "min_value": 10.0, "max_value": 300.0, "is_required": True, "description": "Total Thyroxine"},
            {"name": "t4u", "data_type": "numeric", "unit": "ratio", "min_value": 0.2, "max_value": 2.5, "is_required": True, "description": "T4 Uptake ratio"}
        ]
    },
    {
        "name": "Parkinson's Disease",
        "slug": "parkinsons",
        "category": "Neurology",
        "description": "Acoustic phonation analysis for early Parkinson's tremor and dysphonia detection.",
        "features": [
            {"name": "fo_hz", "data_type": "numeric", "unit": "Hz", "min_value": 80.0, "max_value": 260.0, "is_required": True, "description": "Average vocal fundamental frequency"},
            {"name": "fhi_hz", "data_type": "numeric", "unit": "Hz", "min_value": 90.0, "max_value": 500.0, "is_required": True, "description": "Maximum vocal fundamental frequency"},
            {"name": "flo_hz", "data_type": "numeric", "unit": "Hz", "min_value": 60.0, "max_value": 250.0, "is_required": True, "description": "Minimum vocal fundamental frequency"},
            {"name": "jitter_percent", "data_type": "numeric", "unit": "%", "min_value": 0.001, "max_value": 0.05, "is_required": True, "description": "Cycle-to-cycle frequency variation"},
            {"name": "shimmer", "data_type": "numeric", "unit": "score", "min_value": 0.005, "max_value": 0.15, "is_required": True, "description": "Cycle-to-cycle amplitude variation"},
            {"name": "hnr", "data_type": "numeric", "unit": "dB", "min_value": 5.0, "max_value": 35.0, "is_required": True, "description": "Harmonics-to-Noise Ratio"},
            {"name": "rpde", "data_type": "numeric", "unit": "score", "min_value": 0.1, "max_value": 0.8, "is_required": True, "description": "Recurrence period density entropy"}
        ]
    }
]

def seed():
    print("=" * 72)
    print(" MEDPREDICT AI -- DATABASE SEEDING ENGINE")
    print("=" * 72)
    
    # Initialize schema
    print("[*] Verifying tables exist in target database...")
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        # 1. Seed Roles
        print("[*] Seeding system roles...")
        role_map = {}
        for r_data in ROLES_DATA:
            role = session.query(Role).filter_by(name=r_data["name"]).first()
            if not role:
                role = Role(name=r_data["name"], description=r_data["description"])
                session.add(role)
                session.flush()
                print(f"  [+] Created Role: {role.name}")
            role_map[role.name] = role

        # 2. Seed Permissions
        print("[*] Seeding permissions...")
        for p_data in PERMISSIONS_DATA:
            perm = session.query(Permission).filter_by(name=p_data["name"]).first()
            if not perm:
                perm = Permission(name=p_data["name"], module=p_data["module"], description=p_data["description"])
                session.add(perm)
                print(f"  [+] Created Permission: {perm.name}")

        # 3. Seed Sample Development Users
        print("[*] Seeding sample users (synthetic development accounts)...")
        for u_data in SAMPLE_USERS:
            user = session.query(User).filter_by(email=u_data["email"]).first()
            if not user:
                user = User(
                    email=u_data["email"],
                    hashed_password=get_password_hash(u_data["password"]),
                    first_name=u_data["first_name"],
                    last_name=u_data["last_name"],
                    is_active=True,
                    is_verified=True
                )
                for r_name in u_data["roles"]:
                    if r_name in role_map:
                        user.roles.append(role_map[r_name])
                session.add(user)
                session.flush()
                print(f"  [+] Created User: {user.email} [{','.join(u_data['roles'])}]")

                # Create Doctor profile if applicable
                if "license" in u_data:
                    doc = Doctor(
                        user_id=user.id,
                        license_number=u_data["license"],
                        specialization=u_data["specialization"],
                        hospital_affiliation=u_data["hospital"]
                    )
                    session.add(doc)

                # Create Patient profile if applicable
                if "dob" in u_data:
                    patient = Patient(
                        user_id=user.id,
                        date_of_birth=u_data["dob"],
                        gender=u_data["gender"],
                        blood_group=u_data.get("blood_group"),
                        emergency_contact=u_data.get("emergency")
                    )
                    session.add(patient)
                    session.flush()
                    profile = MedicalProfile(
                        patient_id=patient.id,
                        allergies="No known drug allergies (NKDA)",
                        chronic_conditions="None reported",
                        family_history="Non-contributory",
                        lifestyle_notes="Regular physical exercise, non-smoker"
                    )
                    session.add(profile)

        # 4. Seed Diseases & Features Catalog
        print("[*] Seeding 10 core disease prediction modules and feature specifications...")
        for d_data in DISEASES_CATALOG:
            disease = session.query(Disease).filter_by(slug=d_data["slug"]).first()
            if not disease:
                disease = Disease(
                    name=d_data["name"],
                    slug=d_data["slug"],
                    category=d_data["category"],
                    description=d_data["description"],
                    is_active=True,
                    version="1.0.0"
                )
                session.add(disease)
                session.flush()
                print(f"  [+] Created Disease Module: {disease.name} ({disease.slug})")

                for f_data in d_data["features"]:
                    feat = DiseaseFeature(
                        disease_id=disease.id,
                        name=f_data["name"],
                        data_type=f_data["data_type"],
                        unit=f_data.get("unit"),
                        min_value=f_data.get("min_value"),
                        max_value=f_data.get("max_value"),
                        is_required=f_data.get("is_required", True),
                        description=f_data.get("description")
                    )
                    session.add(feat)

        # 5. Seed System Settings
        print("[*] Seeding system settings...")
        settings_defaults = [
            ("system_disclaimer_enforced", "true", "Enforces medical decision support disclaimer on all UI and API views"),
            ("risk_threshold_moderate", "0.35", "Cutoff threshold for moderate risk category"),
            ("risk_threshold_high", "0.70", "Cutoff threshold for high risk category"),
            ("max_batch_rows", "10000", "Maximum allowed rows in batch prediction file upload")
        ]
        for key, val, desc in settings_defaults:
            setting = session.query(SystemSetting).filter_by(key=key).first()
            if not setting:
                setting = SystemSetting(key=key, value=val, description=desc)
                session.add(setting)

        session.commit()
        print("=" * 72)
        print(" SEEDING COMPLETED SUCCESSFULLY [ALL DEMO DATA INITIALIZED]")
        print("=" * 72)
    except Exception as e:
        session.rollback()
        print(f"[FAIL] Error seeding database: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed()
