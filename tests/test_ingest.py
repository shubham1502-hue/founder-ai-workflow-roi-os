from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from founder_ai_workflow_roi.ingest import IngestError, REQUIRED_COLUMNS, load_workflows, validate_required_columns


def test_load_workflows_reads_sample_data() -> None:
    df = load_workflows("data/sample_workflows.csv")

    assert len(df) >= 20
    assert list(df.columns) == REQUIRED_COLUMNS
    assert df["workflow_id"].is_unique
    assert df["requires_human_judgment"].dtype == bool


def test_required_column_validation_fails_with_clear_error() -> None:
    df = pd.DataFrame({"workflow_id": ["WF-001"]})

    with pytest.raises(IngestError, match="missing required columns"):
        validate_required_columns(df)


def test_duplicate_workflow_ids_are_rejected(tmp_path: Path) -> None:
    sample = load_workflows("data/sample_workflows.csv").head(2)
    sample.loc[sample.index[1], "workflow_id"] = sample.loc[sample.index[0], "workflow_id"]
    csv_path = tmp_path / "duplicate.csv"
    sample.to_csv(csv_path, index=False)

    with pytest.raises(IngestError, match="unique"):
        load_workflows(csv_path)
