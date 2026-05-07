from __future__ import annotations

from founder_ai_workflow_roi.config import load_scoring_rules
from founder_ai_workflow_roi.ingest import load_workflows
from founder_ai_workflow_roi.roi import calculate_payback_period, calculate_roi


def test_monthly_hours_and_savings_calculation() -> None:
    rules = load_scoring_rules("config/scoring_rules.yml")
    df = load_workflows("data/sample_workflows.csv").head(1)

    result = calculate_roi(df, rules).iloc[0]

    assert result["monthly_hours_spent"] == 24.0
    assert result["estimated_monthly_cost"] == 2040.0
    assert result["estimated_monthly_savings"] > 0
    assert result["net_monthly_savings_after_maintenance"] < result["estimated_monthly_savings"]


def test_payback_period_calculation() -> None:
    assert calculate_payback_period(1000, 500) == 2.0
    assert calculate_payback_period(1000, 0) == 999.0
