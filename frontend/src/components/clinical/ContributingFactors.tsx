/**
 * MedPredict AI — Contributing Factors & Explainable AI (XAI) Component
 * Visualizes SHAP feature contributions with clinical explanations and horizontal impact bars
 */

import React from 'react';
import { HelpCircle, ArrowUpRight, ArrowDownRight, Info } from 'lucide-react';

export interface FactorItem {
  featureName: string;
  clinicalLabel: string;
  patientValue: string;
  referenceRange: string;
  impactScore: number; // e.g. +0.28 (pushes risk up) or -0.15 (protective/down)
  direction: 'elevates' | 'protective';
  clinicalExplanation: string;
}

interface ContributingFactorsProps {
  factors: FactorItem[];
  primaryExplanation?: string;
  modelAlgorithm?: string;
}

export const ContributingFactors: React.FC<ContributingFactorsProps> = ({
  factors,
  primaryExplanation = 'Elevated fasting glucose (126 mg/dL) and persistent stage 1 systolic blood pressure (138 mmHg) were the primary drivers elevating the cardiovascular risk estimate above baseline.',
  modelAlgorithm = 'RandomForestClassifier (Calibrated TreeSHAP)',
}) => {
  // Sort factors by absolute impact
  const sorted = [...factors].sort((a, b) => Math.abs(b.impactScore) - Math.abs(a.impactScore));

  return (
    <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-5">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-borderLine pb-3">
        <div>
          <h3 className="font-serif text-lg font-bold text-navy-800">
            Explainable AI — Feature Attribution
          </h3>
          <p className="text-xs text-slateText">
            Decomposition of biometric contributors using local SHAP attribution
          </p>
        </div>
        <span className="text-[10px] font-mono font-medium px-2 py-1 rounded bg-ivory text-medblue border border-borderLine">
          {modelAlgorithm}
        </span>
      </div>

      {/* Narrative Clinical Summary ("Why This Prediction?") */}
      <div className="p-4 bg-medblue-light/60 rounded-btn border border-medblue/20 text-xs text-navy-800 leading-relaxed flex items-start space-x-3">
        <Info className="w-4 h-4 text-medblue shrink-0 mt-0.5" />
        <div>
          <span className="font-bold text-medblue block mb-1">Clinical Interpretability Summary:</span>
          <p className="text-slate-700">{primaryExplanation}</p>
        </div>
      </div>

      {/* Contributing Factors List with Horizontal Bars */}
      <div className="space-y-3.5 pt-1">
        <div className="text-[11px] font-bold text-slateText uppercase tracking-wider font-mono">
          Biomarker Contribution Breakdown
        </div>

        {sorted.map((item, idx) => {
          const isElevating = item.direction === 'elevates';
          const impactPct = Math.min(100, Math.round(Math.abs(item.impactScore) * 100));

          return (
            <div key={idx} className="p-3 bg-ivory rounded-btn border border-borderLine/70 space-y-2">
              <div className="flex items-center justify-between text-xs">
                <div className="flex items-center space-x-2">
                  <span className="font-semibold text-charcoal">{item.clinicalLabel}</span>
                  <span className="text-[11px] text-slateText font-mono">({item.patientValue})</span>
                </div>
                <div className="flex items-center space-x-1.5">
                  <span className="text-[11px] text-slateText">Ref: {item.referenceRange}</span>
                  <span
                    className={`inline-flex items-center font-bold px-2 py-0.5 rounded text-[11px] ${
                      isElevating
                        ? 'bg-status-criticalBg text-status-critical'
                        : 'bg-status-healthyBg text-status-healthy'
                    }`}
                  >
                    {isElevating ? (
                      <ArrowUpRight className="w-3 h-3 mr-0.5" />
                    ) : (
                      <ArrowDownRight className="w-3 h-3 mr-0.5" />
                    )}
                    {isElevating ? `+${impactPct}% Risk` : `-${impactPct}% Risk`}
                  </span>
                </div>
              </div>

              {/* Horizontal Impact Bar */}
              <div className="w-full bg-slate-200/70 h-2 rounded-full overflow-hidden flex">
                <div
                  className={`h-full rounded-full transition-all duration-700 ${
                    isElevating ? 'bg-status-critical' : 'bg-status-healthy'
                  }`}
                  style={{ width: `${impactPct}%` }}
                />
              </div>

              <p className="text-[11px] text-slateText leading-snug">
                {item.clinicalExplanation}
              </p>
            </div>
          );
        })}
      </div>

      {/* Non-Causality Regulatory Advisory */}
      <div className="text-[10px] text-slateText/80 border-t border-borderLine/50 pt-3 italic">
        Notice: SHAP waterfall feature attributions reflect statistical model parameter sensitivity and do not establish direct biologic causality. Always correlate with clinical history.
      </div>
    </div>
  );
};
