"""
MedPredict AI — Clinical Decision Support & Ontologies Endpoints
Exposes ICD-10, LOINC, RxNorm, Drug Interactions, and Evidence-Based Protocols.
"""

from typing import Dict, Any, List, Optional
from fastapi import APIRouter, Query, HTTPException, status
from pydantic import BaseModel, Field

from backend.app.clinical.ontology import (
    ICD10Registry, LOINCRegistry, RxNormRegistry, DrugInteractionEngine
)
from backend.app.clinical.protocols import (
    CardiovascularProtocols, MetabolicEndocrineProtocols, RenalProtocols,
    CriticalCareProtocols, HepaticProtocols, PulmonaryProtocols
)

router = APIRouter(prefix="/clinical", tags=["Clinical Decision Support"])

class AscvdRiskRequest(BaseModel):
    age: int = Field(..., ge=20, le=100)
    gender: str = Field(..., pattern="^(male|female|MALE|FEMALE)$")
    race: str = Field(default="white")
    total_cholesterol: float = Field(..., ge=50, le=500)
    hdl_cholesterol: float = Field(..., ge=10, le=150)
    systolic_bp: float = Field(..., ge=70, le=260)
    bp_treated: bool = Field(default=False)
    smoker: bool = Field(default=False)
    diabetes: bool = Field(default=False)
    hscrp: Optional[float] = None
    cac_score: Optional[float] = None

class InteractionCheckRequest(BaseModel):
    medications: List[str] = Field(..., min_length=2)

class BiomarkerEvalRequest(BaseModel):
    loinc_code: str
    value: float
    unit: str
    gender: str = "male"
    age: int = 45

@router.get("/icd10/search")
def search_icd10(q: str = Query(..., min_length=2)):
    """Search ICD-10 clinical registry by code, disease title, or symptoms."""
    results = ICD10Registry.search(q)
    return {
        "query": q,
        "count": len(results),
        "results": [
            {
                "code": r.code,
                "title": r.title,
                "category": r.category.value,
                "is_chronic": r.is_chronic,
                "severity": r.severity.value,
                "symptoms": r.typical_symptoms,
                "primary_labs": r.primary_lab_tests,
                "first_line_meds": r.first_line_medications
            }
            for r in results[:50]
        ]
    }

@router.get("/loinc/search")
def search_loinc(q: str = Query(..., min_length=2)):
    """Search LOINC biomarker registry by LOINC number or component name."""
    results = LOINCRegistry.search(q)
    return {
        "query": q,
        "count": len(results),
        "results": [
            {
                "loinc": r.loinc_num,
                "component": r.component,
                "short_name": r.short_name,
                "category": r.category.value,
                "specimen": r.specimen.value,
                "conventional_unit": r.conventional_unit,
                "si_unit": r.si_unit
            }
            for r in results[:50]
        ]
    }

@router.post("/biomarker/evaluate")
def evaluate_biomarker(req: BiomarkerEvalRequest):
    """Evaluate patient biomarker value against biological reference intervals."""
    return LOINCRegistry.evaluate_biomarker(
        loinc_num=req.loinc_code,
        value=req.value,
        unit=req.unit,
        gender=req.gender,
        age=req.age
    )

@router.post("/medications/screen-interactions")
def screen_medications(req: InteractionCheckRequest):
    """Screen multi-drug regimen for CYP interactions, contraindications, and QTc risk."""
    return DrugInteractionEngine.screen_medication_regimen(req.medications)

@router.post("/protocols/ascvd-10year")
def calculate_ascvd(req: AscvdRiskRequest):
    """Compute 10-year Atherosclerotic Cardiovascular Disease (ASCVD) risk."""
    res = CardiovascularProtocols.calculate_ascvd_10year_risk(
        age=req.age,
        gender=req.gender,
        race=req.race,
        total_cholesterol=req.total_cholesterol,
        hdl_cholesterol=req.hdl_cholesterol,
        systolic_bp=req.systolic_bp,
        bp_treated=req.bp_treated,
        smoker=req.smoker,
        diabetes=req.diabetes,
        cac_score=req.cac_score,
        hscrp_mg_l=req.hscrp
    )
    return res
