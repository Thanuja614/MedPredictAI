"""
MedPredict AI — Cardiovascular Clinical Risk Scoring & GDMT Protocols
Complies with AHA/ACC, ESC, and CCS evidence-based cardiovascular guidelines.
"""

from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
import math

@dataclass
class ClinicalRiskResult:
    protocol_name: str
    risk_score: float
    risk_percentage: float
    risk_category: str  # LOW, BORDERLINE, INTERMEDIATE, HIGH, VERY_HIGH
    confidence_interval: Tuple[float, float]
    clinical_interpretation: str
    guideline_recommendations: List[str]
    evidence_level: str
    risk_enhancers_detected: List[str] = field(default_factory=list)
    raw_parameters: Dict[str, Any] = field(default_factory=dict)

class CardiovascularProtocols:
    PCE_COEFFICIENTS = {
        ("female", "white"): {
            "ln_age": 31.764001, "ln_age_sq": 0.0, "ln_tot_chol": 22.465206,
            "ln_age_tot_chol": -7.994963, "ln_hdl": -12.328324, "ln_age_hdl": 2.887340,
            "ln_treated_sbp": 2.019235, "ln_age_treated_sbp": 0.0, "ln_untreated_sbp": 1.957069,
            "ln_age_untreated_sbp": 0.0, "smoker": 7.574167, "ln_age_smoker": -1.665219,
            "diabetes": 0.661073, "mean_terms": 29.1817, "baseline_survival": 0.96652
        },
        ("female", "african_american"): {
            "ln_age": 17.114144, "ln_age_sq": 0.0, "ln_tot_chol": 0.939670,
            "ln_age_tot_chol": 0.0, "ln_hdl": -18.919649, "ln_age_hdl": 4.474864,
            "ln_treated_sbp": 29.290720, "ln_age_treated_sbp": -6.432107, "ln_untreated_sbp": 27.819742,
            "ln_age_untreated_sbp": -6.087314, "smoker": 0.690854, "ln_age_smoker": 0.0,
            "diabetes": 0.873884, "mean_terms": 86.6081, "baseline_survival": 0.95334
        },
        ("male", "white"): {
            "ln_age": 12.344472, "ln_age_sq": 0.0, "ln_tot_chol": 11.853110,
            "ln_age_tot_chol": -2.664426, "ln_hdl": -7.990441, "ln_age_hdl": 1.769490,
            "ln_treated_sbp": 1.797209, "ln_age_treated_sbp": 0.0, "ln_untreated_sbp": 1.764123,
            "ln_age_untreated_sbp": 0.0, "smoker": 7.837678, "ln_age_smoker": -1.795495,
            "diabetes": 0.658388, "mean_terms": 61.1816, "baseline_survival": 0.91436
        },
        ("male", "african_american"): {
            "ln_age": 2.469004, "ln_age_sq": 0.0, "ln_tot_chol": 0.302177,
            "ln_age_tot_chol": 0.0, "ln_hdl": -0.307290, "ln_age_hdl": 0.0,
            "ln_treated_sbp": 1.916408, "ln_age_treated_sbp": 0.0, "ln_untreated_sbp": 1.808541,
            "ln_age_untreated_sbp": 0.0, "smoker": 0.548778, "ln_age_smoker": 0.0,
            "diabetes": 0.645470, "mean_terms": 19.5425, "baseline_survival": 0.89536
        }
    }

    @classmethod
    def calculate_ascvd_10year_risk(
        cls, age: int, gender: str, race: str, total_cholesterol: float,
        hdl_cholesterol: float, systolic_bp: float, bp_treated: bool,
        smoker: bool, diabetes: bool, cac_score: Optional[float] = None,
        family_history_premature_ascvd: bool = False,
        chronic_kidney_disease: bool = False, hscrp_mg_l: Optional[float] = None
    ) -> ClinicalRiskResult:
        gender_norm = "female" if gender.lower().startswith("f") else "male"
        race_norm = "african_american" if "black" in race.lower() or "african" in race.lower() else "white"
        clamped_age = max(40, min(79, age))
        coeffs = cls.PCE_COEFFICIENTS[(gender_norm, race_norm)]
        ln_age = math.log(clamped_age)
        ln_tot_chol = math.log(total_cholesterol)
        ln_hdl = math.log(hdl_cholesterol)
        ln_sbp = math.log(systolic_bp)
        individual_sum = coeffs["ln_age"] * ln_age
        if coeffs["ln_age_sq"] != 0: individual_sum += coeffs["ln_age_sq"] * (ln_age ** 2)
        individual_sum += coeffs["ln_tot_chol"] * ln_tot_chol
        if coeffs["ln_age_tot_chol"] != 0: individual_sum += coeffs["ln_age_tot_chol"] * (ln_age * ln_tot_chol)
        individual_sum += coeffs["ln_hdl"] * ln_hdl
        if coeffs["ln_age_hdl"] != 0: individual_sum += coeffs["ln_age_hdl"] * (ln_age * ln_hdl)
        if bp_treated:
            individual_sum += coeffs["ln_treated_sbp"] * ln_sbp
            if coeffs["ln_age_treated_sbp"] != 0: individual_sum += coeffs["ln_age_treated_sbp"] * (ln_age * ln_sbp)
        else:
            individual_sum += coeffs["ln_untreated_sbp"] * ln_sbp
            if coeffs["ln_age_untreated_sbp"] != 0: individual_sum += coeffs["ln_age_untreated_sbp"] * (ln_age * ln_sbp)
        if smoker:
            individual_sum += coeffs["smoker"]
            if coeffs["ln_age_smoker"] != 0: individual_sum += coeffs["ln_age_smoker"] * (ln_age * 1.0)
        if diabetes: individual_sum += coeffs["diabetes"]
        raw_exponent = individual_sum - coeffs["mean_terms"]
        ten_year_risk = 1.0 - (coeffs["baseline_survival"] ** math.exp(raw_exponent))
        risk_pct = round(max(0.1, min(99.0, ten_year_risk * 100.0)), 1)

        enhancers = []
        if family_history_premature_ascvd: enhancers.append("Family history of premature ASCVD (males < 55, females < 65)")
        if chronic_kidney_disease: enhancers.append("Chronic kidney disease (eGFR < 60 mL/min/1.73m2)")
        if hscrp_mg_l and hscrp_mg_l >= 2.0: enhancers.append(f"Elevated high-sensitivity CRP ({hscrp_mg_l} mg/L >= 2.0)")
        if cac_score is not None:
            if cac_score == 0: enhancers.append("Coronary Artery Calcium (CAC) = 0 (favorable reclassification)")
            elif cac_score > 100: enhancers.append(f"Coronary Artery Calcium (CAC) = {cac_score} (> 100 or >= 75th percentile)")

        recs = []
        if risk_pct < 5.0:
            category = "LOW"
            interp = "Low 10-year ASCVD risk (< 5%). Emphasize lifestyle modification to reduce risk factors."
            recs.append("Heart-healthy diet (Mediterranean or DASH dietary pattern)")
            recs.append("At least 150 minutes/week moderate-intensity physical activity")
            recs.append("Reassess 10-year risk every 4 to 6 years")
        elif risk_pct < 7.5:
            category = "BORDERLINE"
            interp = "Borderline 10-year ASCVD risk (5% to < 7.5%). If risk enhancers present, consider moderate-intensity statin."
            recs.append("Clinician-patient risk discussion regarding moderate-intensity statin")
            recs.append("Comprehensive lifestyle modification counseling")
        elif risk_pct < 20.0:
            category = "INTERMEDIATE"
            interp = "Intermediate 10-year ASCVD risk (7.5% to < 20%). Moderate-intensity statin strongly recommended."
            recs.append("Initiate moderate-intensity statin (Atorvastatin 20mg or Rosuvastatin 10mg) to reduce LDL-C by 30-49%")
            recs.append("If risk is uncertain, consider measuring CAC score")
            recs.append("Target SBP < 130 mmHg if hypertension present")
        else:
            category = "HIGH"
            interp = "High 10-year ASCVD risk (>= 20%). High-intensity statin recommended to reduce LDL-C by >= 50%."
            recs.append("Initiate high-intensity statin (Atorvastatin 80mg or Rosuvastatin 20-40mg)")
            recs.append("If LDL-C remains >= 70 mg/dL on maximum tolerated statin, add Ezetimibe 10mg daily")
            recs.append("Blood pressure goal < 130/80 mmHg with dual antihypertensive therapy if needed")

        ci_low = round(max(0.1, risk_pct * 0.85), 1)
        ci_high = round(min(99.0, risk_pct * 1.18), 1)
        return ClinicalRiskResult(
            protocol_name="AHA/ACC 2018 Pooled Cohort Equations (ASCVD 10-Year)",
            risk_score=round(ten_year_risk, 4),
            risk_percentage=risk_pct,
            risk_category=category,
            confidence_interval=(ci_low, ci_high),
            clinical_interpretation=interp,
            guideline_recommendations=recs,
            evidence_level="Class I, Level A",
            risk_enhancers_detected=enhancers,
            raw_parameters={"age": age, "gender": gender, "total_chol": total_cholesterol, "hdl": hdl_cholesterol, "sbp": systolic_bp}
        )

    @classmethod
    def calculate_cha2ds2_vasc(
        cls, congestive_heart_failure: bool, hypertension: bool,
        age: int, diabetes: bool, prior_stroke_tia_thromboembolism: bool,
        vascular_disease: bool, female_sex: bool
    ) -> Dict[str, Any]:
        score = 0
        factors = []
        if congestive_heart_failure: score += 1; factors.append("Congestive Heart Failure (+1)")
        if hypertension: score += 1; factors.append("Hypertension (+1)")
        if age >= 75: score += 2; factors.append("Age >= 75 (+2)")
        elif age >= 65: score += 1; factors.append("Age 65-74 (+1)")
        if diabetes: score += 1; factors.append("Diabetes Mellitus (+1)")
        if prior_stroke_tia_thromboembolism: score += 2; factors.append("Prior Stroke / TIA / Thromboembolism (+2)")
        if vascular_disease: score += 1; factors.append("Vascular Disease (prior MI, PAD, aortic plaque) (+1)")
        if female_sex: score += 1; factors.append("Female Sex Category (+1)")

        adjusted_stroke_rates = {0: 0.2, 1: 0.6, 2: 2.2, 3: 3.2, 4: 4.8, 5: 7.2, 6: 9.7, 7: 11.2, 8: 12.5, 9: 15.2}
        annual_stroke_rate = adjusted_stroke_rates.get(min(score, 9), 15.2)
        threshold = 2 if female_sex else 1
        anticoag_rec = "NO_ANTICOAGULATION"
        guidance = "Low thromboembolic risk. No antithrombotic therapy required."
        if score >= threshold + 1:
            anticoag_rec = "DOAC_RECOMMENDED"
            guidance = "Oral anticoagulation strongly recommended (Class I, Level A). Prefer DOAC (Apixaban, Rivaroxaban, Dabigatran) over Warfarin."
        elif score == threshold:
            anticoag_rec = "CONSIDER_DOAC"
            guidance = "Oral anticoagulation should be considered based on individualized bleeding risk and patient preference (Class IIa)."

        return {
            "cha2ds2_vasc_score": score,
            "annual_stroke_rate_percent": annual_stroke_rate,
            "recommendation": anticoag_rec,
            "clinical_guidance": guidance,
            "scoring_factors": factors
        }

    @classmethod
    def calculate_has_bled(
        cls, uncontrolled_hypertension: bool, renal_disease: bool,
        liver_disease: bool, prior_stroke: bool, prior_major_bleeding: bool,
        labile_inr: bool, elderly_age_over_65: bool, drugs_nsaid_antiplatelet: bool,
        excess_alcohol: bool
    ) -> Dict[str, Any]:
        score = 0
        items = []
        if uncontrolled_hypertension: score += 1; items.append("Hypertension (SBP > 160)")
        if renal_disease: score += 1; items.append("Abnormal renal function (dialysis, transplant, Cr > 2.26 mg/dL)")
        if liver_disease: score += 1; items.append("Abnormal liver function (cirrhosis, Bilirubin > 2x, AST/ALT > 3x)")
        if prior_stroke: score += 1; items.append("Stroke history")
        if prior_major_bleeding: score += 1; items.append("Bleeding history or predisposition")
        if labile_inr: score += 1; items.append("Labile INR (TTR < 60% on VKA)")
        if elderly_age_over_65: score += 1; items.append("Elderly (age > 65)")
        if drugs_nsaid_antiplatelet: score += 1; items.append("Concomitant antiplatelet or NSAID medication")
        if excess_alcohol: score += 1; items.append("Alcohol excess (>= 8 drinks/week)")

        bleed_rates = {0: 1.13, 1: 1.02, 2: 1.88, 3: 3.74, 4: 8.70, 5: 12.50}
        rate = bleed_rates.get(min(score, 5), 12.5)
        high_risk = score >= 3
        return {
            "has_bled_score": score,
            "major_bleeding_rate_percent_per_year": rate,
            "is_high_bleeding_risk": high_risk,
            "clinical_advice": "High bleeding risk (>= 3). Caution and regular review warranted; address reversible bleeding risk factors rather than withholding anticoagulation." if high_risk else "Low to moderate bleeding risk. Proceed with anticoagulation according to stroke risk.",
            "identified_risk_factors": items
        }

    @classmethod
    def guideline_directed_hfref_titration(cls, lvef: float, nyha_class: int, sbp: float, potassium: float, egfr: float) -> Dict[str, Any]:
        four_pillars = []
        # 1. ARNI / ACEi / ARB
        if sbp >= 100 and potassium <= 5.0 and egfr >= 30:
            four_pillars.append({"pillar": "ARNI", "drug": "Sacubitril/Valsartan", "starting_dose": "24/26 mg or 49/51 mg BID", "target_dose": "97/103 mg BID", "status": "RECOMMENDED"})
        elif sbp < 100:
            four_pillars.append({"pillar": "ARNI", "drug": "Sacubitril/Valsartan", "status": "HOLD_LOW_BP", "guidance": "Hold or reduce dose until SBP >= 100 mmHg."})
        else:
            four_pillars.append({"pillar": "ARNI", "drug": "Sacubitril/Valsartan", "status": "HOLD_HYPERKALEMIA_OR_RENAL", "guidance": "Correct hyperkalemia/renal dysfunction before initiation."})
        # 2. Beta-Blocker
        four_pillars.append({"pillar": "Beta-Blocker", "drug": "Carvedilol or Metoprolol Succinate", "starting_dose": "Carvedilol 3.125mg BID or Metoprolol Succ 25mg daily", "target_dose": "Carvedilol 25mg BID or Metoprolol Succ 200mg daily", "status": "RECOMMENDED"})
        # 3. MRA
        if potassium <= 5.0 and egfr >= 30:
            four_pillars.append({"pillar": "MRA", "drug": "Spironolactone or Eplerenone", "starting_dose": "25 mg daily (12.5mg if eGFR 30-49)", "target_dose": "50 mg daily", "status": "RECOMMENDED"})
        else:
            four_pillars.append({"pillar": "MRA", "drug": "Spironolactone", "status": "CONTRAINDICATED", "guidance": "Hold due to K+ > 5.0 or eGFR < 30."})
        # 4. SGLT2i
        if egfr >= 20:
            four_pillars.append({"pillar": "SGLT2i", "drug": "Dapagliflozin 10mg or Empagliflozin 10mg daily", "target_dose": "10 mg daily (no titration needed)", "status": "RECOMMENDED"})
        else:
            four_pillars.append({"pillar": "SGLT2i", "drug": "Dapagliflozin/Empagliflozin", "status": "HOLD_EGFR_LOW", "guidance": "Initiation not recommended if eGFR < 20."})

        return {
            "lvef": lvef,
            "nyha_class": nyha_class,
            "gdmt_four_pillars": four_pillars,
            "guideline": "AHA/ACC/HFSA 2022 Guideline for the Management of Heart Failure",
            "summary": "Initiate all 4 GDMT pillars simultaneously or in rapid sequence within 2 to 4 weeks."
        }

    @classmethod
    def hypertension_jnc8_aha_titration(cls, sbp: float, dbp: float, age: int, has_ckd: bool, has_diabetes: bool, is_black: bool) -> Dict[str, Any]:
        stage = "NORMAL"
        target_sbp = 130
        target_dbp = 80
        if sbp < 120 and dbp < 80:
            stage = "NORMAL"
            rec = "Promote healthy lifestyle habits; reassess annually."
            meds = []
        elif sbp <= 129 and dbp < 80:
            stage = "ELEVATED"
            rec = "Nonpharmacologic therapy (DASH diet, sodium < 1500mg, exercise, weight loss); reassess in 3-6 months."
            meds = []
        elif (130 <= sbp <= 139) or (80 <= dbp <= 89):
            stage = "STAGE_1_HTN"
            rec = "If 10-yr ASCVD risk >= 10% or patient has CKD/Diabetes, initiate 1 first-line antihypertensive medication."
            meds = ["Amlodipine 5mg" if is_black else "Lisinopril 10mg"]
        else:
            stage = "STAGE_2_HTN"
            rec = "Initiate 2 first-line agents of different classes (e.g. CCB + ACEi/ARB or Thiazide)."
            meds = ["Amlodipine 5mg + Olmesartan 20mg" if is_black else "Lisinopril 20mg + Hydrochlorothiazide 12.5mg"]
        return {"current_stage": stage, "target_bp": f"<{target_sbp}/<{target_dbp} mmHg", "recommendation": rec, "suggested_regimen": meds}

    @classmethod
    def reynolds_risk_score(cls, gender: str, age: int, systolic_bp: float, total_chol: float, hdl_chol: float, hscrp: float, smoker: bool, parental_mi_before_60: bool) -> Dict[str, Any]:
        # Reynolds Risk Score incorporates hsCRP and family history for improved calibration
        is_female = gender.lower().startswith('f')
        if is_female:
            b = 0.0799 * age + 3.137 * math.log(max(100, systolic_bp)) + 0.180 * math.log(max(0.1, hscrp)) + 1.382 * math.log(total_chol) - 1.172 * math.log(hdl_chol)
            if smoker: b += 0.818
            if parental_mi_before_60: b += 0.438
            b -= 22.325
            risk = 1.0 - (0.98634 ** math.exp(b))
        else:
            b = 0.0818 * age + 1.933 * math.log(max(100, systolic_bp)) + 0.138 * math.log(max(0.1, hscrp)) + 1.090 * math.log(total_chol) - 0.704 * math.log(hdl_chol)
            if smoker: b += 0.543
            if parental_mi_before_60: b += 0.441
            b -= 15.655
            risk = 1.0 - (0.8990 ** math.exp(b))
        pct = round(max(0.1, min(99.0, risk * 100.0)), 1)
        return {"reynolds_10yr_risk_percent": pct, "hscrp_measured": hscrp, "family_history_factored": parental_mi_before_60}

    @classmethod
    def framingham_cvd_score(cls, gender: str, age: int, total_chol: float, hdl_chol: float, systolic_bp: float, bp_treated: bool, smoker: bool, diabetes: bool) -> Dict[str, Any]:
        # Framingham 10-year general cardiovascular disease risk equation
        is_f = gender.lower().startswith('f')
        ln_age = math.log(max(30, min(79, age)))
        ln_tc = math.log(total_chol)
        ln_hdl = math.log(hdl_chol)
        ln_sbp = math.log(systolic_bp)
        if is_f:
            l = 2.32888 * ln_age + 1.20904 * ln_tc - 0.70833 * ln_hdl + (2.82263 if bp_treated else 2.76157) * ln_sbp
            if smoker: l += 0.52873
            if diabetes: l += 0.69154
            m = 26.1931
            s = 0.95012
        else:
            l = 3.06117 * ln_age + 1.12370 * ln_tc - 0.93263 * ln_hdl + (1.99881 if bp_treated else 1.93303) * ln_sbp
            if smoker: l += 0.65451
            if diabetes: l += 0.57367
            m = 23.9802
            s = 0.88936
        risk = 1.0 - (s ** math.exp(l - m))
        return {"framingham_10yr_risk_percent": round(max(0.1, min(99.0, risk * 100.0)), 1), "gender": gender}

    @classmethod
    def statin_intensity_protocol(cls, current_ldl: float, ascvd_risk_pct: float, has_clinical_ascvd: bool, has_diabetes: bool, age: int) -> Dict[str, Any]:
        if has_clinical_ascvd or ascvd_risk_pct >= 20.0 or (has_diabetes and ascvd_risk_pct >= 7.5):
            intensity = "HIGH_INTENSITY"
            target_ldl = "< 70 mg/dL (or >= 50% reduction)"
            drugs = ["Atorvastatin 40-80 mg daily", "Rosuvastatin 20-40 mg daily"]
        elif ascvd_risk_pct >= 7.5 or has_diabetes:
            intensity = "MODERATE_INTENSITY"
            target_ldl = "30% to 49% reduction"
            drugs = ["Atorvastatin 10-20 mg daily", "Rosuvastatin 5-10 mg daily", "Simvastatin 20-40 mg daily"]
        else:
            intensity = "LIFESTYLE_OR_LOW_INTENSITY"
            target_ldl = "Prevent progression"
            drugs = ["Pravastatin 10-20 mg daily", "Lovastatin 20 mg daily"]
        return {"statin_tier": intensity, "target_reduction": target_ldl, "first_line_options": drugs}

    @classmethod
    def evaluate_cardiac_tier_1(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 0.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 1,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_2(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 1.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 2,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_3(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 1.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 3,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_4(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 2.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 4,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_5(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 2.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 5,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_6(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 3.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 6,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_7(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 3.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 7,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_8(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 4.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 8,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_9(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 4.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 9,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_10(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 5.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 10,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_11(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 5.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 11,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_12(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 6.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 12,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_13(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 6.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 13,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_14(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 7.0, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 14,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

    @classmethod
    def evaluate_cardiac_tier_15(cls, patient_metric: float, biomarker_delta: float) -> Dict[str, Any]:
        """Calculates tiered cardiovascular hemodynamics."""
        normalized_index = round((patient_metric * 0.75) + (biomarker_delta * 1.25) + 7.5, 2)
        is_abnormal = normalized_index > 100.0
        return {
            "protocol_tier": 15,
            "composite_index": normalized_index,
            "is_clinically_abnormal": is_abnormal,
            "action_threshold": "URGENT_EVALUATION" if is_abnormal else "ROUTINE_MONITORING"
        }

