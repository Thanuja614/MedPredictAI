/**
 * MedPredict AI — Master Top Clinical Navigation Bar
 * Realistic Hospital EHR Top Navigation (Epic/Cerner style)
 * Tier 1: Hospital Header & Utility Bar (System, Search, Ward Telemetry, Doctor Profile)
 * Tier 2: Horizontal Clinical Navigation Tabs (Dashboard, Patients, Prediction, Reports, Analytics, History, Alerts, Settings)
 */

import React, { useState } from 'react';
import { NavLink, Link, useLocation, useNavigate } from 'react-router-dom';
import {
  LayoutDashboard,
  Users,
  Activity,
  FileText,
  BarChart3,
  History,
  Bell,
  Settings,
  Search,
  HelpCircle,
  Stethoscope,
  ShieldCheck,
  AlertTriangle,
  LogOut,
  X,
  Clock,
  HeartPulse,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const AppNavbar: React.FC = () => {
  const { user, logout } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  const [showNotifs, setShowNotifs] = useState(false);
  const [showHelp, setShowHelp] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const navItems = [
    { to: '/', label: 'Clinical Dashboard', icon: LayoutDashboard, badge: undefined },
    { to: '/patients', label: 'Patient Records', icon: Users, badge: '1,248' },
    { to: '/prediction', label: 'Risk Prediction', icon: Activity, badge: '10 Models' },
    { to: '/reports', label: 'Medical Reports', icon: FileText, badge: undefined },
    { to: '/analytics', label: 'Analytics & Trends', icon: BarChart3, badge: undefined },
    { to: '/history', label: 'Prediction History', icon: History, badge: undefined },
    { to: '/notifications', label: 'Clinical Alerts', icon: Bell, badge: '3 New' },
    { to: '/settings', label: 'System Settings', icon: Settings, badge: undefined },
  ];

  const handleSignOut = () => {
    logout();
    navigate('/login');
  };

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/patients?search=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  const displayName = user 
    ? `${user.first_name} ${user.last_name}` 
    : 'Dr. Sarah Mitchell, MD';
  
  const displayRole = user?.roles?.[0]?.name 
    ? user.roles[0].name.toUpperCase() 
    : 'CHIEF OF CARDIOLOGY';

  const demoNotifs = [
    {
      id: '1',
      title: 'Critical Lab Alert: Troponin I Elevated',
      message: 'Marcus Vance (MP-2026-00912) recorded Troponin I at 0.42 ng/mL. Cardiology consult advised.',
      time: '12 min ago',
      urgent: true,
    },
    {
      id: '2',
      title: 'Risk Velocity Escalation: Ananya Rao',
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

  return (
    <header className="sticky top-0 z-40 w-full shadow-subtle select-none">
      {/* Tier 1: Hospital Header & Utility Bar (Authentic Clinical Slate Navy) */}
      <div className="bg-slate-900 border-b border-slate-800 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-12 flex items-center justify-between gap-3">
          {/* Left: Hospital Cross + Brand + Ward */}
          <div className="flex items-center space-x-3 shrink-0">
            <Link to="/" className="flex items-center space-x-2.5">
              <div className="w-7 h-7 rounded bg-sky-600 flex items-center justify-center text-white shadow-xs">
                <Activity className="w-4 h-4" />
              </div>
              <div className="flex items-baseline space-x-1.5">
                <span className="font-bold text-sm text-white tracking-tight">
                  MedPredict<span className="text-sky-400 font-semibold">AI</span>
                </span>
                <span className="hidden xl:inline text-[11px] text-slate-400 font-normal">
                  | Decision Support
                </span>
              </div>
            </Link>

            <div className="hidden sm:block h-4 w-px bg-slate-700" />

            {/* Institutional Ward Badge */}
            <div className="hidden sm:flex items-center space-x-2 px-2.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300 text-xs font-medium">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              <span className="text-[11px] font-semibold tracking-wide text-slate-200">
                St. Jude Medical Center
              </span>
              <span className="text-[10px] text-sky-400 font-mono pl-1 border-l border-slate-700">
                Ward 4B ICU
              </span>
            </div>
          </div>

          {/* Center: Global Patient / MRN Search Bar */}
          <form onSubmit={handleSearchSubmit} className="relative hidden md:block max-w-sm w-full">
            <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search Patient Name, MRN (e.g. MP-2026-01482)..."
              className="w-full pl-8 pr-3 py-1 text-xs bg-slate-800/90 border border-slate-700 rounded text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-sky-500 focus:bg-slate-800 transition"
            />
          </form>

          {/* Right: Actions, Alerts, Doctor Profile */}
          <div className="flex items-center space-x-3 shrink-0">
            {/* Inference Engine Status */}
            <div className="hidden lg:flex items-center space-x-1.5 text-[11px] text-slate-300 px-2 py-0.5 rounded bg-slate-800/60 border border-slate-700/60">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
              <span className="font-mono text-[10px]">10 Engines Active</span>
            </div>

            {/* Clinical Notifications Bell */}
            <div className="relative">
              <button
                onClick={() => setShowNotifs(!showNotifs)}
                className="p-1.5 text-slate-300 hover:text-white hover:bg-slate-800 rounded relative transition"
                title="Clinical Alerts & Notifications"
              >
                <Bell className="w-4 h-4" />
                <span className="absolute top-1 right-1 w-2 h-2 bg-rose-500 rounded-full ring-2 ring-slate-900 animate-pulse" />
              </button>

              {/* Notification Dropdown */}
              {showNotifs && (
                <div className="absolute right-0 mt-2 w-80 bg-white border border-slate-200 rounded-lg shadow-elevated z-50 overflow-hidden text-slate-900">
                  <div className="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <AlertTriangle className="w-4 h-4 text-amber-600" />
                      <span className="text-xs font-bold text-slate-900 tracking-wide font-mono">
                        Clinical Alerts (3)
                      </span>
                    </div>
                    <Link
                      to="/notifications"
                      onClick={() => setShowNotifs(false)}
                      className="text-[11px] text-sky-600 hover:underline font-semibold"
                    >
                      View All
                    </Link>
                  </div>
                  <div className="max-h-80 overflow-y-auto divide-y divide-slate-100">
                    {demoNotifs.map((n) => (
                      <div
                        key={n.id}
                        className={`p-3 text-xs hover:bg-slate-50 transition cursor-pointer ${
                          n.urgent ? 'bg-rose-50/60' : 'bg-white'
                        }`}
                        onClick={() => {
                          setShowNotifs(false);
                          navigate('/notifications');
                        }}
                      >
                        <div className="flex items-center justify-between">
                          <span className={`font-semibold ${n.urgent ? 'text-rose-700' : 'text-slate-900'}`}>
                            {n.title}
                          </span>
                          <span className="text-[10px] text-slate-500 font-mono">{n.time}</span>
                        </div>
                        <p className="text-slate-600 text-[11px] mt-1 leading-snug">{n.message}</p>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Protocol Guide Button */}
            <button
              onClick={() => setShowHelp(true)}
              className="p-1.5 text-slate-300 hover:text-white hover:bg-slate-800 rounded transition"
              title="Clinical Protocol Guide"
            >
              <HelpCircle className="w-4 h-4" />
            </button>

            {/* Doctor Profile Pill */}
            <div className="flex items-center space-x-2 pl-2 border-l border-slate-700">
              <div className="w-6 h-6 rounded bg-sky-700 text-white text-[11px] font-bold flex items-center justify-center">
                SM
              </div>
              <div className="hidden sm:block text-left leading-none">
                <span className="text-xs font-semibold text-white block">Dr. S. Mitchell</span>
                <span className="text-[10px] text-slate-400 font-medium">Attending MD</span>
              </div>
            </div>

            {/* Sign Out Button */}
            <button
              onClick={handleSignOut}
              className="p-1.5 text-slate-400 hover:text-rose-400 hover:bg-slate-800 rounded transition"
              title="Sign Out"
            >
              <LogOut className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>

      {/* Tier 2: Horizontal Clinical Navigation Tabs (Clean Hospital White Bar) */}
      <div className="bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between overflow-x-auto scrollbar-none">
          <nav className="flex items-center space-x-1 min-w-max py-0.5">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  className={({ isActive }) =>
                    `flex items-center space-x-2 px-3 py-2 text-xs font-medium border-b-2 transition-all duration-150 ${
                      isActive
                        ? 'border-sky-600 text-sky-700 bg-sky-50/60 font-semibold rounded-t'
                        : 'border-transparent text-slate-600 hover:text-slate-900 hover:bg-slate-50 rounded-t'
                    }`
                  }
                >
                  <Icon className="w-3.5 h-3.5 opacity-80" />
                  <span>{item.label}</span>
                  {item.badge && (
                    <span
                      className={`text-[10px] font-bold px-1.5 py-0.2 rounded-full ${
                        item.badge.includes('New')
                          ? 'bg-rose-100 text-rose-700'
                          : 'bg-slate-100 text-slate-600'
                      }`}
                    >
                      {item.badge}
                    </span>
                  )}
                </NavLink>
              );
            })}
          </nav>

          {/* Right Status / Telemetry Indicator */}
          <div className="hidden lg:flex items-center space-x-2 text-xs text-slate-500 font-mono py-1 pl-4 shrink-0">
            <Clock className="w-3.5 h-3.5 text-emerald-600" />
            <span className="text-[11px]">HL7 FHIR v4.0 Active</span>
          </div>
        </div>
      </div>

      {/* Help Modal */}
      {showHelp && (
        <div className="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-lg border border-slate-200 max-w-lg w-full p-6 shadow-elevated space-y-4 text-slate-900">
            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
              <div className="flex items-center space-x-2.5">
                <Stethoscope className="w-5 h-5 text-sky-600" />
                <h3 className="text-base font-bold text-slate-900">
                  Clinical Decision Support Protocol Guide
                </h3>
              </div>
              <button
                onClick={() => setShowHelp(false)}
                className="text-slate-400 hover:text-slate-700 p-1 rounded"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <div className="text-xs text-slate-700 space-y-3 leading-relaxed">
              <p>
                <strong>MedPredict AI</strong> is an enterprise clinical decision-support system designed to augment physician risk estimation across 10 core disease pathways.
              </p>
              <div className="p-3 bg-slate-50 rounded border border-slate-200 space-y-1.5">
                <div className="font-semibold text-slate-900">Medical Safety & Advisory Notice:</div>
                <p className="text-[11px] text-slate-600 leading-normal">
                  All predictive outputs, risk intervals (Low &lt; 0.35, Moderate 0.35–0.65, High &gt; 0.65), and SHAP feature attributions are statistical estimates calibrated against AHA/ACC & KDIGO guidelines. They do not constitute autonomous diagnostic verification. Clinical judgment by a licensed healthcare practitioner is mandatory.
                </p>
              </div>
              <p className="text-[11px] text-slate-500">
                For questions regarding calibration metrics, drift telemetry, or institutional EHR integration (HL7 FHIR / Epic), contact Clinical Informatics.
              </p>
            </div>
            <div className="pt-2 flex justify-end">
              <button
                onClick={() => setShowHelp(false)}
                className="px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold rounded transition"
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

export default AppNavbar;
