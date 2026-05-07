from __future__ import annotations

from pathlib import Path

import pandas as pd

from founder_ai_workflow_roi.utils import normalize_bool, normalize_text, safe_float


class IngestError(ValueError):
    """Raised when workflow input data is missing or malformed."""


REQUIRED_COLUMNS = [
    "workflow_id",
    "function",
    "workflow_name",
    "owner_role",
    "current_tooling",
    "workflow_description",
    "frequency_per_month",
    "avg_time_minutes_per_run",
    "people_involved",
    "error_rate_percent",
    "monthly_volume",
    "business_impact",
    "customer_impact",
    "data_sensitivity",
    "process_variability",
    "current_pain",
    "current_cost_signal",
    "automation_idea",
    "requires_human_judgment",
    "current_status",
]

NUMERIC_COLUMNS = [
    "frequency_per_month",
    "avg_time_minutes_per_run",
    "people_involved",
    "error_rate_percent",
    "monthly_volume",
    "business_impact",
    "customer_impact",
]

TEXT_COLUMNS = [column for column in REQUIRED_COLUMNS if column not in NUMERIC_COLUMNS]


def validate_required_columns(df: pd.DataFrame) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise IngestError(f"Workflow CSV is missing required columns: {', '.join(missing)}")


def load_workflows(path: str | Path) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise IngestError(f"Workflow CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)
    validate_required_columns(df)

    cleaned = df.copy()
    for column in NUMERIC_COLUMNS:
        cleaned[column] = cleaned[column].map(lambda value: safe_float(value, 0.0))
    for column in TEXT_COLUMNS:
        cleaned[column] = cleaned[column].map(normalize_text)
    cleaned["requires_human_judgment"] = cleaned["requires_human_judgment"].map(normalize_bool)

    if cleaned["workflow_id"].duplicated().any():
        duplicates = sorted(cleaned.loc[cleaned["workflow_id"].duplicated(), "workflow_id"].unique())
        raise IngestError(f"Workflow IDs must be unique. Duplicates: {', '.join(duplicates)}")

    return cleaned[REQUIRED_COLUMNS]
