"""
MedPredict AI — Core Disease Modules Catalog
Aggregates all 10 disease modules with standardized factory lookups.
"""

from typing import Dict, Type, List
from backend.app.ml.framework.base_module import BaseDiseaseModule
from backend.app.ml.modules.diabetes.module import DiabetesDiseaseModule
from backend.app.ml.modules.heart.module import HeartDiseaseModule
from backend.app.ml.modules.liver.module import LiverDiseaseModule
from backend.app.ml.modules.kidney.module import KidneyDiseaseModule
from backend.app.ml.modules.breast_cancer.module import BreastCancerDiseaseModule
from backend.app.ml.modules.stroke.module import StrokeDiseaseModule
from backend.app.ml.modules.hypertension.module import HypertensionDiseaseModule
from backend.app.ml.modules.anemia.module import AnemiaDiseaseModule
from backend.app.ml.modules.thyroid.module import ThyroidDiseaseModule
from backend.app.ml.modules.parkinsons.module import ParkinsonsDiseaseModule

MODULE_REGISTRY: Dict[str, Type[BaseDiseaseModule]] = {
    "diabetes": DiabetesDiseaseModule,
    "heart": HeartDiseaseModule,
    "liver": LiverDiseaseModule,
    "kidney": KidneyDiseaseModule,
    "breast_cancer": BreastCancerDiseaseModule,
    "stroke": StrokeDiseaseModule,
    "hypertension": HypertensionDiseaseModule,
    "anemia": AnemiaDiseaseModule,
    "thyroid": ThyroidDiseaseModule,
    "parkinsons": ParkinsonsDiseaseModule,
}

def get_disease_module(slug: str) -> BaseDiseaseModule:
    """Instantiates a disease module by unique slug."""
    clean_slug = slug.lower().strip()
    if clean_slug not in MODULE_REGISTRY:
        raise KeyError(f"Disease module '{slug}' not found in registry. Supported: {list(MODULE_REGISTRY.keys())}")
    return MODULE_REGISTRY[clean_slug]()

def list_disease_modules() -> List[Dict[str, str]]:
    """Returns metadata summary of all 10 registered disease modules."""
    result = []
    for slug, cls in MODULE_REGISTRY.items():
        instance = cls()
        result.append({
            "name": instance.name,
            "slug": instance.slug,
            "category": instance.category,
            "description": instance.description,
            "target_column": instance.target_column,
            "version": instance.version,
            "feature_count": len(instance.raw_features)
        })
    return result

__all__ = [
    "MODULE_REGISTRY",
    "get_disease_module",
    "list_disease_modules",
    "DiabetesDiseaseModule",
    "HeartDiseaseModule",
    "LiverDiseaseModule",
    "KidneyDiseaseModule",
    "BreastCancerDiseaseModule",
    "StrokeDiseaseModule",
    "HypertensionDiseaseModule",
    "AnemiaDiseaseModule",
    "ThyroidDiseaseModule",
    "ParkinsonsDiseaseModule"
]
