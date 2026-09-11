/**
 * MedPredict AI — Enterprise Medical Login Screen
 * Section 17: Split-screen realistic hospital atmosphere, deep navy & ivory aesthetics,
 * 1-click clinical role presets, institutional compliance statement.
 */

import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import {
  Activity,
  Lock,
  Mail,
  ArrowRight,
  ShieldCheck,
  Stethoscope,
  User,
  Database,
  Building2,
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const { setActiveRole } = useAuth();

  const [email, setEmail] = useState<string>('sarah.mitchell@stjude-medical.org');
  const [password, setPassword] = useState<string>('••••••••••••');
  const [rememberMe, setRememberMe] = useState<boolean>(true);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
      navigate('/');
    }, 400);
  };

  const handleQuickRole = (roleKey: string, demoEmail: string) => {
    setActiveRole(roleKey);
    setEmail(demoEmail);
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-[#F7F5EF] flex items-center justify-center p-4 lg:p-8">
      <div className="max-w-5xl w-full bg-surface rounded-card border border-borderLine shadow-elevated overflow-hidden grid grid-cols-1 lg:grid-cols-12 min-h-[600px]">
        {/* Left Side: Realistic Healthcare Atmosphere & Institutional Heritage (5 Cols) */}
        <div className="lg:col-span-5 bg-navy-800 text-ivory p-8 lg:p-10 flex flex-col justify-between relative overflow-hidden">
          {/* Subtle medical grid & abstract lighting */}
          <div className="absolute inset-0 bg-medical-grid opacity-30 pointer-events-none" />
          <div className="absolute -top-24 -right-24 w-72 h-72 rounded-full bg-medblue/20 blur-3xl pointer-events-none" />
          <div className="absolute -bottom-24 -left-24 w-72 h-72 rounded-full bg-teal/20 blur-3xl pointer-events-none" />

          {/* Top Institutional Header */}
          <div className="relative z-10 space-y-3">
            <div className="flex items-center space-x-2.5">
              <div className="w-9 h-9 rounded-lg bg-medblue flex items-center justify-center text-ivory shadow-md">
                <Activity className="w-5 h-5 text-teal" />
              </div>
              <span className="font-extrabold text-lg tracking-tight">
                MedPredict<span className="text-teal font-serif italic text-xl">AI</span>
              </span>
            </div>
            <div className="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full bg-navy-900/60 text-slate-300 text-[10px] font-mono border border-white/10">
              <Building2 className="w-3 h-3 text-teal" />
              <span>St. Jude Clinical Decision Portal</span>
            </div>
          </div>

          {/* Middle Classic Statement */}
          <div className="relative z-10 my-8 space-y-4">
            <h2 className="font-serif text-2xl lg:text-3xl font-normal text-ivory leading-snug">
              &ldquo;Intelligent Healthcare, <br />
              <span className="italic font-medium text-teal">Designed Around You.</span>&rdquo;
            </h2>
            <p className="text-xs text-slate-300 leading-relaxed max-w-sm">
              Bridging modern machine learning and evidence-based medicine to provide validated, calibrated multi-disease risk predictions for physician decision-support.
            </p>
          </div>

          {/* Bottom Security / Trust Seal */}
          <div className="relative z-10 pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-slate-400">
            <div className="flex items-center space-x-1.5">
              <ShieldCheck className="w-4 h-4 text-sage" />
              <span>HIPAA Security Certified</span>
            </div>
            <span>TLS 1.3 Encrypted</span>
          </div>
        </div>

        {/* Right Side: Clean Enterprise Sign-In Form (7 Cols) */}
        <div className="lg:col-span-7 p-8 lg:p-12 flex flex-col justify-between space-y-8 bg-surface">
          <div>
            <div className="space-y-1">
              <h3 className="text-xl font-bold text-slate-900">
                Sign In to Clinical Terminal
              </h3>
              <p className="text-xs text-slateText">
                Enter your institutional credentials to access electronic health records and prediction engines.
              </p>
            </div>

            {/* Quick Demo Role Presets */}
            <div className="mt-5 p-3 bg-ivory rounded-btn border border-borderLine space-y-2">
              <span className="text-[10px] font-mono uppercase font-bold text-slateText block">
                Instant Demo Role Presets:
              </span>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
                <button
                  type="button"
                  onClick={() => handleQuickRole('doctor', 'dr.mitchell@stjude-medical.org')}
                  className="p-2 bg-surface hover:bg-medblue-light text-navy-800 rounded-btn border border-borderLine font-medium flex items-center space-x-1.5 transition text-left"
                >
                  <Stethoscope className="w-3.5 h-3.5 text-medblue shrink-0" />
                  <span className="truncate">Attending Doctor</span>
                </button>
                <button
                  type="button"
                  onClick={() => handleQuickRole('patient', 'ananya.rao@patient-portal.org')}
                  className="p-2 bg-surface hover:bg-medblue-light text-navy-800 rounded-btn border border-borderLine font-medium flex items-center space-x-1.5 transition text-left"
                >
                  <User className="w-3.5 h-3.5 text-sage shrink-0" />
                  <span className="truncate">Patient Portal</span>
                </button>
                <button
                  type="button"
                  onClick={() => handleQuickRole('data_scientist', 'mlops.vance@medpredict.ai')}
                  className="p-2 bg-surface hover:bg-medblue-light text-navy-800 rounded-btn border border-borderLine font-medium flex items-center space-x-1.5 transition text-left col-span-2 sm:col-span-1"
                >
                  <Database className="w-3.5 h-3.5 text-teal shrink-0" />
                  <span className="truncate">Data Scientist</span>
                </button>
              </div>
            </div>

            {/* Sign In Form */}
            <form onSubmit={handleSubmit} className="mt-6 space-y-4 text-xs">
              <div>
                <label className="block text-slateText font-medium mb-1">
                  Institutional Email / Identity
                </label>
                <div className="relative">
                  <Mail className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slateText" />
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    className="w-full pl-9 pr-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal focus:ring-1 focus:ring-medblue focus:bg-white transition font-sans"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between mb-1">
                  <label className="text-slateText font-medium">Passcode / Token</label>
                  <a href="#" className="text-medblue hover:underline text-[11px]">
                    Forgot passcode?
                  </a>
                </div>
                <div className="relative">
                  <Lock className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slateText" />
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    className="w-full pl-9 pr-3 py-2 bg-ivory border border-borderLine rounded-btn text-charcoal focus:ring-1 focus:ring-medblue focus:bg-white transition"
                  />
                </div>
              </div>

              <div className="flex items-center justify-between pt-1">
                <label className="flex items-center space-x-2 text-slateText cursor-pointer">
                  <input
                    type="checkbox"
                    checked={rememberMe}
                    onChange={(e) => setRememberMe(e.target.checked)}
                    className="rounded text-medblue focus:ring-medblue"
                  />
                  <span>Keep terminal session authenticated</span>
                </label>
              </div>

              <button
                type="submit"
                disabled={isLoading}
                className="w-full py-2.5 bg-navy-800 hover:bg-navy-700 text-ivory font-semibold rounded-btn shadow-md shadow-navy-900/20 flex items-center justify-center space-x-2 transition disabled:opacity-50 mt-2"
              >
                <span>{isLoading ? 'Verifying Credentials...' : 'Sign In to Portal'}</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </form>
          </div>

          <div className="text-[11px] text-slateText border-t border-borderLine/50 pt-4 flex items-center justify-between">
            <span>Hospital Terminal System v2.3.0</span>
            <span className="font-mono">Local Stack Connected</span>
          </div>
        </div>
      </div>
    </div>
  );
};
