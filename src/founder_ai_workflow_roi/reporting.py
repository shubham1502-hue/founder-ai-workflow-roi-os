from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from founder_ai_workflow_roi.roadmap import generate_backlog
from founder_ai_workflow_roi.utils import currency, fmt_number


SCORECARD_COLUMNS = [
    "workflow_id",
    "function",
    "workflow_name",
    "monthly_hours_spent",
    "estimated_monthly_cost",
    "estimated_hours_saved",
    "estimated_monthly_savings",
    "estimated_setup_cost",
    "estimated_monthly_maintenance_cost",
    "payback_period_months",
    "net_monthly_savings_after_maintenance",
    "priority_score",
    "roi_category",
    "recommendation",
]

MATRIX_COLUMNS = [
    "workflow_id",
    "workflow_name",
    "function",
    "impact_score",
    "effort_score",
    "risk_score",
    "priority_score",
    "quadrant",
    "recommended_timing",
]

DECISION_COLUMNS = [
    "workflow_id",
    "workflow_name",
    "function",
    "recommendation",
    "reason",
    "risks",
    "suggested_owner",
    "next_step",
    "decision_confidence",
]


def _section_from_filter(df: pd.DataFrame, title: str, recommendations: set[str], limit: int = 6) -> str:
    subset = df[df["recommendation"].isin(recommendations)].sort_values("priority_score", ascending=False)
    lines = [f"## {title}", ""]
    if subset.empty:
        lines.append("No workflows in this category for the current input data.")
        return "\n".join(lines)
    for _, row in subset.head(limit).iterrows():
        lines.append(
            f"- {row['workflow_name']} ({row['function']}): {row['recommendation']}; "
            f"score {row['priority_score']:.1f}; estimated savings "
            f"{currency(row['net_monthly_savings_after_maintenance'])}/month."
        )
    return "\n".join(lines)


def render_memo(df: pd.DataFrame, company_profile: dict[str, Any]) -> str:
    company_name = company_profile.get("company_name", "Your company")
    total_savings = df["net_monthly_savings_after_maintenance"].clip(lower=0).sum()
    automate_now = df[df["recommendation"] == "Automate now"]
    pilot = df[df["recommendation"] == "Run AI-assisted pilot"]
    hire = df[df["recommendation"] == "Hire"]
    top_risks = df.sort_values("risk_score", ascending=False).head(5)
    automate_count = len(automate_now)
    pilot_count = len(pilot)
    automate_word = "workflow" if automate_count == 1 else "workflows"
    pilot_word = "pilot" if pilot_count == 1 else "pilots"

    lines = [
        "# Founder AI ROI Memo",
        "",
        "## Executive summary",
        "",
        (
            f"{company_name} has {len(df)} mapped workflows. The current workflow inventory shows "
            f"{fmt_number(df['monthly_hours_spent'].sum())} monthly team hours and "
            f"{currency(total_savings)} in potential monthly savings after estimated maintenance costs."
        ),
        (
            f"The strongest near-term path is to automate {automate_count} {automate_word} now, "
            f"run {pilot_count} AI-assisted {pilot_word}, and keep high-risk work behind human approval."
        ),
        "",
        _section_from_filter(df, "Best workflows to automate now", {"Automate now"}),
        "",
        _section_from_filter(df, "Workflows to pilot first", {"Run AI-assisted pilot"}),
        "",
        _section_from_filter(df, "Workflows that need a hire", {"Hire"}),
        "",
        _section_from_filter(df, "Workflows to outsource", {"Outsource"}),
        "",
        _section_from_filter(df, "Workflows to keep manual", {"Keep manual for now", "Document process first"}),
        "",
        "## Biggest risks",
        "",
    ]
    for _, row in top_risks.iterrows():
        lines.append(
            f"- {row['workflow_name']} ({row['function']}): risk score {row['risk_score']:.1f}; "
            f"{row['risks']}"
        )
    lines.extend(
        [
            "",
            "## Estimated monthly savings",
            "",
            f"- Gross estimated AI-assisted savings: {currency(df['estimated_monthly_savings'].sum())}/month.",
            f"- Estimated maintenance cost: {currency(df['estimated_monthly_maintenance_cost'].sum())}/month.",
            f"- Net estimated savings after maintenance: {currency(total_savings)}/month.",
            "",
            "## Recommended next 7-day actions",
            "",
        ]
    )
    next_actions = df.sort_values("priority_score", ascending=False).head(7)
    for _, row in next_actions.iterrows():
        lines.append(f"- {row['workflow_name']}: {row['next_step']}")
    return "\n".join(lines) + "\n"


def render_roadmap(df: pd.DataFrame, backlog: pd.DataFrame) -> str:
    def bullets_for_phase(phase: str) -> list[str]:
        subset = backlog[backlog["phase"] == phase].head(8)
        if subset.empty:
            return ["- No backlog items in this phase yet."]
        return [
            f"- {row['workflow_name']} ({row['function']}): {row['action']}"
            for _, row in subset.iterrows()
        ]

    phases = [
        "Phase 1: quick wins",
        "Phase 2: AI-assisted pilots",
        "Phase 3: deeper automation",
        "Phase 4: hiring or outsourcing decisions",
    ]
    lines = ["# AI Workflow Roadmap", ""]
    for phase in phases:
        lines.extend([f"## {phase}", ""])
        lines.extend(bullets_for_phase(phase))
        lines.append("")

    lines.extend(
        [
            "## Metrics to track",
            "",
            "- Monthly hours saved by workflow.",
            "- Net monthly savings after maintenance.",
            "- Payback period by automation.",
            "- Error rate before and after rollout.",
            "- Human approval exceptions.",
            "- Workflow owner satisfaction.",
            "",
            "## What not to automate yet",
            "",
        ]
    )
    avoid = df[df["quadrant"] == "Avoid for now"].sort_values("risk_score", ascending=False)
    if avoid.empty:
        lines.append("- No workflows are currently marked avoid for now.")
    else:
        for _, row in avoid.iterrows():
            lines.append(f"- {row['workflow_name']} ({row['function']}): {row['risks']}")
    return "\n".join(lines) + "\n"


def render_policy(df: pd.DataFrame, company_profile: dict[str, Any]) -> str:
    sensitive = company_profile.get("sensitive_data_categories", []) or []
    preferred_tools = company_profile.get("preferred_tools", []) or []
    lines = [
        "# AI Operating Policy",
        "",
        "## What AI can be used for",
        "",
        "- Drafting, summarizing, classifying, routing, and preparing first-pass analysis.",
        "- Repetitive workflow support where source data is approved for the tool being used.",
        "- Generating checklists, SOP drafts, and backlog recommendations for human review.",
        "",
        "## What AI should not touch",
        "",
        "- Final decisions on hiring, finance, legal, security, customer commitments, or pricing.",
        "- Raw sensitive data unless the tool and workflow have explicit approval.",
        "- Workflows marked avoid for now or high risk in the priority matrix.",
        "",
        "## Human approval rules",
        "",
        "- A human owner must approve customer-facing, investor-facing, finance, hiring, and legal outputs.",
        "- AI-generated recommendations must show source inputs and assumptions before action.",
        "- No workflow moves from pilot to automation without a before and after metric review.",
        "",
        "## Data sensitivity rules",
        "",
    ]
    if sensitive:
        for item in sensitive:
            lines.append(f"- Treat {item} as sensitive. Use only approved tools and minimize copied data.")
    else:
        lines.append("- Define sensitive data categories in config/company_profile.yml before using AI tools.")
    lines.extend(
        [
            "",
            "## Review cadence",
            "",
            "- Weekly: review new workflow intake and quick-win progress.",
            "- Monthly: refresh ROI assumptions, risk scoring, and backlog priority.",
            "- Quarterly: revisit hire vs automate decisions and retire low-value pilots.",
            "",
            "## Owner responsibilities",
            "",
            "- Founder: approves risk tolerance, hiring tradeoffs, and final roadmap priority.",
            "- Functional owner: validates workflow inputs, examples, and quality thresholds.",
            "- Ops owner: maintains the workflow inventory, scorecard, and backlog.",
            "- Tool owner: confirms access controls, retention settings, and approved tool usage.",
            "",
            "## Approved tool preference",
            "",
        ]
    )
    if preferred_tools:
        for tool in preferred_tools:
            lines.append(f"- {tool}")
    else:
        lines.append("- Add preferred tools in config/company_profile.yml.")
    return "\n".join(lines) + "\n"


def write_outputs(
    df: pd.DataFrame,
    company_profile: dict[str, Any],
    output_dir: str | Path,
) -> dict[str, Path]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    backlog = generate_backlog(df)

    paths = {
        "scorecard": out / "workflow_roi_scorecard.csv",
        "matrix": out / "automation_priority_matrix.csv",
        "decisions": out / "hire_vs_automate_decisions.csv",
        "backlog": out / "ai_implementation_backlog.csv",
        "memo": out / "founder_ai_roi_memo.md",
        "roadmap": out / "ai_workflow_roadmap.md",
        "policy": out / "ai_operating_policy.md",
    }

    df[SCORECARD_COLUMNS].to_csv(paths["scorecard"], index=False)
    df[MATRIX_COLUMNS].to_csv(paths["matrix"], index=False)
    df[DECISION_COLUMNS].to_csv(paths["decisions"], index=False)
    backlog.to_csv(paths["backlog"], index=False)
    paths["memo"].write_text(render_memo(df, company_profile), encoding="utf-8")
    paths["roadmap"].write_text(render_roadmap(df, backlog), encoding="utf-8")
    paths["policy"].write_text(render_policy(df, company_profile), encoding="utf-8")
    return paths
