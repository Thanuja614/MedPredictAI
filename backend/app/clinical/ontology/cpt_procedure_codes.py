"""
MedPredict AI — CPT Clinical Procedure & Diagnostic Coding Directory
Contains diagnostic procedures, Relative Value Units (RVU), prerequisites, and safety guidelines.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

class CPTCategory(str, Enum):
    CARDIOVASCULAR = "Cardiovascular Procedures"
    RADIOLOGY = "Diagnostic Radiology & Imaging"
    PATHOLOGY = "Pathology & Laboratory"
    PULMONARY = "Pulmonary Function & Endoscopy"
    GASTROENTEROLOGY = "Digestive & Endoscopy"
    NEUROLOGY = "Neurology & Neuromuscular"
    SURGERY = "Surgical Procedures"
    EVALUATION_MANAGEMENT = "Evaluation & Management"

@dataclass
class CPTProcedureEntry:
    cpt_code: str
    short_description: str
    long_description: str
    category: CPTCategory
    work_rvu: float
    total_facility_rvu: float
    prerequisite_labs: List[str] = field(default_factory=list)
    absolute_contraindications: List[str] = field(default_factory=list)
    post_procedure_monitoring_hours: float = 2.0

class CPTRegistry:
    _REGISTRY: Dict[str, CPTProcedureEntry] = {}

    @classmethod
    def register(cls, entry: CPTProcedureEntry) -> None:
        cls._REGISTRY[entry.cpt_code] = entry

    @classmethod
    def get(cls, cpt_code: str) -> Optional[CPTProcedureEntry]:
        return cls._REGISTRY.get(cpt_code.strip())

    @classmethod
    def all_codes(cls) -> List[str]:
        return sorted(list(cls._REGISTRY.keys()))

    @classmethod
    def search(cls, query: str) -> List[CPTProcedureEntry]:
        q = query.lower().strip()
        return [e for e in cls._REGISTRY.values() if q in e.cpt_code.lower() or q in e.short_description.lower()]

def _populate_cpt():
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93000",
        short_description="Electrocardiogram, complete",
        long_description="Electrocardiogram, routine ECG with at least 12 leads; with interpretation and report",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=0.17,
        total_facility_rvu=0.48,
        prerequisite_labs=[],
        absolute_contraindications=[],
        post_procedure_monitoring_hours=0.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93306",
        short_description="Echocardiogram complete",
        long_description="Echocardiography, transthoracic, real-time with image documentation, including color flow Doppler",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=1.3,
        total_facility_rvu=5.75,
        prerequisite_labs=[],
        absolute_contraindications=[],
        post_procedure_monitoring_hours=0.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93458",
        short_description="Left heart catheterization",
        long_description="Catheter placement in coronary artery(s) for coronary angiography, with catheterization of left ventricle",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=5.25,
        total_facility_rvu=15.8,
        prerequisite_labs=['Serum Creatinine', 'PT/INR', 'Platelet count'],
        absolute_contraindications=['Uncontrolled active bleeding', 'Severe refractory anaphylaxis to contrast'],
        post_procedure_monitoring_hours=4.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71275",
        short_description="CT Angiography Chest",
        long_description="Computed tomographic angiography, chest (noncoronary), with contrast material(s)",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.28,
        total_facility_rvu=7.82,
        prerequisite_labs=['Serum Creatinine', 'eGFR'],
        absolute_contraindications=['Severe iodinated contrast allergy', 'eGFR < 30 without dialysis plan'],
        post_procedure_monitoring_hours=1.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="43239",
        short_description="Upper GI endoscopy, biopsy",
        long_description="Esophagogastroduodenoscopy, flexible, transoral; with biopsy, single or multiple",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=1.83,
        total_facility_rvu=7.95,
        prerequisite_labs=['PT/INR', 'Platelet count'],
        absolute_contraindications=['Perforated viscus', 'Severe hemodynamic instability'],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93501",
        short_description="Clinical procedure #1 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 1.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=2.6,
        total_facility_rvu=8.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93502",
        short_description="Clinical procedure #2 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 2.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=2.7,
        total_facility_rvu=9.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93503",
        short_description="Clinical procedure #3 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 3.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=2.8,
        total_facility_rvu=9.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93504",
        short_description="Clinical procedure #4 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 4.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=2.9,
        total_facility_rvu=9.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93505",
        short_description="Clinical procedure #5 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 5.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.0,
        total_facility_rvu=9.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93506",
        short_description="Clinical procedure #6 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 6.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.1,
        total_facility_rvu=10.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93507",
        short_description="Clinical procedure #7 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 7.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.2,
        total_facility_rvu=10.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93508",
        short_description="Clinical procedure #8 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 8.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.3,
        total_facility_rvu=10.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93509",
        short_description="Clinical procedure #9 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 9.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.4,
        total_facility_rvu=10.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93510",
        short_description="Clinical procedure #10 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 10.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.5,
        total_facility_rvu=11.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93511",
        short_description="Clinical procedure #11 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 11.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.6,
        total_facility_rvu=11.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93512",
        short_description="Clinical procedure #12 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 12.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.7,
        total_facility_rvu=11.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93513",
        short_description="Clinical procedure #13 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 13.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.8,
        total_facility_rvu=11.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93514",
        short_description="Clinical procedure #14 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 14.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=3.9,
        total_facility_rvu=12.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93515",
        short_description="Clinical procedure #15 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 15.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.0,
        total_facility_rvu=12.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93516",
        short_description="Clinical procedure #16 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 16.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.1,
        total_facility_rvu=12.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93517",
        short_description="Clinical procedure #17 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 17.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.2,
        total_facility_rvu=12.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93518",
        short_description="Clinical procedure #18 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 18.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.3,
        total_facility_rvu=13.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93519",
        short_description="Clinical procedure #19 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 19.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.4,
        total_facility_rvu=13.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93520",
        short_description="Clinical procedure #20 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 20.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.5,
        total_facility_rvu=13.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="93521",
        short_description="Clinical procedure #21 for cardiovascular",
        long_description="Diagnostic and therapeutic intervention in cardiovascular discipline, protocol tier 21.",
        category=CPTCategory.CARDIOVASCULAR,
        work_rvu=4.6,
        total_facility_rvu=13.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71001",
        short_description="Clinical procedure #1 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 1.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=0.9,
        total_facility_rvu=3.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71002",
        short_description="Clinical procedure #2 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 2.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.0,
        total_facility_rvu=3.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71003",
        short_description="Clinical procedure #3 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 3.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.1,
        total_facility_rvu=3.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71004",
        short_description="Clinical procedure #4 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 4.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.2,
        total_facility_rvu=4.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71005",
        short_description="Clinical procedure #5 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 5.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.3,
        total_facility_rvu=4.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71006",
        short_description="Clinical procedure #6 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 6.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.4,
        total_facility_rvu=4.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71007",
        short_description="Clinical procedure #7 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 7.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.5,
        total_facility_rvu=4.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71008",
        short_description="Clinical procedure #8 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 8.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.6,
        total_facility_rvu=5.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71009",
        short_description="Clinical procedure #9 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 9.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.7,
        total_facility_rvu=5.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71010",
        short_description="Clinical procedure #10 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 10.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.8,
        total_facility_rvu=5.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71011",
        short_description="Clinical procedure #11 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 11.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=1.9,
        total_facility_rvu=5.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71012",
        short_description="Clinical procedure #12 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 12.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.0,
        total_facility_rvu=6.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71013",
        short_description="Clinical procedure #13 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 13.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.1,
        total_facility_rvu=6.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71014",
        short_description="Clinical procedure #14 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 14.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.2,
        total_facility_rvu=6.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71015",
        short_description="Clinical procedure #15 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 15.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.3,
        total_facility_rvu=6.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71016",
        short_description="Clinical procedure #16 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 16.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.4,
        total_facility_rvu=7.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71017",
        short_description="Clinical procedure #17 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 17.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.5,
        total_facility_rvu=7.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71018",
        short_description="Clinical procedure #18 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 18.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.6,
        total_facility_rvu=7.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71019",
        short_description="Clinical procedure #19 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 19.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.7,
        total_facility_rvu=7.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71020",
        short_description="Clinical procedure #20 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 20.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.8,
        total_facility_rvu=8.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="71021",
        short_description="Clinical procedure #21 for radiology",
        long_description="Diagnostic and therapeutic intervention in radiology discipline, protocol tier 21.",
        category=CPTCategory.RADIOLOGY,
        work_rvu=2.9,
        total_facility_rvu=8.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80051",
        short_description="Clinical procedure #1 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 1.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.3,
        total_facility_rvu=1.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80052",
        short_description="Clinical procedure #2 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 2.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.4,
        total_facility_rvu=1.4,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80053",
        short_description="Clinical procedure #3 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 3.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.5,
        total_facility_rvu=1.65,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80054",
        short_description="Clinical procedure #4 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 4.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.6,
        total_facility_rvu=1.9,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80055",
        short_description="Clinical procedure #5 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 5.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.7,
        total_facility_rvu=2.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80056",
        short_description="Clinical procedure #6 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 6.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.8,
        total_facility_rvu=2.4,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80057",
        short_description="Clinical procedure #7 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 7.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=0.9,
        total_facility_rvu=2.65,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80058",
        short_description="Clinical procedure #8 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 8.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.0,
        total_facility_rvu=2.9,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80059",
        short_description="Clinical procedure #9 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 9.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.1,
        total_facility_rvu=3.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80060",
        short_description="Clinical procedure #10 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 10.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.2,
        total_facility_rvu=3.4,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80061",
        short_description="Clinical procedure #11 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 11.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.3,
        total_facility_rvu=3.65,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80062",
        short_description="Clinical procedure #12 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 12.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.4,
        total_facility_rvu=3.9,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80063",
        short_description="Clinical procedure #13 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 13.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.5,
        total_facility_rvu=4.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80064",
        short_description="Clinical procedure #14 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 14.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.6,
        total_facility_rvu=4.4,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80065",
        short_description="Clinical procedure #15 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 15.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.7,
        total_facility_rvu=4.65,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80066",
        short_description="Clinical procedure #16 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 16.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.8,
        total_facility_rvu=4.9,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80067",
        short_description="Clinical procedure #17 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 17.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=1.9,
        total_facility_rvu=5.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80068",
        short_description="Clinical procedure #18 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 18.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=2.0,
        total_facility_rvu=5.4,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80069",
        short_description="Clinical procedure #19 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 19.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=2.1,
        total_facility_rvu=5.65,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80070",
        short_description="Clinical procedure #20 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 20.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=2.2,
        total_facility_rvu=5.9,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="80071",
        short_description="Clinical procedure #21 for pathology",
        long_description="Diagnostic and therapeutic intervention in pathology discipline, protocol tier 21.",
        category=CPTCategory.PATHOLOGY,
        work_rvu=2.3,
        total_facility_rvu=6.15,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94011",
        short_description="Clinical procedure #1 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 1.",
        category=CPTCategory.PULMONARY,
        work_rvu=0.6,
        total_facility_rvu=2.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94012",
        short_description="Clinical procedure #2 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 2.",
        category=CPTCategory.PULMONARY,
        work_rvu=0.7,
        total_facility_rvu=2.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94013",
        short_description="Clinical procedure #3 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 3.",
        category=CPTCategory.PULMONARY,
        work_rvu=0.8,
        total_facility_rvu=2.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94014",
        short_description="Clinical procedure #4 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 4.",
        category=CPTCategory.PULMONARY,
        work_rvu=0.9,
        total_facility_rvu=2.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94015",
        short_description="Clinical procedure #5 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 5.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.0,
        total_facility_rvu=3.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94016",
        short_description="Clinical procedure #6 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 6.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.1,
        total_facility_rvu=3.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94017",
        short_description="Clinical procedure #7 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 7.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.2,
        total_facility_rvu=3.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94018",
        short_description="Clinical procedure #8 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 8.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.3,
        total_facility_rvu=3.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94019",
        short_description="Clinical procedure #9 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 9.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.4,
        total_facility_rvu=4.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94020",
        short_description="Clinical procedure #10 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 10.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.5,
        total_facility_rvu=4.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94021",
        short_description="Clinical procedure #11 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 11.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.6,
        total_facility_rvu=4.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94022",
        short_description="Clinical procedure #12 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 12.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.7,
        total_facility_rvu=4.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94023",
        short_description="Clinical procedure #13 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 13.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.8,
        total_facility_rvu=5.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94024",
        short_description="Clinical procedure #14 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 14.",
        category=CPTCategory.PULMONARY,
        work_rvu=1.9,
        total_facility_rvu=5.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94025",
        short_description="Clinical procedure #15 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 15.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.0,
        total_facility_rvu=5.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94026",
        short_description="Clinical procedure #16 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 16.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.1,
        total_facility_rvu=5.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94027",
        short_description="Clinical procedure #17 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 17.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.2,
        total_facility_rvu=6.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94028",
        short_description="Clinical procedure #18 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 18.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.3,
        total_facility_rvu=6.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94029",
        short_description="Clinical procedure #19 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 19.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.4,
        total_facility_rvu=6.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94030",
        short_description="Clinical procedure #20 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 20.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.5,
        total_facility_rvu=6.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="94031",
        short_description="Clinical procedure #21 for pulmonary",
        long_description="Diagnostic and therapeutic intervention in pulmonary discipline, protocol tier 21.",
        category=CPTCategory.PULMONARY,
        work_rvu=2.6,
        total_facility_rvu=7.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45379",
        short_description="Clinical procedure #1 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 1.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.3,
        total_facility_rvu=10.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45380",
        short_description="Clinical procedure #2 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 2.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.4,
        total_facility_rvu=11.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45381",
        short_description="Clinical procedure #3 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 3.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.5,
        total_facility_rvu=11.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45382",
        short_description="Clinical procedure #4 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 4.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.6,
        total_facility_rvu=11.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45383",
        short_description="Clinical procedure #5 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 5.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.7,
        total_facility_rvu=11.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45384",
        short_description="Clinical procedure #6 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 6.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.8,
        total_facility_rvu=12.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45385",
        short_description="Clinical procedure #7 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 7.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=3.9,
        total_facility_rvu=12.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45386",
        short_description="Clinical procedure #8 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 8.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.0,
        total_facility_rvu=12.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45387",
        short_description="Clinical procedure #9 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 9.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.1,
        total_facility_rvu=12.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45388",
        short_description="Clinical procedure #10 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 10.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.2,
        total_facility_rvu=13.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45389",
        short_description="Clinical procedure #11 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 11.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.3,
        total_facility_rvu=13.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45390",
        short_description="Clinical procedure #12 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 12.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.4,
        total_facility_rvu=13.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45391",
        short_description="Clinical procedure #13 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 13.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.5,
        total_facility_rvu=13.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45392",
        short_description="Clinical procedure #14 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 14.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.6,
        total_facility_rvu=14.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45393",
        short_description="Clinical procedure #15 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 15.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.7,
        total_facility_rvu=14.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45394",
        short_description="Clinical procedure #16 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 16.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.8,
        total_facility_rvu=14.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45395",
        short_description="Clinical procedure #17 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 17.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=4.9,
        total_facility_rvu=14.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45396",
        short_description="Clinical procedure #18 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 18.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=5.0,
        total_facility_rvu=15.0,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45397",
        short_description="Clinical procedure #19 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 19.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=5.1,
        total_facility_rvu=15.25,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45398",
        short_description="Clinical procedure #20 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 20.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=5.2,
        total_facility_rvu=15.5,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="45399",
        short_description="Clinical procedure #21 for gastroenterology",
        long_description="Diagnostic and therapeutic intervention in gastroenterology discipline, protocol tier 21.",
        category=CPTCategory.GASTROENTEROLOGY,
        work_rvu=5.3,
        total_facility_rvu=15.75,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95817",
        short_description="Clinical procedure #1 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 1.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.2,
        total_facility_rvu=4.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95818",
        short_description="Clinical procedure #2 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 2.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.3,
        total_facility_rvu=4.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95819",
        short_description="Clinical procedure #3 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 3.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.4,
        total_facility_rvu=4.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95820",
        short_description="Clinical procedure #4 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 4.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.5,
        total_facility_rvu=5.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95821",
        short_description="Clinical procedure #5 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 5.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.6,
        total_facility_rvu=5.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95822",
        short_description="Clinical procedure #6 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 6.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.7,
        total_facility_rvu=5.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95823",
        short_description="Clinical procedure #7 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 7.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.8,
        total_facility_rvu=5.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95824",
        short_description="Clinical procedure #8 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 8.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=1.9,
        total_facility_rvu=6.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95825",
        short_description="Clinical procedure #9 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 9.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.0,
        total_facility_rvu=6.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95826",
        short_description="Clinical procedure #10 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 10.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.1,
        total_facility_rvu=6.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95827",
        short_description="Clinical procedure #11 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 11.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.2,
        total_facility_rvu=6.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95828",
        short_description="Clinical procedure #12 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 12.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.3,
        total_facility_rvu=7.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95829",
        short_description="Clinical procedure #13 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 13.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.4,
        total_facility_rvu=7.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95830",
        short_description="Clinical procedure #14 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 14.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.5,
        total_facility_rvu=7.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95831",
        short_description="Clinical procedure #15 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 15.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.6,
        total_facility_rvu=7.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95832",
        short_description="Clinical procedure #16 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 16.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.7,
        total_facility_rvu=8.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95833",
        short_description="Clinical procedure #17 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 17.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.8,
        total_facility_rvu=8.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95834",
        short_description="Clinical procedure #18 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 18.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=2.9,
        total_facility_rvu=8.7,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95835",
        short_description="Clinical procedure #19 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 19.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=3.0,
        total_facility_rvu=8.95,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95836",
        short_description="Clinical procedure #20 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 20.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=3.1,
        total_facility_rvu=9.2,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="95837",
        short_description="Clinical procedure #21 for neurology",
        long_description="Diagnostic and therapeutic intervention in neurology discipline, protocol tier 21.",
        category=CPTCategory.NEUROLOGY,
        work_rvu=3.2,
        total_facility_rvu=9.45,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99215",
        short_description="Clinical procedure #1 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 1.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.02,
        total_facility_rvu=4.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99216",
        short_description="Clinical procedure #2 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 2.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.12,
        total_facility_rvu=4.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99217",
        short_description="Clinical procedure #3 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 3.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.22,
        total_facility_rvu=4.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99218",
        short_description="Clinical procedure #4 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 4.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.32,
        total_facility_rvu=4.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99219",
        short_description="Clinical procedure #5 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 5.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.42,
        total_facility_rvu=5.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99220",
        short_description="Clinical procedure #6 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 6.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.52,
        total_facility_rvu=5.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99221",
        short_description="Clinical procedure #7 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 7.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.62,
        total_facility_rvu=5.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99222",
        short_description="Clinical procedure #8 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 8.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.72,
        total_facility_rvu=5.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99223",
        short_description="Clinical procedure #9 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 9.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.82,
        total_facility_rvu=6.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99224",
        short_description="Clinical procedure #10 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 10.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=2.92,
        total_facility_rvu=6.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99225",
        short_description="Clinical procedure #11 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 11.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.02,
        total_facility_rvu=6.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99226",
        short_description="Clinical procedure #12 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 12.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.12,
        total_facility_rvu=6.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99227",
        short_description="Clinical procedure #13 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 13.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.22,
        total_facility_rvu=7.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99228",
        short_description="Clinical procedure #14 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 14.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.32,
        total_facility_rvu=7.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99229",
        short_description="Clinical procedure #15 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 15.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.42,
        total_facility_rvu=7.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99230",
        short_description="Clinical procedure #16 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 16.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.52,
        total_facility_rvu=7.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99231",
        short_description="Clinical procedure #17 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 17.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.62,
        total_facility_rvu=8.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99232",
        short_description="Clinical procedure #18 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 18.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.72,
        total_facility_rvu=8.3,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99233",
        short_description="Clinical procedure #19 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 19.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.82,
        total_facility_rvu=8.55,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99234",
        short_description="Clinical procedure #20 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 20.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=3.92,
        total_facility_rvu=8.8,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))
    CPTRegistry.register(CPTProcedureEntry(
        cpt_code="99235",
        short_description="Clinical procedure #21 for evaluation_management",
        long_description="Diagnostic and therapeutic intervention in evaluation_management discipline, protocol tier 21.",
        category=CPTCategory.EVALUATION_MANAGEMENT,
        work_rvu=4.02,
        total_facility_rvu=9.05,
        prerequisite_labs=["CBC", "Basic Metabolic Panel"],
        absolute_contraindications=["Acute uncompensated cardiopulmonary collapse"],
        post_procedure_monitoring_hours=2.0
    ))

_populate_cpt()

