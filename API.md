# MedPredict AI — REST API Specification

## 1. Global API Standards

- **Base URL**: `/api/v1`
- **Protocol**: HTTP/1.1 & HTTP/2 over TLS
- **Content Type**: `application/json` (Multipart for uploads, octet-stream for reports)
- **Authentication**: Bearer Token in `Authorization: Bearer <jwt_access_token>`
- **Response Format Envelope**:
  All standard responses follow a consistent envelope:
  ```json
  {
    "success": true,
    "data": { ... },
    "message": "Operation completed successfully",
    "timestamp": "2026-09-09T11:45:00Z"
  }
  ```
- **Standard Error Envelope**:
  ```json
  {
    "success": false,
    "error": {
      "code": "ENTITY_NOT_FOUND",
      "message": "The requested patient record was not found.",
      "details": []
    },
    "timestamp": "2026-09-09T11:45:00Z"
  }
  ```

---

## 2. API Endpoint Catalog

### 2.1 Authentication (`/auth`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/register` | Public | Register a new user account with default role |
| `POST` | `/auth/login` | Public | Authenticate via email/password, return access + refresh tokens |
| `POST` | `/auth/refresh` | Public | Rotate refresh token and issue new access token |
| `POST` | `/auth/logout` | Authenticated | Revoke current refresh token in Redis |
| `POST` | `/auth/password-reset/request` | Public | Request password reset token |
| `POST` | `/auth/password-reset/confirm` | Public | Reset password with valid reset token |

### 2.2 Users & Governance (`/users`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/users/me` | Authenticated | Get current authenticated user profile |
| `PUT` | `/users/me` | Authenticated | Update current profile details |
| `GET` | `/users/` | Admin, Auditor | List users with pagination and role filters |
| `POST` | `/users/{id}/roles` | Admin | Assign or revoke roles for a user |

### 2.3 Patients & Clinical History (`/patients`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/patients/` | Doctor, Admin | Search/list patient roster |
| `POST` | `/patients/` | Patient, Doctor | Create patient profile |
| `GET` | `/patients/{id}` | Patient (self), Doctor | Get full patient profile & medical history |
| `GET` | `/patients/{id}/assessments`| Patient (self), Doctor | Get assessment timeline |
| `POST` | `/patients/{id}/assessments`| Doctor, Patient | Create an assessment entry |

### 2.4 Diseases & Features (`/diseases`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/diseases/` | Public / Auth | List all 10 active disease modules |
| `GET` | `/diseases/{slug}` | Public / Auth | Get disease details, input feature schemas, and validation ranges |
| `POST` | `/diseases/symptom-match` | Public / Auth | Match symptom checklist to related disease modules |

### 2.5 Predictions & Explanations (`/predictions`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/predictions/evaluate` | Patient, Doctor | Run single-disease ML risk prediction & SHAP explanation |
| `POST` | `/predictions/batch` | Doctor, Data Scientist | Upload CSV of assessments for batch prediction job |
| `GET` | `/predictions/history` | Patient (self), Doctor | Retrieve paginated prediction history |
| `GET` | `/predictions/{id}` | Patient (self), Doctor | Get specific prediction, probability, risk level & SHAP waterfall |

### 2.6 Datasets & Data Quality (`/datasets`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/datasets/` | Data Scientist, Admin | List uploaded datasets and schemas |
| `POST` | `/datasets/upload` | Data Scientist, Admin | Upload dataset (CSV, XLSX, Parquet) with sanitization |
| `GET` | `/datasets/{id}/versions/{v}/quality` | Data Scientist, Admin | Retrieve automated data quality score and profiling metrics |

### 2.7 Model Training & Registry (`/models`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/models/train` | Data Scientist | Trigger background training run with selected algorithm & hyperparams |
| `GET` | `/models/` | Data Scientist, Admin | List registered models and candidates across diseases |
| `GET` | `/models/leaderboard/{disease_id}` | Data Scientist, Admin | Model performance comparison table |
| `POST` | `/models/{id}/promote` | Admin, Data Scientist | Promote model version to active production inference |

### 2.8 Reports (`/reports`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/reports/prediction/{id}` | Patient, Doctor | Generate downloadable PDF clinical risk report |
| `POST` | `/reports/data-quality/{id}` | Data Scientist | Generate Data Quality PDF/CSV report |
| `GET` | `/reports/{id}/download` | Authenticated | Stream report artifact file |

### 2.9 Observability & Audit (`/audit`, `/health`)
| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/audit/logs` | Admin, Auditor | Query structured audit events with filters |
| `GET` | `/audit/security` | Admin, Auditor | View security incidents (failed logins, auth anomalies) |
| `GET` | `/health` | Public | Liveness probe (HTTP 200 OK) |
| `GET` | `/ready` | Public | Readiness probe (verifies DB & Redis connectivity) |
