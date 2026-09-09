/**
 * MedPredict AI — Main Application Router & Shell
 */

import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { AuthProvider, useAuth } from './context/AuthContext';
import { AppNavbar } from './components/layout/AppNavbar';
import { AppSidebar } from './components/layout/AppSidebar';

// Pages
import { LoginPage } from './pages/auth/LoginPage';
import { RegisterPage } from './pages/auth/RegisterPage';
import { PatientDashboardPage } from './pages/patient/PatientDashboardPage';
import { AssessmentWizardPage } from './pages/patient/AssessmentWizardPage';
import { ClinicianConsolePage } from './pages/clinician/ClinicianConsolePage';
import { MLWorkbenchPage } from './pages/workbench/MLWorkbenchPage';
import { AdminGovernancePage } from './pages/admin/AdminGovernancePage';

const queryClient = new QueryClient();

// Dynamic Home Router based on the user's active role
const RoleBasedHome: React.FC = () => {
  const { activeRole } = useAuth();
  if (activeRole === 'doctor') return <ClinicianConsolePage />;
  if (activeRole === 'data_scientist') return <MLWorkbenchPage />;
  if (activeRole === 'admin') return <AdminGovernancePage />;
  return <PatientDashboardPage />;
};

// Application Main Layout
const MainLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <AppNavbar />
      <div className="flex flex-1">
        <AppSidebar />
        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto w-full">
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
            {/* Public Auth Routes */}
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />

            {/* Application Protected Routes with App Shell */}
            <Route
              path="/"
              element={
                <MainLayout>
                  <RoleBasedHome />
                </MainLayout>
              }
            />
            <Route
              path="/assessment"
              element={
                <MainLayout>
                  <AssessmentWizardPage />
                </MainLayout>
              }
            />
            <Route
              path="/history"
              element={
                <MainLayout>
                  <PatientDashboardPage />
                </MainLayout>
              }
            />

            {/* Clinician Specific Views */}
            <Route
              path="/clinician/*"
              element={
                <MainLayout>
                  <ClinicianConsolePage />
                </MainLayout>
              }
            />

            {/* Data Scientist Workbench */}
            <Route
              path="/workbench/*"
              element={
                <MainLayout>
                  <MLWorkbenchPage />
                </MainLayout>
              }
            />

            {/* Administrator Governance */}
            <Route
              path="/admin/*"
              element={
                <MainLayout>
                  <AdminGovernancePage />
                </MainLayout>
              }
            />

            {/* Catch-all redirect */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </QueryClientProvider>
  );
};

export default App;
