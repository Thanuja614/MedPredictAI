/**
 * MedPredict AI — Main Application Router & Shell
 * High-end clinical decision support platform
 */

import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { AuthProvider } from './context/AuthContext';
import { AppNavbar } from './components/layout/AppNavbar';
import { AppSidebar } from './components/layout/AppSidebar';

// Clinical Command Center Pages
import { ClinicalDashboardPage } from './pages/dashboard/ClinicalDashboardPage';
import { PatientProfilePage } from './pages/patients/PatientProfilePage';
import { RiskPredictionPage } from './pages/prediction/RiskPredictionPage';
import { MedicalReportsPage } from './pages/reports/MedicalReportsPage';
import { ClinicalAnalyticsPage } from './pages/analytics/ClinicalAnalyticsPage';
import { PredictionHistoryPage } from './pages/history/PredictionHistoryPage';
import { ClinicalNotificationsPage } from './pages/notifications/ClinicalNotificationsPage';
import { SystemSettingsPage } from './pages/settings/SystemSettingsPage';

// Auth Pages
import { LoginPage } from './pages/auth/LoginPage';
import { RegisterPage } from './pages/auth/RegisterPage';

// Specialized Workspaces
import { AssessmentWizardPage } from './pages/patient/AssessmentWizardPage';
import { MLWorkbenchPage } from './pages/workbench/MLWorkbenchPage';
import { AdminGovernancePage } from './pages/admin/AdminGovernancePage';
import { ClinicianConsolePage } from './pages/clinician/ClinicianConsolePage';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      staleTime: 1000 * 60 * 5, // 5 minutes
    },
  },
});

// Application Main Layout with ivory background and hospital elevation
const MainLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div className="min-h-screen bg-ivory flex flex-col text-charcoal font-sans antialiased selection:bg-medblue/20 selection:text-navy-900">
      <AppNavbar />
      <div className="flex flex-1">
        <AppSidebar />
        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto w-full overflow-x-hidden">
          {children}
        </main>
      </div>
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            {/* Public Authentication */}
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />

            {/* Core Hospital Clinical Platform */}
            <Route
              path="/"
              element={
                <MainLayout>
                  <ClinicalDashboardPage />
                </MainLayout>
              }
            />
            <Route
              path="/patients"
              element={
                <MainLayout>
                  <PatientProfilePage />
                </MainLayout>
              }
            />
            <Route
              path="/patients/:id"
              element={
                <MainLayout>
                  <PatientProfilePage />
                </MainLayout>
              }
            />
            <Route
              path="/prediction"
              element={
                <MainLayout>
                  <RiskPredictionPage />
                </MainLayout>
              }
            />
            <Route
              path="/reports"
              element={
                <MainLayout>
                  <MedicalReportsPage />
                </MainLayout>
              }
            />
            <Route
              path="/analytics"
              element={
                <MainLayout>
                  <ClinicalAnalyticsPage />
                </MainLayout>
              }
            />
            <Route
              path="/history"
              element={
                <MainLayout>
                  <PredictionHistoryPage />
                </MainLayout>
              }
            />
            <Route
              path="/notifications"
              element={
                <MainLayout>
                  <ClinicalNotificationsPage />
                </MainLayout>
              }
            />
            <Route
              path="/settings"
              element={
                <MainLayout>
                  <SystemSettingsPage />
                </MainLayout>
              }
            />

            {/* Extended Specialized Clinical & ML Workbenches */}
            <Route
              path="/assessment"
              element={
                <MainLayout>
                  <AssessmentWizardPage />
                </MainLayout>
              }
            />
            <Route
              path="/clinician/*"
              element={
                <MainLayout>
                  <ClinicianConsolePage />
                </MainLayout>
              }
            />
            <Route
              path="/workbench/*"
              element={
                <MainLayout>
                  <MLWorkbenchPage />
                </MainLayout>
              }
            />
            <Route
              path="/admin/*"
              element={
                <MainLayout>
                  <AdminGovernancePage />
                </MainLayout>
              }
            />

            {/* Fallback to Clinical Command Center */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </QueryClientProvider>
  );
};

export default App;
