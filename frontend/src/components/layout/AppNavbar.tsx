/**
 * MedPredict AI — High-End Clinical Header Navigation
 * Ivory & Navy palette, contextual page titles, search bar, notification center
 */

import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  Activity,
  Bell,
  Search,
  HelpCircle,
  Stethoscope,
  ShieldCheck,
  CheckCircle2,
  AlertTriangle,
  User as UserIcon,
  Database,
  Shield,
  X,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const AppNavbar: React.FC = () => {
  const { user, activeRole, setActiveRole } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const [showNotifs, setShowNotifs] = useState(false);
  const [showHelp, setShowHelp] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  // Contextual Titles & Subtitles based on Route
  const getHeaderContext = () => {
    const p = location.pathname;
    if (p === '/') {
      return {
        title: 'Clinical Command Dashboard',
        subtitle: 'Real-time patient monitoring, active risk assessments, and diagnostic metrics',
      };
    }
    if (p.startsWith('/patients')) {
      return {
        title: 'Electronic Health Records & Patient Registry',
        subtitle: 'Comprehensive patient directory, longitudinal lab histories, and diagnostic records',
      };
    }
    if (p.startsWith('/prediction')) {
      return {
        title: 'Multi-Disease Risk Prediction Engine',
        subtitle: 'Validated clinical decision-support algorithms with calibrated feature attribution',
      };
    }
    if (p.startsWith('/reports')) {
      return {
        title: 'Official Clinical Assessment Reports',
        subtitle: 'Physician-verified diagnostic summaries with cryptographic SHA-256 integrity digests',
      };
    }
    if (p.startsWith('/analytics')) {
      return {
        title: 'Healthcare Analytics & Population Health',
        subtitle: 'Longitudinal risk trajectory curves, cohort distributions, and model calibration',
      };
    }
    if (p.startsWith('/history')) {
      return {
        title: 'Diagnostic Prediction Audit History',
        subtitle: 'Chronological clinical audit log with multi-disease stratification scores',
      };
    }
    if (p.startsWith('/notifications')) {
      return {
        title: 'Clinical Alerts & Laboratory Notifications',
        subtitle: 'Emergency triage thresholds, abnormal biomarker values, and model drift telemetry',
      };
    }
    if (p.startsWith('/settings')) {
      return {
        title: 'System Settings & Decision Governance',
        subtitle: 'Dynamic probability thresholds, clinical guideline versioning, and compliance audit',
      };
    }
    return {
      title: 'Clinical Decision Support Portal',
      subtitle: 'Intelligent multi-disease analytics and risk assessment platform',
    };
  };

  const context = getHeaderContext();

  const demoNotifs = [
    {
      id: '1',
      title: 'Critical Lab Alert: Troponin I Elevated',
      message: 'Patient Marcus Vance (MP-2026-00912) recorded Troponin I at 0.42 ng/mL. Immediate cardiology review advised.',
      time: '12 min ago',
      urgent: true,
    },
    {
      id: '2',
      title: 'Risk Progression Flag: Ananya Rao',
      message: 'ASCVD 10-year risk velocity marked as ESCALATING (+4.2% in 30 days). GDMT optimization suggested.',
      time: '45 min ago',
      urgent: false,
    },
    {
      id: '3',
      title: 'Model Calibration Check Complete',
      message: 'All 10 core disease algorithms validated. Brier score 0.082 across 1,248 patient records.',
      time: '2 hours ago',
      urgent: false,
    },
  ];

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/patients?search=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  return (
    <header className="sticky top-0 z-40 bg-surface border-b border-borderLine shadow-subtle">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Left: Brand + Contextual Page Title */}
        <div className="flex items-center space-x-4">
          <Link to="/" className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-navy-800 flex items-center justify-center text-ivory shadow-sm shadow-navy-800/30">
              <Activity className="w-4 h-4 text-teal" />
            </div>
            <div>
              <span className="font-extrabold text-base text-navy-800 tracking-tight">
                MedPredict<span className="text-medblue font-serif italic text-lg">AI</span>
              </span>
            </div>
          </Link>

          <div className="hidden lg:block h-6 w-px bg-borderLine" />

          {/* Contextual Title */}
          <div className="hidden sm:block">
            <h1 className="text-sm font-semibold text-charcoal font-sans leading-tight">
              {context.title}
            </h1>
            <p className="text-[11px] text-slateText truncate max-w-md">
              {context.subtitle}
            </p>
          </div>
        </div>

        {/* Center / Right: Global Search & Quick Actions */}
        <div className="flex items-center space-x-3">
          {/* Global Patient / Protocol Search */}
          <form onSubmit={handleSearchSubmit} className="relative hidden md:block">
            <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slateText" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search patient, MRN, protocol..."
              className="w-56 lg:w-68 pl-8 pr-3 py-1.5 text-xs bg-ivory border border-borderLine rounded-btn text-charcoal placeholder-slateText focus:outline-none focus:ring-1 focus:ring-medblue focus:bg-white transition"
            />
          </form>

          {/* Clinical Notifications Bell */}
          <div className="relative">
            <button
              onClick={() => setShowNotifs(!showNotifs)}
              className="p-2 text-slateText hover:text-navy-800 hover:bg-ivory rounded-btn relative transition border border-transparent hover:border-borderLine"
              aria-label="Clinical Alerts"
              title="Clinical Alerts & Notifications"
            >
              <Bell className="w-4 h-4" />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-status-critical rounded-full ring-2 ring-surface animate-pulse" />
            </button>

            {/* Notification Dropdown */}
            {showNotifs && (
              <div className="absolute right-0 mt-2 w-88 bg-surface border border-borderLine rounded-card shadow-elevated z-50 overflow-hidden">
                <div className="p-3 bg-ivory border-b border-borderLine flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <AlertTriangle className="w-4 h-4 text-status-warning" />
                    <span className="text-xs font-bold text-navy-800 uppercase tracking-wider font-mono">
                      Clinical Alerts (3)
                    </span>
                  </div>
                  <Link
                    to="/notifications"
                    onClick={() => setShowNotifs(false)}
                    className="text-[11px] text-medblue hover:underline font-medium"
                  >
                    View All
                  </Link>
                </div>
                <div className="max-h-80 overflow-y-auto divide-y divide-borderLine/50">
                  {demoNotifs.map((n) => (
                    <div
                      key={n.id}
                      className={`p-3 text-xs hover:bg-ivory/70 transition cursor-pointer ${
                        n.urgent ? 'bg-status-criticalBg/40' : 'bg-surface'
                      }`}
                      onClick={() => {
                        setShowNotifs(false);
                        navigate('/notifications');
                      }}
                    >
                      <div className="flex items-center justify-between">
                        <span className={`font-semibold ${n.urgent ? 'text-status-critical' : 'text-navy-800'}`}>
                          {n.title}
                        </span>
                        <span className="text-[10px] text-slateText">{n.time}</span>
                      </div>
                      <p className="text-slateText text-[11px] mt-1 leading-snug">{n.message}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Clinical Decision Support Guide */}
          <button
            onClick={() => setShowHelp(true)}
            className="p-2 text-slateText hover:text-navy-800 hover:bg-ivory rounded-btn transition"
            title="Medical Protocol & Decision Support Guide"
          >
            <HelpCircle className="w-4 h-4" />
          </button>

          {/* Doctor Avatar & Role Badge */}
          <div className="flex items-center space-x-2 pl-2 border-l border-borderLine">
            <div className="w-8 h-8 rounded-full bg-navy-800 flex items-center justify-center text-ivory text-xs font-bold ring-2 ring-medblue/20">
              SM
            </div>
            <div className="hidden sm:block text-left leading-tight">
              <span className="text-xs font-semibold text-charcoal block">Dr. S. Mitchell</span>
              <span className="text-[10px] text-medblue font-medium tracking-wide">Attending MD</span>
            </div>
          </div>
        </div>
      </div>

      {/* Help Modal */}
      {showHelp && (
        <div className="fixed inset-0 z-50 bg-navy-900/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-surface rounded-card border border-borderLine max-w-lg w-full p-6 shadow-elevated space-y-4">
            <div className="flex items-center justify-between border-b border-borderLine pb-3">
              <div className="flex items-center space-x-2.5">
                <Stethoscope className="w-5 h-5 text-medblue" />
                <h3 className="font-serif text-lg font-bold text-navy-800">
                  Clinical Decision Support Guide
                </h3>
              </div>
              <button
                onClick={() => setShowHelp(false)}
                className="text-slateText hover:text-charcoal p-1"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <div className="text-xs text-charcoal space-y-3 leading-relaxed">
              <p>
                <strong>MedPredict AI</strong> is an enterprise clinical decision-support system designed to augment physician risk estimation across 10 core disease pathways.
              </p>
              <div className="p-3 bg-ivory rounded-btn border border-borderLine space-y-1.5">
                <div className="font-semibold text-navy-800">Medical Safety & Advisory Notice:</div>
                <p className="text-[11px] text-slateText">
                  All predictive outputs, risk intervals (Low &lt; 0.35, Moderate 0.35–0.65, High &gt; 0.65), and SHAP feature attributions are statistical estimates. They do not constitute autonomous diagnostic verification. Clinical judgment by a licensed healthcare practitioner is mandatory.
                </p>
              </div>
              <p className="text-[11px] text-slateText">
                For questions regarding calibration metrics, drift telemetry, or institutional EHR integration (HL7 FHIR / Epic), contact the Clinical Informatics department.
              </p>
            </div>
            <div className="pt-2 flex justify-end">
              <button
                onClick={() => setShowHelp(false)}
                className="px-4 py-2 bg-navy-800 hover:bg-navy-700 text-ivory text-xs font-medium rounded-btn transition"
              >
                Acknowledge & Close
              </button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};
