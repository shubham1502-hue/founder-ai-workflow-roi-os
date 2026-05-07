from __future__ import annotations

from founder_ai_workflow_roi.config import load_company_profile, load_scoring_rules
from founder_ai_workflow_roi.ingest import load_workflows
from founder_ai_workflow_roi.roi import calculate_roi
from founder_ai_workflow_roi.scoring import add_priority_scores, priority_bucket


def test_config_loading() -> None:
    company = load_company_profile("config/company_profile.yml")
    rules = load_scoring_rules("config/scoring_rules.yml")

    assert company["company_name"] == "Example SeedCo"
    assert "time_saved" in rules["weights"]
    assert rules["assumptions"]["blended_hourly_cost"] > 0


def test_priority_scoring_boundaries() -> None:
    assert priority_bucket(80) == "Automate now"
    assert priority_bucket(60) == "Pilot first"
    assert priority_bucket(40) == "Document first"
    assert priority_bucket(39.9) == "Keep manual"


def test_priority_scores_are_between_zero_and_one_hundred() -> None:
    company = load_company_profile("config/company_profile.yml")
    rules = load_scoring_rules("config/scoring_rules.yml")
    df = calculate_roi(load_workflows("data/sample_workflows.csv"), rules)

    scored = add_priority_scores(df, company, rules)

    assert scored["priority_score"].between(0, 100).all()
    assert scored["roi_category"].notna().all()
