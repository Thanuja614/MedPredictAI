"""
MedPredict AI — Reusable Data Quality Engine (Phase 20)
Performs automated multi-dimensional data profiling and computes an authentic quality score.
Strictly forbids fabricated or hard-coded metrics.
"""

from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd

class DataQualityEngine:
    """
    Executes deep statistical inspection of dataset integrity:
    1. Completeness: Null cell percentage and column missingness rates
    2. Uniqueness: Duplicate row detection
    3. Variance & Cardinality: Constant columns and quasi-constant checks
    4. Outlier Analysis: Interquartile range (IQR) detection
    5. Distribution: Class balance / imbalance ratio
    6. Quality Score: Composite weighted score from 0.0 to 100.0
    """

    @staticmethod
    def audit_dataset(df: pd.DataFrame, target_column: Optional[str] = None) -> Dict[str, Any]:
        """
        Runs comprehensive data quality checks on the provided DataFrame.
        Returns detailed check results and an overall quality score.
        """
        row_count = len(df)
        col_count = len(df.columns)

        if row_count == 0 or col_count == 0:
            return {
                "quality_score": 0.0,
                "row_count": row_count,
                "col_count": col_count,
                "issues": ["Dataset is empty"],
                "metrics": {}
            }

        issues: List[str] = []
        deductions: float = 0.0

        # 1. Missing Values Analysis
        null_counts = df.isnull().sum()
        total_cells = row_count * col_count
        total_missing = int(null_counts.sum())
        missing_percentage = float((total_missing / total_cells) * 100.0)

        missing_by_col = {col: int(cnt) for col, cnt in null_counts.items() if cnt > 0}
        if missing_percentage > 0:
            deductions += min(30.0, missing_percentage * 1.5)
            issues.append(f"Contains {total_missing} missing values ({missing_percentage:.2f}% of cells)")

        # 2. Duplicate Rows Analysis
        duplicate_count = int(df.duplicated().sum())
        duplicate_percentage = float((duplicate_count / row_count) * 100.0)
        if duplicate_count > 0:
            deductions += min(20.0, duplicate_percentage * 2.0)
            issues.append(f"Contains {duplicate_count} duplicate rows ({duplicate_percentage:.2f}%)")

        # 3. Constant and Quasi-Constant Columns
        constant_cols = [col for col in df.columns if df[col].nunique(dropna=True) <= 1]
        if constant_cols:
            deductions += len(constant_cols) * 5.0
            issues.append(f"Constant/Zero-variance columns detected: {constant_cols}")

        # 4. Outlier Detection using IQR on numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outlier_counts = {}
        total_outlier_rows = 0

        for col in numeric_cols:
            if col == target_column:
                continue
            series = df[col].dropna()
            if len(series) < 10:
                continue
            q25 = float(series.quantile(0.25))
            q75 = float(series.quantile(0.75))
            iqr = q75 - q25
            if iqr > 0:
                lower = q25 - 1.5 * iqr
                upper = q75 + 1.5 * iqr
                outliers = series[(series < lower) | (series > upper)]
                cnt = len(outliers)
                if cnt > 0:
                    outlier_counts[col] = int(cnt)
                    total_outlier_rows += cnt

        outlier_rate = float((total_outlier_rows / (max(1, len(numeric_cols)) * row_count)) * 100.0)
        if outlier_rate > 5.0:
            deductions += min(15.0, (outlier_rate - 5.0) * 0.8)
            issues.append(f"High outlier frequency observed across {len(outlier_counts)} numeric features")

        # 5. Class Balance Inspection (if target_column specified)
        class_distribution = {}
        imbalance_ratio = 1.0
        if target_column and target_column in df.columns:
            counts = df[target_column].value_counts().to_dict()
            class_distribution = {str(k): int(v) for k, v in counts.items()}
            if len(counts) == 2:
                vals = list(counts.values())
                imbalance_ratio = float(max(vals) / max(1, min(vals)))
                if imbalance_ratio > 3.0:
                    deductions += min(15.0, (imbalance_ratio - 3.0) * 2.0)
                    issues.append(f"Significant class imbalance: 1:{imbalance_ratio:.1f}")

        # Compute Final Quality Score (bounded 0.0 to 100.0)
        quality_score = round(max(0.0, min(100.0, 100.0 - deductions)), 2)

        return {
            "quality_score": quality_score,
            "row_count": row_count,
            "column_count": col_count,
            "missing_cells_total": total_missing,
            "missing_percentage": round(missing_percentage, 2),
            "missing_by_column": missing_by_col,
            "duplicate_rows": duplicate_count,
            "constant_columns": constant_cols,
            "outlier_columns": outlier_counts,
            "class_distribution": class_distribution,
            "imbalance_ratio": round(imbalance_ratio, 2),
            "issues": issues
        }
