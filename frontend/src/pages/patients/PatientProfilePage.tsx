/**
 * MedPredict AI — Patient Profile & Electronic Health Record (EHR) Page
 * Section 12 & 13: Realistic medical record layout, header, vitals, labs, timeline, notes
 */

import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  User,
  Activity,
  FileText,
  Calendar,
  Clock,
  Heart,
  Droplet,
  FlaskConical,
  Pill,
  ShieldCheck,
  AlertTriangle,
  ChevronLeft,
  Printer,
  Download,
  CheckCircle2,
} from 'lucide-react';
import { StatusBadge } from '../../components/clinical/StatusBadge';
import { MedicalTimeline } from '../../components/clinical/MedicalTimeline';
import { DEMO_PATIENTS, PatientRecord } from '../../clinical/data/demoClinicalData';

export const PatientProfilePage: React.FC = () => {
  const { id } = useParams<{ id?: string }>();
  const [selectedPatientId, setSelectedPatientId] = useState<string>(id || 'pt-1');
  const [activeTab, setActiveTab] = useState<'overview' | 'vitals' | 'labs' | 'timeline' | 'notes'>('overview');

  const patient = DEMO_PATIENTS.find((p) => p.id === selectedPatientId) || DEMO_PATIENTS[0];

  return (
    <div className="space-y-6 pb-12">
      {/* Top Patient Selector Bar if browsing */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <span className="text-xs font-semibold text-slateText">Active Patient Record:</span>
          <select
            value={patient.id}
            onChange={(e) => setSelectedPatientId(e.target.value)}
            className="text-xs font-semibold bg-surface border border-borderLine rounded-btn px-3 py-1.5 text-navy-800 focus:outline-none focus:ring-1 focus:ring-medblue"
          >
            {DEMO_PATIENTS.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name} ({p.mrn}) — {p.primaryCondition}
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => window.print()}
            className="px-3 py-1.5 text-xs font-medium bg-surface hover:bg-ivory border border-borderLine rounded-btn text-navy-800 flex items-center space-x-1.5 transition"
          >
            <Printer className="w-3.5 h-3.5 text-slateText" />
            <span>Print Chart</span>
          </button>
          <Link
            to="/prediction"
            className="px-3 py-1.5 text-xs font-semibold bg-navy-800 hover:bg-navy-700 text-ivory rounded-btn flex items-center space-x-1.5 transition"
          >
            <Activity className="w-3.5 h-3.5 text-teal" />
            <span>Assess Patient</span>
          </Link>
        </div>
      </div>

      {/* 1. Realistic Hospital Patient Header Banner (Section 12) */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical relative overflow-hidden">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div className="flex items-start space-x-4">
            <div className="w-14 h-14 rounded-full bg-medblue-light border-2 border-medblue/30 flex items-center justify-center text-medblue font-serif font-bold text-xl shrink-0">
              {patient.name.split(' ').map((n) => n[0]).join('')}
            </div>
            <div>
              <div className="flex items-center space-x-3">
                <h2 className="font-serif text-2xl font-bold text-navy-800">
                  {patient.name}
                </h2>
                <StatusBadge status={patient.riskTier} label={`${patient.riskTier} RISK`} />
              </div>
              <div className="mt-1 flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-slateText">
                <span>MRN: <strong className="font-mono text-charcoal">{patient.mrn}</strong></span>
                <span>DOB: <strong className="text-charcoal">{patient.dob}</strong> ({patient.age} yrs)</span>
                <span>Sex: <strong className="text-charcoal">{patient.gender}</strong></span>
                <span>Blood: <strong className="text-charcoal">{patient.bloodType}</strong></span>
                <span>Physician: <strong className="text-charcoal">{patient.primaryPhysician}</strong></span>
              </div>
            </div>
          </div>

          <div className="flex items-center space-x-4 text-xs border-t md:border-t-0 md:border-l border-borderLine pt-3 md:pt-0 md:pl-6">
            <div>
              <span className="text-slateText block">Last Clinical Encounter</span>
              <span className="font-semibold text-navy-800">{patient.lastVisit}</span>
            </div>
            <div>
              <span className="text-slateText block">30-Day Risk Velocity</span>
              <span className={`font-semibold ${patient.velocityTrend === 'ESCALATING' ? 'text-status-critical' : 'text-status-healthy'}`}>
                {patient.velocityTrend}
              </span>
            </div>
          </div>
        </div>

        {/* Clinical Tabs */}
        <div className="flex items-center space-x-2 border-t border-borderLine mt-6 pt-3 overflow-x-auto text-xs font-semibold">
          {[
            { key: 'overview', label: 'Medical Overview' },
            { key: 'vitals', label: 'Vital Signs & Trends' },
            { key: 'labs', label: 'Laboratory Results' },
            { key: 'timeline', label: 'Medical Timeline' },
            { key: 'notes', label: 'Physician Notes' },
          ].map((tab) => (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key as any)}
              className={`px-3.5 py-1.5 rounded-btn transition ${
                activeTab === tab.key
                  ? 'bg-navy-800 text-ivory shadow-xs'
                  : 'text-slateText hover:text-navy-800 hover:bg-ivory'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* 2. Tab Content Rendering */}
      {activeTab === 'overview' && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Active Diagnoses & Conditions */}
          <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical space-y-3">
            <h3 className="font-serif text-base font-bold text-navy-800 border-b border-borderLine pb-2">
              Primary & Active Diagnoses
            </h3>
            <div className="space-y-2 text-xs">
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine flex items-start justify-between">
                <div>
                  <span className="font-semibold text-charcoal">{patient.primaryCondition}</span>
                  <p className="text-[11px] text-slateText mt-0.5">ICD-10: I10, E11.9 (Active GDMT Protocol)</p>
                </div>
                <span className="text-[10px] font-bold text-status-warning px-1.5 py-0.5 bg-status-warningBg rounded">
                  Confirmed
                </span>
              </div>
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine flex items-start justify-between">
                <div>
                  <span className="font-semibold text-charcoal">Atherosclerotic Cardiovascular Risk</span>
                  <p className="text-[11px] text-slateText mt-0.5">Calculated 10-Yr Risk Score: {patient.calibratedProbability}%</p>
                </div>
                <span className="text-[10px] font-bold text-medblue px-1.5 py-0.5 bg-medblue-light rounded">
                  Monitored
                </span>
              </div>
            </div>

            <h4 className="font-serif text-sm font-bold text-navy-800 pt-3 border-t border-borderLine/60">
              Documented Allergies
            </h4>
            <div className="flex flex-wrap gap-1.5">
              {patient.allergies.map((all, i) => (
                <span key={i} className="text-xs px-2.5 py-1 bg-status-criticalBg text-status-critical rounded-btn font-medium border border-status-criticalBorder">
                  {all}
                </span>
              ))}
            </div>
          </div>

          {/* Active Pharmacotherapy */}
          <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical space-y-3">
            <h3 className="font-serif text-base font-bold text-navy-800 border-b border-borderLine pb-2">
              Active Guideline Pharmacotherapy
            </h3>
            <div className="space-y-2 text-xs">
              {patient.activeMedications.map((med, idx) => (
                <div key={idx} className="p-2.5 bg-ivory rounded-btn border border-borderLine flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <Pill className="w-3.5 h-3.5 text-sage" />
                    <span className="font-medium text-charcoal">{med}</span>
                  </div>
                  <span className="text-[10px] text-status-healthy font-semibold">Active</span>
                </div>
              ))}
            </div>
          </div>

          {/* Quick Biometric Summary */}
          <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical space-y-3">
            <h3 className="font-serif text-base font-bold text-navy-800 border-b border-borderLine pb-2">
              Current Vital Parameters
            </h3>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine">
                <span className="text-slateText text-[11px]">Blood Pressure</span>
                <p className="font-bold text-navy-800 text-sm mt-0.5">{patient.vitals.bloodPressure} mmHg</p>
              </div>
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine">
                <span className="text-slateText text-[11px]">Heart Rate</span>
                <p className="font-bold text-navy-800 text-sm mt-0.5">{patient.vitals.heartRate} bpm</p>
              </div>
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine">
                <span className="text-slateText text-[11px]">BMI</span>
                <p className="font-bold text-navy-800 text-sm mt-0.5">{patient.vitals.bmi} kg/m²</p>
              </div>
              <div className="p-2.5 bg-ivory rounded-btn border border-borderLine">
                <span className="text-slateText text-[11px]">SpO2 Saturation</span>
                <p className="font-bold text-navy-800 text-sm mt-0.5">{patient.vitals.spo2}%</p>
              </div>
            </div>
          </div>
        </div>
      )}

      {activeTab === 'vitals' && (
        <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
          <h3 className="font-serif text-lg font-bold text-navy-800">
            Vital Signs & Hemodynamic Profile
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
            <div className="p-4 bg-ivory rounded-btn border border-borderLine">
              <span className="text-slateText">Systolic Pressure</span>
              <p className="text-xl font-bold text-navy-800 mt-1">{patient.vitals.systolic} <span className="text-xs font-normal">mmHg</span></p>
              <span className="text-[10px] text-status-warning mt-1 block">Stage 1 HTN</span>
            </div>
            <div className="p-4 bg-ivory rounded-btn border border-borderLine">
              <span className="text-slateText">Diastolic Pressure</span>
              <p className="text-xl font-bold text-navy-800 mt-1">{patient.vitals.diastolic} <span className="text-xs font-normal">mmHg</span></p>
              <span className="text-[10px] text-status-healthy mt-1 block">Normative Range</span>
            </div>
            <div className="p-4 bg-ivory rounded-btn border border-borderLine">
              <span className="text-slateText">Resting Heart Rate</span>
              <p className="text-xl font-bold text-navy-800 mt-1">{patient.vitals.heartRate} <span className="text-xs font-normal">bpm</span></p>
              <span className="text-[10px] text-status-healthy mt-1 block">Sinus Rhythm</span>
            </div>
            <div className="p-4 bg-ivory rounded-btn border border-borderLine">
              <span className="text-slateText">Body Mass Index</span>
              <p className="text-xl font-bold text-navy-800 mt-1">{patient.vitals.bmi} <span className="text-xs font-normal">kg/m²</span></p>
              <span className="text-[10px] text-status-warning mt-1 block">Overweight</span>
            </div>
          </div>
        </div>
      )}

      {activeTab === 'labs' && (
        <div className="bg-surface rounded-card border border-borderLine shadow-medical overflow-hidden">
          <div className="p-5 border-b border-borderLine">
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Diagnostic Laboratory Values
            </h3>
            <p className="text-xs text-slateText">Latest panel collected and validated by Central Pathology</p>
          </div>
          <table className="w-full text-left text-xs text-charcoal">
            <thead className="bg-ivory text-[11px] font-bold text-slateText uppercase font-mono tracking-wider border-b border-borderLine">
              <tr>
                <th className="py-3 px-4">Biomarker / Analyte</th>
                <th className="py-3 px-4">Patient Result</th>
                <th className="py-3 px-4">Reference Interval</th>
                <th className="py-3 px-4">Clinical Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderLine/50">
              <tr>
                <td className="py-3 px-4 font-medium">Fasting Plasma Glucose</td>
                <td className="py-3 px-4 font-mono font-bold text-status-warning">{patient.labs.fastingGlucose} mg/dL</td>
                <td className="py-3 px-4 text-slateText">70 – 99 mg/dL</td>
                <td className="py-3 px-4"><span className="text-[11px] text-status-warning font-semibold">Elevated (Prediabetic)</span></td>
              </tr>
              <tr>
                <td className="py-3 px-4 font-medium">Hemoglobin A1c (HbA1c)</td>
                <td className="py-3 px-4 font-mono font-bold text-status-warning">{patient.labs.hba1c}%</td>
                <td className="py-3 px-4 text-slateText">&lt; 5.7%</td>
                <td className="py-3 px-4"><span className="text-[11px] text-status-warning font-semibold">Suboptimal</span></td>
              </tr>
              <tr>
                <td className="py-3 px-4 font-medium">Serum Creatinine</td>
                <td className="py-3 px-4 font-mono font-bold text-navy-800">{patient.labs.serumCreatinine} mg/dL</td>
                <td className="py-3 px-4 text-slateText">0.60 – 1.10 mg/dL</td>
                <td className="py-3 px-4"><span className="text-[11px] text-status-healthy font-semibold">Normal</span></td>
              </tr>
              <tr>
                <td className="py-3 px-4 font-medium">Estimated GFR (CKD-EPI 2021)</td>
                <td className="py-3 px-4 font-mono font-bold text-navy-800">{patient.labs.egfr} mL/min/1.73m²</td>
                <td className="py-3 px-4 text-slateText">&gt; 60 mL/min</td>
                <td className="py-3 px-4"><span className="text-[11px] text-status-healthy font-semibold">Preserved Renal Function</span></td>
              </tr>
              <tr>
                <td className="py-3 px-4 font-medium">High-Sensitivity CRP</td>
                <td className="py-3 px-4 font-mono font-bold text-status-warning">{patient.labs.hsCrp} mg/L</td>
                <td className="py-3 px-4 text-slateText">&lt; 1.0 mg/L</td>
                <td className="py-3 px-4"><span className="text-[11px] text-status-warning font-semibold">Mild Vascular Inflammation</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      )}

      {activeTab === 'timeline' && (
        <MedicalTimeline events={patient.timeline} />
      )}

      {activeTab === 'notes' && (
        <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
          <h3 className="font-serif text-lg font-bold text-navy-800">
            Attending Physician Progress Notes
          </h3>
          <div className="p-4 bg-ivory rounded-btn border border-borderLine text-xs text-charcoal leading-relaxed space-y-2">
            <div className="flex items-center justify-between font-semibold text-navy-800 border-b border-borderLine/50 pb-2">
              <span>Dr. Sarah Mitchell, MD — Division of Cardiology</span>
              <span className="font-mono text-slateText">Sep 08, 2026</span>
            </div>
            <p>
              Patient seen for routine quarterly follow-up of stage 1 essential hypertension and impaired fasting glycemia. Patient reports good adherence to Telmisartan 40mg with absence of adverse pedal edema.
            </p>
            <p>
              MedPredict AI ASCVD 10-year risk assessment calculated at 68.4% (Moderate Tier) driven primarily by fasting glucose of 126 mg/dL and first-degree family history of premature CAD.
            </p>
            <p className="font-semibold text-navy-800 pt-2">Plan & Recommendations:</p>
            <ul className="list-disc pl-5 space-y-1 text-slate-700">
              <li>Reinforce lifestyle modification: Mediterranean dietary pattern, 150 minutes/week moderate aerobic activity.</li>
              <li>Continue Telmisartan 40mg daily; continue Atorvastatin 20mg daily for primary atheroprotection.</li>
              <li>Repeat HbA1c, fasting lipid panel, and urine albumin-to-creatinine ratio in 90 days.</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
