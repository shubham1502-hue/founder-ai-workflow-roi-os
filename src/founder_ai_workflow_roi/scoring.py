from __future__ import annotations

from typing import Any

import pandas as pd

from founder_ai_workflow_roi.utils import clamp, level_to_risk_score, one_to_five_score, safe_float


def payback_score(months: float) -> float:
    if months <= 1:
        return 100.0
    if months <= 3:
        return 85.0
    if months <= 6:
        return 60.0
    if months <= 12:
        return 35.0
    return 10.0


def setup_cost_score(cost: float) -> float:
    if cost <= 500:
        return 100.0
    if cost <= 1500:
        return 80.0
    if cost <= 4000:
        return 55.0
    if cost <= 8000:
        return 30.0
    return 10.0


def effort_burden_score(complexity: str) -> float:
    return {
        "low": 25.0,
        "medium": 55.0,
        "high": 85.0,
    }.get(complexity, 55.0)


def effort_inverse_score(complexity: str) -> float:
    return 100.0 - effort_burden_score(complexity)


def priority_bucket(score: float) -> str:
    if score >= 80:
        return "Automate now"
    if score >= 60:
        return "Pilot first"
    if score >= 40:
        return "Document first"
    return "Keep manual"


def calculate_component_scores(
    row: pd.Series,
    company_profile: dict[str, Any],
    scoring_rules: dict[str, Any],
) -> dict[str, float]:
    thresholds = scoring_rules.get("normalization_thresholds", {})
    max_hours_saved = max(safe_float(thresholds.get("hours_saved_for_max_score"), 12.0), 1.0)
    max_frequency = max(safe_float(thresholds.get("frequency_per_month_for_max_score"), 30.0), 1.0)
    max_error_rate = max(safe_float(thresholds.get("error_rate_percent_for_max_score"), 20.0), 1.0)

    time_saved = clamp((safe_float(row.get("estimated_hours_saved")) / max_hours_saved) * 100.0)
    frequency = clamp((safe_float(row.get("frequency_per_month")) / max_frequency) * 100.0)
    business_impact = one_to_five_score(row.get("business_impact"))
    customer_impact = one_to_five_score(row.get("customer_impact"))
    error_reduction = clamp((safe_float(row.get("error_rate_percent")) / max_error_rate) * 100.0)
    implementation_effort = effort_inverse_score(str(row.get("implementation_complexity", "medium")))
    data_sensitivity_risk = 100.0 - level_to_risk_score(row.get("data_sensitivity"))
    process_variability_risk = 100.0 - level_to_risk_score(row.get("process_variability"))
    human_judgment_risk = 35.0 if bool(row.get("requires_human_judgment")) else 100.0
    cost_to_automate = setup_cost_score(safe_float(row.get("estimated_setup_cost")))
    payback_period = payback_score(safe_float(row.get("payback_period_months"), 999.0))

    prioritized_functions = set(company_profile.get("functions_to_prioritize", []) or [])
    avoided_functions = set(company_profile.get("functions_to_avoid_for_now", []) or [])
    function_name = str(row.get("function", ""))
    strategic_leverage = (business_impact * 0.55) + (customer_impact * 0.25) + (time_saved * 0.20)
    if function_name in prioritized_functions:
        strategic_leverage += 10.0
    if function_name in avoided_functions:
        strategic_leverage -= 20.0

    return {
        "time_saved": time_saved,
        "workflow_frequency": frequency,
        "business_impact": business_impact,
        "customer_impact": customer_impact,
        "error_reduction": error_reduction,
        "implementation_effort": implementation_effort,
        "data_sensitivity_risk": data_sensitivity_risk,
        "process_variability_risk": process_variability_risk,
        "human_judgment_risk": human_judgment_risk,
        "cost_to_automate": cost_to_automate,
        "payback_period": payback_period,
        "strategic_leverage": clamp(strategic_leverage),
    }


def weighted_priority_score(component_scores: dict[str, float], weights: dict[str, Any]) -> float:
    total_weight = sum(safe_float(value) for value in weights.values())
    if total_weight <= 0:
        raise ValueError("Scoring weights must sum to a positive number")
    weighted = sum(component_scores[key] * safe_float(weights[key]) for key in weights)
    return round(clamp(weighted / total_weight), 1)


def add_priority_scores(
    df: pd.DataFrame,
    company_profile: dict[str, Any],
    scoring_rules: dict[str, Any],
) -> pd.DataFrame:
    weights = scoring_rules["weights"]
    enriched = df.copy()

    component_rows = [
        calculate_component_scores(row, company_profile, scoring_rules)
        for _, row in enriched.iterrows()
    ]
    component_df = pd.DataFrame(component_rows)
    for column in component_df.columns:
        enriched[f"component_{column}"] = component_df[column].values

    enriched["priority_score"] = component_df.apply(
        lambda row: weighted_priority_score(row.to_dict(), weights),
        axis=1,
    )
    enriched["roi_category"] = enriched["priority_score"].map(priority_bucket)
    return enriched
