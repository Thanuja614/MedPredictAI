/**
 * MedPredict AI — Believable Fictional Clinical Data
 * High-fidelity demonstration patient profiles and lab results
 */

export interface PatientRecord {
  id: string;
  mrn: string;
  name: string;
  age: number;
  gender: 'Female' | 'Male';
  dob: string;
  bloodType: string;
  phone: string;
  primaryPhysician: string;
  department: string;
  lastVisit: string;
  primaryCondition: string;
  riskTier: 'LOW' | 'MODERATE' | 'HIGH' | 'CRITICAL';
  calibratedProbability: number;
  velocityTrend: 'IMPROVING' | 'STABLE' | 'ESCALATING';
  vitals: {
    bloodPressure: string;
    systolic: number;
    diastolic: number;
    heartRate: number;
    respiratoryRate: number;
    temperature: number;
    bmi: number;
    spo2: number;
  };
  labs: {
    fastingGlucose: number;
    hba1c: number;
    totalCholesterol: number;
    hdl: number;
    ldl: number;
    triglycerides: number;
    serumCreatinine: number;
    egfr: number;
    hsCrp: number;
  };
  history: {
    smoker: boolean;
    diabetes: boolean;
    hypertension: boolean;
    familyCad: boolean;
    chronicKidneyDisease: boolean;
  };
  activeMedications: string[];
  allergies: string[];
  timeline: Array<{
    id: string;
    date: string;
    year: string;
    title: string;
    category: 'prediction' | 'lab' | 'encounter' | 'medication';
    description: string;
    provider: string;
    badge?: string;
  }>;
}

export const DEMO_PATIENTS: PatientRecord[] = [
  {
    id: 'pt-1',
    mrn: 'MP-2026-01482',
    name: 'Ananya Rao',
    age: 46,
    gender: 'Female',
    dob: '1980-04-14',
    bloodType: 'B+',
    phone: '+1 (555) 384-9102',
    primaryPhysician: 'Dr. Sarah Mitchell, MD',
    department: 'Preventative Cardiology',
    lastVisit: '2026-09-08',
    primaryCondition: 'Essential Hypertension & Prediabetes',
    riskTier: 'MODERATE',
    calibratedProbability: 68.4,
    velocityTrend: 'ESCALATING',
    vitals: {
      bloodPressure: '138/88',
      systolic: 138,
      diastolic: 88,
      heartRate: 82,
      respiratoryRate: 15,
      temperature: 36.8,
      bmi: 27.4,
      spo2: 98,
    },
    labs: {
      fastingGlucose: 126,
      hba1c: 6.2,
      totalCholesterol: 218,
      hdl: 44,
      ldl: 138,
      triglycerides: 180,
      serumCreatinine: 0.92,
      egfr: 88,
      hsCrp: 2.8,
    },
    history: {
      smoker: false,
      diabetes: false,
      hypertension: true,
      familyCad: true,
      chronicKidneyDisease: false,
    },
    activeMedications: ['Telmisartan 40mg daily', 'Atorvastatin 20mg nocte', 'Metformin 500mg daily'],
    allergies: ['Penicillin (Mild urticaria)'],
    timeline: [
      {
        id: 'tl-1',
        date: 'Sep 08, 2026',
        year: '2026',
        title: 'Multi-Disease Risk Assessment Completed',
        category: 'prediction',
        description: 'Comprehensive 10-disease evaluation flagged moderate cardiovascular risk (68.4%) and metabolic resistance.',
        provider: 'Dr. Sarah Mitchell, MD',
        badge: 'Moderate Risk (68.4%)',
      },
      {
        id: 'tl-2',
        date: 'Aug 22, 2026',
        year: '2026',
        title: 'Fasting Lipid & Glycemic Panel Recorded',
        category: 'lab',
        description: 'HbA1c elevated at 6.2%; fasting glucose 126 mg/dL; LDL cholesterol 138 mg/dL.',
        provider: 'Central Pathology Laboratory',
        badge: 'HbA1c 6.2%',
      },
      {
        id: 'tl-3',
        date: 'Mar 15, 2025',
        year: '2025',
        title: 'Annual Comprehensive Medical Examination',
        category: 'encounter',
        description: 'Baseline resting EKG normal sinus rhythm; bilateral carotid ultrasound showed minimal intimal thickening.',
        provider: 'Dr. Sarah Mitchell, MD',
      },
      {
        id: 'tl-4',
        date: 'Jan 10, 2025',
        year: '2025',
        title: 'Antihypertensive Pharmacotherapy Updated',
        category: 'medication',
        description: 'Switched from Amlodipine to Telmisartan 40mg due to mild pedal edema; blood pressure normalized.',
        provider: 'Dr. Sarah Mitchell, MD',
        badge: 'Telmisartan 40mg',
      },
      {
        id: 'tl-5',
        date: 'Oct 04, 2024',
        year: '2024',
        title: 'Initial Outpatient Clinical Registration',
        category: 'encounter',
        description: 'Patient presented for preventative health screening following family history of paternal myocardial infarction.',
        provider: 'Dr. Robert Hayes, MD',
      },
    ],
  },
  {
    id: 'pt-2',
    mrn: 'MP-2026-00912',
    name: 'Marcus Vance',
    age: 62,
    gender: 'Male',
    dob: '1964-07-29',
    bloodType: 'O+',
    phone: '+1 (555) 729-4481',
    primaryPhysician: 'Dr. Sarah Mitchell, MD',
    department: 'Interventional Cardiology',
    lastVisit: '2026-09-10',
    primaryCondition: 'Type 2 Diabetes Mellitus & Dyslipidemia',
    riskTier: 'HIGH',
    calibratedProbability: 84.2,
    velocityTrend: 'ESCALATING',
    vitals: {
      bloodPressure: '154/94',
      systolic: 154,
      diastolic: 94,
      heartRate: 76,
      respiratoryRate: 16,
      temperature: 37.0,
      bmi: 31.2,
      spo2: 96,
    },
    labs: {
      fastingGlucose: 168,
      hba1c: 7.8,
      totalCholesterol: 245,
      hdl: 38,
      ldl: 162,
      triglycerides: 240,
      serumCreatinine: 1.34,
      egfr: 58,
      hsCrp: 4.6,
    },
    history: {
      smoker: true,
      diabetes: true,
      hypertension: true,
      familyCad: true,
      chronicKidneyDisease: true,
    },
    activeMedications: ['Empagliflozin 25mg daily', 'Rosuvastatin 40mg nocte', 'Lisinopril 20mg daily', 'Aspirin 81mg'],
    allergies: ['Sulfa drugs (Rash)'],
    timeline: [
      {
        id: 'tl-21',
        date: 'Sep 10, 2026',
        year: '2026',
        title: 'High-Risk Triage Evaluation',
        category: 'prediction',
        description: 'Multi-organ risk evaluation confirmed high cerebrovascular and CAD vulnerability (84.2%).',
        provider: 'Dr. Sarah Mitchell, MD',
        badge: 'High Risk (84.2%)',
      },
      {
        id: 'tl-22',
        date: 'Jul 14, 2026',
        year: '2026',
        title: 'Microalbuminuria & Renal Function Panel',
        category: 'lab',
        description: 'Urine albumin-to-creatinine ratio (uACR) 180 mg/g; eGFR reduced to 58 mL/min (CKD Stage 3a).',
        provider: 'Clinical Nephrology Lab',
        badge: 'eGFR 58',
      },
    ],
  },
  {
    id: 'pt-3',
    mrn: 'MP-2026-02319',
    name: 'Eleanor Chen',
    age: 38,
    gender: 'Female',
    dob: '1988-11-03',
    bloodType: 'A+',
    phone: '+1 (555) 914-0239',
    primaryPhysician: 'Dr. Sarah Mitchell, MD',
    department: 'Executive Health Screening',
    lastVisit: '2026-08-30',
    primaryCondition: 'Routine Wellness Evaluation',
    riskTier: 'LOW',
    calibratedProbability: 14.8,
    velocityTrend: 'IMPROVING',
    vitals: {
      bloodPressure: '116/74',
      systolic: 116,
      diastolic: 74,
      heartRate: 68,
      respiratoryRate: 14,
      temperature: 36.6,
      bmi: 22.1,
      spo2: 99,
    },
    labs: {
      fastingGlucose: 92,
      hba1c: 5.1,
      totalCholesterol: 172,
      hdl: 62,
      ldl: 94,
      triglycerides: 98,
      serumCreatinine: 0.78,
      egfr: 104,
      hsCrp: 0.6,
    },
    history: {
      smoker: false,
      diabetes: false,
      hypertension: false,
      familyCad: false,
      chronicKidneyDisease: false,
    },
    activeMedications: ['Daily Multivitamin', 'Vitamin D3 1000 IU'],
    allergies: ['No known drug allergies (NKDA)'],
    timeline: [
      {
        id: 'tl-31',
        date: 'Aug 30, 2026',
        year: '2026',
        title: 'Preventative Health Assessment',
        category: 'prediction',
        description: 'Comprehensive baseline evaluation verified low multi-disease risk (14.8%).',
        provider: 'Dr. Sarah Mitchell, MD',
        badge: 'Low Risk (14.8%)',
      },
    ],
  },
  {
    id: 'pt-4',
    mrn: 'MP-2026-00438',
    name: "David O'Connor",
    age: 71,
    gender: 'Male',
    dob: '1955-02-19',
    bloodType: 'AB+',
    phone: '+1 (555) 441-8890',
    primaryPhysician: 'Dr. Sarah Mitchell, MD',
    department: 'Nephrology & Hypertension',
    lastVisit: '2026-09-02',
    primaryCondition: 'Chronic Kidney Disease Stage 3b & Resistant HTN',
    riskTier: 'HIGH',
    calibratedProbability: 79.1,
    velocityTrend: 'STABLE',
    vitals: {
      bloodPressure: '142/86',
      systolic: 142,
      diastolic: 86,
      heartRate: 84,
      respiratoryRate: 16,
      temperature: 36.9,
      bmi: 28.6,
      spo2: 97,
    },
    labs: {
      fastingGlucose: 114,
      hba1c: 5.9,
      totalCholesterol: 198,
      hdl: 41,
      ldl: 122,
      triglycerides: 195,
      serumCreatinine: 1.65,
      egfr: 44,
      hsCrp: 3.2,
    },
    history: {
      smoker: false,
      diabetes: false,
      hypertension: true,
      familyCad: true,
      chronicKidneyDisease: true,
    },
    activeMedications: ['Chlorthalidone 25mg daily', 'Amlodipine 10mg daily', 'Losartan 100mg daily'],
    allergies: ['ACE Inhibitors (Intractable dry cough)'],
    timeline: [
      {
        id: 'tl-41',
        date: 'Sep 02, 2026',
        year: '2026',
        title: 'Renal & Hemodynamic Review',
        category: 'encounter',
        description: 'eGFR stabilized at 44 mL/min on triple-therapy regimen without hyperkalemia.',
        provider: 'Dr. Sarah Mitchell, MD',
      },
    ],
  },
  {
    id: 'pt-5',
    mrn: 'MP-2026-01180',
    name: 'Fatima Al-Mansoor',
    age: 53,
    gender: 'Female',
    dob: '1973-09-12',
    bloodType: 'O-',
    phone: '+1 (555) 672-3391',
    primaryPhysician: 'Dr. Sarah Mitchell, MD',
    department: 'Endocrine & Metabolic Clinic',
    lastVisit: '2026-09-05',
    primaryCondition: 'Hashimoto Thyroiditis & Metabolic Syndrome',
    riskTier: 'MODERATE',
    calibratedProbability: 52.6,
    velocityTrend: 'IMPROVING',
    vitals: {
      bloodPressure: '130/82',
      systolic: 130,
      diastolic: 82,
      heartRate: 72,
      respiratoryRate: 14,
      temperature: 36.7,
      bmi: 26.0,
      spo2: 98,
    },
    labs: {
      fastingGlucose: 108,
      hba1c: 5.7,
      totalCholesterol: 204,
      hdl: 48,
      ldl: 126,
      triglycerides: 160,
      serumCreatinine: 0.85,
      egfr: 94,
      hsCrp: 1.8,
    },
    history: {
      smoker: false,
      diabetes: false,
      hypertension: true,
      familyCad: false,
      chronicKidneyDisease: false,
    },
    activeMedications: ['Levothyroxine 75 mcg daily', 'Omega-3 Acid Ethyl Esters 2g'],
    allergies: ['No known drug allergies (NKDA)'],
    timeline: [
      {
        id: 'tl-51',
        date: 'Sep 05, 2026',
        year: '2026',
        title: 'Thyroid Hormonal Titration',
        category: 'lab',
        description: 'TSH adjusted to 2.4 mIU/L on 75 mcg dosage; clinical fatigue resolved.',
        provider: 'Dr. Sarah Mitchell, MD',
        badge: 'TSH 2.4 mIU/L',
      },
    ],
  },
];
