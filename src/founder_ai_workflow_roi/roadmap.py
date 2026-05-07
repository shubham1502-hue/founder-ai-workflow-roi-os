from __future__ import annotations

import pandas as pd


def phase_for_recommendation(recommendation: str, quadrant: str) -> str:
    if recommendation == "Automate now" or quadrant == "Quick wins":
        return "Phase 1: quick wins"
    if recommendation == "Run AI-assisted pilot":
        return "Phase 2: AI-assisted pilots"
    if quadrant == "Strategic bets":
        return "Phase 3: deeper automation"
    return "Phase 4: hiring or outsourcing decisions"


def action_for_recommendation(recommendation: str, workflow_name: str) -> str:
    return {
        "Automate now": f"Build a deterministic automation or AI-assisted checklist for {workflow_name}.",
        "Run AI-assisted pilot": f"Run a limited pilot using AI for drafts, summaries, or routing on {workflow_name}.",
        "Hire": f"Define ownership requirements and hiring criteria for {workflow_name}.",
        "Outsource": f"Package {workflow_name} into an SOP for a contractor or agency test.",
        "Document process first": f"Document the current state process for {workflow_name} before tooling.",
        "Keep manual for now": f"Keep {workflow_name} manual and monitor volume, risk, and cost changes.",
    }.get(recommendation, f"Review next step for {workflow_name}.")


def due_timing_for_phase(phase: str) -> str:
    return {
        "Phase 1: quick wins": "Next 7 days",
        "Phase 2: AI-assisted pilots": "Next 14 to 30 days",
        "Phase 3: deeper automation": "Next 30 to 60 days",
        "Phase 4: hiring or outsourcing decisions": "Next planning cycle",
    }[phase]


def dependency_for_recommendation(recommendation: str) -> str:
    return {
        "Automate now": "Access to current workflow examples and owner approval",
        "Run AI-assisted pilot": "Pilot success criteria and human review checklist",
        "Hire": "Role scorecard and budget approval",
        "Outsource": "SOP, sample inputs, and acceptance criteria",
        "Document process first": "Current process map and exception list",
        "Keep manual for now": "Monthly workflow volume review",
    }.get(recommendation, "Founder review")


def success_metric_for_row(row: pd.Series) -> str:
    recommendation = str(row.get("recommendation", ""))
    if recommendation in {"Automate now", "Run AI-assisted pilot"}:
        return f"Save at least {row.get('estimated_hours_saved', 0):.1f} hours per month without quality regression."
    if recommendation == "Hire":
        return "Clear owner assigned and decision quality improves within one operating cycle."
    if recommendation == "Outsource":
        return "Contractor completes work to checklist with lower founder time involvement."
    if recommendation == "Document process first":
        return "Workflow has named inputs, outputs, approval rules, and exception handling."
    return "No increase in manual drag or error rate."


def generate_backlog(df: pd.DataFrame) -> pd.DataFrame:
    sorted_df = df.sort_values(
        by=["priority_score", "estimated_hours_saved"],
        ascending=[False, False],
    ).reset_index(drop=True)

    rows: list[dict[str, str]] = []
    for index, row in sorted_df.iterrows():
        phase = phase_for_recommendation(str(row["recommendation"]), str(row["quadrant"]))
        rows.append(
            {
                "backlog_id": f"AI-{index + 1:03d}",
                "workflow_name": row["workflow_name"],
                "function": row["function"],
                "phase": phase,
                "owner": row.get("suggested_owner", row.get("owner_role", "Founder")),
                "action": action_for_recommendation(row["recommendation"], row["workflow_name"]),
                "expected_outcome": row.get("reason", "Workflow has a clear next operating step."),
                "due_timing": due_timing_for_phase(phase),
                "dependency": dependency_for_recommendation(row["recommendation"]),
                "success_metric": success_metric_for_row(row),
            }
        )
    return pd.DataFrame(rows)
