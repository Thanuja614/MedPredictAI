"""
MedPredict AI — Disease Catalog & Symptom Screening Endpoints
"""

from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.models.disease import Disease
from backend.app.ml.modules import list_disease_modules, get_disease_module
from backend.app.core.errors import EntityNotFoundError

router = APIRouter(prefix="/diseases", tags=["Disease Framework"])

class SymptomMatchRequest(BaseModel):
    symptoms: List[str] = Field(..., min_length=1, description="List of observed symptoms")

class SymptomMatchResponse(BaseModel):
    matched_diseases: List[Dict[str, Any]]
    disclaimer: str

SYMPTOM_DISEASE_MAP = {
    "excessive_thirst": ["diabetes"],
    "frequent_urination": ["diabetes", "kidney"],
    "unexplained_weight_loss": ["diabetes", "thyroid"],
    "chest_pain": ["heart", "hypertension"],
    "shortness_of_breath": ["heart", "hypertension", "anemia"],
    "yellow_eyes_skin": ["liver"],
    "abdominal_swelling": ["liver", "kidney"],
    "fatigue": ["anemia", "thyroid", "kidney", "liver"],
    "pale_skin": ["anemia"],
    "high_blood_pressure": ["hypertension", "kidney", "stroke"],
    "facial_droop_arm_weakness": ["stroke"],
    "hand_tremor": ["parkinsons"],
    "slowness_of_movement": ["parkinsons"],
    "breast_lump": ["breast_cancer"]
}

@router.get("/", summary="List Supported Diseases")
def list_diseases(db: Session = Depends(get_db)):
    """Returns metadata for all 10 supported disease prediction modules."""
    return list_disease_modules()

@router.get("/{slug}", summary="Get Disease Feature Schema")
def get_disease_details(slug: str, db: Session = Depends(get_db)):
    """Retrieves feature definitions, validation bounds, and target details for a disease."""
    try:
        module = get_disease_module(slug)
    except KeyError:
        raise EntityNotFoundError(f"Disease module '{slug}' not found")

    return {
        "name": module.name,
        "slug": module.slug,
        "category": module.category,
        "description": module.description,
        "version": module.version,
        "target_variable": module.target_column,
        "features": module.get_feature_schema(),
        "candidates": list(module.get_candidate_models().keys())
    }

@router.post("/symptom-match", response_model=SymptomMatchResponse, summary="Match Symptoms to Disease Modules")
def match_symptoms(request: SymptomMatchRequest):
    """
    Non-diagnostic symptom correlation utility directing patients to appropriate risk screening modules.
    Enforces medical decision-support disclaimer.
    """
    matched_slugs = set()
    for s in request.symptoms:
        s_clean = s.lower().strip().replace(" ", "_")
        if s_clean in SYMPTOM_DISEASE_MAP:
            matched_slugs.update(SYMPTOM_DISEASE_MAP[s_clean])

    matched_details = []
    for slug in matched_slugs:
        mod = get_disease_module(slug)
        matched_details.append({
            "disease_name": mod.name,
            "slug": mod.slug,
            "category": mod.category,
            "description": mod.description
        })

    return SymptomMatchResponse(
        matched_diseases=matched_details,
        disclaimer=(
            "Symptom matching is strictly for educational and decision-support triage. "
            "It does not constitute a clinical diagnosis. Consult a physician for symptom evaluation."
        )
    )
