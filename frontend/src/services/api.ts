/**
 * MedPredict AI — Central API Client & Typed Services
 */

import axios, { AxiosError } from 'axios';
import {
  User,
  AuthResponse,
  DiseaseCatalogItem,
  PredictionResult,
  PatientTimelineResponse,
  PopulationDistribution,
  SystemOverview,
  GovernedModel,
  InAppNotification,
  AuditLogEntry,
  SystemSettingItem,
} from '../types';

export const apiClient = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request Interceptor: Attach JWT Bearer Token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('medpredict_access_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response Interceptor: Handle 401 Unauthorized
apiClient.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    if (error.response?.status === 401) {
      // Clear token and let context handle redirection
      localStorage.removeItem('medpredict_access_token');
      localStorage.removeItem('medpredict_refresh_token');
    }
    return Promise.reject(error);
  }
);

export const api = {
  // Authentication
  auth: {
    login: async (credentials: URLSearchParams): Promise<AuthResponse> => {
      const res = await axios.post<AuthResponse>('/api/v1/auth/login', credentials, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      return res.data;
    },
    register: async (userData: {
      email: string;
      password: string;
      first_name: string;
      last_name: string;
    }): Promise<User> => {
      const res = await apiClient.post<User>('/auth/register', userData);
      return res.data;
    },
    getMe: async (): Promise<User> => {
      const res = await apiClient.get<User>('/users/me');
      return res.data;
    },
  },

  // Disease Catalog & Features
  diseases: {
    list: async (): Promise<DiseaseCatalogItem[]> => {
      const res = await apiClient.get<DiseaseCatalogItem[]>('/diseases');
      return res.data;
    },
    get: async (slug: string): Promise<DiseaseCatalogItem> => {
      const res = await apiClient.get<DiseaseCatalogItem>(`/diseases/${slug}`);
      return res.data;
    },
    screenSymptoms: async (symptoms: string[]): Promise<any[]> => {
      const res = await apiClient.post('/diseases/symptom-screening', { symptoms });
      return res.data;
    },
  },

  // Inference & Predictions
  predictions: {
    submit: async (data: {
      disease_slug: string;
      features: Record<string, any>;
      patient_id?: string;
    }): Promise<PredictionResult> => {
      const res = await apiClient.post<PredictionResult>('/predictions', data);
      return res.data;
    },
    getHistory: async (patientId?: string): Promise<PredictionResult[]> => {
      const params = patientId ? { patient_id: patientId } : {};
      const res = await apiClient.get<PredictionResult[]>('/predictions/history', { params });
      return res.data;
    },
  },

  // Clinical Patients
  patients: {
    list: async (): Promise<any[]> => {
      const res = await apiClient.get<any[]>('/patients');
      return res.data;
    },
    get: async (patientId: string): Promise<any> => {
      const res = await apiClient.get<any>(`/patients/${patientId}`);
      return res.data;
    },
  },

  // Analytics & Cohort
  analytics: {
    getOverview: async (): Promise<SystemOverview> => {
      const res = await apiClient.get<SystemOverview>('/analytics/system-overview');
      return res.data;
    },
    getPatientTimeline: async (patientId: string, diseaseId?: string): Promise<PatientTimelineResponse> => {
      const params = diseaseId ? { disease_id: diseaseId } : {};
      const res = await apiClient.get<PatientTimelineResponse>(`/analytics/patient/${patientId}/timeline`, { params });
      return res.data;
    },
    getPopulationDistribution: async (diseaseId?: string): Promise<PopulationDistribution> => {
      const params = diseaseId ? { disease_id: diseaseId } : {};
      const res = await apiClient.get<PopulationDistribution>('/analytics/population/distribution', { params });
      return res.data;
    },
  },

  // Model Governance
  governance: {
    listModels: async (): Promise<GovernedModel[]> => {
      const res = await apiClient.get<GovernedModel[]>('/governance/models');
      return res.data;
    },
    promoteModel: async (versionId: string): Promise<any> => {
      const res = await apiClient.post(`/governance/models/${versionId}/promote`);
      return res.data;
    },
    rollbackModel: async (versionId: string): Promise<any> => {
      const res = await apiClient.post(`/governance/models/${versionId}/rollback`);
      return res.data;
    },
    runDriftCheck: async (diseaseSlug: string): Promise<any> => {
      const res = await apiClient.post(`/governance/drift-check?disease_slug=${diseaseSlug}`);
      return res.data;
    },
  },

  // Reports
  reports: {
    generate: async (predictionId: string): Promise<{ report_id: string; download_url: string }> => {
      const res = await apiClient.post(`/reports/generate/${predictionId}`);
      return res.data;
    },
    downloadUrl: (reportId: string): string => `/api/v1/reports/${reportId}/download`,
    verify: async (reportId: string): Promise<any> => {
      const res = await apiClient.get(`/reports/${reportId}/verify`);
      return res.data;
    },
  },

  // Notifications
  notifications: {
    list: async (unreadOnly = false): Promise<InAppNotification[]> => {
      const res = await apiClient.get<InAppNotification[]>('/notifications', {
        params: { unread_only: unreadOnly },
      });
      return res.data;
    },
    markRead: async (id: string): Promise<any> => {
      const res = await apiClient.put(`/notifications/${id}/read`);
      return res.data;
    },
    markAllRead: async (): Promise<any> => {
      const res = await apiClient.post('/notifications/mark-all-read');
      return res.data;
    },
  },

  // Security Audit
  audit: {
    listLogs: async (params?: any): Promise<{ total_returned: number; logs: AuditLogEntry[] }> => {
      const res = await apiClient.get('/audit/logs', { params });
      return res.data;
    },
    exportUrl: '/api/v1/audit/export',
  },

  // System Settings
  settings: {
    list: async (): Promise<SystemSettingItem[]> => {
      const res = await apiClient.get<SystemSettingItem[]>('/settings');
      return res.data;
    },
    update: async (key: string, value: string): Promise<SystemSettingItem> => {
      const res = await apiClient.put<SystemSettingItem>(`/settings/${key}`, { value });
      return res.data;
    },
  },
};
