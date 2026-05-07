from __future__ import annotations

import argparse
from pathlib import Path

from founder_ai_workflow_roi.config import load_company_profile, load_scoring_rules
from founder_ai_workflow_roi.decision import add_decisions, add_matrix_scores
from founder_ai_workflow_roi.ingest import load_workflows
from founder_ai_workflow_roi.reporting import write_outputs
from founder_ai_workflow_roi.roi import calculate_roi
from founder_ai_workflow_roi.scoring import add_priority_scores


DEFAULT_INPUT = Path("data/sample_workflows.csv")
DEFAULT_COMPANY_CONFIG = Path("config/company_profile.yml")
DEFAULT_SCORING_CONFIG = Path("config/scoring_rules.yml")
DEFAULT_OUTPUT_DIR = Path("outputs")


def run_pipeline(
    input_path: str | Path = DEFAULT_INPUT,
    company_config_path: str | Path = DEFAULT_COMPANY_CONFIG,
    scoring_config_path: str | Path = DEFAULT_SCORING_CONFIG,
    output_dir: str | Path = DEFAULT_OUTPUT_DIR,
) -> dict[str, Path]:
    company_profile = load_company_profile(company_config_path)
    scoring_rules = load_scoring_rules(scoring_config_path)
    workflows = load_workflows(input_path)
    with_roi = calculate_roi(workflows, scoring_rules)
    with_scores = add_priority_scores(with_roi, company_profile, scoring_rules)
    with_matrix = add_matrix_scores(with_scores)
    with_decisions = add_decisions(with_matrix, company_profile)
    return write_outputs(with_decisions, company_profile, output_dir)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="founder-ai-workflow-roi",
        description="Generate an offline AI workflow ROI roadmap from CSV and YAML inputs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run the ROI decision system.")
    run_parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Workflow CSV input path.")
    run_parser.add_argument(
        "--company-config",
        default=str(DEFAULT_COMPANY_CONFIG),
        help="Company profile YAML path.",
    )
    run_parser.add_argument(
        "--scoring-config",
        default=str(DEFAULT_SCORING_CONFIG),
        help="Scoring rules YAML path.",
    )
    run_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Output directory.")

    subparsers.add_parser("demo", help="Run the bundled sample workflow demo.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "demo":
        paths = run_pipeline()
    else:
        paths = run_pipeline(
            input_path=args.input,
            company_config_path=args.company_config,
            scoring_config_path=args.scoring_config,
            output_dir=args.output_dir,
        )

    print("Generated outputs:")
    for path in paths.values():
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
