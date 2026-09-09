"""
MedPredict AI — Data Quality Engine Test Suite (Phase 20)
Verifies multi-dimensional quality auditing, missing value checks, duplicate detection, and scoring.
"""

import pandas as pd
import numpy as np
from backend.app.ml.data_quality.engine import DataQualityEngine

def test_data_quality_clean_dataset():
    np.random.seed(42)
    df_clean = pd.DataFrame({
        "feature_1": np.random.normal(50, 10, 100),
        "feature_2": np.random.normal(100, 15, 100),
        "target": np.random.choice([0, 1], size=100)
    })
    audit = DataQualityEngine.audit_dataset(df_clean, target_column="target")
    assert audit["quality_score"] >= 90.0
    assert audit["missing_cells_total"] == 0
    assert audit["duplicate_rows"] == 0

def test_data_quality_contaminated_dataset():
    df_dirty = pd.DataFrame({
        "feature_1": [1.0, 2.0, np.nan, 2.0, 5.0, 1000.0, np.nan, 2.0],
        "feature_2": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],  # Constant column!
        "target": [0, 0, 0, 0, 0, 0, 0, 1]  # Severe imbalance!
    })
    # Add duplicate row
    df_dirty = pd.concat([df_dirty, df_dirty.iloc[[0]]], ignore_index=True)

    audit = DataQualityEngine.audit_dataset(df_dirty, target_column="target")
    assert audit["quality_score"] < 75.0
    assert audit["missing_cells_total"] > 0
    assert len(audit["constant_columns"]) >= 1
    assert audit["duplicate_rows"] >= 1
    assert len(audit["issues"]) >= 2
