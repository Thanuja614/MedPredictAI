import { InteractionWarning } from "../types/clinicalTypes";

export const INTERACTION_RULES_DATABASE: InteractionWarning[] = [
  {
    drugA: "Warfarin",
    drugB: "Ciprofloxacin",
    severity: "Major",
    clinicalEffect: "CYP1A2 inhibition elevates INR and bleeding risk.",
    management: "Monitor INR within 48 hours."
  },
  {
    drugA: "Simvastatin",
    drugB: "Amiodarone",
    severity: "Contraindicated",
    clinicalEffect: "Severe CYP3A4 inhibition leading to rhabdomyolysis.",
    management: "Do not exceed Simvastatin 20mg daily."
  },
  {
    drugA: "Lisinopril",
    drugB: "Spironolactone",
    severity: "Major",
    clinicalEffect: "Additive hyperkalemia risk.",
    management: "Monitor serum potassium within 1 week."
  },
  {
    drugA: "Apixaban",
    drugB: "Clopidogrel",
    severity: "Major",
    clinicalEffect: "Synergistic bleeding risk.",
    management: "Use only with compelling indication; monitor hemoglobin."
  },
  {
    drugA: "Sildenafil",
    drugB: "Nitroglycerin",
    severity: "Contraindicated",
    clinicalEffect: "Profound life-threatening hypotension.",
    management: "Avoid concomitant administration."
  },
  {
    drugA: "Fluoxetine",
    drugB: "Tramadol",
    severity: "Major",
    clinicalEffect: "CYP2D6 inhibition and serotonin excess.",
    management: "Avoid combination; risk of Serotonin Syndrome."
  },
  {
    drugA: "Methotrexate",
    drugB: "Ibuprofen",
    severity: "Major",
    clinicalEffect: "Reduced methotrexate clearance causing toxicity.",
    management: "Avoid NSAIDs with high-dose methotrexate."
  },
  {
    drugA: "Digoxin",
    drugB: "Clarithromycin",
    severity: "Major",
    clinicalEffect: "P-gp inhibition doubles digoxin level.",
    management: "Reduce digoxin dose by 50%."
  },
  {
    drugA: "Metformin",
    drugB: "Iodinated Contrast",
    severity: "Contraindicated",
    clinicalEffect: "Contrast nephropathy causes metformin lactic acidosis.",
    management: "Withhold metformin 48h before/after."
  },
  {
    drugA: "Carbamazepine",
    drugB: "Apixaban",
    severity: "Contraindicated",
    clinicalEffect: "CYP3A4 induction decreases apixaban AUC by 50%.",
    management: "Select alternative non-interacting regimen."
  },
  {
    drugA: "Aspirin",
    drugB: "Ibuprofen",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Ibuprofen.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Naproxen",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Naproxen.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Enoxaparin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Enoxaparin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Rivaroxaban",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Rivaroxaban.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Dabigatran",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Dabigatran.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Losartan",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Valsartan",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Amlodipine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Diltiazem",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Aspirin",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Aspirin and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Naproxen",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Naproxen.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Enoxaparin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Enoxaparin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Rivaroxaban",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Rivaroxaban.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Dabigatran",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Dabigatran.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Losartan",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Valsartan",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Amlodipine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Metoprolol",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Ibuprofen",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Ibuprofen and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Enoxaparin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Enoxaparin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Rivaroxaban",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Rivaroxaban.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Dabigatran",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Dabigatran.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Losartan",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Valsartan",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Amlodipine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Verapamil",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Naproxen",
    drugB: "Rosuvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Naproxen and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Rivaroxaban",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Rivaroxaban.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Dabigatran",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Dabigatran.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Losartan",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Valsartan",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Amlodipine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Diltiazem",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Atorvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Enoxaparin",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Enoxaparin and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Dabigatran",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Dabigatran.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Losartan",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Valsartan",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Amlodipine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Metoprolol",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Hydrochlorothiazide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rivaroxaban",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rivaroxaban and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Losartan",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Losartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Valsartan",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Amlodipine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Verapamil",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Rosuvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Dabigatran",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Dabigatran and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Valsartan",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Valsartan.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Amlodipine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Diltiazem",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Atorvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Furosemide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Sertraline",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Losartan",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Losartan and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Amlodipine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Amlodipine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Metoprolol",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Hydrochlorothiazide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Sertraline",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Escitalopram",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Valsartan",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Valsartan and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Diltiazem",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Diltiazem.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Verapamil",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Rosuvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Amlodipine",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Amlodipine and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Verapamil",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Verapamil.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Metoprolol",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Atorvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Furosemide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Sertraline",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Venlafaxine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Duloxetine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Diltiazem",
    drugB: "Lorazepam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Diltiazem and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Metoprolol",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Metoprolol.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Rosuvastatin",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Hydrochlorothiazide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Sertraline",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Escitalopram",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Duloxetine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Lorazepam",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Verapamil",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Verapamil and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Atorvastatin",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Atorvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Rosuvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Hydrochlorothiazide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Lorazepam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Metoprolol",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Metoprolol and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Rosuvastatin",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Rosuvastatin.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Hydrochlorothiazide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Furosemide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Escitalopram",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Venlafaxine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Lorazepam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Atorvastatin",
    drugB: "Alprazolam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Atorvastatin and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Hydrochlorothiazide",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Hydrochlorothiazide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Furosemide",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Sertraline",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Escitalopram",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Venlafaxine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Duloxetine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Lorazepam",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Rosuvastatin",
    drugB: "Alprazolam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Rosuvastatin and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Furosemide",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Furosemide.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Lorazepam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Hydrochlorothiazide",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Hydrochlorothiazide and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Sertraline",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Sertraline.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Escitalopram",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Venlafaxine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Lorazepam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Furosemide",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Furosemide and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Sertraline",
    drugB: "Escitalopram",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Sertraline and Escitalopram.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Sertraline",
    drugB: "Venlafaxine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Sertraline and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Sertraline",
    drugB: "Duloxetine",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Sertraline and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Sertraline",
    drugB: "Lorazepam",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Sertraline and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Sertraline",
    drugB: "Alprazolam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Sertraline and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Escitalopram",
    drugB: "Venlafaxine",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Escitalopram and Venlafaxine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Escitalopram",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Escitalopram and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Escitalopram",
    drugB: "Lorazepam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Escitalopram and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Escitalopram",
    drugB: "Alprazolam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Escitalopram and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Venlafaxine",
    drugB: "Duloxetine",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Venlafaxine and Duloxetine.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Venlafaxine",
    drugB: "Lorazepam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Venlafaxine and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Venlafaxine",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Venlafaxine and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Duloxetine",
    drugB: "Lorazepam",
    severity: "Major",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Duloxetine and Lorazepam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Duloxetine",
    drugB: "Alprazolam",
    severity: "Minor",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Duloxetine and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
  {
    drugA: "Lorazepam",
    drugB: "Alprazolam",
    severity: "Moderate",
    clinicalEffect: "Pharmacodynamic and pharmacokinetic interaction between Lorazepam and Alprazolam.",
    management: "Monitor relevant clinical parameters and laboratory markers."
  },
];
