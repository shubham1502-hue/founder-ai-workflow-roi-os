from __future__ import annotations

from founder_ai_workflow_roi.config import load_company_profile, load_scoring_rules
from founder_ai_workflow_roi.decision import add_decisions, add_matrix_scores
from founder_ai_workflow_roi.ingest import load_workflows
from founder_ai_workflow_roi.roadmap import generate_backlog
from founder_ai_workflow_roi.roi import calculate_roi
from founder_ai_workflow_roi.scoring import add_priority_scores


def test_roadmap_generation() -> None:
    company = load_company_profile("config/company_profile.yml")
    rules = load_scoring_rules("config/scoring_rules.yml")
    df = load_workflows("data/sample_workflows.csv")
    df = calculate_roi(df, rules)
    df = add_priority_scores(df, company, rules)
    df = add_matrix_scores(df)
    df = add_decisions(df, company)

    backlog = generate_backlog(df)

    assert len(backlog) == len(df)
    assert backlog.iloc[0]["backlog_id"] == "AI-001"
    assert "phase" in backlog.columns
    assert backlog["success_metric"].notna().all()
    pilot_rows = df[df["recommendation"] == "Run AI-assisted pilot"]
    pilot_backlog = backlog[backlog["workflow_name"].isin(pilot_rows["workflow_name"])]
    assert set(pilot_backlog["phase"]) == {"Phase 2: AI-assisted pilots"}
