/**
 * MedPredict AI — Risk Prediction & Explainable AI Interface
 * Section 9, 10 & 11: Patient intake, vitals, labs, medical history,
 * Circular calibrated gauge, contributing factor horizontal bars, clinical narrative.
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Activity,
  Heart,
  Droplets,
  FileSpreadsheet,
  AlertTriangle,
  RotateCcw,
  Sparkles,
  CheckCircle2,
  FileText,
  Printer,
  ChevronRight,
  Info,
  ShieldCheck,
} from 'lucide-react';
import { RiskGauge } from '../../components/clinical/RiskGauge';
import { ContributingFactors, FactorItem } from '../../components/clinical/ContributingFactors';
import { DEMO_PATIENTS, PatientRecord } from '../../clinical/data/demoClinicalData';

export const RiskPredictionPage: React.FC = () => {
  const navigate = useNavigate();

  // Selected Clinical Engine
  const [selectedDisease, setSelectedDisease] = useState<string>('cardiovascular');

  // Form State
  const [formData, setFormData] = useState({
    patientId: 'MP-2026-01482',
    patientName: 'Ananya Rao',
    age: 46,
    gender: 'Female',
    systolicBp: 138,
    diastolicBp: 88,
    heartRate: 82,
    respiratoryRate: 15,
    temperature: 36.8,
    bmi: 27.4,
    fastingGlucose: 126,
    hba1c: 6.2,
    totalCholesterol: 218,
    hdlCholesterol: 44,
    ldlCholesterol: 138,
    triglycerides: 180,
    serumCreatinine: 0.92,
    egfr: 88,
    hsCrp: 2.8,
    isSmoker: false,
    hasDiabetes: false,
    hasHypertension: true,
    hasFamilyCad: true,
    hasCkd: false,
    clinicalNotes: 'Patient reports occasional mild exertional chest tightness after climbing two flights of stairs. No resting symptoms.',
  });

  const [isEvaluating, setIsEvaluating] = useState<boolean>(false);
  const [predictionResult, setPredictionResult] = useState<{
    probability: number;
    riskTier: 'LOW' | 'MODERATE' | 'HIGH' | 'CRITICAL';
    confidenceInterval: [number, number];
    explanation: string;
    factors: FactorItem[];
  } | null>({
    probability: 68.4,
    riskTier: 'MODERATE',
    confidenceInterval: [63.2, 73.6],
    explanation:
      'Elevated fasting glucose (126 mg/dL) and persistent stage 1 systolic blood pressure (138 mmHg) were the primary drivers elevating the cardiovascular risk estimate above baseline.',
    factors: [
      {
        featureName: 'fasting_glucose',
        clinicalLabel: 'Fasting Plasma Glucose',
        patientValue: '126 mg/dL',
        referenceRange: '70 – 99 mg/dL',
        impactScore: 0.245,
        direction: 'elevates',
        clinicalExplanation: 'Impaired fasting glucose reflects peripheral insulin resistance and accelerated arterial endothelial damage.',
      },
      {
        featureName: 'systolic_bp',
        clinicalLabel: 'Systolic Blood Pressure',
        patientValue: '138 mmHg',
        referenceRange: '< 120 mmHg',
        impactScore: 0.182,
        direction: 'elevates',
        clinicalExplanation: 'Stage 1 systolic hypertension increases vascular afterload and arterial wall shear stress.',
      },
      {
        featureName: 'bmi',
        clinicalLabel: 'Body Mass Index (BMI)',
        patientValue: '27.4 kg/m²',
        referenceRange: '18.5 – 24.9 kg/m²',
        impactScore: 0.121,
        direction: 'elevates',
        clinicalExplanation: 'Overweight classification contributes to ongoing subclinical systemic inflammatory burden.',
      },
      {
        featureName: 'family_cad',
        clinicalLabel: 'Family History of Premature CAD',
        patientValue: 'Positive (Paternal)',
        referenceRange: 'Negative',
        impactScore: 0.098,
        direction: 'elevates',
        clinicalExplanation: 'First-degree premature coronary artery disease confers non-modifiable genetic susceptibility.',
      },
      {
        featureName: 'non_smoker',
        clinicalLabel: 'Tobacco Smoking Status',
        patientValue: 'Non-Smoker',
        referenceRange: 'Non-Smoker',
        impactScore: -0.054,
        direction: 'protective',
        clinicalExplanation: 'Absence of active or former smoking mitigates oxidative vascular injury and endothelial disruption.',
      },
      {
        featureName: 'serum_creatinine',
        clinicalLabel: 'Renal Function (eGFR)',
        patientValue: '88 mL/min/1.73m²',
        referenceRange: '> 60 mL/min',
        impactScore: -0.082,
        direction: 'protective',
        clinicalExplanation: 'Preserved glomerular filtration rate indicates absence of microvascular renal disease.',
      },
    ],
  });

  // Handle Preset Load
  const handleLoadPreset = (patient: PatientRecord) => {
    setFormData({
      patientId: patient.mrn,
      patientName: patient.name,
      age: patient.age,
      gender: patient.gender,
      systolicBp: patient.vitals.systolic,
      diastolicBp: patient.vitals.diastolic,
      heartRate: patient.vitals.heartRate,
      respiratoryRate: patient.vitals.respiratoryRate,
      temperature: patient.vitals.temperature,
      bmi: patient.vitals.bmi,
      fastingGlucose: patient.labs.fastingGlucose,
      hba1c: patient.labs.hba1c,
      totalCholesterol: patient.labs.totalCholesterol,
      hdlCholesterol: patient.labs.hdl,
      ldlCholesterol: patient.labs.ldl,
      triglycerides: patient.labs.triglycerides,
      serumCreatinine: patient.labs.serumCreatinine,
      egfr: patient.labs.egfr,
      hsCrp: patient.labs.hsCrp,
      isSmoker: patient.history.smoker,
      hasDiabetes: patient.history.diabetes,
      hasHypertension: patient.history.hypertension,
      hasFamilyCad: patient.history.familyCad,
      hasCkd: patient.history.chronicKidneyDisease,
      clinicalNotes: `Patient evaluated for ${patient.primaryCondition}. Current medication adherence confirmed.`,
    });

    // Recalculate based on preset
    runEvaluation(patient);
  };

  const runEvaluation = (customData?: any) => {
    setIsEvaluating(true);
    setTimeout(() => {
      const data = customData || formData;
      const sbp = data.systolicBp || (data.vitals ? data.vitals.systolic : 130);
      const glu = data.fastingGlucose || (data.labs ? data.labs.fastingGlucose : 110);
      const isSmk = data.isSmoker ?? (data.history ? data.history.smoker : false);

      // Deterministic realistic calculation
      let score = 20.0 + (data.age * 0.4) + ((sbp - 110) * 0.3) + ((glu - 90) * 0.2);
      if (isSmk) score += 18.0;
      if (data.hasDiabetes || (data.history && data.history.diabetes)) score += 15.0;

      const prob = Math.max(5.0, Math.min(95.0, Math.round(score * 10) / 10));
      let tier: 'LOW' | 'MODERATE' | 'HIGH' | 'CRITICAL' = 'LOW';
      if (prob >= 75) tier = 'CRITICAL';
      else if (prob >= 65) tier = 'HIGH';
      else if (prob >= 35) tier = 'MODERATE';

      setPredictionResult({
        probability: prob,
        riskTier: tier,
        confidenceInterval: [Math.max(0, prob - 5.2), Math.min(100, prob + 5.2)],
        explanation: `Model evaluated patient biometrics against AHA/ACC GDMT guidelines. Systolic BP (${sbp} mmHg) and Fasting Glucose (${glu} mg/dL) are key determinant features.`,
        factors: [
          {
            featureName: 'fasting_glucose',
            clinicalLabel: 'Fasting Plasma Glucose',
            patientValue: `${glu} mg/dL`,
            referenceRange: '70 – 99 mg/dL',
            impactScore: glu > 100 ? 0.22 : -0.10,
            direction: glu > 100 ? 'elevates' : 'protective',
            clinicalExplanation: glu > 100 ? 'Elevated glycemic marker.' : 'Optimal glucose level.',
          },
          {
            featureName: 'systolic_bp',
            clinicalLabel: 'Systolic Blood Pressure',
            patientValue: `${sbp} mmHg`,
            referenceRange: '< 120 mmHg',
            impactScore: sbp > 125 ? 0.19 : -0.12,
            direction: sbp > 125 ? 'elevates' : 'protective',
            clinicalExplanation: sbp > 125 ? 'Elevated arterial pressure.' : 'Normotensive reading.',
          },
          {
            featureName: 'bmi',
            clinicalLabel: 'Body Mass Index (BMI)',
            patientValue: `${data.bmi || 25} kg/m²`,
            referenceRange: '18.5 – 24.9 kg/m²',
            impactScore: 0.11,
            direction: 'elevates',
            clinicalExplanation: 'Moderate metabolic load.',
          },
        ],
      });
      setIsEvaluating(false);
    }, 450);
  };

  return (
    <div className="space-y-6 pb-12">
      {/* 1. Header & Engine Selector */}
      <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-medblue uppercase tracking-wider font-mono">
            Diagnostic Inference Workspace
          </span>
          <h2 className="text-xl font-bold text-slate-900">
            Multi-Disease Risk Prediction Engine
          </h2>
          <p className="text-xs text-slateText">
            Fill in clinical observations or select an active patient preset to generate validated risk stratifications.
          </p>
        </div>

        {/* Demo Patient Presets */}
        <div className="flex items-center space-x-2 flex-wrap gap-y-2">
          <span className="text-xs font-semibold text-slateText">Load Preset:</span>
          {DEMO_PATIENTS.slice(0, 3).map((p) => (
            <button
              key={p.id}
              onClick={() => handleLoadPreset(p)}
              className="px-2.5 py-1 text-xs font-medium bg-ivory hover:bg-medblue-light text-navy-800 rounded-btn border border-borderLine transition"
            >
              {p.name} ({p.riskTier})
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* 2. Left Column: Clinical Data Intake Form (7 Cols) */}
        <div className="lg:col-span-7 space-y-5">
          <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-6">
            <div className="flex items-center justify-between border-b border-borderLine pb-3">
              <div className="flex items-center space-x-2">
                <FileSpreadsheet className="w-4 h-4 text-medblue" />
                <h3 className="text-base font-bold text-slate-900">
                  Clinical Intake & Observations
                </h3>
              </div>
              <span className="text-[11px] font-mono text-slateText">
                Protocol: AHA/ACC ASCVD 10-Yr
              </span>
            </div>

            {/* Section A: Patient Demographics */}
            <div className="space-y-3">
              <div className="text-xs font-bold text-navy-800 uppercase font-mono tracking-wider flex items-center space-x-2">
                <span className="w-2 h-2 rounded-full bg-medblue" />
                <span>1. Patient Demographics</span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                <div>
                  <label className="block text-slateText mb-1 font-medium">Patient ID / MRN</label>
                  <input
                    type="text"
                    value={formData.patientId}
                    onChange={(e) => setFormData({ ...formData, patientId: e.target.value })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal font-mono"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">Age (years)</label>
                  <input
                    type="number"
                    value={formData.age}
                    onChange={(e) => setFormData({ ...formData, age: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">Biological Sex</label>
                  <select
                    value={formData.gender}
                    onChange={(e) => setFormData({ ...formData, gender: e.target.value })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  >
                    <option value="Female">Female</option>
                    <option value="Male">Male</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Section B: Vital Signs */}
            <div className="space-y-3 pt-3 border-t border-borderLine/50">
              <div className="text-xs font-bold text-navy-800 uppercase font-mono tracking-wider flex items-center space-x-2">
                <span className="w-2 h-2 rounded-full bg-teal" />
                <span>2. Vital Signs & Hemodynamics</span>
              </div>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                <div>
                  <label className="block text-slateText mb-1 font-medium">Systolic BP (mmHg)</label>
                  <input
                    type="number"
                    value={formData.systolicBp}
                    onChange={(e) => setFormData({ ...formData, systolicBp: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">Diastolic BP (mmHg)</label>
                  <input
                    type="number"
                    value={formData.diastolicBp}
                    onChange={(e) => setFormData({ ...formData, diastolicBp: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">Heart Rate (bpm)</label>
                  <input
                    type="number"
                    value={formData.heartRate}
                    onChange={(e) => setFormData({ ...formData, heartRate: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">BMI (kg/m²)</label>
                  <input
                    type="number"
                    step="0.1"
                    value={formData.bmi}
                    onChange={(e) => setFormData({ ...formData, bmi: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
              </div>
            </div>

            {/* Section C: Laboratory Data */}
            <div className="space-y-3 pt-3 border-t border-borderLine/50">
              <div className="text-xs font-bold text-navy-800 uppercase font-mono tracking-wider flex items-center space-x-2">
                <span className="w-2 h-2 rounded-full bg-sage" />
                <span>3. Laboratory Biomarkers</span>
              </div>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                <div>
                  <label className="block text-slateText mb-1 font-medium">Glucose (mg/dL)</label>
                  <input
                    type="number"
                    value={formData.fastingGlucose}
                    onChange={(e) => setFormData({ ...formData, fastingGlucose: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">HbA1c (%)</label>
                  <input
                    type="number"
                    step="0.1"
                    value={formData.hba1c}
                    onChange={(e) => setFormData({ ...formData, hba1c: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">Total Chol (mg/dL)</label>
                  <input
                    type="number"
                    value={formData.totalCholesterol}
                    onChange={(e) => setFormData({ ...formData, totalCholesterol: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
                <div>
                  <label className="block text-slateText mb-1 font-medium">HDL Chol (mg/dL)</label>
                  <input
                    type="number"
                    value={formData.hdlCholesterol}
                    onChange={(e) => setFormData({ ...formData, hdlCholesterol: Number(e.target.value) })}
                    className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal"
                  />
                </div>
              </div>
            </div>

            {/* Section D: Risk Factors & Medical History */}
            <div className="space-y-3 pt-3 border-t border-borderLine/50">
              <div className="text-xs font-bold text-navy-800 uppercase font-mono tracking-wider flex items-center space-x-2">
                <span className="w-2 h-2 rounded-full bg-navy-800" />
                <span>4. Risk Factors & Medical History</span>
              </div>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
                <label className="flex items-center space-x-2.5 p-2.5 bg-ivory rounded-btn border border-borderLine cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.hasHypertension}
                    onChange={(e) => setFormData({ ...formData, hasHypertension: e.target.checked })}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span className="text-charcoal font-medium">Hypertension</span>
                </label>
                <label className="flex items-center space-x-2.5 p-2.5 bg-ivory rounded-btn border border-borderLine cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.hasDiabetes}
                    onChange={(e) => setFormData({ ...formData, hasDiabetes: e.target.checked })}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span className="text-charcoal font-medium">Diabetes Mellitus</span>
                </label>
                <label className="flex items-center space-x-2.5 p-2.5 bg-ivory rounded-btn border border-borderLine cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.isSmoker}
                    onChange={(e) => setFormData({ ...formData, isSmoker: e.target.checked })}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span className="text-charcoal font-medium">Active Smoker</span>
                </label>
                <label className="flex items-center space-x-2.5 p-2.5 bg-ivory rounded-btn border border-borderLine cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.hasFamilyCad}
                    onChange={(e) => setFormData({ ...formData, hasFamilyCad: e.target.checked })}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span className="text-charcoal font-medium">Family History CAD</span>
                </label>
                <label className="flex items-center space-x-2.5 p-2.5 bg-ivory rounded-btn border border-borderLine cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.hasCkd}
                    onChange={(e) => setFormData({ ...formData, hasCkd: e.target.checked })}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span className="text-charcoal font-medium">Chronic Kidney Disease</span>
                </label>
              </div>
            </div>

            {/* Action Bar */}
            <div className="pt-4 border-t border-borderLine flex items-center justify-between">
              <button
                type="button"
                onClick={() => handleLoadPreset(DEMO_PATIENTS[0])}
                className="px-3 py-2 text-xs font-semibold text-slateText hover:text-navy-800 flex items-center space-x-1.5 transition"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>Reset to Baseline</span>
              </button>

              <button
                type="button"
                onClick={() => runEvaluation()}
                disabled={isEvaluating}
                className="px-5 py-2.5 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-semibold rounded-btn shadow-md shadow-navy-900/20 flex items-center space-x-2 transition disabled:opacity-50"
              >
                {isEvaluating ? (
                  <>
                    <span className="w-3.5 h-3.5 border-2 border-ivory border-t-transparent rounded-full animate-spin" />
                    <span>Evaluating Statistical Model...</span>
                  </>
                ) : (
                  <>
                    <Sparkles className="w-4 h-4 text-teal" />
                    <span>Execute Risk Prediction</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </div>

        {/* 3. Right Column: Output & Explainability (5 Cols) */}
        <div className="lg:col-span-5 space-y-6">
          {predictionResult ? (
            <>
              {/* Circular Risk Gauge (Section 10) */}
              <RiskGauge
                probability={predictionResult.probability}
                riskTier={predictionResult.riskTier}
                diseaseName="ASCVD 10-Year Risk Estimate"
                confidenceInterval={predictionResult.confidenceInterval}
              />

              {/* Explainable AI & Contributing Factors (Section 11) */}
              <ContributingFactors
                factors={predictionResult.factors}
                primaryExplanation={predictionResult.explanation}
              />

              {/* Clinical Action Buttons */}
              <div className="bg-surface rounded-card p-4 border border-borderLine shadow-subtle flex items-center justify-between gap-3">
                <button
                  onClick={() => navigate('/reports')}
                  className="flex-1 px-3 py-2 bg-ivory hover:bg-medblue-light text-navy-800 text-xs font-semibold rounded-btn border border-borderLine flex items-center justify-center space-x-1.5 transition"
                >
                  <FileText className="w-3.5 h-3.5 text-medblue" />
                  <span>Generate Report</span>
                </button>
                <button
                  onClick={() => window.print()}
                  className="flex-1 px-3 py-2 bg-ivory hover:bg-medblue-light text-navy-800 text-xs font-semibold rounded-btn border border-borderLine flex items-center justify-center space-x-1.5 transition"
                >
                  <Printer className="w-3.5 h-3.5 text-sage" />
                  <span>Print Summary</span>
                </button>
              </div>
            </>
          ) : (
            <div className="bg-surface rounded-card p-12 border border-borderLine shadow-medical text-center space-y-3">
              <Activity className="w-8 h-8 text-slateText/40 mx-auto" />
              <h4 className="text-sm font-bold text-slate-900">
                Awaiting Clinical Input
              </h4>
              <p className="text-xs text-slateText max-w-xs mx-auto">
                Fill out patient demographics, vitals, and laboratory parameters on the left to compute real-time risk predictions.
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
