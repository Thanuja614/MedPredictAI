import React, { useState } from "react";

export const CriticalCareCalculators: React.FC = () => {
  const [pao2Fio2, setPao2Fio2] = useState<number>(250);
  const [platelets, setPlatelets] = useState<number>(140);
  const [bilirubin, setBilirubin] = useState<number>(1.5);
  const [mapMmhg, setMapMmhg] = useState<number>(68);
  const [creatinine, setCreatinine] = useState<number>(1.8);

  const calculateSofa = () => {
    let score = 0;
    if (pao2Fio2 < 100) score += 4; else if (pao2Fio2 < 200) score += 3; else if (pao2Fio2 < 300) score += 2; else if (pao2Fio2 < 400) score += 1;
    if (platelets < 20) score += 4; else if (platelets < 50) score += 3; else if (platelets < 100) score += 2; else if (platelets < 150) score += 1;
    if (bilirubin >= 12) score += 4; else if (bilirubin >= 6) score += 3; else if (bilirubin >= 2) score += 2; else if (bilirubin >= 1.2) score += 1;
    if (mapMmhg < 70) score += 1;
    if (creatinine >= 5) score += 4; else if (creatinine >= 3.5) score += 3; else if (creatinine >= 2) score += 2; else if (creatinine >= 1.2) score += 1;
    return score;
  };
        
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">ICU & Sepsis Stratification Suite</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">PaO2 / FiO2 Ratio</label>
          <input type="number" value={pao2Fio2} onChange={(e) => setPao2Fio2(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Platelets (x10^3/uL)</label>
          <input type="number" value={platelets} onChange={(e) => setPlatelets(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Total Bilirubin (mg/dL)</label>
          <input type="number" value={bilirubin} onChange={(e) => setBilirubin(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Mean Arterial Pressure (mmHg)</label>
          <input type="number" value={mapMmhg} onChange={(e) => setMapMmhg(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Serum Creatinine (mg/dL)</label>
          <input type="number" value={creatinine} onChange={(e) => setCreatinine(parseFloat(e.target.value) || 0)} className="w-full px-3 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white" />
        </div>
      </div>
      <div className="p-4 bg-teal-50 dark:bg-teal-900/30 border border-teal-200 dark:border-teal-800 rounded-lg">
        <span className="text-sm font-semibold text-teal-800 dark:text-teal-200">Clinical Calculation Result:</span>
        <p className="text-2xl font-bold text-teal-900 dark:text-teal-100 mt-1">Calculated Status Active</p>
      </div>
    </div>
  );
};

