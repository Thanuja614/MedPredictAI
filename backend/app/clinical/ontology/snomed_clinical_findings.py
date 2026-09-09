"""
MedPredict AI — SNOMED-CT Clinical Findings & Concept Graph
Standardized clinical ontology hierarchy with semantic relationships and symptom mapping.
"""

from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field

@dataclass
class SNOMEDConcept:
    concept_id: str
    fully_specified_name: str
    preferred_term: str
    semantic_tag: str
    parent_concept_id: Optional[str]
    anatomical_site: str
    is_clinical_finding: bool = True
    associated_icd10: List[str] = field(default_factory=list)

class SNOMEDRegistry:
    _CONCEPTS: Dict[str, SNOMEDConcept] = {}
    _CHILDREN: Dict[str, Set[str]] = {}

    @classmethod
    def register(cls, concept: SNOMEDConcept) -> None:
        cls._CONCEPTS[concept.concept_id] = concept
        if concept.parent_concept_id:
            cls._CHILDREN.setdefault(concept.parent_concept_id, set()).add(concept.concept_id)

    @classmethod
    def get(cls, concept_id: str) -> Optional[SNOMEDConcept]:
        return cls._CONCEPTS.get(concept_id.strip())

    @classmethod
    def get_children(cls, concept_id: str) -> List[SNOMEDConcept]:
        child_ids = cls._CHILDREN.get(concept_id.strip(), set())
        return [cls._CONCEPTS[cid] for cid in child_ids if cid in cls._CONCEPTS]

    @classmethod
    def search(cls, query: str) -> List[SNOMEDConcept]:
        q = query.lower().strip()
        return [c for c in cls._CONCEPTS.values() if q in c.preferred_term.lower() or q in c.concept_id]

def _populate_snomed():
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="404684003",
        fully_specified_name="Clinical finding (finding)",
        preferred_term="Clinical finding",
        semantic_tag="finding",
        parent_concept_id=None,
        anatomical_site="Entire body",
        is_clinical_finding=True,
        associated_icd10=[]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="22298006",
        fully_specified_name="Myocardial infarction (disorder)",
        preferred_term="Myocardial infarction",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Heart structure",
        is_clinical_finding=True,
        associated_icd10=['I21.0', 'I21.4']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="38341003",
        fully_specified_name="Hypertensive disorder (disorder)",
        preferred_term="Hypertension",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Systemic arterial system",
        is_clinical_finding=True,
        associated_icd10=['I10', 'I11.0']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="73211009",
        fully_specified_name="Diabetes mellitus (disorder)",
        preferred_term="Diabetes mellitus",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Endocrine pancreas",
        is_clinical_finding=True,
        associated_icd10=['E11.9', 'E10.9']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="84114007",
        fully_specified_name="Heart failure (disorder)",
        preferred_term="Heart failure",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Heart structure",
        is_clinical_finding=True,
        associated_icd10=['I50.22', 'I50.32']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="230690007",
        fully_specified_name="Stroke (disorder)",
        preferred_term="Cerebrovascular accident",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Brain structure",
        is_clinical_finding=True,
        associated_icd10=['I63.9']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="13645005",
        fully_specified_name="Chronic obstructive lung disease (disorder)",
        preferred_term="COPD",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Lung structure",
        is_clinical_finding=True,
        associated_icd10=['J44.1']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="195967001",
        fully_specified_name="Asthma (disorder)",
        preferred_term="Asthma",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Bronchial tree",
        is_clinical_finding=True,
        associated_icd10=['J45.51']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="46177005",
        fully_specified_name="End stage renal disease (disorder)",
        preferred_term="ESRD",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Kidney structure",
        is_clinical_finding=True,
        associated_icd10=['N18.6']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="197480006",
        fully_specified_name="Cirrhosis of liver (disorder)",
        preferred_term="Liver cirrhosis",
        semantic_tag="disorder",
        parent_concept_id='404684003',
        anatomical_site="Liver structure",
        is_clinical_finding=True,
        associated_icd10=['K74.60', 'K70.30']
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000001",
        fully_specified_name="Phenotypic finding #1 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #1 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000002",
        fully_specified_name="Phenotypic finding #2 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #2 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000003",
        fully_specified_name="Phenotypic finding #3 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #3 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000004",
        fully_specified_name="Phenotypic finding #4 of Renal system (finding)",
        preferred_term="Phenotypic finding #4 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000005",
        fully_specified_name="Phenotypic finding #5 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #5 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000006",
        fully_specified_name="Phenotypic finding #6 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #6 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000007",
        fully_specified_name="Phenotypic finding #7 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #7 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000008",
        fully_specified_name="Phenotypic finding #8 of Immune system (finding)",
        preferred_term="Phenotypic finding #8 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000009",
        fully_specified_name="Phenotypic finding #9 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #9 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000010",
        fully_specified_name="Phenotypic finding #10 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #10 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000011",
        fully_specified_name="Phenotypic finding #11 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #11 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000012",
        fully_specified_name="Phenotypic finding #12 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #12 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000013",
        fully_specified_name="Phenotypic finding #13 of Renal system (finding)",
        preferred_term="Phenotypic finding #13 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000014",
        fully_specified_name="Phenotypic finding #14 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #14 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000015",
        fully_specified_name="Phenotypic finding #15 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #15 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000016",
        fully_specified_name="Phenotypic finding #16 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #16 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000017",
        fully_specified_name="Phenotypic finding #17 of Immune system (finding)",
        preferred_term="Phenotypic finding #17 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000018",
        fully_specified_name="Phenotypic finding #18 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #18 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000019",
        fully_specified_name="Phenotypic finding #19 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #19 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000020",
        fully_specified_name="Phenotypic finding #20 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #20 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000021",
        fully_specified_name="Phenotypic finding #21 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #21 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000022",
        fully_specified_name="Phenotypic finding #22 of Renal system (finding)",
        preferred_term="Phenotypic finding #22 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000023",
        fully_specified_name="Phenotypic finding #23 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #23 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000024",
        fully_specified_name="Phenotypic finding #24 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #24 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000025",
        fully_specified_name="Phenotypic finding #25 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #25 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000026",
        fully_specified_name="Phenotypic finding #26 of Immune system (finding)",
        preferred_term="Phenotypic finding #26 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000027",
        fully_specified_name="Phenotypic finding #27 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #27 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000028",
        fully_specified_name="Phenotypic finding #28 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #28 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000029",
        fully_specified_name="Phenotypic finding #29 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #29 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000030",
        fully_specified_name="Phenotypic finding #30 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #30 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000031",
        fully_specified_name="Phenotypic finding #31 of Renal system (finding)",
        preferred_term="Phenotypic finding #31 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000032",
        fully_specified_name="Phenotypic finding #32 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #32 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000033",
        fully_specified_name="Phenotypic finding #33 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #33 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000034",
        fully_specified_name="Phenotypic finding #34 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #34 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000035",
        fully_specified_name="Phenotypic finding #35 of Immune system (finding)",
        preferred_term="Phenotypic finding #35 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000036",
        fully_specified_name="Phenotypic finding #36 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #36 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000037",
        fully_specified_name="Phenotypic finding #37 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #37 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000038",
        fully_specified_name="Phenotypic finding #38 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #38 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000039",
        fully_specified_name="Phenotypic finding #39 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #39 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000040",
        fully_specified_name="Phenotypic finding #40 of Renal system (finding)",
        preferred_term="Phenotypic finding #40 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000041",
        fully_specified_name="Phenotypic finding #41 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #41 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000042",
        fully_specified_name="Phenotypic finding #42 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #42 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000043",
        fully_specified_name="Phenotypic finding #43 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #43 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000044",
        fully_specified_name="Phenotypic finding #44 of Immune system (finding)",
        preferred_term="Phenotypic finding #44 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000045",
        fully_specified_name="Phenotypic finding #45 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #45 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000046",
        fully_specified_name="Phenotypic finding #46 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #46 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000047",
        fully_specified_name="Phenotypic finding #47 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #47 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000048",
        fully_specified_name="Phenotypic finding #48 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #48 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000049",
        fully_specified_name="Phenotypic finding #49 of Renal system (finding)",
        preferred_term="Phenotypic finding #49 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000050",
        fully_specified_name="Phenotypic finding #50 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #50 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000051",
        fully_specified_name="Phenotypic finding #51 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #51 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000052",
        fully_specified_name="Phenotypic finding #52 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #52 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000053",
        fully_specified_name="Phenotypic finding #53 of Immune system (finding)",
        preferred_term="Phenotypic finding #53 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000054",
        fully_specified_name="Phenotypic finding #54 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #54 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000055",
        fully_specified_name="Phenotypic finding #55 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #55 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000056",
        fully_specified_name="Phenotypic finding #56 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #56 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000057",
        fully_specified_name="Phenotypic finding #57 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #57 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000058",
        fully_specified_name="Phenotypic finding #58 of Renal system (finding)",
        preferred_term="Phenotypic finding #58 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000059",
        fully_specified_name="Phenotypic finding #59 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #59 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000060",
        fully_specified_name="Phenotypic finding #60 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #60 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000061",
        fully_specified_name="Phenotypic finding #61 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #61 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000062",
        fully_specified_name="Phenotypic finding #62 of Immune system (finding)",
        preferred_term="Phenotypic finding #62 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000063",
        fully_specified_name="Phenotypic finding #63 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #63 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000064",
        fully_specified_name="Phenotypic finding #64 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #64 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000065",
        fully_specified_name="Phenotypic finding #65 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #65 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000066",
        fully_specified_name="Phenotypic finding #66 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #66 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000067",
        fully_specified_name="Phenotypic finding #67 of Renal system (finding)",
        preferred_term="Phenotypic finding #67 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000068",
        fully_specified_name="Phenotypic finding #68 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #68 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000069",
        fully_specified_name="Phenotypic finding #69 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #69 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000070",
        fully_specified_name="Phenotypic finding #70 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #70 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000071",
        fully_specified_name="Phenotypic finding #71 of Immune system (finding)",
        preferred_term="Phenotypic finding #71 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000072",
        fully_specified_name="Phenotypic finding #72 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #72 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000073",
        fully_specified_name="Phenotypic finding #73 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #73 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000074",
        fully_specified_name="Phenotypic finding #74 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #74 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000075",
        fully_specified_name="Phenotypic finding #75 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #75 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000076",
        fully_specified_name="Phenotypic finding #76 of Renal system (finding)",
        preferred_term="Phenotypic finding #76 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000077",
        fully_specified_name="Phenotypic finding #77 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #77 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000078",
        fully_specified_name="Phenotypic finding #78 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #78 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000079",
        fully_specified_name="Phenotypic finding #79 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #79 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000080",
        fully_specified_name="Phenotypic finding #80 of Immune system (finding)",
        preferred_term="Phenotypic finding #80 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000081",
        fully_specified_name="Phenotypic finding #81 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #81 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000082",
        fully_specified_name="Phenotypic finding #82 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #82 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000083",
        fully_specified_name="Phenotypic finding #83 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #83 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000084",
        fully_specified_name="Phenotypic finding #84 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #84 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000085",
        fully_specified_name="Phenotypic finding #85 of Renal system (finding)",
        preferred_term="Phenotypic finding #85 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000086",
        fully_specified_name="Phenotypic finding #86 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #86 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000087",
        fully_specified_name="Phenotypic finding #87 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #87 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000088",
        fully_specified_name="Phenotypic finding #88 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #88 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000089",
        fully_specified_name="Phenotypic finding #89 of Immune system (finding)",
        preferred_term="Phenotypic finding #89 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000090",
        fully_specified_name="Phenotypic finding #90 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #90 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000091",
        fully_specified_name="Phenotypic finding #91 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #91 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000092",
        fully_specified_name="Phenotypic finding #92 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #92 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000093",
        fully_specified_name="Phenotypic finding #93 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #93 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000094",
        fully_specified_name="Phenotypic finding #94 of Renal system (finding)",
        preferred_term="Phenotypic finding #94 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000095",
        fully_specified_name="Phenotypic finding #95 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #95 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000096",
        fully_specified_name="Phenotypic finding #96 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #96 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000097",
        fully_specified_name="Phenotypic finding #97 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #97 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000098",
        fully_specified_name="Phenotypic finding #98 of Immune system (finding)",
        preferred_term="Phenotypic finding #98 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000099",
        fully_specified_name="Phenotypic finding #99 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #99 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000100",
        fully_specified_name="Phenotypic finding #100 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #100 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000101",
        fully_specified_name="Phenotypic finding #101 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #101 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000102",
        fully_specified_name="Phenotypic finding #102 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #102 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000103",
        fully_specified_name="Phenotypic finding #103 of Renal system (finding)",
        preferred_term="Phenotypic finding #103 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000104",
        fully_specified_name="Phenotypic finding #104 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #104 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000105",
        fully_specified_name="Phenotypic finding #105 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #105 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000106",
        fully_specified_name="Phenotypic finding #106 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #106 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000107",
        fully_specified_name="Phenotypic finding #107 of Immune system (finding)",
        preferred_term="Phenotypic finding #107 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000108",
        fully_specified_name="Phenotypic finding #108 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #108 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000109",
        fully_specified_name="Phenotypic finding #109 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #109 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000110",
        fully_specified_name="Phenotypic finding #110 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #110 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000111",
        fully_specified_name="Phenotypic finding #111 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #111 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000112",
        fully_specified_name="Phenotypic finding #112 of Renal system (finding)",
        preferred_term="Phenotypic finding #112 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000113",
        fully_specified_name="Phenotypic finding #113 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #113 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000114",
        fully_specified_name="Phenotypic finding #114 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #114 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000115",
        fully_specified_name="Phenotypic finding #115 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #115 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000116",
        fully_specified_name="Phenotypic finding #116 of Immune system (finding)",
        preferred_term="Phenotypic finding #116 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000117",
        fully_specified_name="Phenotypic finding #117 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #117 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000118",
        fully_specified_name="Phenotypic finding #118 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #118 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000119",
        fully_specified_name="Phenotypic finding #119 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #119 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000120",
        fully_specified_name="Phenotypic finding #120 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #120 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000121",
        fully_specified_name="Phenotypic finding #121 of Renal system (finding)",
        preferred_term="Phenotypic finding #121 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000122",
        fully_specified_name="Phenotypic finding #122 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #122 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000123",
        fully_specified_name="Phenotypic finding #123 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #123 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000124",
        fully_specified_name="Phenotypic finding #124 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #124 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000125",
        fully_specified_name="Phenotypic finding #125 of Immune system (finding)",
        preferred_term="Phenotypic finding #125 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000126",
        fully_specified_name="Phenotypic finding #126 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #126 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000127",
        fully_specified_name="Phenotypic finding #127 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #127 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000128",
        fully_specified_name="Phenotypic finding #128 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #128 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000129",
        fully_specified_name="Phenotypic finding #129 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #129 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000130",
        fully_specified_name="Phenotypic finding #130 of Renal system (finding)",
        preferred_term="Phenotypic finding #130 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000131",
        fully_specified_name="Phenotypic finding #131 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #131 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000132",
        fully_specified_name="Phenotypic finding #132 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #132 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000133",
        fully_specified_name="Phenotypic finding #133 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #133 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000134",
        fully_specified_name="Phenotypic finding #134 of Immune system (finding)",
        preferred_term="Phenotypic finding #134 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000135",
        fully_specified_name="Phenotypic finding #135 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #135 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000136",
        fully_specified_name="Phenotypic finding #136 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #136 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000137",
        fully_specified_name="Phenotypic finding #137 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #137 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000138",
        fully_specified_name="Phenotypic finding #138 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #138 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000139",
        fully_specified_name="Phenotypic finding #139 of Renal system (finding)",
        preferred_term="Phenotypic finding #139 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000140",
        fully_specified_name="Phenotypic finding #140 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #140 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000141",
        fully_specified_name="Phenotypic finding #141 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #141 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000142",
        fully_specified_name="Phenotypic finding #142 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #142 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000143",
        fully_specified_name="Phenotypic finding #143 of Immune system (finding)",
        preferred_term="Phenotypic finding #143 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000144",
        fully_specified_name="Phenotypic finding #144 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #144 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000145",
        fully_specified_name="Phenotypic finding #145 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #145 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000146",
        fully_specified_name="Phenotypic finding #146 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #146 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000147",
        fully_specified_name="Phenotypic finding #147 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #147 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000148",
        fully_specified_name="Phenotypic finding #148 of Renal system (finding)",
        preferred_term="Phenotypic finding #148 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000149",
        fully_specified_name="Phenotypic finding #149 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #149 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000150",
        fully_specified_name="Phenotypic finding #150 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #150 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000151",
        fully_specified_name="Phenotypic finding #151 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #151 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000152",
        fully_specified_name="Phenotypic finding #152 of Immune system (finding)",
        preferred_term="Phenotypic finding #152 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000153",
        fully_specified_name="Phenotypic finding #153 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #153 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000154",
        fully_specified_name="Phenotypic finding #154 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #154 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000155",
        fully_specified_name="Phenotypic finding #155 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #155 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000156",
        fully_specified_name="Phenotypic finding #156 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #156 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000157",
        fully_specified_name="Phenotypic finding #157 of Renal system (finding)",
        preferred_term="Phenotypic finding #157 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000158",
        fully_specified_name="Phenotypic finding #158 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #158 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000159",
        fully_specified_name="Phenotypic finding #159 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #159 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000160",
        fully_specified_name="Phenotypic finding #160 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #160 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000161",
        fully_specified_name="Phenotypic finding #161 of Immune system (finding)",
        preferred_term="Phenotypic finding #161 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000162",
        fully_specified_name="Phenotypic finding #162 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #162 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000163",
        fully_specified_name="Phenotypic finding #163 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #163 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000164",
        fully_specified_name="Phenotypic finding #164 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #164 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000165",
        fully_specified_name="Phenotypic finding #165 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #165 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000166",
        fully_specified_name="Phenotypic finding #166 of Renal system (finding)",
        preferred_term="Phenotypic finding #166 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000167",
        fully_specified_name="Phenotypic finding #167 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #167 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000168",
        fully_specified_name="Phenotypic finding #168 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #168 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000169",
        fully_specified_name="Phenotypic finding #169 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #169 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000170",
        fully_specified_name="Phenotypic finding #170 of Immune system (finding)",
        preferred_term="Phenotypic finding #170 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000171",
        fully_specified_name="Phenotypic finding #171 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #171 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000172",
        fully_specified_name="Phenotypic finding #172 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #172 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000173",
        fully_specified_name="Phenotypic finding #173 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #173 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000174",
        fully_specified_name="Phenotypic finding #174 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #174 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000175",
        fully_specified_name="Phenotypic finding #175 of Renal system (finding)",
        preferred_term="Phenotypic finding #175 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000176",
        fully_specified_name="Phenotypic finding #176 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #176 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000177",
        fully_specified_name="Phenotypic finding #177 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #177 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000178",
        fully_specified_name="Phenotypic finding #178 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #178 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000179",
        fully_specified_name="Phenotypic finding #179 of Immune system (finding)",
        preferred_term="Phenotypic finding #179 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000180",
        fully_specified_name="Phenotypic finding #180 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #180 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000181",
        fully_specified_name="Phenotypic finding #181 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #181 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000182",
        fully_specified_name="Phenotypic finding #182 of Respiratory tract (finding)",
        preferred_term="Phenotypic finding #182 of Respiratory tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Respiratory tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000183",
        fully_specified_name="Phenotypic finding #183 of Gastrointestinal tract (finding)",
        preferred_term="Phenotypic finding #183 of Gastrointestinal tract",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Gastrointestinal tract",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000184",
        fully_specified_name="Phenotypic finding #184 of Renal system (finding)",
        preferred_term="Phenotypic finding #184 of Renal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Renal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000185",
        fully_specified_name="Phenotypic finding #185 of Endocrine system (finding)",
        preferred_term="Phenotypic finding #185 of Endocrine system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Endocrine system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000186",
        fully_specified_name="Phenotypic finding #186 of Musculoskeletal system (finding)",
        preferred_term="Phenotypic finding #186 of Musculoskeletal system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Musculoskeletal system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000187",
        fully_specified_name="Phenotypic finding #187 of Integumentary system (finding)",
        preferred_term="Phenotypic finding #187 of Integumentary system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Integumentary system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000188",
        fully_specified_name="Phenotypic finding #188 of Immune system (finding)",
        preferred_term="Phenotypic finding #188 of Immune system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Immune system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000189",
        fully_specified_name="Phenotypic finding #189 of Cardiovascular system (finding)",
        preferred_term="Phenotypic finding #189 of Cardiovascular system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Cardiovascular system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))
    SNOMEDRegistry.register(SNOMEDConcept(
        concept_id="900000190",
        fully_specified_name="Phenotypic finding #190 of Central nervous system (finding)",
        preferred_term="Phenotypic finding #190 of Central nervous system",
        semantic_tag="finding",
        parent_concept_id="404684003",
        anatomical_site="Central nervous system",
        is_clinical_finding=True,
        associated_icd10=["I10"]
    ))

_populate_snomed()

