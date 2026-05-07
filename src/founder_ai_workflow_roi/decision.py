from __future__ import annotations

from typing import Any

import pandas as pd

from founder_ai_workflow_roi.scoring import effort_burden_score
from founder_ai_workflow_roi.utils import level_to_risk_score, safe_float


def impact_score(row: pd.Series) -> float:
    business = safe_float(row.get("component_business_impact"))
    customer = safe_float(row.get("component_customer_impact"))
    time_saved = safe_float(row.get("component_time_saved"))
    error = safe_float(row.get("component_error_reduction"))
    return round((business * 0.35) + (customer * 0.25) + (time_saved * 0.25) + (error * 0.15), 1)


def risk_score(row: pd.Series) -> float:
    data = level_to_risk_score(row.get("data_sensitivity"))
    variability = level_to_risk_score(row.get("process_variability"))
    judgment = 75.0 if bool(row.get("requires_human_judgment")) else 15.0
    return round((data * 0.35) + (variability * 0.35) + (judgment * 0.30), 1)


def matrix_quadrant(row: pd.Series) -> str:
    impact = safe_float(row.get("impact_score"))
    effort = safe_float(row.get("effort_score"))
    risk = safe_float(row.get("risk_score"))
    status = str(row.get("current_status", "")).lower()

    if risk >= 70 or safe_float(row.get("priority_score")) < 40:
        return "Avoid for now"
    if status in {"chaotic", "undefined", "ad_hoc", "ad hoc"} or (
        risk >= 55 and effort >= 55
    ):
        return "Process first"
    if impact >= 60 and effort <= 50 and risk <= 50:
        return "Quick wins"
    return "Strategic bets"


def recommended_timing(quadrant: str) -> str:
    return {
        "Quick wins": "This week",
        "Strategic bets": "Next 30 days",
        "Process first": "Document in next 2 weeks",
        "Avoid for now": "Do not automate yet",
    }[quadrant]


def add_matrix_scores(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["impact_score"] = enriched.apply(impact_score, axis=1)
    enriched["effort_score"] = enriched["implementation_complexity"].map(effort_burden_score)
    enriched["risk_score"] = enriched.apply(risk_score, axis=1)
    enriched["quadrant"] = enriched.apply(matrix_quadrant, axis=1)
    enriched["recommended_timing"] = enriched["quadrant"].map(recommended_timing)
    return enriched


def recommend_workflow(row: pd.Series, company_profile: dict[str, Any]) -> dict[str, str | float]:
    priority = safe_float(row.get("priority_score"))
    impact = safe_float(row.get("impact_score"))
    effort = safe_float(row.get("effort_score"))
    risk = safe_float(row.get("risk_score"))
    monthly_savings = safe_float(row.get("net_monthly_savings_after_maintenance"))
    human_judgment = bool(row.get("requires_human_judgment"))
    business_impact = safe_float(row.get("business_impact"))
    customer_impact = safe_float(row.get("customer_impact"))
    frequency = safe_float(row.get("frequency_per_month"))
    status = str(row.get("current_status", "")).lower()
    owner = str(row.get("owner_role", "Founder"))

    if status in {"chaotic", "undefined", "ad_hoc", "ad hoc"}:
        return {
            "recommendation": "Document process first",
            "reason": "The workflow is not stable enough for reliable automation.",
            "risks": "Automating an undefined process can create rework and inconsistent outputs.",
            "suggested_owner": owner,
            "next_step": "Write the current steps, inputs, outputs, exceptions, and approval points.",
            "decision_confidence": 0.78,
        }

    if human_judgment and business_impact >= 4 and customer_impact >= 4 and frequency >= 12:
        return {
            "recommendation": "Hire",
            "reason": "This is strategic, judgment-heavy work that needs accountable ownership.",
            "risks": "AI can assist with research and drafts, but final decisions need human context.",
            "suggested_owner": "Founder or functional lead",
            "next_step": "Define the role scope and use AI only for preparation and analysis support.",
            "decision_confidence": 0.72,
        }

    if impact <= 65 and monthly_savings > 500 and risk <= 55 and not human_judgment:
        return {
            "recommendation": "Outsource",
            "reason": "The work is repetitive and not strategically important enough to own internally yet.",
            "risks": "External quality may vary without a clear brief and acceptance checklist.",
            "suggested_owner": "Founder Office or Ops",
            "next_step": "Create a short SOP and test one vendor or contractor before scaling.",
            "decision_confidence": 0.68,
        }

    if (
        priority >= 80
        and risk <= 50
        and effort <= 55
        and monthly_savings > 400
    ):
        return {
            "recommendation": "Automate now",
            "reason": "The workflow has strong savings potential, frequent repetition, and manageable risk.",
            "risks": "Monitor quality drift and keep a human approval checkpoint during rollout.",
            "suggested_owner": owner,
            "next_step": "Build a narrow automation for the highest-volume path and measure time saved.",
            "decision_confidence": 0.86,
        }

    if priority >= 60 and impact >= 55 and risk <= 70 and monthly_savings > 0:
        return {
            "recommendation": "Run AI-assisted pilot",
            "reason": "The upside is meaningful, but the workflow needs validation before full automation.",
            "risks": "Pilot outputs may vary until examples, guardrails, and approval rules are explicit.",
            "suggested_owner": owner,
            "next_step": "Run a two-week AI-assisted pilot with sampled outputs reviewed by a human.",
            "decision_confidence": 0.76,
        }

    return {
        "recommendation": "Keep manual for now",
        "reason": "The current ROI, risk, or frequency does not justify automation work yet.",
        "risks": "Manual drag can grow if volume increases, so revisit when frequency or pain changes.",
        "suggested_owner": owner,
        "next_step": "Track volume for one month and revisit if time spent or errors increase.",
        "decision_confidence": 0.70,
    }


def add_decisions(df: pd.DataFrame, company_profile: dict[str, Any]) -> pd.DataFrame:
    enriched = df.copy()
    decisions = [recommend_workflow(row, company_profile) for _, row in enriched.iterrows()]
    decisions_df = pd.DataFrame(decisions)
    for column in decisions_df.columns:
        enriched[column] = decisions_df[column].values
    return enriched
