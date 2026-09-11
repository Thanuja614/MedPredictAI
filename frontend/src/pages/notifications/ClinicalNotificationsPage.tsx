/**
 * MedPredict AI — Clinical Alerts & Notification Center
 * Section 18: Triage alerts, laboratory panic values, drift notifications
 */

import React, { useState } from 'react';
import {
  Bell,
  AlertTriangle,
  AlertCircle,
  CheckCircle2,
  Info,
  ShieldAlert,
  Clock,
  Filter,
  CheckCheck,
} from 'lucide-react';

interface AlertItem {
  id: string;
  type: 'CRITICAL' | 'WARNING' | 'INFO' | 'SUCCESS';
  title: string;
  message: string;
  time: string;
  source: string;
  isRead: boolean;
}

export const ClinicalNotificationsPage: React.FC = () => {
  const [filterType, setFilterType] = useState<string>('ALL');
  const [alerts, setAlerts] = useState<AlertItem[]>([
    {
      id: 'AL-1',
      type: 'CRITICAL',
      title: 'Lab Panic Value: High-Sensitivity Troponin I',
      message: 'Patient Marcus Vance (MP-2026-00912) recorded Troponin I at 0.42 ng/mL (Reference < 0.04 ng/mL). Immediate bedside cardiology review and 12-lead EKG recommended.',
      time: '14 minutes ago',
      source: 'Central Pathology Automation',
      isRead: false,
    },
    {
      id: 'AL-2',
      type: 'WARNING',
      title: 'Longitudinal Risk Acceleration: Ananya Rao',
      message: 'ASCVD 10-year probability rose from 58.2% to 68.4% over 30 days (+10.2% velocity). Primary driver: rising fasting glycemia (126 mg/dL).',
      time: '48 minutes ago',
      source: 'MedPredict AI Longitudinal Engine',
      isRead: false,
    },
    {
      id: 'AL-3',
      type: 'CRITICAL',
      title: 'Electrolyte Panic Value: Potassium K+',
      message: 'Patient David O\'Connor (MP-2026-00438) recorded Serum Potassium at 5.7 mmol/L. Review Chlorthalidone and Losartan dosing.',
      time: '1 hour ago',
      source: 'Nephrology Telemetry Unit',
      isRead: false,
    },
    {
      id: 'AL-4',
      type: 'INFO',
      title: 'Automated Model Drift Calibration Complete',
      message: 'Weekly population stability index (PSI) calculated at 0.042 across all 10 modules. Calibration curves demonstrate optimal reliability (Brier score: 0.076).',
      time: '3 hours ago',
      source: 'MLOps Governance Pipeline',
      isRead: true,
    },
    {
      id: 'AL-5',
      type: 'SUCCESS',
      title: 'Electronic Prescription Synchronized',
      message: 'Guideline-directed medical therapy for Eleanor Chen (MP-2026-02319) transmitted and verified by Outpatient Pharmacy.',
      time: '5 hours ago',
      source: 'Pharmacy HL7 Interface',
      isRead: true,
    },
  ]);

  const handleMarkAllRead = () => {
    setAlerts((prev) => prev.map((a) => ({ ...a, isRead: true })));
  };

  const filtered = alerts.filter((a) => {
    if (filterType === 'ALL') return true;
    return a.type === filterType;
  });

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-medblue uppercase tracking-wider font-mono">
            Clinical Telemetry & Alert Stream
          </span>
          <h2 className="text-xl lg:text-2xl font-bold text-slate-900">
            Active Alerts & Notifications
          </h2>
          <p className="text-xs text-slateText">
            Prioritized clinical emergencies, critical analyte thresholds, and machine learning calibration notices.
          </p>
        </div>

        <button
          onClick={handleMarkAllRead}
          className="px-4 py-2 bg-ivory hover:bg-medblue-light text-navy-800 text-xs font-semibold rounded-btn border border-borderLine flex items-center space-x-1.5 transition shadow-xs self-start md:self-auto"
        >
          <CheckCheck className="w-3.5 h-3.5 text-medblue" />
          <span>Mark All as Read</span>
        </button>
      </div>

      {/* Filter Tabs */}
      <div className="flex items-center space-x-2 bg-surface p-2 rounded-card border border-borderLine overflow-x-auto text-xs font-semibold">
        {[
          { key: 'ALL', label: 'All Alerts' },
          { key: 'CRITICAL', label: 'Critical Emergencies' },
          { key: 'WARNING', label: 'Warnings & Risk Flags' },
          { key: 'INFO', label: 'Telemetry & MLOps' },
        ].map((tab) => (
          <button
            key={tab.key}
            onClick={() => setFilterType(tab.key)}
            className={`px-3.5 py-1.5 rounded-btn transition ${
              filterType === tab.key
                ? 'bg-navy-800 text-ivory shadow-xs'
                : 'text-slateText hover:text-navy-800 hover:bg-ivory'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Alert Feed */}
      <div className="space-y-3">
        {filtered.map((alert) => {
          const isCritical = alert.type === 'CRITICAL';
          const isWarning = alert.type === 'WARNING';

          return (
            <div
              key={alert.id}
              className={`p-4 bg-surface rounded-card border transition ${
                !alert.isRead ? 'border-medblue/40 shadow-subtle' : 'border-borderLine'
              } flex items-start space-x-3.5`}
            >
              <div
                className={`p-2 rounded-btn shrink-0 ${
                  isCritical
                    ? 'bg-status-criticalBg text-status-critical'
                    : isWarning
                    ? 'bg-status-warningBg text-status-warning'
                    : 'bg-medblue-light text-medblue'
                }`}
              >
                {isCritical ? (
                  <AlertCircle className="w-4 h-4" />
                ) : isWarning ? (
                  <AlertTriangle className="w-4 h-4" />
                ) : (
                  <Info className="w-4 h-4" />
                )}
              </div>

              <div className="flex-1 min-w-0 space-y-1">
                <div className="flex items-center justify-between flex-wrap gap-1">
                  <span className={`text-xs font-bold ${isCritical ? 'text-status-critical' : 'text-navy-800'}`}>
                    {alert.title}
                  </span>
                  <span className="text-[11px] text-slateText font-mono flex items-center space-x-1">
                    <Clock className="w-3 h-3" />
                    <span>{alert.time}</span>
                  </span>
                </div>

                <p className="text-xs text-charcoal leading-relaxed">
                  {alert.message}
                </p>

                <div className="flex items-center space-x-2 pt-1 text-[10px] text-slateText">
                  <span className="font-semibold text-slate-700">Source:</span>
                  <span>{alert.source}</span>
                  <span>•</span>
                  <span className={alert.isRead ? 'text-slate-400' : 'text-medblue font-semibold'}>
                    {alert.isRead ? 'Acknowledged' : 'Unread'}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
