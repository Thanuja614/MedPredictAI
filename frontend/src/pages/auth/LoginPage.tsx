/**
 * MedPredict AI — Clinical Portal Login Page
 */

import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Activity, Lock, Mail, AlertCircle, Sparkles } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { MedicalDisclaimerBanner } from '../../components/common/MedicalDisclaimerBanner';

export const LoginPage: React.FC = () => {
  const { login, setActiveRole } = useAuth();
  const navigate = useNavigate();

  const [email, setEmail] = useState('admin@medpredict.local');
  const [password, setPassword] = useState('AdminSecurePass123!');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await login(email, password);
      navigate('/');
    } catch (err: any) {
      setError(
        err.response?.data?.error?.message ||
          'Failed to sign in. Please verify your email and password.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDemoPreset = (presetEmail: string, presetRole: string) => {
    setEmail(presetEmail);
    setPassword('AdminSecurePass123!');
    setActiveRole(presetRole);
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
        <div className="inline-flex w-12 h-12 rounded-2xl bg-sky-600 items-center justify-center text-white shadow-lg shadow-sky-600/30 mb-4">
          <Activity className="w-7 h-7" />
        </div>
        <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight">
          MedPredict<span className="text-sky-600">.AI</span>
        </h2>
        <p className="mt-2 text-sm text-slate-600">
          Intelligent Multi-Disease Risk Prediction & Clinical Analytics
        </p>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md px-4">
        {/* Medical disclaimer note */}
        <MedicalDisclaimerBanner compact />

        <div className="bg-white py-8 px-6 shadow-md rounded-2xl border border-slate-200 sm:px-10 mt-4">
          {error && (
            <div className="mb-4 p-3 bg-rose-50 border border-rose-200 text-rose-700 text-xs rounded-lg flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 uppercase tracking-wide">
                Email Address
              </label>
              <div className="mt-1 relative rounded-md shadow-xs">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                  <Mail className="w-4 h-4" />
                </div>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="block w-full pl-9 pr-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-hidden focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                  placeholder="doctor@medpredict.local"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 uppercase tracking-wide">
                Password
              </label>
              <div className="mt-1 relative rounded-md shadow-xs">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full pl-9 pr-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-hidden focus:ring-2 focus:ring-sky-500 focus:border-sky-500"
                  placeholder="••••••••••••"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-2 flex justify-center py-2.5 px-4 border border-transparent rounded-lg shadow-sm text-sm font-semibold text-white bg-sky-600 hover:bg-sky-700 focus:outline-hidden focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition disabled:opacity-50"
            >
              {loading ? 'Authenticating...' : 'Sign In'}
            </button>
          </form>

          {/* Quick Demo Role Selector */}
          <div className="mt-6 pt-5 border-t border-slate-200">
            <div className="flex items-center space-x-1 text-xs font-bold text-slate-500 uppercase tracking-wider mb-2.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              <span>Instant Demo Role Presets:</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => handleDemoPreset('admin@medpredict.local', 'admin')}
                className="text-left p-2 rounded-lg border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 transition text-xs"
              >
                <div className="font-semibold text-slate-800">Administrator</div>
                <div className="text-[10px] text-slate-500">System & Governance</div>
              </button>
              <button
                type="button"
                onClick={() => handleDemoPreset('doctor@medpredict.local', 'doctor')}
                className="text-left p-2 rounded-lg border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 transition text-xs"
              >
                <div className="font-semibold text-slate-800">Clinician / Doctor</div>
                <div className="text-[10px] text-slate-500">Diagnostic Console</div>
              </button>
              <button
                type="button"
                onClick={() => handleDemoPreset('datascientist@medpredict.local', 'data_scientist')}
                className="text-left p-2 rounded-lg border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 transition text-xs"
              >
                <div className="font-semibold text-slate-800">Data Scientist</div>
                <div className="text-[10px] text-slate-500">ML Model Workbench</div>
              </button>
              <button
                type="button"
                onClick={() => handleDemoPreset('patient@medpredict.local', 'patient')}
                className="text-left p-2 rounded-lg border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 transition text-xs"
              >
                <div className="font-semibold text-slate-800">Patient</div>
                <div className="text-[10px] text-slate-500">Health Screening</div>
              </button>
            </div>
          </div>
        </div>

        <div className="text-center mt-4 text-xs text-slate-500">
          New to the platform?{' '}
          <Link to="/register" className="text-sky-600 hover:text-sky-800 font-semibold">
            Create an account
          </Link>
        </div>
      </div>
    </div>
  );
};
