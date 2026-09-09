"""
MedPredict AI — Longitudinal Risk Analytics & Population Health Service
Provides risk trajectory velocity, multi-timepoint patient timelines,
and cohort risk distribution analytics.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
import json
import numpy as np
from sqlalchemy.orm import Session
from sqlalchemy import select, func, desc, asc

from backend.app.models.prediction import Prediction, PredictionInput, Explanation
from backend.app.models.patient import Patient, Assessment
from backend.app.models.disease import Disease
from backend.app.models.user import User


class AnalyticsService:
    @staticmethod
    def get_patient_timeline(
        db: Session,
        patient_id: str,
        disease_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Retrieves chronological risk scores for a patient, calculating
        risk delta, progression velocity, and trend trajectory.
        """
        query = select(Prediction).where(Prediction.patient_id == patient_id)
        if disease_id:
            query = query.where(Prediction.disease_id == disease_id)
        query = query.order_by(asc(Prediction.created_at))

        predictions = db.execute(query).scalars().all()
        
        timeline_points = []
        prev_prob = None
        prev_time = None
        velocities = []

        for p in predictions:
            point = {
                "prediction_id": p.id,
                "disease_id": p.disease_id,
                "disease_name": p.disease.name if p.disease else "Unknown Disease",
                "probability": round(float(p.probability), 4),
                "risk_level": p.risk_level,
                "created_at": p.created_at.isoformat() if p.created_at else None,
                "delta": None,
                "days_since_prev": None
            }

            if prev_prob is not None and prev_time is not None and p.created_at:
                delta = float(p.probability) - prev_prob
                days = max(1, (p.created_at - prev_time).days)
                point["delta"] = round(delta, 4)
                point["days_since_prev"] = days
                # Velocity: risk change per 30-day month
                monthly_velocity = (delta / days) * 30.0
                velocities.append(monthly_velocity)
                point["monthly_velocity"] = round(monthly_velocity, 4)
            else:
                point["monthly_velocity"] = 0.0

            prev_prob = float(p.probability)
            prev_time = p.created_at
            timeline_points.append(point)

        # Determine trajectory classification
        if not velocities:
            trajectory = "BASELINE"
        else:
            avg_vel = float(np.mean(velocities))
            if avg_vel > 0.05:
                trajectory = "ESCALATING"
            elif avg_vel < -0.05:
                trajectory = "IMPROVING"
            else:
                trajectory = "STABLE"

        return {
            "patient_id": patient_id,
            "total_assessments": len(timeline_points),
            "trajectory": trajectory,
            "timeline": timeline_points,
            "disclaimer": (
                "Longitudinal progression tracking is an educational clinical decision-support tool. "
                "Velocities and risk classifications must be verified with formal laboratory and diagnostic evaluations."
            )
        }

    @staticmethod
    def get_population_risk_distribution(
        db: Session,
        disease_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Aggregates risk levels and probability percentiles across the cohort,
        optionally filtered by disease.
        """
        query = select(Prediction)
        if disease_id:
            query = query.where(Prediction.disease_id == disease_id)

        preds = db.execute(query).scalars().all()

        total = len(preds)
        if total == 0:
            return {
                "total_inferences": 0,
                "distribution": {"LOW": 0, "MODERATE": 0, "HIGH": 0},
                "percentages": {"LOW": 0.0, "MODERATE": 0.0, "HIGH": 0.0},
                "summary_stats": {"mean": 0.0, "median": 0.0, "min": 0.0, "max": 0.0, "std": 0.0},
                "demographic_breakdown": []
            }

        probs = [float(p.probability) for p in preds]
        counts = {"LOW": 0, "MODERATE": 0, "HIGH": 0}
        for p in preds:
            counts[p.risk_level] = counts.get(p.risk_level, 0) + 1

        pcts = {k: round((v / total) * 100, 2) for k, v in counts.items()}

        stats = {
            "mean": round(float(np.mean(probs)), 4),
            "median": round(float(np.median(probs)), 4),
            "min": round(float(np.min(probs)), 4),
            "max": round(float(np.max(probs)), 4),
            "std": round(float(np.std(probs)), 4)
        }

        # Demographic distribution (for predictions with linked patients)
        demo_groups = {}
        for p in preds:
            if p.patient:
                age = 0
                if hasattr(p.patient, "date_of_birth") and p.patient.date_of_birth:
                    today = datetime.now(timezone.utc).date()
                    age = today.year - p.patient.date_of_birth.year

                if age < 30:
                    age_bracket = "<30"
                elif age <= 45:
                    age_bracket = "30-45"
                elif age <= 60:
                    age_bracket = "46-60"
                else:
                    age_bracket = "60+"
                
                gender = p.patient.gender if hasattr(p.patient, "gender") and p.patient.gender else "Unknown"
                group_key = f"{gender} ({age_bracket})"
                if group_key not in demo_groups:
                    demo_groups[group_key] = {"LOW": 0, "MODERATE": 0, "HIGH": 0, "total": 0}
                demo_groups[group_key][p.risk_level] += 1
                demo_groups[group_key]["total"] += 1

        demographic_breakdown = [
            {"group": k, **v}
            for k, v in demo_groups.items()
        ]

        return {
            "disease_id": disease_id,
            "total_inferences": total,
            "distribution": counts,
            "percentages": pcts,
            "summary_stats": stats,
            "demographic_breakdown": demographic_breakdown
        }

    @staticmethod
    def get_system_overview(db: Session) -> Dict[str, Any]:
        """Provides high-level platform statistics for the administrator and doctor dashboards."""
        total_patients = db.execute(select(func.count(Patient.id))).scalar_one()
        total_predictions = db.execute(select(func.count(Prediction.id))).scalar_one()
        total_diseases = db.execute(select(func.count(Disease.id))).scalar_one()

        high_risk_count = db.execute(
            select(func.count(Prediction.id)).where(Prediction.risk_level == "HIGH")
        ).scalar_one()

        # Recent 5 predictions
        recent_preds = db.execute(
            select(Prediction)
            .order_by(desc(Prediction.created_at))
            .limit(5)
        ).scalars().all()

        recent_feed = []
        for p in recent_preds:
            p_name = "Anonymous"
            if p.patient and p.patient.user:
                p_name = f"{p.patient.user.first_name} {p.patient.user.last_name}"
            recent_feed.append({
                "id": p.id,
                "disease_name": p.disease.name if p.disease else "Unknown",
                "risk_level": p.risk_level,
                "probability": round(float(p.probability), 3),
                "patient_name": p_name,
                "created_at": p.created_at.isoformat() if p.created_at else None
            })

        return {
            "total_patients": total_patients,
            "total_predictions": total_predictions,
            "total_diseases": total_diseases,
            "high_risk_count": high_risk_count,
            "recent_activity": recent_feed
        }

