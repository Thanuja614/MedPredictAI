import React, { useState } from "react";

export const RenalCalculators: React.FC = () => {
  const [creatinine, setCreatinine] = useState<number>(1.0);
  const [age, setAge] = useState<number>(60);
  const [weightKg, setWeightKg] = useState<number>(75);
  const [urineSodium, setUrineSodium] = useState<number>(40);

  const calculateEgfr = () => {
    const k = 0.9;
    const scrK = creatinine / k;
    const egfr = 142 * Math.pow(Math.min(scrK, 1), -0.302) * Math.pow(Math.max(scrK, 1), -1.2) * Math.pow(0.9938, age);
    return egfr.toFixed(1);
  };
        
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Renal Function & eGFR Suite</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Serum Creatinine (mg/dL)</label>
          <input type="number" value={creatinine} onChange={(e) => setCreatinine(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Age (years)</label>
          <input type="number" value={age} onChange={(e) => setAge(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Weight (kg)</label>
          <input type="number" value={weightKg} onChange={(e) => setWeightKg(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Urine Sodium (mEq/L)</label>
          <input type="number" value={urineSodium} onChange={(e) => setUrineSodium(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
      </div>
      <div className="p-4 bg-teal-50 dark:bg-teal-900/30 border border-teal-200 dark:border-teal-800 rounded-lg">
        <span className="text-sm font-semibold text-teal-800 dark:text-teal-200">Clinical Calculation Result:</span>
        <p className="text-2xl font-bold text-teal-900 dark:text-teal-100 mt-1">Calculated Status Active</p>
      </div>
    </div>
  );
};

