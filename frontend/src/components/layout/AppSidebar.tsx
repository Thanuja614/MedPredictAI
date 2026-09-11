/**
 * MedPredict AI — High-End Clinical Desktop Sidebar
 * Deep Navy (#16324F), gold/ivory accents, clean typography, medical navigation
 */

import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import {
  LayoutDashboard,
  Users,
  Activity,
  FileText,
  BarChart3,
  History,
  Bell,
  Settings,
  ShieldCheck,
  LogOut,
  Stethoscope,
  HeartPulse,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const AppSidebar: React.FC = () => {
  const { user, activeRole, logout } = useAuth();
  const navigate = useNavigate();

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

  const displayName = user 
    ? `${user.first_name} ${user.last_name}` 
    : 'Dr. Sarah Mitchell, MD';
  
  const displayRole = user?.roles?.[0]?.name 
    ? user.roles[0].name.toUpperCase() 
    : 'CHIEF OF CARDIOLOGY';

  return (
    <aside className="w-68 bg-navy-800 text-ivory border-r border-navy-900/60 min-h-[calc(100vh-4rem)] p-4 flex flex-col justify-between hidden md:flex shrink-0 shadow-xl select-none">
      <div className="space-y-6">
        {/* Hospital Division Sub-badge */}
        <div className="px-3 py-2 bg-navy-900/50 rounded-lg border border-white/5 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span className="text-[11px] font-semibold text-slate-300 tracking-wide uppercase">
              St. Jude Medical Center
            </span>
          </div>
          <span className="text-[10px] font-bold text-teal px-1.5 py-0.5 bg-teal/10 rounded border border-teal/20">
            Ward 4B
          </span>
        </div>

        {/* Primary Navigation */}
        <div>
          <div className="px-3 text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-2 font-mono">
            Clinical Navigation
          </div>
          <nav className="space-y-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  className={({ isActive }) =>
                    `flex items-center justify-between px-3 py-2.5 text-xs font-medium rounded-lg transition-all duration-150 ${
                      isActive
                        ? 'bg-medblue text-white font-semibold shadow-md shadow-navy-900/30 border-l-3 border-teal'
                        : 'text-slate-300 hover:text-white hover:bg-navy-700/60'
                    }`
                  }
                >
                  <div className="flex items-center space-x-3">
                    <Icon className="w-4 h-4 opacity-80" />
                    <span>{item.label}</span>
                  </div>
                  {item.badge && (
                    <span className="text-[10px] font-semibold px-1.5 py-0.5 rounded bg-white/10 text-slate-200">
                      {item.badge}
                    </span>
                  )}
                </NavLink>
              );
            })}
          </nav>
        </div>

        {/* Clinical Decision Support Status Box */}
        <div className="p-3 bg-navy-900/60 rounded-xl border border-white/5 text-xs text-slate-300 space-y-2">
          <div className="flex items-center space-x-2 text-sage font-semibold">
            <HeartPulse className="w-4 h-4" />
            <span>Inference Engine v2.3</span>
          </div>
          <p className="text-[11px] text-slate-400 leading-relaxed">
            10 disease prediction algorithms calibrated against AHA/ACC & KDIGO guidelines.
          </p>
          <div className="flex items-center space-x-2 text-[10px] text-teal pt-1 border-t border-white/5">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>HIPAA Audit Trail Active</span>
          </div>
        </div>
      </div>

      {/* User Profile & Role Footer */}
      <div className="pt-4 border-t border-white/10 flex items-center justify-between">
        <div className="flex items-center space-x-2.5 min-w-0">
          <div className="w-8 h-8 rounded-full bg-medblue flex items-center justify-center text-white text-xs font-bold ring-2 ring-white/10 shrink-0">
            <Stethoscope className="w-4 h-4" />
          </div>
          <div className="min-w-0">
            <p className="text-xs font-semibold text-white truncate">{displayName}</p>
            <p className="text-[10px] text-slate-400 truncate">{displayRole}</p>
          </div>
        </div>
        <button
          onClick={handleSignOut}
          className="p-1.5 text-slate-400 hover:text-rose-400 hover:bg-white/5 rounded-md transition"
          title="Sign Out of Terminal"
        >
          <LogOut className="w-4 h-4" />
        </button>
      </div>
    </aside>
  );
};
