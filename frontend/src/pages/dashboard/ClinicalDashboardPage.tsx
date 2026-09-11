/**
 * MedPredict AI — Master Clinical Dashboard Page
 * Section 7 & 8: Welcome panel, key medical statistics, active risk queue, charts
 */

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Users,
  Activity,
  AlertTriangle,
  ShieldCheck,
  Calendar,
  Clock,
  ArrowRight,
  TrendingUp,
  Stethoscope,
  Filter,
  FileText,
  Search,
  CheckCircle2,
  ChevronRight,
} from 'lucide-react';
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from 'recharts';
import { StatCard } from '../../components/clinical/StatCard';
import { StatusBadge } from '../../components/clinical/StatusBadge';
import { DEMO_PATIENTS, PatientRecord } from '../../clinical/data/demoClinicalData';

export const ClinicalDashboardPage: React.FC = () => {
  const navigate = useNavigate();
  const [filterTier, setFilterTier] = useState<string>('ALL');

  // Trend data for prediction volume
  const monthlyVolumeData = [
    { month: 'Apr', volume: 240, highRisk: 18 },
    { month: 'May', volume: 298, highRisk: 22 },
    { month: 'Jun', volume: 345, highRisk: 28 },
    { month: 'Jul', volume: 390, highRisk: 31 },
    { month: 'Aug', volume: 462, highRisk: 36 },
    { month: 'Sep', volume: 512, highRisk: 42 },
  ];

  // Risk Distribution Data (Restrained medical palette)
  const riskDistributionData = [
    { name: 'Low Risk', value: 680, color: '#2E7D32' },
    { name: 'Moderate Risk', value: 442, color: '#C97A2B' },
    { name: 'High Risk', value: 126, color: '#B33939' },
  ];

  const filteredPatients = DEMO_PATIENTS.filter((pt) => {
    if (filterTier === 'ALL') return true;
    return pt.riskTier === filterTier;
  });

  return (
    <div className="space-y-6 pb-12">
      {/* 1. Welcome Clinical Panel */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical relative overflow-hidden">
        {/* Subtle grid pattern background */}
        <div className="absolute inset-0 bg-medical-grid opacity-60 pointer-events-none" />
        
        <div className="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div className="space-y-1.5 max-w-2xl">
            <div className="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-medblue-light text-medblue text-[11px] font-semibold border border-medblue/20">
              <Stethoscope className="w-3.5 h-3.5" />
              <span>Cardiopulmonary & Metabolic Clinical Command</span>
            </div>
            <h2 className="font-serif text-2xl lg:text-3xl font-bold text-navy-800 tracking-tight">
              Good morning, Dr. Mitchell
            </h2>
            <p className="text-xs text-slateText leading-relaxed">
              Review current inpatient and ambulatory disease risk predictions, verify flagged biomarker alerts, and access calibrated clinical decision-support telemetry.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 shrink-0">
            <div className="text-left sm:text-right text-xs">
              <div className="flex items-center sm:justify-end space-x-1.5 text-navy-800 font-semibold font-mono">
                <Calendar className="w-3.5 h-3.5 text-medblue" />
                <span>Friday, September 11, 2026</span>
              </div>
              <div className="flex items-center sm:justify-end space-x-1.5 text-[11px] text-slateText mt-0.5">
                <Clock className="w-3 h-3 text-sage" />
                <span>Sync: 4 mins ago (HL7 FHIR v4.0)</span>
              </div>
            </div>
            <Link
              to="/prediction"
              className="inline-flex items-center space-x-2 px-4 py-2 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-semibold rounded-btn shadow-sm transition"
            >
              <span>New Risk Assessment</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>
      </div>

      {/* 2. Key Medical Statistics (Section 8) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          label="Total Monitored Patients"
          value="1,248"
          change="+4.2%"
          changeType="positive"
          subtext="Active in registry"
          icon={Users}
        />
        <StatCard
          label="Predictions Completed"
          value="3,842"
          change="+12.8%"
          changeType="positive"
          subtext="Across 10 disease modules"
          icon={Activity}
        />
        <StatCard
          label="High-Risk Priority Cases"
          value="126"
          change="-2.1%"
          changeType="positive"
          subtext="Requires clinical review"
          icon={AlertTriangle}
        />
        <StatCard
          label="Model Calibration / Accuracy"
          value="94.7%"
          change="Brier: 0.082"
          changeType="neutral"
          subtext="Validated test cohort"
          icon={ShieldCheck}
        />
      </div>

      {/* 3. Charts & Analytics Overview */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Monthly Prediction Volume (Area Chart) */}
        <div className="lg:col-span-2 bg-surface rounded-card p-5 border border-borderLine shadow-medical flex flex-col justify-between">
          <div className="flex items-center justify-between border-b border-borderLine pb-3 mb-4">
            <div>
              <h3 className="font-serif text-lg font-bold text-navy-800">
                Monthly Clinical Prediction Trajectory
              </h3>
              <p className="text-xs text-slateText">
                Volume of diagnostic assessments evaluated across inpatient and outpatient services
              </p>
            </div>
            <span className="text-[11px] font-mono px-2 py-1 rounded bg-ivory text-medblue font-semibold border border-borderLine">
              2026 YTD
            </span>
          </div>

          <div className="h-56 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={monthlyVolumeData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="volGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#2F6F8F" stopOpacity={0.25} />
                    <stop offset="95%" stopColor="#2F6F8F" stopOpacity={0.0} />
                  </linearGradient>
                </defs>
                <XAxis dataKey="month" tick={{ fontSize: 11, fill: '#65727E' }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: '#65727E' }} axisLine={false} tickLine={false} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#FCFBF8',
                    border: '1px solid #DCE3E2',
                    borderRadius: '8px',
                    fontSize: '11px',
                    boxShadow: '0 4px 12px rgba(22, 50, 79, 0.08)',
                  }}
                />
                <Area type="monotone" dataKey="volume" stroke="#16324F" strokeWidth={2} fillOpacity={1} fill="url(#volGrad)" name="Total Assessments" />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="mt-2 pt-3 border-t border-borderLine/50 flex items-center justify-between text-xs text-slateText">
            <span>Average monthly growth: +8.4%</span>
            <span className="font-semibold text-navy-800">Zero inference downtime detected</span>
          </div>
        </div>

        {/* Risk Category Distribution (Donut Chart) */}
        <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical flex flex-col justify-between">
          <div className="border-b border-borderLine pb-3 mb-2">
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Cohort Risk Stratification
            </h3>
            <p className="text-xs text-slateText">
              Active patient population distribution
            </p>
          </div>

          <div className="h-44 relative flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={riskDistributionData}
                  innerRadius={48}
                  outerRadius={68}
                  paddingAngle={4}
                  dataKey="value"
                >
                  {riskDistributionData.map((entry, index) => (
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

          <div className="space-y-1.5 pt-2 border-t border-borderLine/50 text-xs">
            {riskDistributionData.map((d, i) => (
              <div key={i} className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: d.color }} />
                  <span className="text-slateText">{d.name}</span>
                </div>
                <span className="font-bold text-navy-800 font-mono">
                  {d.value} ({Math.round((d.value / 1248) * 100)}%)
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 4. Active Patient Risk Triage Queue */}
      <div className="bg-surface rounded-card border border-borderLine shadow-medical overflow-hidden">
        <div className="p-5 bg-surface border-b border-borderLine flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
          <div>
            <h3 className="font-serif text-lg font-bold text-navy-800">
              Active Patient Risk Triage Queue
            </h3>
            <p className="text-xs text-slateText">
              Prioritized clinical assessments requiring physician review or therapeutic escalation
            </p>
          </div>

          {/* Filter Pills */}
          <div className="flex items-center space-x-1.5 bg-ivory p-1 rounded-btn border border-borderLine">
            {['ALL', 'HIGH', 'MODERATE', 'LOW'].map((t) => (
              <button
                key={t}
                onClick={() => setFilterTier(t)}
                className={`px-3 py-1 text-xs font-semibold rounded-md transition ${
                  filterTier === t
                    ? 'bg-navy-800 text-ivory shadow-xs'
                    : 'text-slateText hover:text-navy-800'
                }`}
              >
                {t === 'ALL' ? 'All Patients' : t}
              </button>
            ))}
          </div>
        </div>

        {/* Table View */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-charcoal">
            <thead className="bg-ivory/80 text-[11px] font-bold text-slateText uppercase font-mono tracking-wider border-b border-borderLine">
              <tr>
                <th className="py-3 px-4">Patient / MRN</th>
                <th className="py-3 px-4">Demographics</th>
                <th className="py-3 px-4">Primary Condition</th>
                <th className="py-3 px-4">Risk Stratification</th>
                <th className="py-3 px-4">Probability</th>
                <th className="py-3 px-4">30-Day Velocity</th>
                <th className="py-3 px-4 text-right">Clinical Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderLine/50">
              {filteredPatients.map((pt) => (
                <tr key={pt.id} className="hover:bg-ivory/50 transition">
                  <td className="py-3.5 px-4 font-semibold text-navy-800">
                    <div>{pt.name}</div>
                    <div className="text-[11px] text-slateText font-mono font-normal">{pt.mrn}</div>
                  </td>
                  <td className="py-3.5 px-4 text-slateText">
                    {pt.age} yrs • {pt.gender} • {pt.bloodType}
                  </td>
                  <td className="py-3.5 px-4 text-charcoal">
                    {pt.primaryCondition}
                  </td>
                  <td className="py-3.5 px-4">
                    <StatusBadge status={pt.riskTier} label={`${pt.riskTier} RISK`} />
                  </td>
                  <td className="py-3.5 px-4 font-mono font-bold text-navy-800">
                    {pt.calibratedProbability.toFixed(1)}%
                  </td>
                  <td className="py-3.5 px-4">
                    <span
                      className={`text-[11px] font-semibold px-2 py-0.5 rounded ${
                        pt.velocityTrend === 'ESCALATING'
                          ? 'bg-status-criticalBg text-status-critical'
                          : pt.velocityTrend === 'IMPROVING'
                          ? 'bg-status-healthyBg text-status-healthy'
                          : 'bg-ivory text-slateText'
                      }`}
                    >
                      {pt.velocityTrend}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 text-right">
                    <Link
                      to={`/patients/${pt.id}`}
                      className="inline-flex items-center space-x-1 text-xs font-semibold text-medblue hover:text-navy-800 hover:underline"
                    >
                      <span>Review Record</span>
                      <ChevronRight className="w-3.5 h-3.5" />
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
