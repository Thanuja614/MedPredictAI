#!/usr/bin/env python3
"""
MedPredict AI — Demonstration Dataset & Schema Generator
Generates realistic, medically consistent, clearly labeled synthetic demonstration datasets
for all 10 core disease modules, accompanied by dataset_schema.json files.

LABEL: "SYNTHETIC DEMONSTRATION DATA — NOT REAL PATIENT DATA"
"""

import os
import sys
import json
from pathlib import Path
import random
import csv

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
DATASETS_ROOT = ROOT_DIR / "data" / "datasets"

random.seed(42)

DATASET_SPECS = {
    "diabetes": {
        "folder": "diabetes",
        "filename": "diabetes.csv",
        "description": "Synthetic demonstration dataset for Type-2 Diabetes risk screening",
        "target": "outcome",
        "fields": [
            ("pregnancies", "integer", 0, 15, "count"),
            ("glucose", "float", 65.0, 260.0, "mg/dL"),
            ("blood_pressure", "float", 50.0, 130.0, "mmHg"),
            ("skin_thickness", "float", 10.0, 60.0, "mm"),
            ("insulin", "float", 15.0, 550.0, "mu U/ml"),
            ("bmi", "float", 18.0, 52.0, "kg/m^2"),
            ("diabetes_pedigree", "float", 0.08, 2.20, "score"),
            ("age", "integer", 21, 85, "years"),
            ("outcome", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "pregnancies": random.randint(0, 8),
            "glucose": round(random.gauss(120, 32), 1),
            "blood_pressure": round(random.gauss(72, 12), 1),
            "skin_thickness": round(random.gauss(24, 8), 1),
            "insulin": round(max(15.0, random.gauss(140, 75)), 1),
            "bmi": round(max(18.0, random.gauss(31.5, 6.2)), 1),
            "diabetes_pedigree": round(max(0.08, random.gauss(0.48, 0.32)), 3),
            "age": random.randint(21, 75),
        }
    },
    "heart": {
        "folder": "heart",
        "filename": "heart.csv",
        "description": "Synthetic demonstration dataset for Coronary Artery / Heart Disease risk prediction",
        "target": "target",
        "fields": [
            ("age", "integer", 25, 80, "years"),
            ("sex", "integer", 0, 1, "code"),
            ("chest_pain_type", "integer", 0, 3, "code"),
            ("resting_bp", "float", 90.0, 200.0, "mmHg"),
            ("cholesterol", "float", 120.0, 480.0, "mg/dL"),
            ("fasting_blood_sugar", "integer", 0, 1, "flag"),
            ("resting_ecg", "integer", 0, 2, "code"),
            ("max_hr", "float", 75.0, 205.0, "bpm"),
            ("exercise_angina", "integer", 0, 1, "flag"),
            ("st_depression", "float", 0.0, 6.0, "mm"),
            ("st_slope", "integer", 0, 2, "code"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "age": random.randint(30, 78),
            "sex": random.choice([0, 1]),
            "chest_pain_type": random.choice([0, 1, 2, 3]),
            "resting_bp": round(random.gauss(131, 17), 1),
            "cholesterol": round(random.gauss(246, 51), 1),
            "fasting_blood_sugar": 1 if random.random() < 0.15 else 0,
            "resting_ecg": random.choice([0, 1, 2]),
            "max_hr": round(random.gauss(149, 23), 1),
            "exercise_angina": 1 if random.random() < 0.32 else 0,
            "st_depression": round(max(0.0, random.gauss(1.04, 1.15)), 1),
            "st_slope": random.choice([0, 1, 2]),
        }
    },
    "liver": {
        "folder": "liver",
        "filename": "liver.csv",
        "description": "Synthetic demonstration dataset for Hepatic Disease risk evaluation",
        "target": "target",
        "fields": [
            ("age", "integer", 12, 85, "years"),
            ("gender", "integer", 0, 1, "code"),
            ("total_bilirubin", "float", 0.4, 25.0, "mg/dL"),
            ("direct_bilirubin", "float", 0.1, 12.0, "mg/dL"),
            ("alkaline_phosphatase", "float", 80.0, 1800.0, "IU/L"),
            ("alamine_aminotransferase", "float", 10.0, 1200.0, "IU/L"),
            ("aspartate_aminotransferase", "float", 10.0, 1200.0, "IU/L"),
            ("total_proteins", "float", 2.5, 9.5, "g/dL"),
            ("albumin", "float", 1.2, 5.5, "g/dL"),
            ("ag_ratio", "float", 0.3, 2.8, "ratio"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "age": random.randint(18, 75),
            "gender": 1 if random.random() < 0.7 else 0,
            "total_bilirubin": round(max(0.4, random.gauss(2.8, 3.5)), 2),
            "direct_bilirubin": round(max(0.1, random.gauss(1.2, 2.1)), 2),
            "alkaline_phosphatase": round(max(80.0, random.gauss(290, 180)), 1),
            "alamine_aminotransferase": round(max(10.0, random.gauss(75, 95)), 1),
            "aspartate_aminotransferase": round(max(10.0, random.gauss(98, 120)), 1),
            "total_proteins": round(random.gauss(6.4, 1.0), 1),
            "albumin": round(random.gauss(3.1, 0.7), 1),
            "ag_ratio": round(max(0.3, random.gauss(0.95, 0.3)), 2),
        }
    },
    "kidney": {
        "folder": "kidney",
        "filename": "kidney.csv",
        "description": "Synthetic demonstration dataset for Chronic Kidney Disease (CKD) risk screening",
        "target": "target",
        "fields": [
            ("age", "integer", 15, 88, "years"),
            ("blood_pressure", "float", 50.0, 180.0, "mmHg"),
            ("specific_gravity", "float", 1.005, 1.030, "sg"),
            ("albumin", "integer", 0, 5, "grade"),
            ("sugar", "integer", 0, 5, "grade"),
            ("blood_urea", "float", 15.0, 250.0, "mg/dL"),
            ("serum_creatinine", "float", 0.5, 12.0, "mg/dL"),
            ("sodium", "float", 110.0, 160.0, "mEq/L"),
            ("potassium", "float", 2.5, 7.5, "mEq/L"),
            ("hemoglobin", "float", 4.5, 17.5, "g/dL"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "age": random.randint(18, 80),
            "blood_pressure": round(random.gauss(76, 14), 1),
            "specific_gravity": random.choice([1.005, 1.010, 1.015, 1.020, 1.025]),
            "albumin": random.choice([0, 0, 0, 1, 2, 3]),
            "sugar": random.choice([0, 0, 0, 0, 1, 2]),
            "blood_urea": round(max(15.0, random.gauss(55, 38)), 1),
            "serum_creatinine": round(max(0.5, random.gauss(2.1, 2.3)), 2),
            "sodium": round(random.gauss(137, 8), 1),
            "potassium": round(random.gauss(4.6, 0.8), 1),
            "hemoglobin": round(random.gauss(12.5, 2.7), 1),
        }
    },
    "breast_cancer": {
        "folder": "breast_cancer",
        "filename": "breast_cancer.csv",
        "description": "Synthetic demonstration dataset for Breast Malignancy cell morphological risk prediction",
        "target": "target",
        "fields": [
            ("radius_mean", "float", 6.0, 30.0, "mm"),
            ("texture_mean", "float", 9.0, 40.0, "score"),
            ("perimeter_mean", "float", 45.0, 190.0, "mm"),
            ("area_mean", "float", 140.0, 2500.0, "mm^2"),
            ("smoothness_mean", "float", 0.05, 0.18, "score"),
            ("compactness_mean", "float", 0.02, 0.32, "score"),
            ("concavity_mean", "float", 0.0, 0.45, "score"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "radius_mean": round(random.gauss(14.1, 3.5), 2),
            "texture_mean": round(random.gauss(19.3, 4.3), 2),
            "perimeter_mean": round(random.gauss(91.9, 24.3), 2),
            "area_mean": round(random.gauss(654.8, 351.9), 1),
            "smoothness_mean": round(random.gauss(0.096, 0.014), 4),
            "compactness_mean": round(random.gauss(0.104, 0.052), 4),
            "concavity_mean": round(max(0.0, random.gauss(0.088, 0.079)), 4),
        }
    },
    "stroke": {
        "folder": "stroke",
        "filename": "stroke.csv",
        "description": "Synthetic demonstration dataset for Cerebrovascular Stroke risk detection",
        "target": "stroke",
        "fields": [
            ("gender", "integer", 0, 1, "code"),
            ("age", "float", 18.0, 90.0, "years"),
            ("hypertension", "integer", 0, 1, "flag"),
            ("heart_disease", "integer", 0, 1, "flag"),
            ("ever_married", "integer", 0, 1, "flag"),
            ("avg_glucose_level", "float", 55.0, 280.0, "mg/dL"),
            ("bmi", "float", 15.0, 58.0, "kg/m^2"),
            ("stroke", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "gender": random.choice([0, 1]),
            "age": round(random.gauss(52, 18), 1),
            "hypertension": 1 if random.random() < 0.18 else 0,
            "heart_disease": 1 if random.random() < 0.12 else 0,
            "ever_married": 1 if random.random() < 0.65 else 0,
            "avg_glucose_level": round(random.gauss(106, 45), 1),
            "bmi": round(max(15.0, random.gauss(28.8, 7.5)), 1),
        }
    },
    "hypertension": {
        "folder": "hypertension",
        "filename": "hypertension.csv",
        "description": "Synthetic demonstration dataset for Essential Hypertension risk prediction",
        "target": "target",
        "fields": [
            ("age", "integer", 18, 88, "years"),
            ("systolic_bp", "float", 90.0, 220.0, "mmHg"),
            ("diastolic_bp", "float", 55.0, 135.0, "mmHg"),
            ("heart_rate", "float", 50.0, 160.0, "bpm"),
            ("bmi", "float", 17.0, 50.0, "kg/m^2"),
            ("cholesterol", "float", 120.0, 380.0, "mg/dL"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "age": random.randint(20, 80),
            "systolic_bp": round(random.gauss(128, 18), 1),
            "diastolic_bp": round(random.gauss(82, 11), 1),
            "heart_rate": round(random.gauss(74, 12), 1),
            "bmi": round(max(17.0, random.gauss(27.4, 5.2)), 1),
            "cholesterol": round(random.gauss(208, 42), 1),
        }
    },
    "anemia": {
        "folder": "anemia",
        "filename": "anemia.csv",
        "description": "Synthetic demonstration dataset for Hemoglobin & Erythrocyte Anemia deficiency",
        "target": "target",
        "fields": [
            ("gender", "integer", 0, 1, "code"),
            ("hemoglobin", "float", 5.0, 19.0, "g/dL"),
            ("mch", "float", 14.0, 38.0, "pg"),
            ("mchc", "float", 22.0, 38.0, "g/dL"),
            ("mcv", "float", 55.0, 115.0, "fL"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "gender": random.choice([0, 1]),
            "hemoglobin": round(random.gauss(12.8, 2.6), 1),
            "mch": round(random.gauss(28.2, 4.1), 1),
            "mchc": round(random.gauss(31.5, 3.2), 1),
            "mcv": round(random.gauss(88.4, 9.8), 1),
        }
    },
    "thyroid": {
        "folder": "thyroid",
        "filename": "thyroid.csv",
        "description": "Synthetic demonstration dataset for Thyroid Dysfunction (Hypo/Hyperthyroidism)",
        "target": "target",
        "fields": [
            ("age", "integer", 15, 88, "years"),
            ("sex", "integer", 0, 1, "code"),
            ("on_thyroxine", "integer", 0, 1, "flag"),
            ("tsh", "float", 0.05, 40.0, "mIU/L"),
            ("t3", "float", 0.2, 8.0, "nmol/L"),
            ("tt4", "float", 15.0, 280.0, "nmol/L"),
            ("t4u", "float", 0.3, 2.2, "ratio"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "age": random.randint(18, 78),
            "sex": random.choice([0, 1]),
            "on_thyroxine": 1 if random.random() < 0.12 else 0,
            "tsh": round(max(0.05, random.gauss(3.8, 5.2)), 2),
            "t3": round(max(0.2, random.gauss(1.9, 0.8)), 2),
            "tt4": round(max(15.0, random.gauss(108, 38)), 1),
            "t4u": round(max(0.3, random.gauss(0.98, 0.22)), 2),
        }
    },
    "parkinsons": {
        "folder": "parkinsons",
        "filename": "parkinsons.csv",
        "description": "Synthetic demonstration dataset for Acoustic Tremor & Parkinson's Disease risk screening",
        "target": "target",
        "fields": [
            ("fo_hz", "float", 88.0, 260.0, "Hz"),
            ("fhi_hz", "float", 100.0, 550.0, "Hz"),
            ("flo_hz", "float", 65.0, 240.0, "Hz"),
            ("jitter_percent", "float", 0.001, 0.04, "%"),
            ("shimmer", "float", 0.008, 0.12, "score"),
            ("hnr", "float", 8.0, 33.0, "dB"),
            ("rpde", "float", 0.25, 0.72, "score"),
            ("target", "integer", 0, 1, "class")
        ],
        "generator": lambda: {
            "fo_hz": round(random.gauss(154, 41), 2),
            "fhi_hz": round(random.gauss(197, 65), 2),
            "flo_hz": round(random.gauss(116, 43), 2),
            "jitter_percent": round(max(0.001, random.gauss(0.006, 0.004)), 4),
            "shimmer": round(max(0.008, random.gauss(0.03, 0.018)), 4),
            "hnr": round(random.gauss(21.8, 4.4), 1),
            "rpde": round(random.gauss(0.49, 0.10), 3),
        }
    }
}

def generate_datasets(num_rows=400):
    print("=" * 72)
    print(" MEDPREDICT AI -- SYNTHETIC DEMONSTRATION DATASET GENERATOR")
    print(" NOTICE: SYNTHETIC DEMONSTRATION DATA -- NOT REAL PATIENT DATA")
    print("=" * 72)

    for key, spec in DATASET_SPECS.items():
        folder = DATASETS_ROOT / spec["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        csv_path = folder / spec["filename"]
        schema_path = folder / "dataset_schema.json"

        field_names = [f[0] for f in spec["fields"]]
        target_name = spec["target"]

        # Generate rows
        rows = []
        for _ in range(num_rows):
            row = spec["generator"]()
            
            # Formulate realistic non-trivial target signal
            # Logistic calculation using key features
            score = 0.0
            if key == "diabetes":
                score = (row["glucose"] - 120)/30 + (row["bmi"] - 30)/8 + (row["age"] - 45)/20
            elif key == "heart":
                score = (row["age"] - 55)/15 + (row["cholesterol"] - 240)/50 + (row["resting_bp"] - 130)/20 + row["chest_pain_type"]*0.5
            elif key == "liver":
                score = (row["total_bilirubin"] - 2.0)/2 + (row["alkaline_phosphatase"] - 300)/150 + (row["alamine_aminotransferase"] - 60)/40
            elif key == "kidney":
                score = (row["serum_creatinine"] - 1.8)/1.5 + (row["blood_urea"] - 50)/30 + row["albumin"]*0.8 - (row["hemoglobin"] - 12)/3
            elif key == "breast_cancer":
                score = (row["radius_mean"] - 14)/3 + (row["concavity_mean"] - 0.08)/0.06 + (row["compactness_mean"] - 0.10)/0.04
            elif key == "stroke":
                score = (row["age"] - 60)/15 + row["hypertension"]*1.2 + (row["avg_glucose_level"] - 120)/40 + row["heart_disease"]*1.1
            elif key == "hypertension":
                score = (row["systolic_bp"] - 135)/15 + (row["diastolic_bp"] - 85)/10 + (row["bmi"] - 28)/5
            elif key == "anemia":
                score = (12.0 - row["hemoglobin"])/2.0 + (28.0 - row["mch"])/4.0
            elif key == "thyroid":
                score = (row["tsh"] - 4.5)/3.0 + (1.2 - row["t3"])/0.5
            elif key == "parkinsons":
                score = (row["jitter_percent"] - 0.006)/0.003 + (row["shimmer"] - 0.03)/0.015 - (row["hnr"] - 22)/4

            # Add random noise
            prob = 1.0 / (1.0 + random.expovariate(1.0) if score < 0 else 1.0 + 2.71828**(-score))
            target_val = 1 if prob > 0.5 else 0
            row[target_name] = target_val
            rows.append(row)

        # Write CSV
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(rows)

        # Write dataset_schema.json
        schema_def = {
            "dataset_name": f"{key.replace('_', ' ').title()} Demo Dataset",
            "disease_slug": key,
            "version": "1.0.0",
            "data_classification": "SYNTHETIC DEMONSTRATION DATA — NOT REAL PATIENT DATA",
            "row_count": num_rows,
            "target_variable": target_name,
            "features": [
                {
                    "name": f[0],
                    "data_type": f[1],
                    "min_value": f[2],
                    "max_value": f[3],
                    "unit": f[4]
                }
                for f in spec["fields"] if f[0] != target_name
            ]
        }
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(schema_def, f, indent=2)

        print(f"[+] Generated {key} dataset: {num_rows} rows -> {csv_path.relative_to(ROOT_DIR)}")

    print("=" * 72)
    print(" ALL 10 SYNTHETIC DEMO DATASETS & SCHEMAS SUCCESSFULLY GENERATED")
    print("=" * 72)

if __name__ == "__main__":
    generate_datasets()
