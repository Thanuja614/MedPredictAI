/**
 * MedPredict AI — Master Frontend TypeScript Interfaces
 */

export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  is_active: boolean;
  roles: Array<{ id: string; name: string; description?: string }>;
  created_at: string;
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
}

export interface DiseaseFeature {
  name: string;
  data_type: 'numeric' | 'categorical' | 'boolean';
  unit?: string;
  min_value?: number;
  max_value?: number;
  is_required: boolean;
  description?: string;
}

export interface DiseaseCatalogItem {
  id: string;
  name: string;
  slug: string;
  category: string;
  description: string;
  version: string;
  features: DiseaseFeature[];
}

export interface PredictionResult {
  id: string;
  disease_id: string;
  disease_name: string;
  probability: number;
  risk_level: 'LOW' | 'MODERATE' | 'HIGH';
  confidence_score: number;
  explanations?: {
    method: string;
    feature_contributions: Record<string, number>;
    base_value?: number;
  };
  disclaimer: string;
  created_at: string;
}

export interface PatientTimelinePoint {
  prediction_id: string;
  disease_id: string;
  disease_name: string;
  probability: number;
  risk_level: 'LOW' | 'MODERATE' | 'HIGH';
  created_at: string;
  delta: number | null;
  days_since_prev: number | null;
  monthly_velocity: number;
}

export interface PatientTimelineResponse {
  patient_id: string;
  total_assessments: number;
  trajectory: 'BASELINE' | 'STABLE' | 'ESCALATING' | 'IMPROVING';
  timeline: PatientTimelinePoint[];
  disclaimer: string;
}

export interface PopulationDistribution {
  disease_id: string | null;
  total_inferences: number;
  distribution: {
    LOW: number;
    MODERATE: number;
    HIGH: number;
  };
  percentages: {
    LOW: number;
    MODERATE: number;
    HIGH: number;
  };
  summary_stats: {
    mean: number;
    median: number;
    min: number;
    max: number;
    std: number;
  };
  demographic_breakdown: Array<{
    group: string;
    LOW: number;
    MODERATE: number;
    HIGH: number;
    total: number;
  }>;
}

export interface SystemOverview {
  total_patients: number;
  total_predictions: number;
  total_diseases: number;
  high_risk_count: number;
  recent_activity: Array<{
    id: string;
    disease_name: string;
    risk_level: string;
    probability: number;
    patient_name: string;
    created_at: string;
  }>;
}

export interface GovernedModel {
  model_id: string;
  name: string;
  disease_id: string;
  disease_name: string;
  versions: Array<{
    id: string;
    version_tag: string;
    status: 'staged' | 'active' | 'archived' | 'shadow';
    artifact_hash_sha256: string;
    metrics: Record<string, any>;
    created_at: string;
  }>;
}

export interface InAppNotification {
  id: string;
  title: string;
  message: string;
  type: 'info' | 'success' | 'warning' | 'alert';
  is_read: boolean;
  created_at: string;
}

export interface AuditLogEntry {
  id: string;
  action: string;
  entity_type: string;
  entity_id?: string;
  user_id?: string;
  user_email?: string;
  ip_address?: string;
  details: Record<string, any>;
  created_at: string;
}

export interface SystemSettingItem {
  key: string;
  value: string;
  description?: string;
  updated_at: string;
}
