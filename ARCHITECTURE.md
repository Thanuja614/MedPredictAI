# MedPredict AI — System Architecture Specification

## 1. Architectural Philosophy

MedPredict AI is engineered on the principles of **Clean Architecture**, **Domain-Driven Design (DDD)**, and **Separation of Concerns**. The platform decouples web protocols from domain models and data science algorithms, ensuring that business rules, machine learning pipelines, and database interactions can evolve independently.

```
+-----------------------------------------------------------------------+
|                           Presentation Layer                          |
|   React 18 SPA (TypeScript, Tailwind, TanStack Query, Recharts)       |
+-----------------------------------+-----------------------------------+
                                    | HTTP / JSON (REST API)
+-----------------------------------v-----------------------------------+
|                         API Gateway & Security                        |
|   FastAPI, CORS, Rate Limiting, Request Correlation ID, JWT Auth      |
+-----------------------------------+-----------------------------------+
                                    |
          +-------------------------+-------------------------+
          |                                                   |
+---------v-----------------------+         +-----------------v---------+
|        Application Services     |         |     ML & Analytics Engine |
| - AuthService (JWT, Tokens)     |         | - Disease Framework       |
| - PatientService (Assessments)  |         | - Data Preprocessor       |
| - DatasetService (Validation)   |         | - Feature Selection       |
| - ReportService (PDF/CSV/XLSX)  |         | - Model Training & Tuning |
| - AuditService (Event logging)  |         | - SHAP Explainer Service  |
+---------+-----------------------+         | - Model Registry Engine   |
          |                                 +-----------------+---------+
          |                                                   |
+---------v---------------------------------------------------v---------+
|                            Persistence Layer                          |
| - SQLAlchemy 2.0 ORM & Alembic Migrations                            |
| - PostgreSQL 16 (Relational, JSONB)                                   |
| - Redis 7 (Cache, Session invalidation, Async task queue)             |
+-----------------------------------------------------------------------+
```

---

## 2. Component Boundaries & Responsibilities

### 2.1 API Layer (`backend/app/api/`)
- **Version Prefix**: `/api/v1`
- **Routers**:
  - `/auth`: Registration, Login, Refresh, Logout, Password Reset.
  - `/users`: Profile management, role assignment (Admin only).
  - `/patients`: Demographics, medical history, assessments.
  - `/diseases`: Disease metadata, feature schemas, symptom matching.
  - `/predictions`: Single and batch inference, probability output, explanations.
  - `/datasets`: File uploads (CSV/XLSX/Parquet), profiling, quality scoring.
  - `/training`: Workspace training runs, hyperparameter sweeps.
  - `/models`: Registry of active/staged/archived model artifacts, comparison.
  - `/analytics`: Population risk distributions, training metrics, audit stats.
  - `/reports`: PDF risk report generation, CSV data export.
  - `/audit`: Security events, system events, administrative audit trail.
  - `/health`: Liveness (`/health`) and readiness (`/ready`) probes.

### 2.2 Core Infrastructure Layer (`backend/app/core/`)
- `config.py`: Environment configuration via Pydantic `BaseSettings`.
- `database.py`: SQLAlchemy 2.0 async/sync engine, session dependency provider, transaction boundaries.
- `logging.py`: Structured JSON logger with contextual correlation IDs.
- `security.py`: Password hashing (Bcrypt/Argon2id), JWT generation, claims parsing.
- `errors.py`: Global HTTP exception handlers and standardized API error envelopes.

### 2.3 Domain Entities & Models Layer (`backend/app/models/`)
- Contains 27 normalized relational entities adhering to strict integrity constraints, foreign keys, and indexes.

### 2.4 Machine Learning Framework Layer (`backend/app/ml/`)
- `base.py`: Abstract Base Classes (`BaseDiseaseModule`, `BasePreprocessor`, `BaseFeatureEngineer`, `BaseModelTrainer`, `BasePredictor`, `BaseExplainer`).
- `modules/`: Disease-specific implementations for 10 target diseases.
- `pipeline.py`: Leakage-free training pipeline wrapping scikit-learn and imbalanced-learn pipelines.
- `explainability.py`: SHAP tree/linear/kernel explainer wrappers returning both global feature importance and local instance waterfall explanations.
- `registry.py`: Model serialization via `joblib`, SHA-256 artifact hashing, metadata generation, and staging-to-production promotion.

---

## 3. Data Flow Workflows

### 3.1 Prediction & Explanation Workflow
```
User (Form Input)
      │
      ▼
API: POST /api/v1/predictions/
      │  (Validate against DiseaseFeatureSchema via Pydantic)
      ▼
PredictionService:
      ├── Retrieve active ModelVersion from ModelRegistry
      ├── Apply Preprocessing (imputation, scaling fitted ONLY on training set)
      ├── Compute Probability: model.predict_proba(X)
      ├── Map to Risk Level: LOW (<0.35), MODERATE (0.35-0.70), HIGH (>0.70)
      ├── Compute SHAP values via ExplainerService
      └── Persist Prediction record + PredictionInput + Explanation in DB
      │
      ▼
Return JSON with Risk Level, Probability, Waterfall Contributions, and Medical Disclaimer
```

### 3.2 Dataset Ingestion & Quality Profiling Workflow
```
Client (Uploads CSV / XLSX / Parquet)
      │
      ▼
API: POST /api/v1/datasets/upload
      │  (Validate MIME type, size limit, filename sanitization)
      ▼
DatasetService:
      ├── Secure storage write
      ├── Detect schema (types, columns, nulls)
      ├── Run DataQualityEngine (missingness, duplicates, outliers, class balance)
      ├── Compute Data Quality Score (0 - 100)
      └── Store DatasetVersion + DataQualityReport in PostgreSQL
```

---

## 4. Scalability & Resilience

- **Stateless Application Server**: The FastAPI instance carries no server-side session state; all state is persisted in PostgreSQL or Redis. Instances scale horizontally behind a reverse proxy (Nginx or AWS ALB).
- **Asynchronous Processing**: Long-running operations (model training, high-volume batch predictions, PDF report generation) run asynchronously in worker queues to avoid blocking HTTP worker threads.
- **Fail-Safe Offline Mode**: The system provides automated fallbacks (in-memory caching and SQLite test database support) when auxiliary services are temporarily unreachable in local environments.
