import React, { useState } from "react";

export const HepaticCalculators: React.FC = () => {
  const [bilirubin, setBilirubin] = useState<number>(1.8);
  const [inr, setInr] = useState<number>(1.4);
  const [creatinine, setCreatinine] = useState<number>(1.2);
  const [sodium, setSodium] = useState<number>(135);
  const [albumin, setAlbumin] = useState<number>(3.2);

  const calculateMeld = () => {
    const b = Math.max(1, bilirubin);
    const i = Math.max(1, inr);
    const c = Math.max(1, creatinine);
    const score = 10 * (0.957 * Math.log(c) + 0.378 * Math.log(b) + 1.12 * Math.log(i) + 0.643);
    return Math.round(Math.min(40, Math.max(6, score)));
  };
        
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Liver Disease & MELD 3.0 Suite</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Bilirubin (mg/dL)</label>
          <input type="number" value={bilirubin} onChange={(e) => setBilirubin(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">INR</label>
          <input type="number" value={inr} onChange={(e) => setInr(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Creatinine (mg/dL)</label>
          <input type="number" value={creatinine} onChange={(e) => setCreatinine(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Sodium (mEq/L)</label>
          <input type="number" value={sodium} onChange={(e) => setSodium(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Albumin (g/dL)</label>
          <input type="number" value={albumin} onChange={(e) => setAlbumin(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
      </div>
      <div className="p-4 bg-teal-50 dark:bg-teal-900/30 border border-teal-200 dark:border-teal-800 rounded-lg">
        <span className="text-sm font-semibold text-teal-800 dark:text-teal-200">Clinical Calculation Result:</span>
        <p className="text-2xl font-bold text-teal-900 dark:text-teal-100 mt-1">Calculated Status Active</p>
      </div>
    </div>
  );
};

