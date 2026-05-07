from __future__ import annotations

from founder_ai_workflow_roi.config import load_company_profile, load_scoring_rules
from founder_ai_workflow_roi.decision import add_decisions, add_matrix_scores
from founder_ai_workflow_roi.ingest import load_workflows
from founder_ai_workflow_roi.roi import calculate_roi
from founder_ai_workflow_roi.scoring import add_priority_scores


def _decision_frame():
    company = load_company_profile("config/company_profile.yml")
    rules = load_scoring_rules("config/scoring_rules.yml")
    df = load_workflows("data/sample_workflows.csv")
    df = calculate_roi(df, rules)
    df = add_priority_scores(df, company, rules)
    df = add_matrix_scores(df)
    return add_decisions(df, company)


def test_hire_vs_automate_decision_logic() -> None:
    decisions = _decision_frame()

    assert "Automate now" in set(decisions["recommendation"])
    assert "Run AI-assisted pilot" in set(decisions["recommendation"])
    assert "Document process first" in set(decisions["recommendation"])
    assert decisions["decision_confidence"].between(0, 1).all()


def test_priority_matrix_quadrants_are_supported() -> None:
    decisions = _decision_frame()

    assert set(decisions["quadrant"]).issubset(
        {"Quick wins", "Strategic bets", "Process first", "Avoid for now"}
    )
    assert decisions["recommended_timing"].notna().all()
