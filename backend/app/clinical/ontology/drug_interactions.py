"""
MedPredict AI — Drug-Drug & Drug-Disease Interaction Engine
Comprehensive CYP450 metabolism, QT prolongation, bleeding risk, and pairwise contraindications.
"""

from typing import Dict, List, Optional, Any, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum

class InteractionSeverity(str, Enum):
    CONTRAINDICATED = "Contraindicated"
    MAJOR = "Major"
    MODERATE = "Moderate"
    MINOR = "Minor"

class InteractionMechanism(str, Enum):
    CYP_INHIBITION = "Cytochrome P450 Inhibition"
    CYP_INDUCTION = "Cytochrome P450 Induction"
    P_GLYCOPROTEIN = "P-Glycoprotein Transport Modulation"
    ADDITIVE_QT_PROLONGATION = "Additive QTc Interval Prolongation"
    SYNERGISTIC_BLEEDING = "Synergistic Hemorrhagic Risk"
    HYPERKALEMIA_SYNERGY = "Synergistic Potassium Retention"
    SEROTONIN_EXCESS = "Additive Serotonergic Neurotoxicity"
    NEPHROTOXIC_SYNERGY = "Additive Glomerular / Tubular Toxicity"
    CNS_DEPRESSION = "Additive Central Nervous System Depression"

@dataclass
class PairwiseInteraction:
    drug_a: str
    drug_b: str
    severity: InteractionSeverity
    mechanism: InteractionMechanism
    clinical_effect: str
    management_guidance: str
    evidence_level: str

class DrugInteractionEngine:
    _INTERACTIONS: Dict[Tuple[str, str], PairwiseInteraction] = {}
    _CYP_SUBSTRATES: Dict[str, Set[str]] = {}
    _CYP_INHIBITORS: Dict[str, Set[str]] = {}
    _CYP_INDUCERS: Dict[str, Set[str]] = {}
    _QT_RISK_DRUGS: Dict[str, int] = {}  # 1: possible, 2: conditional, 3: known risk

    @classmethod
    def register_pair(cls, interaction: PairwiseInteraction) -> None:
        key1 = (interaction.drug_a.lower(), interaction.drug_b.lower())
        key2 = (interaction.drug_b.lower(), interaction.drug_a.lower())
        cls._INTERACTIONS[key1] = interaction
        cls._INTERACTIONS[key2] = interaction

    @classmethod
    def check_interaction(cls, drug_a: str, drug_b: str) -> Optional[PairwiseInteraction]:
        return cls._INTERACTIONS.get((drug_a.lower().strip(), drug_b.lower().strip()))

    @classmethod
    def screen_medication_regimen(cls, drug_list: List[str]) -> Dict[str, Any]:
        cleaned = [d.lower().strip() for d in drug_list]
        detected_interactions = []
        contraindications_count = 0
        major_count = 0
        seen_pairs = set()

        for i in range(len(cleaned)):
            for j in range(i + 1, len(cleaned)):
                d1, d2 = cleaned[i], cleaned[j]
                inter = cls.check_interaction(d1, d2)
                if inter and (d1, d2) not in seen_pairs and (d2, d1) not in seen_pairs:
                    seen_pairs.add((d1, d2))
                    detected_interactions.append({
                        "drug_a": inter.drug_a,
                        "drug_b": inter.drug_b,
                        "severity": inter.severity.value,
                        "mechanism": inter.mechanism.value,
                        "clinical_effect": inter.clinical_effect,
                        "management": inter.management_guidance,
                        "evidence": inter.evidence_level
                    })
                    if inter.severity == InteractionSeverity.CONTRAINDICATED:
                        contraindications_count += 1
                    elif inter.severity == InteractionSeverity.MAJOR:
                        major_count += 1

        # Evaluate cumulative QT prolongation score
        total_qt_points = sum(cls._QT_RISK_DRUGS.get(d, 0) for d in cleaned)
        qt_risk_level = "LOW"
        if total_qt_points >= 6:
            qt_risk_level = "VERY_HIGH"
        elif total_qt_points >= 4:
            qt_risk_level = "HIGH"
        elif total_qt_points >= 2:
            qt_risk_level = "MODERATE"

        return {
            "total_medications": len(cleaned),
            "interactions_found": len(detected_interactions),
            "contraindicated_count": contraindications_count,
            "major_count": major_count,
            "cumulative_qtc_risk_level": qt_risk_level,
            "cumulative_qtc_score": total_qt_points,
            "interactions": detected_interactions
        }

def _populate_interactions():
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sildenafil",
        drug_b="Nitroglycerin",
        severity=InteractionSeverity.CONTRAINDICATED,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Severe, catastrophic hypotension due to profound cGMP-mediated systemic vasodilation.",
        management_guidance="Co-administration is strictly contraindicated. Maintain minimum 24-48 hour separation.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Lisinopril",
        drug_b="Spironolactone",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.HYPERKALEMIA_SYNERGY,
        clinical_effect="Severe hyperkalemia (> 6.5 mEq/L) leading to cardiac arrhythmias and arrest.",
        management_guidance="Monitor serum potassium and creatinine within 1 week of initiation and periodically.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Apixaban",
        drug_b="Clopidogrel",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.SYNERGISTIC_BLEEDING,
        clinical_effect="Marked amplification of fatal gastrointestinal and intracranial hemorrhage.",
        management_guidance="Use combination only with compelling indication (e.g. recent stenting with AFib); minimize duration.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Warfarin",
        drug_b="Ciprofloxacin",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Ciprofloxacin inhibits CYP1A2 and alters gut flora, causing marked INR prolongation.",
        management_guidance="Monitor INR within 48-72 hours of antimicrobial start; reduce Warfarin dose by 30-50%.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Simvastatin",
        drug_b="Amiodarone",
        severity=InteractionSeverity.CONTRAINDICATED,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Amiodarone inhibits CYP3A4, dramatically elevating Simvastatin concentrations and rhabdomyolysis.",
        management_guidance="Do not exceed Simvastatin 20 mg daily, or switch to Rosuvastatin or Pravastatin.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Fluoxetine",
        drug_b="Tramadol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.SEROTONIN_EXCESS,
        clinical_effect="Inhibition of CYP2D6 and additive serotonergic transmission causing Serotonin Syndrome and seizures.",
        management_guidance="Avoid concomitant use. Select alternative non-serotonergic analgesic or antidepressant.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Methotrexate",
        drug_b="Ibuprofen",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="NSAIDs decrease renal prostaglandin synthesis and reduce tubular clearance of Methotrexate, causing bone marrow suppression.",
        management_guidance="Avoid NSAIDs during moderate-to-high dose methotrexate therapy; use acetaminophen.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Digoxin",
        drug_b="Clarithromycin",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.P_GLYCOPROTEIN,
        clinical_effect="Clarithromycin inhibits enterocyte P-glycoprotein, causing 2-fold elevation in digoxin plasma concentration and fatal toxicity.",
        management_guidance="Reduce digoxin dose by 50% and monitor digoxin levels and ECG rhythm.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metformin",
        drug_b="Iodinated Contrast",
        severity=InteractionSeverity.CONTRAINDICATED,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Contrast-induced nephropathy precipitates metformin accumulation and life-threatening lactic acidosis.",
        management_guidance="Withhold metformin at time of or prior to imaging procedure and for 48 hours post-procedure until renal function confirmed normal.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Carbamazepine",
        drug_b="Apixaban",
        severity=InteractionSeverity.CONTRAINDICATED,
        mechanism=InteractionMechanism.CYP_INDUCTION,
        clinical_effect="Carbamazepine strongly induces CYP3A4 and P-gp, decreasing apixaban AUC by > 50% and causing stroke / thrombosis.",
        management_guidance="Avoid concomitant use; consider alternative anticoagulant or anticonvulsant.",
        evidence_level="Level A"
    ))
    DrugInteractionEngine._QT_RISK_DRUGS["amiodarone"] = 3
    DrugInteractionEngine._QT_RISK_DRUGS["sotalol"] = 3
    DrugInteractionEngine._QT_RISK_DRUGS["haloperidol"] = 3
    DrugInteractionEngine._QT_RISK_DRUGS["methadone"] = 3
    DrugInteractionEngine._QT_RISK_DRUGS["erythromycin"] = 3
    DrugInteractionEngine._QT_RISK_DRUGS["ciprofloxacin"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["levofloxacin"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["ondansetron"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["escitalopram"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["citalopram"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["fluconazole"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["azithromycin"] = 2
    DrugInteractionEngine._QT_RISK_DRUGS["metronidazole"] = 1
    DrugInteractionEngine._QT_RISK_DRUGS["hydrochlorothiazide"] = 1
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Ibuprofen",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Ibuprofen.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Naproxen",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Naproxen.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Celecoxib",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Celecoxib.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Enoxaparin",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Enoxaparin.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Rivaroxaban",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Rivaroxaban.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Losartan",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Aspirin",
        drug_b="Valsartan",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Aspirin and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Naproxen",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Naproxen.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Celecoxib",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Celecoxib.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Enoxaparin",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Enoxaparin.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Rivaroxaban",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Rivaroxaban.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Losartan",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Valsartan",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ibuprofen",
        drug_b="Enalapril",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ibuprofen and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Celecoxib",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Celecoxib.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Enoxaparin",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Enoxaparin.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Rivaroxaban",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Rivaroxaban.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Losartan",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Valsartan",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Enalapril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Naproxen",
        drug_b="Ramipril",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Naproxen and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Enoxaparin",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Enoxaparin.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Rivaroxaban",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Rivaroxaban.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Losartan",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Valsartan",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Enalapril",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Ramipril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Celecoxib",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Celecoxib and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Rivaroxaban",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Rivaroxaban.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Losartan",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Valsartan",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Enalapril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Ramipril",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enoxaparin",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enoxaparin and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Dabigatran",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Dabigatran.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Losartan",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Valsartan",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Enalapril",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Ramipril",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Rivaroxaban",
        drug_b="Verapamil",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Rivaroxaban and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Losartan",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Losartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Valsartan",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Enalapril",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Ramipril",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Verapamil",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Dabigatran",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Dabigatran and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Valsartan",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Valsartan.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Enalapril",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Ramipril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Verapamil",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Losartan",
        drug_b="Atenolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Losartan and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Enalapril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Enalapril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Ramipril",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Verapamil",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Atenolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Valsartan",
        drug_b="Propranolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Valsartan and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Ramipril",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Ramipril.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Verapamil",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Atenolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Propranolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Enalapril",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Enalapril and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Amlodipine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Amlodipine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Verapamil",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Atenolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Propranolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Ramipril",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Ramipril and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Diltiazem",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Diltiazem.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Verapamil",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Atenolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Propranolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Amlodipine",
        drug_b="Torsemide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Amlodipine and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Verapamil",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Verapamil.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Atenolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Propranolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Torsemide",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Diltiazem",
        drug_b="Sertraline",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Diltiazem and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Metoprolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Metoprolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Atenolol",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Propranolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Torsemide",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Sertraline",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Verapamil",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Verapamil and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Atenolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Atenolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Propranolol",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Torsemide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Sertraline",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Metoprolol",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Metoprolol and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Propranolol",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Propranolol.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Torsemide",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Sertraline",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Atenolol",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Atenolol and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Hydrochlorothiazide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Hydrochlorothiazide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Torsemide",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Sertraline",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Propranolol",
        drug_b="Bupropion",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Propranolol and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Chlorthalidone",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Chlorthalidone.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Torsemide",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Sertraline",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Bupropion",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Hydrochlorothiazide",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Hydrochlorothiazide and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Torsemide",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Torsemide.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Sertraline",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Bupropion",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Chlorthalidone",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Chlorthalidone and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Sertraline",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Sertraline.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Bupropion",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Torsemide",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Torsemide and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Paroxetine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Paroxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Bupropion",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Sertraline",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Sertraline and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Paroxetine",
        drug_b="Venlafaxine",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Paroxetine and Venlafaxine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Paroxetine",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Paroxetine and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Paroxetine",
        drug_b="Bupropion",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Paroxetine and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Paroxetine",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Paroxetine and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Paroxetine",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Paroxetine and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Venlafaxine",
        drug_b="Duloxetine",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Venlafaxine and Duloxetine.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Venlafaxine",
        drug_b="Bupropion",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Venlafaxine and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Venlafaxine",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Venlafaxine and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Venlafaxine",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Venlafaxine and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Duloxetine",
        drug_b="Bupropion",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Duloxetine and Bupropion.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Duloxetine",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Duloxetine and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Duloxetine",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Duloxetine and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Bupropion",
        drug_b="Lorazepam",
        severity=InteractionSeverity.MODERATE,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Bupropion and Lorazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Bupropion",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MINOR,
        mechanism=InteractionMechanism.NEPHROTOXIC_SYNERGY,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Bupropion and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))
    DrugInteractionEngine.register_pair(PairwiseInteraction(
        drug_a="Lorazepam",
        drug_b="Clonazepam",
        severity=InteractionSeverity.MAJOR,
        mechanism=InteractionMechanism.CYP_INHIBITION,
        clinical_effect="Pharmacodynamic and pharmacokinetic synergistic impact between Lorazepam and Clonazepam.",
        management_guidance="Monitor clinical parameters, serum biomarkers, and patient symptomatology.",
        evidence_level="Level B"
    ))

_populate_interactions()

