/**
 * MedPredict AI — Medical Safety & Decision-Support Banner
 * Prominently displayed across all clinical, prediction, and screening interfaces.
 */

import React, { useState } from 'react';
import { AlertTriangle, ShieldCheck, ChevronDown, ChevronUp } from 'lucide-react';

interface MedicalDisclaimerBannerProps {
  compact?: boolean;
}

export const MedicalDisclaimerBanner: React.FC<MedicalDisclaimerBannerProps> = ({ compact = false }) => {
  const [expanded, setExpanded] = useState(false);

  if (compact) {
    return (
      <div className="bg-amber-50 border border-amber-200 text-amber-900 px-4 py-2 rounded-lg flex items-center justify-between text-xs">
        <div className="flex items-center space-x-2">
          <AlertTriangle className="w-4 h-4 text-amber-600 flex-shrink-0" />
          <span className="font-semibold">
            Clinical Decision-Support Only:
          </span>
          <span className="text-amber-800 hidden sm:inline">
            Non-diagnostic statistical risk estimation for educational research and clinician guidance.
          </span>
        </div>
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-amber-700 hover:text-amber-900 underline font-medium ml-2 flex items-center"
        >
          {expanded ? 'Less info' : 'View full safety notice'}
        </button>
      </div>
    );
  }

  return (
    <div className="bg-gradient-to-r from-amber-50 to-orange-50 border-l-4 border-amber-500 p-4 rounded-r-lg shadow-sm mb-6 text-sm text-amber-950">
      <div className="flex items-start justify-between">
        <div className="flex items-start space-x-3">
          <div className="p-1.5 bg-amber-100 rounded-md text-amber-700 mt-0.5">
            <AlertTriangle className="w-5 h-5" />
          </div>
          <div>
            <h4 className="font-bold tracking-wide uppercase text-xs text-amber-800 flex items-center space-x-1.5">
              <span>CRITICAL MEDICAL SAFETY & DECISION-SUPPORT NOTICE</span>
              <span className="bg-amber-200 text-amber-800 text-[10px] px-1.5 py-0.5 rounded font-mono font-normal">
                REGULATORY ADVISORY
              </span>
            </h4>
            <p className="mt-1 text-slate-700 leading-relaxed">
              MedPredict AI generates <strong>probabilistic, multi-disease statistical risk estimates</strong> designed strictly for clinical decision support, academic research, and health education.
              Outputs <strong>DO NOT</strong> constitute a clinical diagnosis, medical prescription, or definitive therapeutic guidance.
            </p>

            {expanded && (
              <div className="mt-3 pt-3 border-t border-amber-200 text-xs text-slate-600 space-y-2">
                <div className="flex items-center space-x-2 text-slate-700 font-medium">
                  <ShieldCheck className="w-4 h-4 text-emerald-600" />
                  <span>Physician Oversight Required:</span>
                </div>
                <p>
                  Any elevated risk probability or SHAP contribution factor must be interpreted by a licensed medical provider in accordance with standard diagnostic protocols, comprehensive patient history, physical examination, and certified laboratory tests.
                </p>
                <div className="flex items-center space-x-2 text-slate-700 font-medium pt-1">
                  <span>Non-Causal Explanation Disclaimer:</span>
                </div>
                <p>
                  Feature importance scores (SHAP waterfall values) indicate associative statistical weight within the trained machine learning model and do not imply direct medical etiology or physiological causality.
                </p>
              </div>
            )}
          </div>
        </div>

        <button
          onClick={() => setExpanded(!expanded)}
          className="text-amber-800 hover:text-amber-950 text-xs font-semibold flex items-center space-x-1 px-2.5 py-1 bg-amber-100/70 hover:bg-amber-100 rounded transition"
        >
          <span>{expanded ? 'Collapse' : 'Safety Details'}</span>
          {expanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
        </button>
      </div>
    </div>
  );
};
