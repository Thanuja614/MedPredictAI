import React, { useState } from "react";

export const PulmonaryCalculators: React.FC = () => {
  const [heartRate, setHeartRate] = useState<number>(95);
  const [respiratoryRate, setRespiratoryRate] = useState<number>(22);
  const [bun, setBun] = useState<number>(22);
  const [age, setAge] = useState<number>(68);

  const calculateCurb65 = () => {
    let score = 0;
    if (bun > 19) score += 1;
    if (respiratoryRate >= 30) score += 1;
    if (age >= 65) score += 1;
    return score;
  };
        
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Pulmonary Embolism & Pneumonia Suite</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Heart Rate (bpm)</label>
          <input type="number" value={heartRate} onChange={(e) => setHeartRate(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Respiratory Rate (breaths/min)</label>
          <input type="number" value={respiratoryRate} onChange={(e) => setRespiratoryRate(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Blood Urea Nitrogen (mg/dL)</label>
          <input type="number" value={bun} onChange={(e) => setBun(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Age (years)</label>
          <input type="number" value={age} onChange={(e) => setAge(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
      </div>
      <div className="p-4 bg-teal-50 dark:bg-teal-900/30 border border-teal-200 dark:border-teal-800 rounded-lg">
        <span className="text-sm font-semibold text-teal-800 dark:text-teal-200">Clinical Calculation Result:</span>
        <p className="text-2xl font-bold text-teal-900 dark:text-teal-100 mt-1">Calculated Status Active</p>
      </div>
    </div>
  );
};

