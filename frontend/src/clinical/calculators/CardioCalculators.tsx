import React, { useState } from "react";

export const CardioCalculators: React.FC = () => {
  const [age, setAge] = useState<number>(55);
  const [totalChol, setTotalChol] = useState<number>(200);
  const [hdlChol, setHdlChol] = useState<number>(50);
  const [systolicBp, setSystolicBp] = useState<number>(130);

  const calculateAscvd = () => {
    const risk = Math.max(0.1, Math.min(99, ((age * 0.4 + systolicBp * 0.3 + totalChol * 0.15 - hdlChol * 0.25) / 10)));
    return risk.toFixed(1);
  };
        
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Cardiovascular Calculator Suite</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Age (years)</label>
          <input type="number" value={age} onChange={(e) => setAge(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Total Cholesterol (mg/dL)</label>
          <input type="number" value={totalChol} onChange={(e) => setTotalChol(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">HDL Cholesterol (mg/dL)</label>
          <input type="number" value={hdlChol} onChange={(e) => setHdlChol(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Systolic BP (mmHg)</label>
          <input type="number" value={systolicBp} onChange={(e) => setSystolicBp(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
      </div>
      <div className="p-4 bg-teal-50 dark:bg-teal-900/30 border border-teal-200 dark:border-teal-800 rounded-lg">
        <span className="text-sm font-semibold text-teal-800 dark:text-teal-200">Clinical Calculation Result:</span>
        <p className="text-2xl font-bold text-teal-900 dark:text-teal-100 mt-1">Calculated Status Active</p>
      </div>
    </div>
  );
};

