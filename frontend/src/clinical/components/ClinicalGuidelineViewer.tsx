import React, { useState } from "react";
import { DRUG_DATABASE } from "../data/drugDatabase";
import { BIOMARKER_DATABASE } from "../data/biomarkerDatabase";
import { ICD10_DATABASE } from "../data/icd10Database";

export const ClinicalGuidelineViewer: React.FC = () => {
  const [search, setSearch] = useState<string>("");
  const [activeTab, setActiveTab] = useState<number>(0);
  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl p-6 shadow-md border border-slate-200 dark:border-slate-700">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Evidence-Based Clinical Practice Guidelines Portal</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search clinical registries..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full px-4 py-2 border rounded-lg border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white"
        />
      </div>
      <div className="flex gap-2 mb-4 border-b border-slate-200 dark:border-slate-700 pb-2">
        <button onClick={() => setActiveTab(0)} className={`px-4 py-2 rounded-lg text-sm font-medium ${activeTab === 0 ? "bg-teal-600 text-white" : "text-slate-600 dark:text-slate-400"}`}>Primary View</button>
        <button onClick={() => setActiveTab(1)} className={`px-4 py-2 rounded-lg text-sm font-medium ${activeTab === 1 ? "bg-teal-600 text-white" : "text-slate-600 dark:text-slate-400"}`}>Reference Table</button>
      </div>
      <div className="p-4 bg-slate-50 dark:bg-slate-900 rounded-lg text-sm text-slate-700 dark:text-slate-300">
        <p>Registry active: {Object.keys(DRUG_DATABASE).length} pharmaceuticals, {Object.keys(BIOMARKER_DATABASE).length} laboratory biomarkers, {Object.keys(ICD10_DATABASE).length} diagnostic entities loaded.</p>
      </div>
    </div>
  );
};

