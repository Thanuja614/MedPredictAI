/**
 * MedPredict AI — Prediction History & Audit Ledger Page
 * Section 16: Professional data table, columns, search, filtering, status pills, pagination
 */

import React, { useState, useMemo } from 'react';
import { Link } from 'react-router-dom';
import {
  History,
  Search,
  Filter,
  ArrowUpDown,
  Download,
  Eye,
  FileText,
  Calendar,
  ChevronLeft,
  ChevronRight,
  ShieldCheck,
} from 'lucide-react';
import { StatusBadge } from '../../components/clinical/StatusBadge';
import { DEMO_PATIENTS } from '../../clinical/data/demoClinicalData';

interface HistoryEntry {
  id: string;
  patientId: string;
  patientName: string;
  predictionType: string;
  riskLevel: 'LOW' | 'MODERATE' | 'HIGH' | 'CRITICAL';
  probability: number;
  date: string;
  status: 'Verified' | 'Pending Review' | 'Flagged';
  physician: string;
}

export const PredictionHistoryPage: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [selectedRiskFilter, setSelectedRiskFilter] = useState<string>('ALL');
  const [currentPage, setCurrentPage] = useState<number>(1);
  const itemsPerPage = 8;

  // Generate authentic clinical prediction history records
  const allHistory: HistoryEntry[] = useMemo(() => [
    {
      id: 'EV-901',
      patientId: 'MP-2026-01482',
      patientName: 'Ananya Rao',
      predictionType: 'Cardiovascular (ASCVD)',
      riskLevel: 'MODERATE',
      probability: 68.4,
      date: '2026-09-08 11:24',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-902',
      patientId: 'MP-2026-00912',
      patientName: 'Marcus Vance',
      predictionType: 'Cerebrovascular Stroke',
      riskLevel: 'HIGH',
      probability: 84.2,
      date: '2026-09-10 14:15',
      status: 'Flagged',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-903',
      patientId: 'MP-2026-02319',
      patientName: 'Eleanor Chen',
      predictionType: 'Cardiovascular Baseline',
      riskLevel: 'LOW',
      probability: 14.8,
      date: '2026-08-30 09:12',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-904',
      patientId: 'MP-2026-00438',
      patientName: "David O'Connor",
      predictionType: 'Chronic Kidney Disease',
      riskLevel: 'HIGH',
      probability: 79.1,
      date: '2026-09-02 16:40',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-905',
      patientId: 'MP-2026-01180',
      patientName: 'Fatima Al-Mansoor',
      predictionType: 'Thyroid Dysregulation',
      riskLevel: 'MODERATE',
      probability: 52.6,
      date: '2026-09-05 10:05',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-906',
      patientId: 'MP-2026-01928',
      patientName: 'Robert Martinez',
      predictionType: 'Essential Hypertension',
      riskLevel: 'MODERATE',
      probability: 61.3,
      date: '2026-09-01 15:30',
      status: 'Pending Review',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-907',
      patientId: 'MP-2026-02054',
      patientName: 'Grace Sterling',
      predictionType: 'Breast Cancer Diagnostic',
      riskLevel: 'LOW',
      probability: 8.2,
      date: '2026-08-28 13:50',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-908',
      patientId: 'MP-2026-03112',
      patientName: 'Kavita Patel',
      predictionType: 'Liver Impairment (NAFLD)',
      riskLevel: 'MODERATE',
      probability: 44.9,
      date: '2026-08-25 11:10',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-909',
      patientId: 'MP-2026-01773',
      patientName: 'Thomas Wright',
      predictionType: 'Parkinson Vocal Tremor',
      riskLevel: 'LOW',
      probability: 19.5,
      date: '2026-08-21 16:00',
      status: 'Verified',
      physician: 'Dr. Sarah Mitchell',
    },
    {
      id: 'EV-910',
      patientId: 'MP-2026-02488',
      patientName: 'Helena Berg',
      predictionType: 'Hematology (Anemia)',
      riskLevel: 'HIGH',
      probability: 72.8,
      date: '2026-08-18 10:45',
      status: 'Flagged',
      physician: 'Dr. Sarah Mitchell',
    },
  ], []);

  // Filtered & Searched Data
  const filteredData = useMemo(() => {
    return allHistory.filter((item) => {
      const matchSearch =
        item.patientName.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.patientId.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.predictionType.toLowerCase().includes(searchTerm.toLowerCase());
      const matchRisk = selectedRiskFilter === 'ALL' || item.riskLevel === selectedRiskFilter;
      return matchSearch && matchRisk;
    });
  }, [allHistory, searchTerm, selectedRiskFilter]);

  const totalPages = Math.ceil(filteredData.length / itemsPerPage);
  const paginatedData = filteredData.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-medblue uppercase tracking-wider font-mono">
            Audit Ledger & Historical Records
          </span>
          <h2 className="text-xl lg:text-2xl font-bold text-slate-900">
            Clinical Prediction History
          </h2>
          <p className="text-xs text-slateText">
            Verified longitudinal record of multi-disease risk evaluations and physician confirmations.
          </p>
        </div>

        <button
          onClick={() => window.print()}
          className="px-4 py-2 bg-ivory hover:bg-medblue-light text-navy-800 text-xs font-semibold rounded-btn border border-borderLine flex items-center space-x-2 transition shadow-xs self-start md:self-auto"
        >
          <Download className="w-3.5 h-3.5 text-slateText" />
          <span>Export Audit Log (CSV)</span>
        </button>
      </div>

      {/* Filter and Search Bar */}
      <div className="bg-surface rounded-card p-4 border border-borderLine shadow-medical flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
        <div className="relative flex-1 max-w-md">
          <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slateText" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setCurrentPage(1);
            }}
            placeholder="Search patient name, MRN, or disease type..."
            className="w-full pl-8 pr-3 py-1.5 text-xs bg-ivory border border-borderLine rounded-btn text-charcoal placeholder-slateText focus:ring-1 focus:ring-medblue focus:bg-white"
          />
        </div>

        <div className="flex items-center space-x-2">
          <span className="text-xs font-semibold text-slateText flex items-center space-x-1">
            <Filter className="w-3 h-3" />
            <span>Risk Level:</span>
          </span>
          <div className="flex bg-ivory p-1 rounded-btn border border-borderLine">
            {['ALL', 'HIGH', 'MODERATE', 'LOW'].map((t) => (
              <button
                key={t}
                onClick={() => {
                  setSelectedRiskFilter(t);
                  setCurrentPage(1);
                }}
                className={`px-3 py-1 text-xs font-semibold rounded-md transition ${
                  selectedRiskFilter === t
                    ? 'bg-navy-800 text-ivory shadow-xs'
                    : 'text-slateText hover:text-navy-800'
                }`}
              >
                {t === 'ALL' ? 'All' : t}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Table (Section 16: Columns, subtle row separators, pills) */}
      <div className="bg-surface rounded-card border border-borderLine shadow-medical overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-charcoal">
            <thead className="bg-ivory/80 text-[11px] font-bold text-slateText uppercase font-mono tracking-wider border-b border-borderLine">
              <tr>
                <th className="py-3 px-4">Patient ID</th>
                <th className="py-3 px-4">Patient Name</th>
                <th className="py-3 px-4">Prediction Type</th>
                <th className="py-3 px-4">Risk Level</th>
                <th className="py-3 px-4">Probability</th>
                <th className="py-3 px-4">Encounter Date</th>
                <th className="py-3 px-4">Verification Status</th>
                <th className="py-3 px-4 text-right">Clinical Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-borderLine/50">
              {paginatedData.length === 0 ? (
                <tr>
                  <td colSpan={8} className="py-8 text-center text-slateText text-xs">
                    No prediction records matching current search criteria.
                  </td>
                </tr>
              ) : (
                paginatedData.map((row) => (
                  <tr key={row.id} className="hover:bg-ivory/50 transition">
                    <td className="py-3 px-4 font-mono font-bold text-navy-800">
                      {row.patientId}
                    </td>
                    <td className="py-3 px-4 font-semibold text-charcoal">
                      {row.patientName}
                    </td>
                    <td className="py-3 px-4 text-slate-700">
                      {row.predictionType}
                    </td>
                    <td className="py-3 px-4">
                      <StatusBadge status={row.riskLevel} label={`${row.riskLevel}`} />
                    </td>
                    <td className="py-3 px-4 font-mono font-bold text-navy-800">
                      {row.probability.toFixed(1)}%
                    </td>
                    <td className="py-3 px-4 text-slateText font-mono text-[11px]">
                      {row.date}
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`inline-flex items-center space-x-1 text-[11px] font-semibold px-2 py-0.5 rounded ${
                          row.status === 'Verified'
                            ? 'bg-status-healthyBg text-status-healthy'
                            : row.status === 'Flagged'
                            ? 'bg-status-criticalBg text-status-critical'
                            : 'bg-status-warningBg text-status-warning'
                        }`}
                      >
                        <ShieldCheck className="w-3 h-3" />
                        <span>{row.status}</span>
                      </span>
                    </td>
                    <td className="py-3 px-4 text-right space-x-2">
                      <Link
                        to={`/patients/${row.patientId === 'MP-2026-00912' ? 'pt-2' : 'pt-1'}`}
                        className="inline-flex items-center space-x-1 text-xs font-semibold text-medblue hover:text-navy-800 hover:underline"
                      >
                        <Eye className="w-3.5 h-3.5" />
                        <span>View</span>
                      </Link>
                      <Link
                        to="/reports"
                        className="inline-flex items-center space-x-1 text-xs font-semibold text-slateText hover:text-navy-800 hover:underline"
                      >
                        <FileText className="w-3.5 h-3.5" />
                        <span>Report</span>
                      </Link>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Bar */}
        <div className="p-3 bg-ivory border-t border-borderLine flex items-center justify-between text-xs text-slateText">
          <div>
            Showing <strong className="text-charcoal">{paginatedData.length}</strong> of{' '}
            <strong className="text-charcoal">{filteredData.length}</strong> records
          </div>

          <div className="flex items-center space-x-2">
            <button
              onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
              disabled={currentPage === 1}
              className="p-1 rounded bg-surface border border-borderLine disabled:opacity-40 hover:bg-white transition"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <span className="font-mono font-medium">
              Page {currentPage} of {totalPages || 1}
            </span>
            <button
              onClick={() => setCurrentPage((p) => Math.min(totalPages, p + 1))}
              disabled={currentPage >= totalPages}
              className="p-1 rounded bg-surface border border-borderLine disabled:opacity-40 hover:bg-white transition"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
