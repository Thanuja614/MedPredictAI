"""
MedPredict AI — Abstract Feature Engineering Base Class
Encapsulates domain-specific, medically justified feature transformations.
"""

from abc import ABC, abstractmethod
from typing import List
import pandas as pd

class BaseFeatureEngineer(ABC):
    """
    Abstract Feature Engineer responsible for computing derived biomarkers,
    ratios, and risk groupings without creating medically misleading features.
    """

    @abstractmethod
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Derives clinical indicators and interaction terms."""
        pass

    @abstractmethod
    def get_engineered_feature_names(self) -> List[str]:
        """Returns the list of generated feature column names."""
        pass
