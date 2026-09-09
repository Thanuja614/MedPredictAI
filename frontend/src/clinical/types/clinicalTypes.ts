/**
 * MedPredict AI — Clinical Domain TypeScript Types & Interfaces
 */

export type SeverityLevel = "MILD" | "MODERATE" | "SEVERE" | "LIFE_THREATENING";
export type RiskCategory = "LOW" | "BORDERLINE" | "INTERMEDIATE" | "HIGH" | "VERY_HIGH";
export type SpecimenType = "Serum" | "Plasma" | "Whole Blood" | "Urine" | "CSF" | "Arterial Blood";
export type InteractionSeverity = "Contraindicated" | "Major" | "Moderate" | "Minor";

export interface ReferenceRange {
  low: number;
  high: number;
  unit: string;
  panicLow?: number;
  panicHigh?: number;
}

export interface BiomarkerDefinition {
  loincCode: string;
  name: string;
  shortName: string;
  category: string;
  specimen: SpecimenType;
  conventionalUnit: string;
  siUnit: string;
  siConversionFactor: number;
  adultMaleRange: ReferenceRange;
  adultFemaleRange: ReferenceRange;
  clinicalSignificance: string;
  elevatedInterpretation: string;
  decreasedInterpretation: string;
}

export interface DrugMonograph {
  rxcui: string;
  genericName: string;
  brandNames: string[];
  drugClass: string;
  standardDose: string;
  maxDailyDose: string;
  primaryElimination: string;
  renalAdjustment: string;
  hepaticAdjustment: string;
  blackBoxWarning?: string;
  commonAdverseEffects: string[];
}

export interface ICD10DiseaseEntry {
  code: string;
  title: string;
  category: string;
  isChronic: boolean;
  severity: SeverityLevel;
  typicalSymptoms: string[];
  primaryLabs: string[];
  firstLineMeds: string[];
}

export interface InteractionWarning {
  drugA: string;
  drugB: string;
  severity: InteractionSeverity;
  clinicalEffect: string;
  management: string;
}

export interface ClinicalAssessmentRecordTier1 {
  recordId: string;
  assessmentTier: 1;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier2 {
  recordId: string;
  assessmentTier: 2;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier3 {
  recordId: string;
  assessmentTier: 3;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier4 {
  recordId: string;
  assessmentTier: 4;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier5 {
  recordId: string;
  assessmentTier: 5;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier6 {
  recordId: string;
  assessmentTier: 6;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier7 {
  recordId: string;
  assessmentTier: 7;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier8 {
  recordId: string;
  assessmentTier: 8;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier9 {
  recordId: string;
  assessmentTier: 9;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier10 {
  recordId: string;
  assessmentTier: 10;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier11 {
  recordId: string;
  assessmentTier: 11;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier12 {
  recordId: string;
  assessmentTier: 12;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier13 {
  recordId: string;
  assessmentTier: 13;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier14 {
  recordId: string;
  assessmentTier: 14;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier15 {
  recordId: string;
  assessmentTier: 15;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier16 {
  recordId: string;
  assessmentTier: 16;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier17 {
  recordId: string;
  assessmentTier: 17;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier18 {
  recordId: string;
  assessmentTier: 18;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier19 {
  recordId: string;
  assessmentTier: 19;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier20 {
  recordId: string;
  assessmentTier: 20;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier21 {
  recordId: string;
  assessmentTier: 21;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier22 {
  recordId: string;
  assessmentTier: 22;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier23 {
  recordId: string;
  assessmentTier: 23;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier24 {
  recordId: string;
  assessmentTier: 24;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier25 {
  recordId: string;
  assessmentTier: 25;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier26 {
  recordId: string;
  assessmentTier: 26;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier27 {
  recordId: string;
  assessmentTier: 27;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier28 {
  recordId: string;
  assessmentTier: 28;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier29 {
  recordId: string;
  assessmentTier: 29;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier30 {
  recordId: string;
  assessmentTier: 30;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier31 {
  recordId: string;
  assessmentTier: 31;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier32 {
  recordId: string;
  assessmentTier: 32;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier33 {
  recordId: string;
  assessmentTier: 33;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier34 {
  recordId: string;
  assessmentTier: 34;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier35 {
  recordId: string;
  assessmentTier: 35;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier36 {
  recordId: string;
  assessmentTier: 36;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier37 {
  recordId: string;
  assessmentTier: 37;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier38 {
  recordId: string;
  assessmentTier: 38;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier39 {
  recordId: string;
  assessmentTier: 39;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

export interface ClinicalAssessmentRecordTier40 {
  recordId: string;
  assessmentTier: 40;
  patientIdentifier: string;
  timestampUtc: string;
  compositeRiskIndex: number;
  confidenceUpper: number;
  confidenceLower: number;
  qualityCheckPassed: boolean;
  clinicalNotes: string[];
  flags: Record<string, boolean>;
}

