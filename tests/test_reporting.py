from __future__ import annotations

from pathlib import Path

from founder_ai_workflow_roi.cli import run_pipeline


def test_memo_and_output_generation(tmp_path: Path) -> None:
    output_dir = tmp_path / "outputs"

    paths = run_pipeline(
        input_path="data/sample_workflows.csv",
        company_config_path="config/company_profile.yml",
        scoring_config_path="config/scoring_rules.yml",
        output_dir=output_dir,
    )

    assert paths["scorecard"].exists()
    assert paths["matrix"].exists()
    assert paths["decisions"].exists()
    assert paths["backlog"].exists()
    assert paths["memo"].exists()
    assert paths["roadmap"].exists()
    assert paths["policy"].exists()
    assert "Executive summary" in paths["memo"].read_text(encoding="utf-8")
    assert "Phase 1: quick wins" in paths["roadmap"].read_text(encoding="utf-8")
