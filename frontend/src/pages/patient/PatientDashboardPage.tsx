/**
 * MedPredict AI — Patient Health Dashboard
 */

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  Activity,
  Heart,
  Droplet,
  Brain,
  ShieldAlert,
  ClipboardList,
  ChevronRight,
  TrendingUp,
  FileText,
  AlertTriangle,
  Sparkles,
} from 'lucide-react';
import { MedicalDisclaimerBanner } from '../../components/common/MedicalDisclaimerBanner';
import { api } from '../../services/api';
import { DiseaseCatalogItem, PredictionResult } from '../../types';

export const PatientDashboardPage: React.FC = () => {
  const [diseases, setDiseases] = useState<DiseaseCatalogItem[]>([]);
  const [history, setHistory] = useState<PredictionResult[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [diseasesList, preds] = await Promise.all([
          api.diseases.list(),
          api.predictions.getHistory(),
        ]);
        setDiseases(diseasesList);
        setHistory(preds);
      } catch (err) {
        console.error('Failed to load dashboard data', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const getDiseaseIcon = (slug: string) => {
    switch (slug) {
      case 'heart':
      case 'hypertension':
        return Heart;
      case 'diabetes':
      case 'anemia':
        return Droplet;
      case 'stroke':
      case 'parkinsons':
        return Brain;
      default:
        return Activity;
    }
  };

  const getRiskBadge = (level: string) => {
    if (level === 'HIGH') {
      return (
        <span className="px-2.5 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-700 border border-rose-200">
          HIGH RISK
        </span>
      );
    }
    if (level === 'MODERATE') {
      return (
        <span className="px-2.5 py-1 text-xs font-bold rounded-full bg-amber-100 text-amber-800 border border-amber-200">
          MODERATE RISK
        </span>
      );
    }
    return (
      <span className="px-2.5 py-1 text-xs font-bold rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200">
        LOW RISK
      </span>
    );
  };

  return (
    <div className="space-y-6">
      {/* Mandatory Regulatory Safety Disclaimer */}
      <MedicalDisclaimerBanner />

      {/* Hero Header */}
      <div className="bg-gradient-to-r from-sky-700 to-indigo-800 rounded-2xl p-6 sm:p-8 text-white shadow-lg shadow-sky-900/10">
        <div className="max-w-2xl">
          <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-white/10 text-sky-100 text-xs font-semibold backdrop-blur-xs mb-3">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            <span>Intelligent Predictive Health Platform</span>
          </span>
          <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
            Preventative Multi-Disease Health Screening
          </h1>
          <p className="mt-2 text-sky-100 text-sm sm:text-base leading-relaxed">
            Assess clinical health risks early across 10 specialized conditions using calibrated machine learning models and interpretable SHAP explainability.
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            <Link
              to="/assessment"
              className="px-5 py-2.5 bg-white text-sky-800 font-bold rounded-xl shadow hover:bg-sky-50 transition text-sm flex items-center space-x-2"
            >
              <ClipboardList className="w-4 h-4 text-sky-600" />
              <span>Start Health Assessment</span>
            </Link>
          </div>
        </div>
      </div>

      {/* 10 Specialized Screening Modules */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-lg font-extrabold text-slate-900">
              10 Specialized Screening Modules
            </h2>
            <p className="text-xs text-slate-500">
              Select any disease module to input clinical parameters and generate an instant risk assessment.
            </p>
          </div>
        </div>

        {loading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            {[...Array(10)].map((_, i) => (
              <div key={i} className="h-36 bg-slate-200 animate-pulse rounded-xl" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            {diseases.map((d) => {
              const Icon = getDiseaseIcon(d.slug);
              return (
                <Link
                  key={d.id}
                  to={`/assessment?disease=${d.slug}`}
                  className="group bg-white p-4 rounded-xl border border-slate-200 hover:border-sky-500 hover:shadow-md transition flex flex-col justify-between"
                >
                  <div>
                    <div className="w-9 h-9 rounded-lg bg-sky-50 text-sky-600 flex items-center justify-center mb-3 group-hover:bg-sky-600 group-hover:text-white transition">
                      <Icon className="w-5 h-5" />
                    </div>
                    <h3 className="font-bold text-sm text-slate-900 group-hover:text-sky-600 transition">
                      {d.name}
                    </h3>
                    <p className="text-[11px] text-slate-500 mt-1 line-clamp-2">
                      {d.description}
                    </p>
                  </div>
                  <div className="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-sky-600">
                    <span>{d.features?.length || 8} Parameters</span>
                    <ChevronRight className="w-4 h-4 group-hover:translate-x-0.5 transition" />
                  </div>
                </Link>
              );
            })}
          </div>
        )}
      </div>

      {/* Recent Assessment History */}
      <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-xs">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="text-base font-extrabold text-slate-900">
              Recent Assessment Activity
            </h3>
            <p className="text-xs text-slate-500">
              Your latest probabilistic health evaluations
            </p>
          </div>
          <Link
            to="/history"
            className="text-xs font-semibold text-sky-600 hover:text-sky-800"
          >
            View all history &rarr;
          </Link>
        </div>

        {history.length === 0 ? (
          <div className="text-center py-8 text-slate-500 text-xs">
            <ClipboardList className="w-8 h-8 mx-auto text-slate-400 mb-2" />
            No screening assessments recorded yet. Select a condition above to begin.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
                <tr>
                  <th className="py-2.5 px-3 font-semibold">Disease Target</th>
                  <th className="py-2.5 px-3 font-semibold">Risk Stratification</th>
                  <th className="py-2.5 px-3 font-semibold">Probability</th>
                  <th className="py-2.5 px-3 font-semibold">Assessment Date</th>
                  <th className="py-2.5 px-3 font-semibold text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {history.slice(0, 5).map((h) => (
                  <tr key={h.id} className="hover:bg-slate-50/70 transition">
                    <td className="py-3 px-3 font-bold text-slate-800">
                      {h.disease_name}
                    </td>
                    <td className="py-3 px-3">{getRiskBadge(h.risk_level)}</td>
                    <td className="py-3 px-3 font-mono font-medium text-slate-700">
                      {(h.probability * 100).toFixed(1)}%
                    </td>
                    <td className="py-3 px-3 text-slate-500">
                      {new Date(h.created_at).toLocaleDateString()}
                    </td>
                    <td className="py-3 px-3 text-right">
                      <Link
                        to={`/assessment?prediction_id=${h.id}`}
                        className="text-sky-600 hover:text-sky-800 font-semibold"
                      >
                        View Details &rarr;
                      </Link>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
