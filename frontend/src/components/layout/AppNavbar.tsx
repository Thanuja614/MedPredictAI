/**
 * MedPredict AI — Application Top Navigation Bar
 */

import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Activity,
  Bell,
  LogOut,
  User as UserIcon,
  Shield,
  Stethoscope,
  Database,
  CheckCircle2,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { api } from '../../services/api';
import { InAppNotification } from '../../types';

export const AppNavbar: React.FC = () => {
  const { user, activeRole, setActiveRole, logout } = useAuth();
  const navigate = useNavigate();
  const [notifications, setNotifications] = useState<InAppNotification[]>([]);
  const [showNotifs, setShowNotifs] = useState(false);

  const fetchNotifs = async () => {
    if (user) {
      try {
        const notifs = await api.notifications.list(false);
        setNotifications(notifs);
      } catch (e) {
        // quiet fallback
      }
    }
  };

  useEffect(() => {
    fetchNotifs();
  }, [user]);

  const unreadCount = notifications.filter((n) => !n.is_read).length;

  const handleMarkAllRead = async () => {
    try {
      await api.notifications.markAllRead();
      setNotifications((prev) => prev.map((n) => ({ ...n, is_read: true })));
    } catch (e) {
      console.error(e);
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const rolesList = [
    { key: 'patient', label: 'Patient Portal', icon: UserIcon },
    { key: 'doctor', label: 'Clinician Console', icon: Stethoscope },
    { key: 'data_scientist', label: 'ML Workbench', icon: Database },
    { key: 'admin', label: 'Admin Governance', icon: Shield },
  ];

  return (
    <header className="sticky top-0 z-40 bg-white border-b border-slate-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center space-x-3">
          <Link to="/" className="flex items-center space-x-2.5">
            <div className="w-9 h-9 rounded-xl bg-sky-600 flex items-center justify-center text-white shadow-md shadow-sky-600/30">
              <Activity className="w-5 h-5 animate-pulse" />
            </div>
            <div>
              <span className="font-extrabold text-lg text-slate-900 tracking-tight">
                MedPredict<span className="text-sky-600">.AI</span>
              </span>
              <span className="hidden sm:inline-block ml-2 px-1.5 py-0.5 text-[10px] font-semibold bg-slate-100 text-slate-600 rounded border border-slate-200 uppercase tracking-wider">
                Clinical v1.0
              </span>
            </div>
          </Link>
        </div>

        {/* Center: Role Switcher */}
        <div className="flex items-center space-x-1 sm:space-x-2">
          <span className="text-xs font-medium text-slate-500 hidden md:inline">
            Active Role:
          </span>
          <div className="flex bg-slate-100 p-1 rounded-lg border border-slate-200">
            {rolesList.map((r) => {
              const Icon = r.icon;
              const isSelected = activeRole === r.key;
              return (
                <button
                  key={r.key}
                  onClick={() => setActiveRole(r.key)}
                  className={`flex items-center space-x-1.5 px-2.5 py-1 text-xs font-semibold rounded-md transition ${
                    isSelected
                      ? 'bg-white text-sky-700 shadow-xs border border-slate-200/60'
                      : 'text-slate-600 hover:text-slate-900 hover:bg-slate-200/50'
                  }`}
                  title={`Switch to ${r.label}`}
                >
                  <Icon className="w-3.5 h-3.5" />
                  <span className="hidden lg:inline">{r.label}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Right Section: Notifications & User */}
        <div className="flex items-center space-x-3">
          {/* Notification Bell */}
          <div className="relative">
            <button
              onClick={() => setShowNotifs(!showNotifs)}
              className="p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg relative transition"
              aria-label="Notifications"
            >
              <Bell className="w-5 h-5" />
              {unreadCount > 0 && (
                <span className="absolute top-1.5 right-1.5 w-4 h-4 text-[10px] font-bold bg-rose-600 text-white rounded-full flex items-center justify-center ring-2 ring-white">
                  {unreadCount}
                </span>
              )}
            </button>

            {/* Notification Dropdown */}
            {showNotifs && (
              <div className="absolute right-0 mt-2 w-80 bg-white border border-slate-200 rounded-xl shadow-xl z-50 overflow-hidden">
                <div className="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                    Alerts & Notifications
                  </span>
                  {unreadCount > 0 && (
                    <button
                      onClick={handleMarkAllRead}
                      className="text-[11px] text-sky-600 hover:text-sky-800 font-medium flex items-center space-x-1"
                    >
                      <CheckCircle2 className="w-3 h-3" />
                      <span>Mark all read</span>
                    </button>
                  )}
                </div>
                <div className="max-h-72 overflow-y-auto divide-y divide-slate-100">
                  {notifications.length === 0 ? (
                    <div className="p-4 text-center text-xs text-slate-500">
                      No notifications at this time.
                    </div>
                  ) : (
                    notifications.map((n) => (
                      <div
                        key={n.id}
                        className={`p-3 text-xs ${
                          n.is_read ? 'bg-white' : 'bg-sky-50/50'
                        } hover:bg-slate-50`}
                      >
                        <div className="font-semibold text-slate-800">{n.title}</div>
                        <div className="text-slate-600 mt-0.5">{n.message}</div>
                        <div className="text-[10px] text-slate-400 mt-1">
                          {new Date(n.created_at).toLocaleTimeString()}
                        </div>
                      </div>
                    ))
                  )}
                </div>
              </div>
            )}
          </div>

          {/* User Account Info */}
          {user ? (
            <div className="flex items-center space-x-3 border-l border-slate-200 pl-3">
              <div className="hidden sm:block text-right">
                <div className="text-xs font-bold text-slate-900">
                  {user.first_name} {user.last_name}
                </div>
                <div className="text-[11px] text-slate-500 capitalize">{activeRole}</div>
              </div>
              <button
                onClick={handleLogout}
                className="p-2 text-slate-500 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition"
                title="Sign out"
              >
                <LogOut className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <Link
              to="/login"
              className="text-xs font-semibold px-3 py-1.5 bg-sky-600 hover:bg-sky-700 text-white rounded-lg transition"
            >
              Sign In
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};
