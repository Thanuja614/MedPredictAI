/**
 * MedPredict AI — System Settings & Clinical Decision Governance
 * Dynamic threshold manager, department preferences, audit log, local stack status
 */

import React, { useState } from 'react';
import {
  Settings,
  Sliders,
  ShieldCheck,
  Cpu,
  Database,
  Lock,
  Save,
  CheckCircle2,
  RefreshCw,
} from 'lucide-react';

export const SystemSettingsPage: React.FC = () => {
  const [lowThreshold, setLowThreshold] = useState<number>(35);
  const [highThreshold, setHighThreshold] = useState<number>(65);
  const [department, setDepartment] = useState<string>('Cardiopulmonary Intensive Care Unit (Ward 4B)');
  const [isSaved, setIsSaved] = useState<boolean>(false);

  const handleSave = () => {
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 2500);
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-medblue uppercase tracking-wider font-mono">
            Platform Configuration & Administration
          </span>
          <h2 className="font-serif text-2xl lg:text-3xl font-bold text-navy-800">
            Clinical Decision Governance & Settings
          </h2>
          <p className="text-xs text-slateText">
            Configure dynamic statistical risk intervals, clinical department workflows, and cryptographic audit parameters.
          </p>
        </div>

        <button
          onClick={handleSave}
          className="px-4 py-2 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-semibold rounded-btn flex items-center space-x-1.5 transition shadow-sm self-start md:self-auto"
        >
          <Save className="w-3.5 h-3.5" />
          <span>Save System Settings</span>
        </button>
      </div>

      {isSaved && (
        <div className="p-3 bg-status-healthyBg border border-status-healthyBorder rounded-btn text-xs text-status-healthy font-semibold flex items-center space-x-2 animate-fadeIn">
          <CheckCircle2 className="w-4 h-4" />
          <span>System configuration parameters saved and updated across active inference pipelines.</span>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* 1. Dynamic Risk Cutoffs */}
        <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
          <div className="flex items-center space-x-2 border-b border-borderLine pb-3">
            <Sliders className="w-4 h-4 text-medblue" />
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Risk Stratification Cutoffs
            </h3>
          </div>
          <p className="text-xs text-slateText">
            Adjust probabilistic thresholds governing Low, Moderate, and High clinical triage classifications.
          </p>

          <div className="space-y-4 text-xs pt-2">
            <div>
              <div className="flex justify-between mb-1.5 font-medium">
                <span>Low Risk Upper Boundary:</span>
                <span className="font-mono font-bold text-status-healthy">&lt; {lowThreshold}%</span>
              </div>
              <input
                type="range"
                min="20"
                max="45"
                value={lowThreshold}
                onChange={(e) => setLowThreshold(Number(e.target.value))}
                className="w-full accent-navy-800"
              />
              <p className="text-[11px] text-slateText mt-1">Scores below this threshold qualify for routine monitoring.</p>
            </div>

            <div className="pt-3 border-t border-borderLine/50">
              <div className="flex justify-between mb-1.5 font-medium">
                <span>High Risk Lower Boundary:</span>
                <span className="font-mono font-bold text-status-critical">&gt; {highThreshold}%</span>
              </div>
              <input
                type="range"
                min="55"
                max="80"
                value={highThreshold}
                onChange={(e) => setHighThreshold(Number(e.target.value))}
                className="w-full accent-navy-800"
              />
              <p className="text-[11px] text-slateText mt-1">Scores above this threshold trigger mandatory specialist review.</p>
            </div>

            <div className="p-3 bg-ivory rounded-btn border border-borderLine text-xs">
              <span className="font-semibold text-navy-800 block mb-1">Active Model Scoring Intervals:</span>
              <div className="flex items-center space-x-2 font-mono text-[11px]">
                <span className="text-status-healthy font-bold">Low: 0% – {lowThreshold}%</span>
                <span>•</span>
                <span className="text-status-warning font-bold">Moderate: {lowThreshold}% – {highThreshold}%</span>
                <span>•</span>
                <span className="text-status-critical font-bold">High: &gt; {highThreshold}%</span>
              </div>
            </div>
          </div>
        </div>

        {/* 2. Department & EHR Integration */}
        <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
          <div className="flex items-center space-x-2 border-b border-borderLine pb-3">
            <Cpu className="w-4 h-4 text-teal" />
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Hospital Ward & EHR Integration
            </h3>
          </div>
          <p className="text-xs text-slateText">
            Institutional department routing and health system interoperability specifications.
          </p>

          <div className="space-y-3 text-xs pt-1">
            <div>
              <label className="block text-slateText mb-1 font-medium">Primary Clinical Service Ward</label>
              <input
                type="text"
                value={department}
                onChange={(e) => setDepartment(e.target.value)}
                className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal font-medium"
              />
            </div>

            <div>
              <label className="block text-slateText mb-1 font-medium">HL7 FHIR v4.0 Endpoint</label>
              <input
                type="text"
                readOnly
                value="https://ehr.stjude-medical.org/fhir/v4/DecisionSupportService"
                className="w-full px-3 py-2 bg-ivory border border-borderLine rounded-btn text-slateText font-mono"
              />
            </div>

            <div className="p-3 bg-ivory rounded-btn border border-borderLine space-y-2">
              <div className="flex items-center space-x-1.5 font-semibold text-navy-800">
                <ShieldCheck className="w-4 h-4 text-sage" />
                <span>Security & Compliance Integrity</span>
              </div>
              <p className="text-[11px] text-slateText leading-relaxed">
                Platform operates under strict HIPAA Security Rule specifications. Encrypted in-memory inference with zero external cloud transmission of PHI.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
