from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class ConfigError(ValueError):
    """Raised when a YAML config file is missing required fields."""


REQUIRED_COMPANY_KEYS = {
    "company_name",
    "stage",
    "team_size",
    "business_model",
    "current_ai_maturity",
    "monthly_burn_sensitivity",
    "hiring_constraints",
    "preferred_tools",
    "risk_tolerance",
    "sensitive_data_categories",
    "functions_to_prioritize",
    "functions_to_avoid_for_now",
    "founder_operating_goals",
}

REQUIRED_SCORING_KEYS = {
    "weights",
    "assumptions",
}

REQUIRED_WEIGHT_KEYS = {
    "time_saved",
    "workflow_frequency",
    "business_impact",
    "customer_impact",
    "error_reduction",
    "implementation_effort",
    "data_sensitivity_risk",
    "process_variability_risk",
    "human_judgment_risk",
    "cost_to_automate",
    "payback_period",
    "strategic_leverage",
}

REQUIRED_ASSUMPTION_KEYS = {
    "blended_hourly_cost",
    "default_setup_cost_low",
    "default_setup_cost_medium",
    "default_setup_cost_high",
    "default_maintenance_cost_percent",
    "automation_coverage_by_complexity",
}


def load_yaml(path: str | Path) -> dict[str, Any]:
    yaml_path = Path(path)
    if not yaml_path.exists():
        raise ConfigError(f"Config file not found: {yaml_path}")
    with yaml_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"Config file must contain a YAML mapping: {yaml_path}")
    return data


def _missing(required: set[str], data: dict[str, Any]) -> list[str]:
    return sorted(required.difference(data.keys()))


def load_company_profile(path: str | Path) -> dict[str, Any]:
    data = load_yaml(path)
    missing = _missing(REQUIRED_COMPANY_KEYS, data)
    if missing:
        raise ConfigError(f"Company config is missing required keys: {', '.join(missing)}")
    return data


def load_scoring_rules(path: str | Path) -> dict[str, Any]:
    data = load_yaml(path)
    missing = _missing(REQUIRED_SCORING_KEYS, data)
    if missing:
        raise ConfigError(f"Scoring config is missing required keys: {', '.join(missing)}")

    weights = data.get("weights", {})
    assumptions = data.get("assumptions", {})
    if not isinstance(weights, dict):
        raise ConfigError("scoring_rules.yml key 'weights' must be a mapping")
    if not isinstance(assumptions, dict):
        raise ConfigError("scoring_rules.yml key 'assumptions' must be a mapping")

    missing_weights = _missing(REQUIRED_WEIGHT_KEYS, weights)
    missing_assumptions = _missing(REQUIRED_ASSUMPTION_KEYS, assumptions)
    if missing_weights:
        raise ConfigError(f"Scoring weights are missing required keys: {', '.join(missing_weights)}")
    if missing_assumptions:
        raise ConfigError(f"Scoring assumptions are missing required keys: {', '.join(missing_assumptions)}")
    return data
