# MedPredict AI — Database Schema Specification

## 1. Overview & Engine Specification

The persistent data storage of MedPredict AI is built upon **PostgreSQL 16** using **SQLAlchemy 2.0 ORM** and version-controlled via **Alembic** migrations. The schema is normalized into 27 tables organized across 7 logical domains:

1. **Authentication & Authorization** (`users`, `roles`, `permissions`, `user_roles`)
2. **Clinical & Patient Profiles** (`patients`, `doctors`, `medical_profiles`, `assessments`)
3. **Disease Framework** (`diseases`, `disease_features`)
4. **Dataset Management** (`datasets`, `dataset_versions`, `data_quality_reports`)
5. **Machine Learning Lifecycle** (`experiments`, `training_runs`, `models`, `model_versions`)
6. **Inference & Explainability** (`predictions`, `prediction_inputs`, `explanations`)
7. **Governance & Operations** (`reports`, `jobs`, `notifications`, `audit_logs`, `system_events`, `security_events`, `settings`)

---

## 2. Entity Relationship Diagram (High-Level)

```
[users] ──< [user_roles] >── [roles] ──< [permissions]
   │
   ├── [patients] ──< [medical_profiles]
   │       │
   │       └──< [assessments] ──< [predictions]
   │                                   │
   │                                   ├── [prediction_inputs]
   │                                   └── [explanations]
   │
   ├── [doctors]
   │
   └──< [audit_logs]

[diseases] ──< [disease_features]
    │
    ├──< [datasets] ──< [dataset_versions] ──< [data_quality_reports]
    │
    └──< [models] ──< [model_versions] ──< [training_runs] >── [experiments]
```

---

## 3. Schema Definitions & Table Descriptions

### 3.1 Authentication & RBAC

#### `users`
- `id` (UUID, Primary Key)
- `email` (VARCHAR(255), Unique, Indexed, NOT NULL)
- `hashed_password` (VARCHAR(255), NOT NULL)
- `first_name` (VARCHAR(100), NOT NULL)
- `last_name` (VARCHAR(100), NOT NULL)
- `is_active` (BOOLEAN, Default True)
- `is_verified` (BOOLEAN, Default False)
- `created_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)
- `updated_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)

#### `roles`
- `id` (INTEGER, Primary Key)
- `name` (VARCHAR(50), Unique, NOT NULL) — `PATIENT`, `DOCTOR`, `DATA_SCIENTIST`, `ADMIN`, `AUDITOR`
- `description` (TEXT)

#### `permissions`
- `id` (INTEGER, Primary Key)
- `name` (VARCHAR(100), Unique, NOT NULL)
- `module` (VARCHAR(50), NOT NULL)
- `description` (TEXT)

#### `user_roles`
- `user_id` (UUID, FK -> `users.id`, Primary Key)
- `role_id` (INTEGER, FK -> `roles.id`, Primary Key)
- `assigned_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)

---

### 3.2 Clinical Domain

#### `patients`
- `id` (UUID, Primary Key)
- `user_id` (UUID, FK -> `users.id`, Unique, NOT NULL)
- `date_of_birth` (DATE, NOT NULL)
- `gender` (VARCHAR(20), NOT NULL)
- `blood_group` (VARCHAR(5))
- `emergency_contact` (VARCHAR(100))
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `doctors`
- `id` (UUID, Primary Key)
- `user_id` (UUID, FK -> `users.id`, Unique, NOT NULL)
- `license_number` (VARCHAR(100), Unique, NOT NULL)
- `specialization` (VARCHAR(100), NOT NULL)
- `hospital_affiliation` (VARCHAR(255))
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `medical_profiles`
- `id` (UUID, Primary Key)
- `patient_id` (UUID, FK -> `patients.id`, Unique, NOT NULL)
- `allergies` (JSONB / TEXT)
- `chronic_conditions` (JSONB / TEXT)
- `family_history` (JSONB / TEXT)
- `lifestyle_notes` (TEXT)
- `updated_at` (TIMESTAMP WITH TIME ZONE)

#### `assessments`
- `id` (UUID, Primary Key)
- `patient_id` (UUID, FK -> `patients.id`, NOT NULL)
- `created_by_user_id` (UUID, FK -> `users.id`, NOT NULL)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `notes` (TEXT)
- `created_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)

---

### 3.3 Disease & Feature Catalog

#### `diseases`
- `id` (UUID, Primary Key)
- `name` (VARCHAR(100), Unique, NOT NULL)
- `slug` (VARCHAR(100), Unique, NOT NULL)
- `category` (VARCHAR(100), NOT NULL)
- `description` (TEXT)
- `is_active` (BOOLEAN, Default True)
- `version` (VARCHAR(20), Default '1.0.0')

#### `disease_features`
- `id` (UUID, Primary Key)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `name` (VARCHAR(100), NOT NULL)
- `data_type` (VARCHAR(30), NOT NULL) — `numeric`, `categorical`, `boolean`
- `unit` (VARCHAR(30))
- `min_value` (FLOAT)
- `max_value` (FLOAT)
- `is_required` (BOOLEAN, Default True)
- `description` (TEXT)

---

### 3.4 Datasets & Quality

#### `datasets`
- `id` (UUID, Primary Key)
- `name` (VARCHAR(150), Unique, NOT NULL)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `source_description` (TEXT)
- `is_synthetic` (BOOLEAN, Default True)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `dataset_versions`
- `id` (UUID, Primary Key)
- `dataset_id` (UUID, FK -> `datasets.id`, NOT NULL)
- `version_tag` (VARCHAR(30), NOT NULL)
- `file_path` (VARCHAR(500), NOT NULL)
- `file_format` (VARCHAR(20), NOT NULL) — `csv`, `parquet`, `xlsx`
- `row_count` (INTEGER, NOT NULL)
- `column_count` (INTEGER, NOT NULL)
- `checksum_sha256` (VARCHAR(64), NOT NULL)
- `uploaded_by_user_id` (UUID, FK -> `users.id`, NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `data_quality_reports`
- `id` (UUID, Primary Key)
- `dataset_version_id` (UUID, FK -> `dataset_versions.id`, Unique, NOT NULL)
- `quality_score` (FLOAT, NOT NULL) — 0.0 to 100.0
- `missing_cell_count` (INTEGER, NOT NULL)
- `duplicate_row_count` (INTEGER, NOT NULL)
- `metrics_json` (JSONB / TEXT, NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

---

### 3.5 ML Engine & Model Registry

#### `experiments`
- `id` (UUID, Primary Key)
- `name` (VARCHAR(150), NOT NULL)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `created_by_user_id` (UUID, FK -> `users.id`, NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `training_runs`
- `id` (UUID, Primary Key)
- `experiment_id` (UUID, FK -> `experiments.id`, NOT NULL)
- `dataset_version_id` (UUID, FK -> `dataset_versions.id`, NOT NULL)
- `algorithm` (VARCHAR(100), NOT NULL)
- `hyperparameters_json` (JSONB / TEXT)
- `metrics_json` (JSONB / TEXT) — accuracy, precision, recall, f1, roc_auc
- `duration_seconds` (FLOAT)
- `status` (VARCHAR(30)) — `queued`, `running`, `completed`, `failed`
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `models`
- `id` (UUID, Primary Key)
- `name` (VARCHAR(150), Unique, NOT NULL)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `description` (TEXT)

#### `model_versions`
- `id` (UUID, Primary Key)
- `model_id` (UUID, FK -> `models.id`, NOT NULL)
- `training_run_id` (UUID, FK -> `training_runs.id`, NOT NULL)
- `version_tag` (VARCHAR(30), NOT NULL)
- `artifact_path` (VARCHAR(500), NOT NULL)
- `artifact_hash_sha256` (VARCHAR(64), NOT NULL)
- `status` (VARCHAR(30), NOT NULL) — `staged`, `active`, `archived`
- `metrics_summary_json` (JSONB / TEXT)
- `created_at` (TIMESTAMP WITH TIME ZONE)

---

### 3.6 Prediction & Explainability

#### `predictions`
- `id` (UUID, Primary Key)
- `patient_id` (UUID, FK -> `patients.id`)
- `assessment_id` (UUID, FK -> `assessments.id`)
- `model_version_id` (UUID, FK -> `model_versions.id`, NOT NULL)
- `disease_id` (UUID, FK -> `diseases.id`, NOT NULL)
- `probability` (FLOAT, NOT NULL) — 0.0 to 1.0
- `risk_level` (VARCHAR(20), NOT NULL) — `LOW`, `MODERATE`, `HIGH`
- `is_batch` (BOOLEAN, Default False)
- `created_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)

#### `prediction_inputs`
- `id` (UUID, Primary Key)
- `prediction_id` (UUID, FK -> `predictions.id`, Unique, NOT NULL)
- `input_features_json` (JSONB / TEXT, NOT NULL)

#### `explanations`
- `id` (UUID, Primary Key)
- `prediction_id` (UUID, FK -> `predictions.id`, Unique, NOT NULL)
- `method` (VARCHAR(50), NOT NULL) — `SHAP_TREE`, `SHAP_KERNEL`, `SHAP_LINEAR`
- `feature_contributions_json` (JSONB / TEXT, NOT NULL)
- `base_value` (FLOAT)
- `created_at` (TIMESTAMP WITH TIME ZONE)

---

### 3.7 Governance & Audit

#### `reports`
- `id` (UUID, Primary Key)
- `title` (VARCHAR(200), NOT NULL)
- `report_type` (VARCHAR(50), NOT NULL) — `prediction_summary`, `patient_risk`, `data_quality`, `model_card`
- `format` (VARCHAR(10), NOT NULL) — `pdf`, `csv`, `xlsx`
- `file_path` (VARCHAR(500), NOT NULL)
- `generated_by_user_id` (UUID, FK -> `users.id`, NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `jobs`
- `id` (UUID, Primary Key)
- `job_type` (VARCHAR(50), NOT NULL) — `model_training`, `batch_prediction`, `data_profiling`
- `status` (VARCHAR(30), NOT NULL) — `pending`, `running`, `succeeded`, `failed`
- `progress_percent` (INTEGER, Default 0)
- `error_message` (TEXT)
- `payload_json` (JSONB / TEXT)
- `started_at` (TIMESTAMP WITH TIME ZONE)
- `completed_at` (TIMESTAMP WITH TIME ZONE)

#### `notifications`
- `id` (UUID, Primary Key)
- `user_id` (UUID, FK -> `users.id`, NOT NULL)
- `title` (VARCHAR(200), NOT NULL)
- `message` (TEXT, NOT NULL)
- `is_read` (BOOLEAN, Default False)
- `type` (VARCHAR(50), NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `audit_logs`
- `id` (UUID, Primary Key)
- `user_id` (UUID, FK -> `users.id`)
- `action` (VARCHAR(100), NOT NULL)
- `entity_type` (VARCHAR(100), NOT NULL)
- `entity_id` (VARCHAR(100))
- `ip_address` (VARCHAR(50))
- `user_agent` (VARCHAR(255))
- `details_json` (JSONB / TEXT)
- `created_at` (TIMESTAMP WITH TIME ZONE, NOT NULL)

#### `system_events`
- `id` (UUID, Primary Key)
- `event_type` (VARCHAR(100), NOT NULL)
- `severity` (VARCHAR(20), NOT NULL) — `info`, `warning`, `error`, `critical`
- `message` (TEXT, NOT NULL)
- `metadata_json` (JSONB / TEXT)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `security_events`
- `id` (UUID, Primary Key)
- `event_type` (VARCHAR(100), NOT NULL) — `login_failure`, `unauthorized_access`, `token_tampering`
- `ip_address` (VARCHAR(50))
- `user_identifier` (VARCHAR(255))
- `severity` (VARCHAR(20), NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE)

#### `settings`
- `key` (VARCHAR(100), Primary Key)
- `value` (TEXT, NOT NULL)
- `description` (TEXT)
- `updated_at` (TIMESTAMP WITH TIME ZONE)
