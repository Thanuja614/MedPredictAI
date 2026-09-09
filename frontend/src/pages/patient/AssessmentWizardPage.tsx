/**
 * MedPredict AI — Interactive Disease Risk Assessment Wizard
 * Supports all 10 specialized conditions with dynamic form generation,
 * calibrated probability inference, SHAP waterfall explainability, and PDF reports.
 */

import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import {
  Activity,
  AlertTriangle,
  FileDown,
  CheckCircle2,
  RefreshCw,
  HelpCircle,
  BarChart3,
  Shield,
  Sparkles,
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine,
  Cell,
} from 'recharts';
import { MedicalDisclaimerBanner } from '../../components/common/MedicalDisclaimerBanner';
import { api } from '../../services/api';
import { DiseaseCatalogItem, PredictionResult } from '../../types';

export const AssessmentWizardPage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialDiseaseSlug = searchParams.get('disease') || 'diabetes';

  const [diseases, setDiseases] = useState<DiseaseCatalogItem[]>([]);
  const [selectedSlug, setSelectedSlug] = useState<string>(initialDiseaseSlug);
  const [currentDisease, setCurrentDisease] = useState<DiseaseCatalogItem | null>(null);
  const [formData, setFormData] = useState<Record<string, any>>({});
  const [loadingSchema, setLoadingSchema] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [downloadingReport, setDownloadingReport] = useState(false);
  const [reportUrl, setReportUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Load Catalog of Diseases
  useEffect(() => {
    const fetchCatalog = async () => {
      try {
        const list = await api.diseases.list();
        setDiseases(list);
      } catch (err) {
        console.error('Failed to load disease catalog', err);
      }
    };
    fetchCatalog();
  }, []);

  // Load Schema for Selected Disease
  useEffect(() => {
    const loadDisease = async () => {
      setLoadingSchema(true);
      setPrediction(null);
      setReportUrl(null);
      setError(null);
      try {
        const details = await api.diseases.get(selectedSlug);
        setCurrentDisease(details);

        // Prepopulate with reasonable median baseline defaults
        const defaults: Record<string, any> = {};
        details.features.forEach((f) => {
          if (f.min_value !== undefined && f.max_value !== undefined) {
            defaults[f.name] = Number(((f.min_value + f.max_value) / 2).toFixed(1));
          } else {
            defaults[f.name] = f.data_type === 'numeric' ? 50 : 0;
          }
        });
        setFormData(defaults);
      } catch (err) {
        console.error('Failed to load disease schema', err);
      } finally {
        setLoadingSchema(false);
      }
    };

    if (selectedSlug) {
      loadDisease();
    }
  }, [selectedSlug]);

  const handleDiseaseChange = (slug: string) => {
    setSelectedSlug(slug);
    setSearchParams({ disease: slug });
  };

  const handleInputChange = (featureName: string, value: any) => {
    setFormData((prev) => ({
      ...prev,
      [featureName]: Number(value),
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      const result = await api.predictions.submit({
        disease_slug: selectedSlug,
        features: formData,
      });
      setPrediction(result);
    } catch (err: any) {
      console.error('Inference error', err);
      const msg =
        err.response?.data?.error?.message ||
        err.response?.data?.detail ||
        err.message ||
        'Failed to evaluate clinical risk. Please check inputs and try again.';
      setError(msg);
    } finally {
      setSubmitting(false);
    }
  };

  const handleGenerateReport = async () => {
    if (!prediction) return;
    setDownloadingReport(true);
    try {
      const rep = await api.reports.generate(prediction.id);
      setReportUrl(rep.download_url);
      window.open(rep.download_url, '_blank');
    } catch (err) {
      console.error('Report generation error', err);
    } finally {
      setDownloadingReport(false);
    }
  };

  // Convert SHAP contributions to Recharts data
  const shapData = React.useMemo(() => {
    if (!prediction) return [];
    if (prediction?.explanations?.feature_contributions) {
      return Object.entries(prediction.explanations.feature_contributions).map(([feat, val]) => ({
        feature: feat,
        impact: Number(val),
        color: Number(val) > 0 ? '#dc2626' : '#16a34a',
      }));
    }
    const anyPred = prediction as any;
    if (anyPred.explanation?.contributions) {
      return anyPred.explanation.contributions.map((c: any) => ({
        feature: c.feature,
        impact: Number(c.contribution),
        color: Number(c.contribution) > 0 ? '#dc2626' : '#16a34a',
      }));
    }
    return [];
  }, [prediction]);

  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      {/* Prominent Medical Safety Notice */}
      <MedicalDisclaimerBanner />

      {/* Disease Selection Tabs */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-xs">
        <label className="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-2">
          Target Clinical Condition (10 Available):
        </label>
        <div className="flex flex-wrap gap-2">
          {diseases.map((d) => (
            <button
              key={d.slug}
              onClick={() => handleDiseaseChange(d.slug)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition ${
                selectedSlug === d.slug
                  ? 'bg-sky-600 text-white shadow-sm'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {d.name}
            </button>
          ))}
        </div>
      </div>

      {/* Main Assessment Form and Results Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Clinical Parameters Input Form */}
        <div className="lg:col-span-7 bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
          <div className="flex items-center justify-between pb-4 border-b border-slate-100 mb-4">
            <div>
              <h2 className="text-base font-extrabold text-slate-900">
                {currentDisease?.name || 'Condition'} Parameters
              </h2>
              <p className="text-xs text-slate-500">
                {currentDisease?.description}
              </p>
            </div>
            <span className="text-[11px] font-semibold bg-sky-50 text-sky-700 px-2 py-1 rounded">
              Model v{currentDisease?.version || '1.0.0'}
            </span>
          </div>

          {loadingSchema ? (
            <div className="py-12 text-center text-xs text-slate-400">
              <RefreshCw className="w-6 h-6 animate-spin mx-auto mb-2 text-sky-600" />
              Loading disease parameter specifications...
            </div>
          ) : (
            <>
              {error && (
                <div className="mb-4 p-3 bg-rose-50 border border-rose-200 text-rose-800 text-xs rounded-xl flex items-center space-x-2">
                  <AlertTriangle className="w-4 h-4 text-rose-600 flex-shrink-0" />
                  <span>{error}</span>
                </div>
              )}
              <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {currentDisease?.features.map((feat) => (
                  <div key={feat.name} className="space-y-1">
                    <div className="flex items-center justify-between">
                      <label className="text-xs font-semibold text-slate-700">
                        {feat.name}
                      </label>
                      {feat.unit && (
                        <span className="text-[10px] text-slate-400">{feat.unit}</span>
                      )}
                    </div>
                    <input
                      type="number"
                      step="any"
                      required={feat.is_required}
                      min={feat.min_value}
                      max={feat.max_value}
                      value={formData[feat.name] ?? ''}
                      onChange={(e) => handleInputChange(feat.name, e.target.value)}
                      className="w-full px-3 py-2 text-xs border border-slate-300 rounded-lg focus:ring-2 focus:ring-sky-500 focus:border-sky-500 font-mono"
                      placeholder={`Enter ${feat.name}`}
                    />
                    {feat.min_value !== undefined && feat.max_value !== undefined && (
                      <div className="text-[10px] text-slate-400">
                        Normal range: {feat.min_value} – {feat.max_value}
                      </div>
                    )}
                  </div>
                ))}
              </div>

              <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
                <button
                  type="button"
                  onClick={() => {
                    // Populate with randomized representative demo values
                    const demo: Record<string, any> = {};
                    currentDisease?.features.forEach((f) => {
                      if (f.min_value !== undefined && f.max_value !== undefined) {
                        const mid = (f.min_value + f.max_value) / 2;
                        demo[f.name] = Number((mid + (Math.random() - 0.5) * (f.max_value - f.min_value) * 0.4).toFixed(1));
                      } else {
                        demo[f.name] = Math.random() > 0.5 ? 1 : 0;
                      }
                    });
                    setFormData(demo);
                  }}
                  className="text-xs text-sky-600 hover:text-sky-800 font-semibold flex items-center space-x-1"
                >
                  <Sparkles className="w-3.5 h-3.5 text-amber-500" />
                  <span>Autofill Sample Values</span>
                </button>

                <button
                  type="submit"
                  disabled={submitting}
                  className="px-5 py-2.5 bg-sky-600 hover:bg-sky-700 text-white font-bold rounded-xl shadow text-xs transition flex items-center space-x-2 disabled:opacity-50"
                >
                  {submitting ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin" />
                      <span>Computing Inference...</span>
                    </>
                  ) : (
                    <>
                      <Activity className="w-4 h-4" />
                      <span>Evaluate Clinical Risk</span>
                    </>
                  )}
                </button>
              </div>
            </form>
            </>
          )}
        </div>

        {/* Right Column: Prediction Score & SHAP Explainability */}
        <div className="lg:col-span-5 space-y-6">
          {prediction ? (
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-5">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-extrabold text-slate-900 uppercase tracking-wide">
                  Clinical Risk Evaluation
                </h3>
                <span className="text-[11px] text-slate-400">
                  {new Date(prediction.created_at).toLocaleTimeString()}
                </span>
              </div>

              {/* Risk Level Badge & Probability Dial */}
              <div
                className={`p-5 rounded-xl border text-center ${
                  prediction.risk_level === 'HIGH'
                    ? 'bg-rose-50 border-rose-200 text-rose-950'
                    : prediction.risk_level === 'MODERATE'
                    ? 'bg-amber-50 border-amber-200 text-amber-950'
                    : 'bg-emerald-50 border-emerald-200 text-emerald-950'
                }`}
              >
                <span
                  className={`inline-block px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider mb-2 ${
                    prediction.risk_level === 'HIGH'
                      ? 'bg-rose-600 text-white'
                      : prediction.risk_level === 'MODERATE'
                      ? 'bg-amber-600 text-white'
                      : 'bg-emerald-600 text-white'
                  }`}
                >
                  {prediction.risk_level} RISK
                </span>
                <div className="text-4xl font-extrabold font-mono tracking-tight my-1">
                  {(prediction.probability * 100).toFixed(1)}%
                </div>
                <p className="text-xs opacity-80">
                  Calibrated Disease Risk Probability (0.00 – 1.00)
                </p>
              </div>

              {/* Operating Thresholds Reference */}
              <div className="grid grid-cols-3 gap-1 text-center text-[10px] bg-slate-50 p-2 rounded-lg border border-slate-200">
                <div className="p-1 rounded bg-emerald-50 text-emerald-800 font-medium">
                  LOW (&lt;35%)
                </div>
                <div className="p-1 rounded bg-amber-50 text-amber-800 font-medium">
                  MODERATE (35-65%)
                </div>
                <div className="p-1 rounded bg-rose-50 text-rose-800 font-medium">
                  HIGH (&gt;65%)
                </div>
              </div>

              {/* SHAP Feature Contribution Waterfall Bar Chart */}
              {shapData.length > 0 && (
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-bold text-slate-800 flex items-center space-x-1.5">
                      <BarChart3 className="w-3.5 h-3.5 text-sky-600" />
                      <span>Feature Contributions (SHAP Waterfall)</span>
                    </span>
                  </div>
                  <div className="h-48 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart
                        layout="vertical"
                        data={shapData}
                        margin={{ top: 5, right: 20, left: 40, bottom: 5 }}
                      >
                        <XAxis type="number" tick={{ fontSize: 10 }} />
                        <YAxis
                          type="category"
                          dataKey="feature"
                          tick={{ fontSize: 10 }}
                          width={80}
                        />
                        <Tooltip
                          contentStyle={{ fontSize: 11, borderRadius: 8 }}
                          formatter={(val: any) => [Number(val).toFixed(4), 'SHAP Impact']}
                        />
                        <ReferenceLine x={0} stroke="#94a3b8" />
                        <Bar dataKey="impact" radius={[0, 4, 4, 0]}>
                          {shapData.map((entry: { color: string }, index: number) => (
                            <Cell key={`cell-${index}`} fill={entry.color} />
                          ))}
                        </Bar>
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                  <div className="flex items-center justify-center space-x-4 text-[10px] text-slate-500 mt-1">
                    <div className="flex items-center space-x-1">
                      <span className="w-2.5 h-2.5 bg-rose-600 rounded-sm" />
                      <span>Elevates Risk</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <span className="w-2.5 h-2.5 bg-emerald-600 rounded-sm" />
                      <span>Lowers Risk</span>
                    </div>
                  </div>
                </div>
              )}

              {/* PDF Clinical Report Download Action */}
              <div className="pt-3 border-t border-slate-100">
                <button
                  type="button"
                  onClick={handleGenerateReport}
                  disabled={downloadingReport}
                  className="w-full py-2.5 px-4 bg-slate-900 hover:bg-slate-800 text-white font-bold rounded-xl shadow text-xs flex items-center justify-center space-x-2 transition disabled:opacity-50"
                >
                  <FileDown className="w-4 h-4 text-sky-400" />
                  <span>
                    {downloadingReport
                      ? 'Compiling PDF Report...'
                      : 'Download Official Clinical PDF Report'}
                  </span>
                </button>
              </div>
            </div>
          ) : (
            <div className="bg-white p-8 rounded-2xl border border-slate-200 text-center text-slate-500 space-y-3 shadow-xs">
              <div className="w-12 h-12 bg-sky-50 rounded-full flex items-center justify-center mx-auto text-sky-600">
                <Activity className="w-6 h-6" />
              </div>
              <h3 className="font-bold text-slate-800 text-sm">
                Ready for Risk Assessment
              </h3>
              <p className="text-xs text-slate-500 max-w-xs mx-auto">
                Fill in the clinical indicators on the left or use the autofill button, then click <strong>Evaluate Clinical Risk</strong> to generate a calibrated risk score and SHAP explainability waterfall.
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
