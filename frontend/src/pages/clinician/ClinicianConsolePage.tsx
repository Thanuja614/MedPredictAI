/**
 * MedPredict AI — Clinician & Doctor Diagnostic Console
 */

import React, { useState, useEffect } from 'react';
import {
  Stethoscope,
  Users,
  TrendingUp,
  AlertCircle,
  FileDown,
  Activity,
  CheckCircle2,
  Clock,
  Search,
} from 'lucide-react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine,
} from 'recharts';
import { MedicalDisclaimerBanner } from '../../components/common/MedicalDisclaimerBanner';
import { api } from '../../services/api';
import { PatientTimelineResponse } from '../../types';

export const ClinicianConsolePage: React.FC = () => {
  const [patients, setPatients] = useState<any[]>([]);
  const [selectedPatientId, setSelectedPatientId] = useState<string>('');
  const [timelineData, setTimelineData] = useState<PatientTimelineResponse | null>(null);
  const [loadingTimeline, setLoadingTimeline] = useState(false);
  const [downloadingReport, setDownloadingReport] = useState(false);

  useEffect(() => {
    const fetchPatients = async () => {
      try {
        const list = await api.patients.list();
        setPatients(list);
        if (list.length > 0) {
          setSelectedPatientId(list[0].id);
        }
      } catch (err) {
        console.error('Failed to load patients', err);
      }
    };
    fetchPatients();
  }, []);

  useEffect(() => {
    const fetchTimeline = async () => {
      if (!selectedPatientId) return;
      setLoadingTimeline(true);
      try {
        const res = await api.analytics.getPatientTimeline(selectedPatientId);
        setTimelineData(res);
      } catch (err) {
        console.error('Failed to load timeline', err);
      } finally {
        setLoadingTimeline(false);
      }
    };
    fetchTimeline();
  }, [selectedPatientId]);

  const selectedPatient = patients.find((p) => p.id === selectedPatientId);

  const handleDownloadReport = async (predictionId: string) => {
    setDownloadingReport(true);
    try {
      const rep = await api.reports.generate(predictionId);
      window.open(rep.download_url, '_blank');
    } catch (err) {
      console.error(err);
    } finally {
      setDownloadingReport(false);
    }
  };

  return (
    <div className="space-y-6">
      <MedicalDisclaimerBanner />

      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
        <div>
          <div className="flex items-center space-x-2 text-sky-600 font-bold text-xs uppercase tracking-wide">
            <Stethoscope className="w-4 h-4" />
            <span>Clinician Diagnostic & Decision-Support Console</span>
          </div>
          <h1 className="text-2xl font-extrabold text-slate-900 mt-1">
            Longitudinal Patient Risk Monitoring
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            Review multi-timepoint risk trajectories, velocity indicators, and generate signed clinical assessment reports.
          </p>
        </div>

        {/* Patient Selection Dropdown */}
        <div className="flex items-center space-x-2">
          <label className="text-xs font-bold text-slate-700">Patient:</label>
          <select
            value={selectedPatientId}
            onChange={(e) => setSelectedPatientId(e.target.value)}
            className="px-3 py-2 text-xs border border-slate-300 rounded-lg focus:ring-2 focus:ring-sky-500 font-medium bg-white"
          >
            {patients.map((p) => (
              <option key={p.id} value={p.id}>
                {p.user?.first_name} {p.user?.last_name} (MRN: {p.id.slice(0, 8)})
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Patient Bio & Trajectory Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Patient Card */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-4">
          <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">
            Patient Demographics
          </h3>
          <div className="flex items-center space-x-3">
            <div className="w-12 h-12 rounded-full bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-lg">
              {selectedPatient?.user?.first_name?.[0] || 'P'}
            </div>
            <div>
              <div className="font-extrabold text-base text-slate-900">
                {selectedPatient?.user?.first_name} {selectedPatient?.user?.last_name}
              </div>
              <div className="text-xs text-slate-500 font-mono">
                MRN: {selectedPatient?.id.slice(0, 8)}
              </div>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-2 text-xs pt-2 border-t border-slate-100">
            <div>
              <span className="text-slate-400 block text-[10px]">Gender</span>
              <span className="font-semibold capitalize text-slate-700">
                {selectedPatient?.gender || 'N/A'}
              </span>
            </div>
            <div>
              <span className="text-slate-400 block text-[10px]">Blood Group</span>
              <span className="font-semibold text-slate-700">
                {selectedPatient?.blood_group || 'O+'}
              </span>
            </div>
            <div>
              <span className="text-slate-400 block text-[10px]">Date of Birth</span>
              <span className="font-semibold text-slate-700">
                {selectedPatient?.date_of_birth || '1982-05-14'}
              </span>
            </div>
            <div>
              <span className="text-slate-400 block text-[10px]">Status</span>
              <span className="inline-flex items-center space-x-1 font-semibold text-emerald-600">
                <CheckCircle2 className="w-3 h-3" />
                <span>Active Profile</span>
              </span>
            </div>
          </div>
        </div>

        {/* Trajectory Velocity Indicator */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
          <div>
            <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
              Risk Trajectory Velocity
            </h3>
            <div className="flex items-center space-x-2">
              <TrendingUp className="w-5 h-5 text-sky-600" />
              <span className="text-xl font-extrabold text-slate-900">
                {timelineData?.trajectory || 'STABLE'}
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-2 leading-relaxed">
              Based on {timelineData?.total_assessments || 0} recorded timepoints.
              Progression slope reflects 30-day moving delta across calibrated disease risk scores.
            </p>
          </div>
          <div className="mt-4 p-2 bg-slate-50 rounded-lg text-[11px] text-slate-600 border border-slate-200">
            Recommendation: Regular 6-month laboratory panels and glycemic monitoring.
          </div>
        </div>

        {/* Quick Action Box */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
          <div>
            <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
              Physician Actions
            </h3>
            <p className="text-xs text-slate-600">
              Generate full multi-disease assessment reports with SHA-256 digital verification hashes for clinical records.
            </p>
          </div>
          <div className="space-y-2 mt-4">
            <button
              onClick={() => {
                if (timelineData?.timeline?.[0]) {
                  handleDownloadReport(timelineData.timeline[0].prediction_id);
                }
              }}
              disabled={downloadingReport || !timelineData?.timeline?.length}
              className="w-full py-2.5 px-3 bg-sky-600 hover:bg-sky-700 text-white rounded-xl font-bold text-xs shadow transition flex items-center justify-center space-x-2 disabled:opacity-50"
            >
              <FileDown className="w-4 h-4" />
              <span>
                {downloadingReport ? 'Compiling PDF...' : 'Download Latest Clinical Report'}
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* Longitudinal Risk Trajectory Graph */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
        <h3 className="text-base font-extrabold text-slate-900 mb-1">
          Multi-Timepoint Risk Evolution Curve
        </h3>
        <p className="text-xs text-slate-500 mb-4">
          Chronological progression of calibrated risk probability over time
        </p>

        {loadingTimeline ? (
          <div className="h-64 flex items-center justify-center text-xs text-slate-400">
            Loading longitudinal trajectory...
          </div>
        ) : timelineData?.timeline && timelineData.timeline.length > 0 ? (
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                data={timelineData.timeline}
                margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
              >
                <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                <XAxis
                  dataKey="created_at"
                  tickFormatter={(t) => new Date(t).toLocaleDateString()}
                  tick={{ fontSize: 10 }}
                />
                <YAxis
                  domain={[0, 1]}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`}
                  tick={{ fontSize: 10 }}
                />
                <Tooltip
                  formatter={(val: any) => [`${(Number(val) * 100).toFixed(1)}%`, 'Risk Score']}
                  labelFormatter={(l) => new Date(l).toLocaleString()}
                />
                <ReferenceLine y={0.35} stroke="#16a34a" strokeDasharray="3 3" label="Low Threshold" />
                <ReferenceLine y={0.65} stroke="#dc2626" strokeDasharray="3 3" label="High Threshold" />
                <Line
                  type="monotone"
                  dataKey="probability"
                  stroke="#0284c7"
                  strokeWidth={3}
                  dot={{ r: 5, fill: '#0284c7' }}
                  activeDot={{ r: 7 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="text-center py-12 text-xs text-slate-400">
            No historical evaluations recorded for this patient yet. Run an assessment to populate trajectory data.
          </div>
        )}
      </div>
    </div>
  );
};
