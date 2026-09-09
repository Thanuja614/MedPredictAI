"""
MedPredict AI — Abstract Preprocessor Base Class
Guarantees leakage-free data transformations, fitting strictly on training sets.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd

class BasePreprocessor(ABC):
    """
    Abstract Preprocessor encapsulating imputation, encoding, and scaling transformations.
    All state must be fitted strictly during fit() on training data.
    """

    def __init__(self, feature_names: List[str], target_name: Optional[str] = None):
        self.feature_names = feature_names
        self.target_name = target_name
        self.is_fitted: bool = False
        self.feature_statistics: Dict[str, Any] = {}

    @abstractmethod
    def fit(self, df: pd.DataFrame) -> "BasePreprocessor":
        """Computes transformation parameters strictly from training data."""
        pass

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Applies fitted transformations to feature data."""
        pass

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fits transformers on df and applies transformation."""
        return self.fit(df).transform(df)

    def check_fitted(self) -> None:
        """Verifies that preprocessor has been fitted before transform."""
        if not self.is_fitted:
            raise ValueError("Preprocessor instance is not fitted yet. Call 'fit' first.")
