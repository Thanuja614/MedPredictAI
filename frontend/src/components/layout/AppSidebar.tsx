/**
 * MedPredict AI — Role-Adaptive Application Sidebar
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  ClipboardList,
  History,
  Users,
  FileText,
  Activity,
  Cpu,
  BarChart3,
  Sliders,
  Settings,
  ShieldCheck,
  Zap,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const AppSidebar: React.FC = () => {
  const { activeRole } = useAuth();

  // Route definitions by role
  const patientNav = [
    { to: '/', label: 'My Health Dashboard', icon: LayoutDashboard },
    { to: '/assessment', label: 'Start Health Assessment', icon: ClipboardList },
    { to: '/history', label: 'Past Assessments', icon: History },
  ];

  const doctorNav = [
    { to: '/', label: 'Clinical Overview', icon: LayoutDashboard },
    { to: '/clinician/patients', label: 'Patient Directory', icon: Users },
    { to: '/assessment', label: 'Diagnostic Assessment', icon: Activity },
    { to: '/clinician/reports', label: 'Clinical Reports', icon: FileText },
  ];

  const dataScientistNav = [
    { to: '/', label: 'Platform Summary', icon: LayoutDashboard },
    { to: '/workbench', label: '10 Disease Modules', icon: Cpu },
    { to: '/workbench/drift', label: 'Drift & Fairness Monitor', icon: BarChart3 },
    { to: '/workbench/governance', label: 'Model Registry Lifecycle', icon: Sliders },
  ];

  const adminNav = [
    { to: '/', label: 'Command Center', icon: LayoutDashboard },
    { to: '/admin/users', label: 'User & Role Access', icon: Users },
    { to: '/admin/settings', label: 'System Configurations', icon: Settings },
    { to: '/admin/jobs', label: 'Background Tasks', icon: Zap },
    { to: '/admin/audit', label: 'HIPAA Audit Trail', icon: ShieldCheck },
  ];

  let currentNav = patientNav;
  if (activeRole === 'doctor') currentNav = doctorNav;
  else if (activeRole === 'data_scientist') currentNav = dataScientistNav;
  else if (activeRole === 'admin') currentNav = adminNav;

  return (
    <aside className="w-64 bg-white border-r border-slate-200 min-h-[calc(100vh-4rem)] p-4 flex flex-col justify-between hidden md:flex">
      <div className="space-y-6">
        <div>
          <div className="px-3 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
            Navigation Menu
          </div>
          <nav className="space-y-1">
            {currentNav.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  className={({ isActive }) =>
                    `flex items-center space-x-3 px-3 py-2 text-sm font-medium rounded-lg transition ${
                      isActive
                        ? 'bg-sky-50 text-sky-700 font-semibold border-r-2 border-sky-600'
                        : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
                    }`
                  }
                >
                  <Icon className="w-4 h-4 text-slate-500" />
                  <span>{item.label}</span>
                </NavLink>
              );
            })}
          </nav>
        </div>
      </div>

      <div className="p-3 bg-slate-50 rounded-xl border border-slate-200/80 text-xs text-slate-600">
        <div className="flex items-center space-x-2 font-semibold text-slate-800">
          <Activity className="w-4 h-4 text-sky-600" />
          <span>Local Engine Active</span>
        </div>
        <p className="mt-1 text-[11px] text-slate-500">
          FastAPI Backend & SQLite / PostgreSQL Local Stack.
        </p>
      </div>
    </aside>
  );
};
