/**
 * MedPredict AI — Clinical Analytics & Population Health Dashboard
 * Section 14: Prediction trends, risk distribution, model performance, accuracy curves
 * Palette: Navy, Teal, Sage, Muted Amber, Restrained Red
 */

import React from 'react';
import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  CartesianGrid,
  Legend,
} from 'recharts';
import { BarChart3, TrendingUp, ShieldCheck, Activity, Cpu, Filter, Download } from 'lucide-react';
import { StatCard } from '../../components/clinical/StatCard';

export const ClinicalAnalyticsPage: React.FC = () => {
  // Monthly Volume & Escalation Rates
  const monthlyTrends = [
    { month: 'Oct 25', total: 210, lowRisk: 140, modRisk: 55, highRisk: 15 },
    { month: 'Nov 25', total: 235, lowRisk: 150, modRisk: 65, highRisk: 20 },
    { month: 'Dec 25', total: 260, lowRisk: 165, modRisk: 72, highRisk: 23 },
    { month: 'Jan 26', total: 310, lowRisk: 190, modRisk: 90, highRisk: 30 },
    { month: 'Feb 26', total: 345, lowRisk: 210, modRisk: 105, highRisk: 30 },
    { month: 'Mar 26', total: 380, lowRisk: 230, modRisk: 115, highRisk: 35 },
    { month: 'Apr 26', total: 420, lowRisk: 250, modRisk: 130, highRisk: 40 },
    { month: 'May 26', total: 465, lowRisk: 280, modRisk: 145, highRisk: 40 },
    { month: 'Jun 26', total: 512, lowRisk: 305, modRisk: 160, highRisk: 47 },
    { month: 'Jul 26', total: 540, lowRisk: 320, modRisk: 170, highRisk: 50 },
    { month: 'Aug 26', total: 580, lowRisk: 345, modRisk: 185, highRisk: 50 },
    { month: 'Sep 26', total: 625, lowRisk: 370, modRisk: 200, highRisk: 55 },
  ];

  // 10 Disease Modules Calibration & Accuracy Metrics
  const diseaseModuleAccuracy = [
    { name: 'Diabetes', accuracy: 95.2, f1: 94.8, brier: 0.071 },
    { name: 'Coronary CAD', accuracy: 94.6, f1: 93.9, brier: 0.082 },
    { name: 'Liver Disease', accuracy: 93.8, f1: 92.5, brier: 0.091 },
    { name: 'Kidney (CKD)', accuracy: 96.1, f1: 95.7, brier: 0.065 },
    { name: 'Breast Cancer', accuracy: 97.4, f1: 96.8, brier: 0.048 },
    { name: 'Stroke Risk', accuracy: 94.1, f1: 93.2, brier: 0.088 },
    { name: 'Hypertension', accuracy: 95.8, f1: 95.0, brier: 0.074 },
    { name: 'Anemia', accuracy: 96.5, f1: 96.1, brier: 0.062 },
    { name: 'Thyroid', accuracy: 94.9, f1: 94.2, brier: 0.079 },
    { name: 'Parkinson\'s', accuracy: 93.2, f1: 92.4, brier: 0.096 },
  ];

  const riskPie = [
    { name: 'Low Risk (< 35%)', value: 680, color: '#2E7D32' },
    { name: 'Moderate (35–65%)', value: 442, color: '#C97A2B' },
    { name: 'High Risk (> 65%)', value: 126, color: '#B33939' },
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Header Banner */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-medblue uppercase tracking-wider font-mono">
            Medical Informatics Division
          </span>
          <h2 className="font-serif text-2xl lg:text-3xl font-bold text-navy-800">
            Healthcare Analytics & Population Telemetry
          </h2>
          <p className="text-xs text-slateText">
            Longitudinal multi-disease prediction distributions, clinical drift monitoring, and cross-validation metrics.
          </p>
        </div>

        <button
          onClick={() => window.print()}
          className="px-4 py-2 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-semibold rounded-btn flex items-center space-x-2 transition shadow-sm self-start md:self-auto"
        >
          <Download className="w-3.5 h-3.5" />
          <span>Export Analytics Digest</span>
        </button>
      </div>

      {/* High-Level Stat Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          label="Total Historical Predictions"
          value="3,842"
          change="+14.2%"
          changeType="positive"
          subtext="Past 12 months"
          icon={Activity}
        />
        <StatCard
          label="Mean Model Accuracy"
          value="95.1%"
          change="AUC: 0.962"
          changeType="positive"
          subtext="10 validated modules"
          icon={ShieldCheck}
        />
        <StatCard
          label="Population Brier Score"
          value="0.076"
          change="Calibration: High"
          changeType="neutral"
          subtext="Well-calibrated probabilities"
          icon={TrendingUp}
        />
        <StatCard
          label="Feature Drift Index (PSI)"
          value="0.042"
          change="Stable Cohort"
          changeType="positive"
          subtext="KS-test p > 0.05"
          icon={Cpu}
        />
      </div>

      {/* Chart 1: 12-Month Longitudinal Volume Breakdown */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
        <div className="flex items-center justify-between border-b border-borderLine pb-3">
          <div>
            <h3 className="font-serif text-lg font-bold text-navy-800">
              12-Month Population Risk Volume & Escalation Rates
            </h3>
            <p className="text-xs text-slateText">
              Stratified breakdown by clinical severity interval across inpatient and outpatient encounters
            </p>
          </div>
          <span className="text-[11px] font-mono font-medium px-2 py-1 bg-ivory rounded text-medblue border border-borderLine">
            N = 3,842 Encounters
          </span>
        </div>

        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={monthlyTrends} margin={{ top: 10, right: 10, left: -15, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#DCE3E2" vertical={false} />
              <XAxis dataKey="month" tick={{ fontSize: 11, fill: '#65727E' }} axisLine={{ stroke: '#DCE3E2' }} />
              <YAxis tick={{ fontSize: 11, fill: '#65727E' }} axisLine={{ stroke: '#DCE3E2' }} />
              <Tooltip
                contentStyle={{
                  backgroundColor: '#FCFBF8',
                  border: '1px solid #DCE3E2',
                  borderRadius: '8px',
                  fontSize: '11px',
                }}
              />
              <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
              <Bar dataKey="lowRisk" stackId="a" fill="#7C9A92" name="Low Risk (<35%)" />
              <Bar dataKey="modRisk" stackId="a" fill="#C97A2B" name="Moderate Risk (35-65%)" />
              <Bar dataKey="highRisk" stackId="a" fill="#B33939" name="High Risk (>65%)" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Chart 2 & 3: Model Performance by Disease + Cohort Pie */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* 10 Disease Modules Accuracy Table / Bar Chart (8 Cols) */}
        <div className="lg:col-span-8 bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
          <div className="flex items-center justify-between border-b border-borderLine pb-3">
            <div>
              <h3 className="font-serif text-lg font-bold text-navy-800">
                10 Core Disease Engines — Cross-Validation Metrics
              </h3>
              <p className="text-xs text-slateText">
                Test set accuracy, balanced F1-score, and probability calibration across 10 disease modules
              </p>
            </div>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={diseaseModuleAccuracy} layout="vertical" margin={{ top: 5, right: 20, left: 30, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#DCE3E2" horizontal={false} />
                <XAxis type="number" domain={[85, 100]} tick={{ fontSize: 11, fill: '#65727E' }} />
                <YAxis type="category" dataKey="name" tick={{ fontSize: 11, fill: '#263238' }} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#FCFBF8',
                    border: '1px solid #DCE3E2',
                    borderRadius: '8px',
                    fontSize: '11px',
                  }}
                />
                <Bar dataKey="accuracy" fill="#16324F" name="Accuracy (%)" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Risk Distribution Donut (4 Cols) */}
        <div className="lg:col-span-4 bg-surface rounded-card p-6 border border-borderLine shadow-medical flex flex-col justify-between">
          <div className="border-b border-borderLine pb-3">
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Active Risk Stratification
            </h3>
            <p className="text-xs text-slateText">
              Current cohort risk proportions
            </p>
          </div>

          <div className="h-44 relative flex items-center justify-center my-4">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={riskPie}
                  innerRadius={48}
                  outerRadius={68}
                  paddingAngle={4}
                  dataKey="value"
                >
                  {riskPie.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#FCFBF8',
                    border: '1px solid #DCE3E2',
                    borderRadius: '8px',
                    fontSize: '11px',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-xl font-bold text-navy-800 font-sans">1,248</span>
              <span className="text-[10px] text-slateText uppercase font-semibold">Patients</span>
            </div>
          </div>

          <div className="space-y-2 border-t border-borderLine/50 pt-3 text-xs">
            {riskPie.map((item, idx) => (
              <div key={idx} className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: item.color }} />
                  <span className="text-slateText">{item.name}</span>
                </div>
                <span className="font-bold text-navy-800 font-mono">
                  {item.value} ({Math.round((item.value / 1248) * 100)}%)
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
