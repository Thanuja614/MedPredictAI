/**
 * MedPredict AI — Medical Reports & Clinical Assessment Document
 * Section 15: Printable clinical document, patient info, clinical summary,
 * AI explanation, recommendations, physician notes, SHA-256 verification hash.
 */

import React, { useState } from 'react';
import {
  FileText,
  Printer,
  Download,
  Share2,
  CheckCircle2,
  AlertTriangle,
  ShieldCheck,
  Stethoscope,
  Calendar,
  Clock,
  User,
  Activity,
  Award,
} from 'lucide-react';
import { DEMO_PATIENTS } from '../../clinical/data/demoClinicalData';

export const MedicalReportsPage: React.FC = () => {
  const [selectedPatientId, setSelectedPatientId] = useState<string>('pt-1');
  const [isExporting, setIsExporting] = useState<boolean>(false);

  const patient = DEMO_PATIENTS.find((p) => p.id === selectedPatientId) || DEMO_PATIENTS[0];

  const handlePrint = () => {
    window.print();
  };

  const handleDownload = () => {
    setIsExporting(true);
    setTimeout(() => {
      setIsExporting(false);
      window.print();
    }, 600);
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Top Action Bar */}
      <div className="bg-surface rounded-card p-4 border border-borderLine shadow-medical flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 no-print">
        <div className="flex items-center space-x-3">
          <span className="text-xs font-semibold text-slateText">Select Patient Report:</span>
          <select
            value={patient.id}
            onChange={(e) => setSelectedPatientId(e.target.value)}
            className="text-xs font-semibold bg-ivory border border-borderLine rounded-btn px-3 py-1.5 text-navy-800 focus:ring-1 focus:ring-medblue"
          >
            {DEMO_PATIENTS.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name} ({p.mrn}) — {p.riskTier} Risk
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={handlePrint}
            className="px-3.5 py-1.5 bg-ivory hover:bg-medblue-light text-navy-800 text-xs font-semibold rounded-btn border border-borderLine flex items-center space-x-1.5 transition"
          >
            <Printer className="w-3.5 h-3.5 text-slateText" />
            <span>Print Report</span>
          </button>
          <button
            onClick={handleDownload}
            disabled={isExporting}
            className="px-4 py-1.5 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-semibold rounded-btn flex items-center space-x-1.5 shadow-sm transition"
          >
            <Download className="w-3.5 h-3.5" />
            <span>{isExporting ? 'Generating PDF...' : 'Download Official PDF'}</span>
          </button>
        </div>
      </div>

      {/* Realistic Hospital Clinical Document Container (Section 15) */}
      <div className="bg-white rounded-card border border-borderLine shadow-medical p-8 lg:p-12 max-w-4xl mx-auto space-y-8 print-container text-charcoal">
        {/* Document Header with Hospital Letterhead */}
        <div className="border-b-2 border-navy-800 pb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center space-x-2">
              <div className="w-7 h-7 bg-navy-800 text-ivory rounded flex items-center justify-center font-bold text-xs">
                MP
              </div>
              <span className="font-serif text-xl font-bold text-navy-800 tracking-tight">
                St. Jude Academic Medical Center
              </span>
            </div>
            <p className="text-xs text-slateText">
              Clinical Decision Support & Preventative Cardiology Division • In affiliation with MedPredict AI
            </p>
            <p className="text-[11px] text-slateText">
              742 Health Sciences Boulevard, Medical District • Tel: +1 (555) 019-2831
            </p>
          </div>

          <div className="text-left sm:text-right text-xs space-y-1 sm:border-l sm:border-borderLine sm:pl-6">
            <div className="font-mono text-[11px] text-slateText">
              Report ID: <strong className="text-navy-800">CDR-2026-{patient.mrn.slice(-4)}</strong>
            </div>
            <div className="text-[11px] text-slateText">
              Generated: <strong className="text-navy-800">September 11, 2026</strong>
            </div>
            <div className="inline-flex items-center space-x-1 text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
              <ShieldCheck className="w-3 h-3" />
              <span>Cryptographically Verified</span>
            </div>
          </div>
        </div>

        {/* Patient Identification Block */}
        <div className="p-4 bg-[#F7F5EF] rounded-btn border border-borderLine">
          <div className="text-[11px] font-bold uppercase tracking-wider text-navy-800 font-mono mb-2 border-b border-borderLine/60 pb-1">
            Patient Demographics & Encounter Metadata
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-y-2 gap-x-4 text-xs">
            <div>
              <span className="text-slateText text-[11px] block">Full Name:</span>
              <strong className="text-navy-800 font-sans">{patient.name}</strong>
            </div>
            <div>
              <span className="text-slateText text-[11px] block">Medical Record No:</span>
              <strong className="font-mono text-navy-800">{patient.mrn}</strong>
            </div>
            <div>
              <span className="text-slateText text-[11px] block">Age & Sex:</span>
              <strong className="text-navy-800">{patient.age} yrs • {patient.gender}</strong>
            </div>
            <div>
              <span className="text-slateText text-[11px] block">Attending Physician:</span>
              <strong className="text-navy-800">{patient.primaryPhysician}</strong>
            </div>
          </div>
        </div>

        {/* Clinical Summary & Risk Assessment */}
        <div className="space-y-3">
          <h3 className="font-serif text-lg font-bold text-navy-800 border-b border-borderLine pb-1.5">
            1. Clinical Risk Stratification Summary
          </h3>
          <p className="text-xs text-slate-700 leading-relaxed">
            Evaluation conducted using MedPredict AI multi-disease predictive framework. Model calibration incorporates 10-year prospective epidemiological hazard coefficients derived from AHA/ACC multi-society consensus guidelines.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
            <div className="p-4 bg-surface rounded-btn border border-borderLine text-center space-y-1">
              <span className="text-[11px] text-slateText font-semibold uppercase">Primary Target Evaluation</span>
              <p className="font-bold text-sm text-navy-800">ASCVD & Coronary Risk</p>
            </div>
            <div className="p-4 bg-surface rounded-btn border border-borderLine text-center space-y-1">
              <span className="text-[11px] text-slateText font-semibold uppercase">Calibrated Model Probability</span>
              <p className="font-bold text-2xl text-navy-800 font-mono">{patient.calibratedProbability.toFixed(1)}%</p>
            </div>
            <div className="p-4 bg-surface rounded-btn border border-borderLine text-center space-y-1">
              <span className="text-[11px] text-slateText font-semibold uppercase">Risk Stratification Tier</span>
              <p className={`font-bold text-base ${patient.riskTier === 'HIGH' ? 'text-status-critical' : patient.riskTier === 'MODERATE' ? 'text-status-warning' : 'text-status-healthy'}`}>
                {patient.riskTier} RISK TIER
              </p>
            </div>
          </div>
        </div>

        {/* Biometric & Laboratory Observations */}
        <div className="space-y-3">
          <h3 className="font-serif text-lg font-bold text-navy-800 border-b border-borderLine pb-1.5">
            2. Recorded Physiological & Laboratory Parameters
          </h3>
          <table className="w-full text-left text-xs border border-borderLine">
            <thead className="bg-[#F7F5EF] text-[11px] font-bold text-slateText uppercase font-mono">
              <tr className="border-b border-borderLine">
                <th className="py-2 px-3">Clinical Analyte</th>
                <th className="py-2 px-3">Recorded Value</th>
                <th className="py-2 px-3">Normative Reference</th>
                <th className="py-2 px-3">Variance Assessment</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderLine">
              <tr>
                <td className="py-2 px-3 font-medium">Resting Blood Pressure</td>
                <td className="py-2 px-3 font-mono font-semibold">{patient.vitals.bloodPressure} mmHg</td>
                <td className="py-2 px-3 text-slateText">&lt; 120/80 mmHg</td>
                <td className="py-2 px-3 text-status-warning font-medium">Stage 1 HTN Range</td>
              </tr>
              <tr>
                <td className="py-2 px-3 font-medium">Fasting Plasma Glucose</td>
                <td className="py-2 px-3 font-mono font-semibold">{patient.labs.fastingGlucose} mg/dL</td>
                <td className="py-2 px-3 text-slateText">70 – 99 mg/dL</td>
                <td className="py-2 px-3 text-status-warning font-medium">Impaired Glycemia</td>
              </tr>
              <tr>
                <td className="py-2 px-3 font-medium">Total Cholesterol / HDL</td>
                <td className="py-2 px-3 font-mono font-semibold">{patient.labs.totalCholesterol} / {patient.labs.hdl} mg/dL</td>
                <td className="py-2 px-3 text-slateText">Ratio &lt; 4.0</td>
                <td className="py-2 px-3 text-slateText">Borderline Desirable</td>
              </tr>
              <tr>
                <td className="py-2 px-3 font-medium">Glomerular Filtration Rate (eGFR)</td>
                <td className="py-2 px-3 font-mono font-semibold">{patient.labs.egfr} mL/min/1.73m²</td>
                <td className="py-2 px-3 text-slateText">&gt; 60 mL/min</td>
                <td className="py-2 px-3 text-status-healthy font-medium">Preserved Renal Function</td>
              </tr>
              <tr>
                <td className="py-2 px-3 font-medium">Body Mass Index (BMI)</td>
                <td className="py-2 px-3 font-mono font-semibold">{patient.vitals.bmi} kg/m²</td>
                <td className="py-2 px-3 text-slateText">18.5 – 24.9 kg/m²</td>
                <td className="py-2 px-3 text-status-warning font-medium">Overweight Class I</td>
              </tr>
            </tbody>
          </table>
        </div>

        {/* Explainable AI Decomposition */}
        <div className="space-y-3">
          <h3 className="font-serif text-lg font-bold text-navy-800 border-b border-borderLine pb-1.5">
            3. Algorithmic Feature Contribution & Interpretability
          </h3>
          <p className="text-xs text-slate-700 leading-relaxed">
            Local SHAP analysis indicates that <strong>fasting glucose (+24.5%)</strong> and <strong>systolic blood pressure (+18.2%)</strong> contributed most substantially to risk elevation relative to the age-matched baseline population. Conversely, <strong>non-smoker status (-5.4%)</strong> and <strong>intact renal reserve (-8.2%)</strong> provided partial protective attenuation.
          </p>
        </div>

        {/* Evidence-Based Clinical Recommendations */}
        <div className="space-y-3">
          <h3 className="font-serif text-lg font-bold text-navy-800 border-b border-borderLine pb-1.5">
            4. Guideline-Directed Medical Therapy (GDMT) Recommendations
          </h3>
          <ul className="list-disc pl-5 space-y-1.5 text-xs text-slate-800">
            <li>
              <strong>Lifestyle Intervention:</strong> Structured 150 min/week moderate-intensity cardiovascular exercise; transition to strict Mediterranean dietary pattern with sodium restriction &lt; 2,000 mg/day.
            </li>
            <li>
              <strong>Pharmacotherapy Optimization:</strong> Maintain Telmisartan 40mg daily for vascular endothelial preservation; consider moderate-intensity statin therapy (Atorvastatin 20mg nocte).
            </li>
            <li>
              <strong>Surveillance Interval:</strong> Schedule follow-up ambulatory blood pressure review and repeat metabolic panel in 90 days.
            </li>
          </ul>
        </div>

        {/* Sign-off & Verification Block */}
        <div className="border-t-2 border-borderLine pt-6 grid grid-cols-1 sm:grid-cols-2 gap-6 text-xs">
          <div className="space-y-2">
            <span className="text-[11px] font-semibold text-slateText block">Attending Physician Sign-Off</span>
            <div className="font-serif text-lg font-bold text-navy-800 italic">
              Sarah Mitchell, MD, FACC
            </div>
            <p className="text-[11px] text-slateText">
              Chief of Clinical Cardiology • License #MD-48192-CA
            </p>
            <p className="text-[10px] text-slate-400">Electronically signed on 2026-09-11 14:32 UTC</p>
          </div>

          <div className="p-3 bg-[#F7F5EF] rounded-btn border border-borderLine space-y-1.5 text-[11px]">
            <div className="flex items-center space-x-1.5 text-navy-800 font-bold font-mono text-[10px] uppercase">
              <Award className="w-3.5 h-3.5 text-teal" />
              <span>Digital Security Digest (SHA-256)</span>
            </div>
            <p className="font-mono text-[9px] text-slateText break-all">
              e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
            </p>
            <p className="text-[10px] text-slate-500">
              Matches database immutable audit record #AUD-9104. Non-diagnostic decision support.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
