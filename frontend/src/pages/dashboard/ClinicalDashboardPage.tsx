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
    <div className="space-y-5 pb-12">
      {/* 1. Clinical Command Welcome Header */}
      <div className="bg-white rounded-lg p-5 border border-slate-200 shadow-xs flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div className="space-y-1 max-w-2xl">
          <div className="inline-flex items-center space-x-2 px-2 py-0.5 rounded bg-sky-50 text-sky-700 text-xs font-semibold border border-sky-100">
            <Stethoscope className="w-3.5 h-3.5" />
            <span>Cardiopulmonary & Critical Care Medicine</span>
          </div>
          <h2 className="text-xl lg:text-2xl font-bold text-slate-900 tracking-tight">
            Clinical Command Dashboard
          </h2>
          <p className="text-xs text-slate-600 leading-normal">
            Active inpatient monitoring, real-time multi-disease risk triage, and algorithmic decision support.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 shrink-0">
          <div className="text-left sm:text-right text-xs">
            <div className="flex items-center sm:justify-end space-x-1.5 text-slate-800 font-semibold font-mono">
              <Calendar className="w-3.5 h-3.5 text-sky-600" />
              <span>Friday, September 11, 2026</span>
            </div>
            <div className="flex items-center sm:justify-end space-x-1.5 text-[11px] text-slate-500 mt-0.5">
              <Clock className="w-3 h-3 text-emerald-600" />
              <span>HL7 FHIR v4.0 Active (Latency: 14ms)</span>
            </div>
          </div>
          <Link
            to="/prediction"
            className="inline-flex items-center space-x-2 px-3.5 py-2 bg-sky-600 hover:bg-sky-700 text-white text-xs font-semibold rounded shadow-xs transition"
          >
            <span>Run Risk Assessment</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
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
        <div className="lg:col-span-2 bg-white rounded-lg p-5 border border-slate-200 shadow-xs flex flex-col justify-between">
          <div className="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
            <div>
              <h3 className="text-base font-bold text-slate-900">
                Monthly Clinical Prediction Trajectory
              </h3>
              <p className="text-xs text-slate-500">
                Diagnostic evaluations performed across inpatient and outpatient registry cohorts
              </p>
            </div>
            <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-100 text-sky-700 font-semibold border border-slate-200">
              2026 YTD
            </span>
          </div>

          <div className="h-56 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={monthlyVolumeData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="volGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#0284C7" stopOpacity={0.15} />
                    <stop offset="95%" stopColor="#0284C7" stopOpacity={0.0} />
                  </linearGradient>
                </defs>
                <XAxis dataKey="month" tick={{ fontSize: 11, fill: '#64748B' }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 11, fill: '#64748B' }} axisLine={false} tickLine={false} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#FFFFFF',
                    border: '1px solid #E2E8F0',
                    borderRadius: '6px',
                    fontSize: '11px',
                    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.05)',
                  }}
                />
                <Area type="monotone" dataKey="volume" stroke="#0284C7" strokeWidth={2} fillOpacity={1} fill="url(#volGrad)" name="Total Assessments" />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="mt-2 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>Average monthly volume growth: +8.4%</span>
            <span className="font-semibold text-slate-700">Zero algorithmic downtime detected</span>
          </div>
        </div>

        {/* Risk Category Distribution (Donut Chart) */}
        <div className="bg-white rounded-lg p-5 border border-slate-200 shadow-xs flex flex-col justify-between">
          <div className="border-b border-slate-100 pb-3 mb-2">
            <h3 className="text-base font-bold text-slate-900">
              Cohort Risk Stratification
            </h3>
            <p className="text-xs text-slate-500">
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
                    backgroundColor: '#FFFFFF',
                    border: '1px solid #E2E8F0',
                    borderRadius: '6px',
                    fontSize: '11px',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
            <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
              <span className="text-xl font-bold text-slate-900 font-sans">1,248</span>
              <span className="text-[10px] text-slate-500 uppercase font-semibold">Patients</span>
            </div>
          </div>

          <div className="space-y-1.5 pt-2 border-t border-slate-100 text-xs">
            {riskDistributionData.map((d, i) => (
              <div key={i} className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: d.color }} />
                  <span className="text-slate-600">{d.name}</span>
                </div>
                <span className="font-bold text-slate-900 font-mono">
                  {d.value} ({Math.round((d.value / 1248) * 100)}%)
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 4. Active Patient Risk Triage Queue */}
      <div className="bg-white rounded-lg border border-slate-200 shadow-xs overflow-hidden">
        <div className="p-4 bg-white border-b border-slate-200 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
          <div>
            <h3 className="text-base font-bold text-slate-900">
              Active Patient Risk Triage Queue
            </h3>
            <p className="text-xs text-slate-500">
              Prioritized clinical assessments requiring physician review or therapeutic escalation
            </p>
          </div>

          {/* Filter Pills */}
          <div className="flex items-center space-x-1.5 bg-slate-100 p-1 rounded border border-slate-200">
            {['ALL', 'HIGH', 'MODERATE', 'LOW'].map((t) => (
              <button
                key={t}
                onClick={() => setFilterTier(t)}
                className={`px-3 py-1 text-xs font-semibold rounded transition ${
                  filterTier === t
                    ? 'bg-white text-slate-900 shadow-xs border border-slate-200'
                    : 'text-slate-600 hover:text-slate-900'
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
