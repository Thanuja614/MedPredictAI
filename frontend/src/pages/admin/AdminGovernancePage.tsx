/**
 * MedPredict AI — Administrator & Governance Control Center
 * Platform overview, dynamic system settings, background tasks, and HIPAA audit trail.
 */

import React, { useState, useEffect } from 'react';
import {
  ShieldCheck,
  Settings,
  Zap,
  Download,
  Users,
  Activity,
  CheckCircle2,
  RefreshCw,
  AlertOctagon,
  FileSpreadsheet,
} from 'lucide-react';
import { MedicalDisclaimerBanner } from '../../components/common/MedicalDisclaimerBanner';
import { api } from '../../services/api';
import { SystemOverview, AuditLogEntry, SystemSettingItem } from '../../types';

export const AdminGovernancePage: React.FC = () => {
  const [overview, setOverview] = useState<SystemOverview | null>(null);
  const [auditLogs, setAuditLogs] = useState<AuditLogEntry[]>([]);
  const [settingsList, setSettingsList] = useState<SystemSettingItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [editingKey, setEditingKey] = useState<string | null>(null);
  const [editValue, setEditValue] = useState<string>('');
  const [savingSetting, setSavingSetting] = useState(false);

  const fetchAdminData = async () => {
    setLoading(true);
    try {
      const [ov, logsRes, settingsRes] = await Promise.all([
        api.analytics.getOverview(),
        api.audit.listLogs({ limit: 20 }),
        api.settings.list(),
      ]);
      setOverview(ov);
      setAuditLogs(logsRes.logs);
      setSettingsList(settingsRes);
    } catch (err) {
      console.error('Failed to load admin governance data', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAdminData();
  }, []);

  const handleUpdateSetting = async (key: string) => {
    setSavingSetting(true);
    try {
      await api.settings.update(key, editValue);
      setEditingKey(null);
      await fetchAdminData();
    } catch (err) {
      console.error(err);
    } finally {
      setSavingSetting(false);
    }
  };

  return (
    <div className="space-y-6">
      <MedicalDisclaimerBanner />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
        <div>
          <div className="flex items-center space-x-2 text-sky-600 font-bold text-xs uppercase tracking-wide">
            <ShieldCheck className="w-4 h-4" />
            <span>Platform Administration & Compliance Control Center</span>
          </div>
          <h1 className="text-2xl font-extrabold text-slate-900 mt-1">
            System Operations & Security Audit
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            Manage dynamic system thresholds, background job queues, and inspect immutable HIPAA-compliant access logs.
          </p>
        </div>

        <button
          onClick={fetchAdminData}
          disabled={loading}
          className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition self-start sm:self-auto"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          <span>Refresh Metrics</span>
        </button>
      </div>

      {/* Platform Counters */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block">
            Registered Patients
          </span>
          <div className="text-3xl font-extrabold text-slate-900 mt-1 font-mono">
            {overview?.total_patients ?? '—'}
          </div>
          <div className="text-[11px] text-slate-500 mt-1">
            Unique clinical patient profiles
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block">
            Total Predictions Run
          </span>
          <div className="text-3xl font-extrabold text-sky-600 mt-1 font-mono">
            {overview?.total_predictions ?? '—'}
          </div>
          <div className="text-[11px] text-slate-500 mt-1">
            Across 10 disease modules
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block">
            High Risk Flags
          </span>
          <div className="text-3xl font-extrabold text-rose-600 mt-1 font-mono">
            {overview?.high_risk_count ?? '—'}
          </div>
          <div className="text-[11px] text-slate-500 mt-1">
            Probability &gt; 65% (Attention flagged)
          </div>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block">
            Active Disease Models
          </span>
          <div className="text-3xl font-extrabold text-emerald-600 mt-1 font-mono">
            {overview?.total_diseases ?? 10} / 10
          </div>
          <div className="text-[11px] text-slate-500 mt-1">
            Fully validated modules
          </div>
        </div>
      </div>

      {/* Dynamic System Settings */}
      <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs">
        <h3 className="text-base font-extrabold text-slate-900 mb-1">
          Dynamic System Settings & Risk Thresholds
        </h3>
        <p className="text-xs text-slate-500 mb-4">
          Configure operational classification boundaries and security session limits without requiring redeployment.
        </p>

        <div className="divide-y divide-slate-100 text-xs">
          {settingsList.map((st) => {
            const isEditing = editingKey === st.key;
            return (
              <div key={st.key} className="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                  <span className="font-bold text-slate-800 font-mono">{st.key}</span>
                  <p className="text-[11px] text-slate-500 mt-0.5">{st.description}</p>
                </div>

                <div className="flex items-center space-x-2">
                  {isEditing ? (
                    <>
                      <input
                        type="text"
                        value={editValue}
                        onChange={(e) => setEditValue(e.target.value)}
                        className="px-2 py-1 border border-slate-300 rounded font-mono text-xs w-36"
                      />
                      <button
                        onClick={() => handleUpdateSetting(st.key)}
                        disabled={savingSetting}
                        className="px-3 py-1 bg-sky-600 text-white font-bold rounded hover:bg-sky-700 transition"
                      >
                        Save
                      </button>
                      <button
                        onClick={() => setEditingKey(null)}
                        className="px-2 py-1 bg-slate-100 text-slate-600 rounded hover:bg-slate-200 transition"
                      >
                        Cancel
                      </button>
                    </>
                  ) : (
                    <>
                      <span className="font-mono font-bold bg-slate-100 text-slate-800 px-2 py-1 rounded">
                        {st.value}
                      </span>
                      <button
                        onClick={() => {
                          setEditingKey(st.key);
                          setEditValue(st.value);
                        }}
                        className="text-xs text-sky-600 hover:text-sky-800 font-semibold"
                      >
                        Edit
                      </button>
                    </>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Immutable HIPAA / GDPR Audit Trail */}
      <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
          <div>
            <h3 className="text-base font-extrabold text-slate-900">
              HIPAA / GDPR Immutable Audit Trail
            </h3>
            <p className="text-xs text-slate-500">
              Tamper-evident logs of all clinical predictions, authentication events, and administrative edits.
            </p>
          </div>

          <a
            href={api.audit.exportUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold shadow flex items-center space-x-1.5 transition self-start sm:self-auto"
          >
            <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-400" />
            <span>Export Compliance CSV</span>
          </a>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
              <tr>
                <th className="py-2.5 px-3 font-semibold">Timestamp</th>
                <th className="py-2.5 px-3 font-semibold">Action Event</th>
                <th className="py-2.5 px-3 font-semibold">Target Entity</th>
                <th className="py-2.5 px-3 font-semibold">Actor / User</th>
                <th className="py-2.5 px-3 font-semibold">IP Address</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {auditLogs.slice(0, 10).map((log) => (
                <tr key={log.id} className="hover:bg-slate-50/70 transition">
                  <td className="py-2.5 px-3 text-slate-500 font-mono text-[11px]">
                    {new Date(log.created_at).toLocaleString()}
                  </td>
                  <td className="py-2.5 px-3 font-bold text-slate-800 font-mono text-[11px]">
                    {log.action}
                  </td>
                  <td className="py-2.5 px-3 text-slate-600">
                    {log.entity_type} {log.entity_id ? `(${log.entity_id.slice(0, 8)})` : ''}
                  </td>
                  <td className="py-2.5 px-3 text-slate-700">
                    {log.user_email || 'System / Service'}
                  </td>
                  <td className="py-2.5 px-3 font-mono text-slate-400 text-[11px]">
                    {log.ip_address || '127.0.0.1'}
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
