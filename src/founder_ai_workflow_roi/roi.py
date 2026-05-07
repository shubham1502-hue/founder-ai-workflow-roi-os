from __future__ import annotations

from typing import Any

import pandas as pd

from founder_ai_workflow_roi.utils import level_to_number, safe_float


def infer_complexity(row: pd.Series) -> str:
    risk_points = 0
    risk_points += level_to_number(row.get("data_sensitivity"), default=2)
    risk_points += level_to_number(row.get("process_variability"), default=2)
    risk_points += 2 if bool(row.get("requires_human_judgment")) else 0
    status = str(row.get("current_status", "")).strip().lower()
    if status in {"chaotic", "undefined", "ad_hoc", "ad hoc"}:
        risk_points += 2
    elif status in {"partially_documented", "partial", "partially documented"}:
        risk_points += 1

    if risk_points <= 4:
        return "low"
    if risk_points <= 7:
        return "medium"
    return "high"


def estimate_setup_cost(complexity: str, assumptions: dict[str, Any]) -> float:
    return safe_float(assumptions.get(f"default_setup_cost_{complexity}"), 0.0)


def estimate_coverage(complexity: str, assumptions: dict[str, Any]) -> float:
    coverage = assumptions.get("automation_coverage_by_complexity", {})
    return safe_float(coverage.get(complexity), 0.0)


def calculate_payback_period(setup_cost: float, net_monthly_savings: float) -> float:
    if net_monthly_savings <= 0:
        return 999.0
    return round(setup_cost / net_monthly_savings, 2)


def financial_roi_category(payback_period_months: float, net_monthly_savings: float) -> str:
    if net_monthly_savings <= 0:
        return "Negative or unclear ROI"
    if payback_period_months <= 1.5:
        return "Very fast payback"
    if payback_period_months <= 3:
        return "Fast payback"
    if payback_period_months <= 6:
        return "Moderate payback"
    return "Long payback"


def calculate_roi(df: pd.DataFrame, scoring_rules: dict[str, Any]) -> pd.DataFrame:
    assumptions = scoring_rules["assumptions"]
    hourly_cost = safe_float(assumptions.get("blended_hourly_cost"), 75.0)
    maintenance_percent = safe_float(assumptions.get("default_maintenance_cost_percent"), 0.12)

    enriched = df.copy()
    enriched["monthly_hours_spent"] = (
        enriched["frequency_per_month"]
        * enriched["avg_time_minutes_per_run"]
        * enriched["people_involved"]
        / 60.0
    ).round(2)
    enriched["estimated_monthly_cost"] = (enriched["monthly_hours_spent"] * hourly_cost).round(2)
    enriched["implementation_complexity"] = enriched.apply(infer_complexity, axis=1)
    enriched["automation_coverage_percent"] = enriched["implementation_complexity"].map(
        lambda complexity: estimate_coverage(complexity, assumptions)
    )
    enriched["estimated_hours_saved"] = (
        enriched["monthly_hours_spent"] * enriched["automation_coverage_percent"]
    ).round(2)
    enriched["estimated_monthly_savings"] = (
        enriched["estimated_hours_saved"] * hourly_cost
    ).round(2)
    enriched["estimated_setup_cost"] = enriched["implementation_complexity"].map(
        lambda complexity: estimate_setup_cost(complexity, assumptions)
    )
    enriched["estimated_monthly_maintenance_cost"] = (
        enriched["estimated_setup_cost"] * maintenance_percent
    ).round(2)
    enriched["net_monthly_savings_after_maintenance"] = (
        enriched["estimated_monthly_savings"] - enriched["estimated_monthly_maintenance_cost"]
    ).round(2)
    enriched["payback_period_months"] = enriched.apply(
        lambda row: calculate_payback_period(
            row["estimated_setup_cost"],
            row["net_monthly_savings_after_maintenance"],
        ),
        axis=1,
    )
    enriched["financial_roi_category"] = enriched.apply(
        lambda row: financial_roi_category(
            row["payback_period_months"],
            row["net_monthly_savings_after_maintenance"],
        ),
        axis=1,
    )
    return enriched
