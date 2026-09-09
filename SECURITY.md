# MedPredict AI — Security & Privacy Architecture

## 1. Security Architecture Principles

MedPredict AI handles healthcare-adjacent decision support data and enforces a **Defense-in-Depth** security model across the entire technology stack.

```
       [ Client HTTPS / TLS 1.3 ]
                   │
                   ▼
  [ Secure HTTP Headers & CORS Firewall ]
                   │
                   ▼
     [ Rate Limiter & Slowloris Guard ]
                   │
                   ▼
  [ JWT Authentication & RBAC Authorization ]
                   │
                   ▼
  [ Pydantic Strict Schema & File Sanitizer ]
                   │
                   ▼
  [ Parameterized ORM Queries (SQLAlchemy) ]
                   │
                   ▼
 [ PostgreSQL RBAC + Encrypted Columns & Storage ]
                   │
                   ▼
[ Immutable Structured Audit Trail & Security Events ]
```

---

## 2. Authentication & Credential Hygiene

### 2.1 Password Security
- Passwords must be at least 10 characters long and contain uppercase, lowercase, numbers, and special symbols.
- Passwords are hashed using **Argon2id** (or **Bcrypt** with cost factor >= 12) with per-user cryptographic salts. Plaintext passwords are never logged, cached, or stored.

### 2.2 Token Management
- Authentication utilizes standard JSON Web Tokens (JWT) using `HS256` (or `RS256` in enterprise deployments).
- Short-lived Access Tokens (30 minutes expiry) minimize exposure.
- Long-lived Refresh Tokens (7 days expiry) are hashed and tracked in Redis to support instant token revocation and logout.

---

## 3. Role-Based Access Control (RBAC)

The system defines 5 non-overlapping roles following the principle of least privilege:

| Role | Permitted Actions | Prohibited Actions |
| :--- | :--- | :--- |
| `PATIENT` | View own profile, submit self-assessments, view own predictions and risk reports | Access other patients' records, upload datasets, train models, view audit logs |
| `DOCTOR` | View assigned patients, create clinical assessments, run predictions, generate reports | Modify ML models, promote registry artifacts, modify user roles |
| `DATA_SCIENTIST` | Upload datasets, run data quality audits, train models, compare metrics, register models | Access patient personal identifying information (PII), manage user roles |
| `ADMIN` | Manage users and roles, system configuration, inspect system health, trigger backups | Tamper with audit logs |
| `AUDITOR` | Read-only inspection of audit logs, security events, model changes, and system access logs | Mutate patient data, train models, modify system configuration |

---

## 4. Injection & Input Sanitization

- **SQL Injection**: Prevented universally by using SQLAlchemy 2.0 ORM query builders and parameter binding. Raw string concatenation in SQL queries is strictly prohibited.
- **XSS & Content Security**: All user-supplied string data is sanitized. The React frontend escapes variables by default. HTTP responses set `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, and `X-Frame-Options: DENY`.
- **File Upload Security**:
  - Whitelist file extensions (`.csv`, `.xlsx`, `.parquet`).
  - Verify MIME type via magic bytes.
  - Reject executable files, symlinks, and path traversal sequences (`../`, `..\`).
  - Max upload size limited (e.g. 50MB). Files are processed in isolated memory buffers without execution.

---

## 5. Medical Data Privacy & Synthetic Data Policy

1. **Zero Real Patient PII in Source Control**: All training datasets and demonstration fixtures committed to this repository are synthetic, simulated, or sourced from de-identified public clinical research repositories.
2. **De-identification**: In demo mode, synthetic datasets are labeled:
   `"SYNTHETIC DEMONSTRATION DATA — NOT REAL PATIENT DATA"`.
3. **Audit Trails**: Access to patient assessment records and predictions produces an immutable audit record containing timestamp, user ID, IP address, and operation type.
