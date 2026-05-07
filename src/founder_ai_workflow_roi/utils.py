from __future__ import annotations

from math import isfinite
from typing import Any


LOW_MED_HIGH = {
    "none": 0,
    "low": 1,
    "medium": 2,
    "med": 2,
    "high": 3,
    "critical": 4,
}


def clamp(value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
    return max(minimum, min(maximum, value))


def safe_float(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default
    return parsed if isfinite(parsed) else default


def normalize_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    return text in {"yes", "true", "1", "y", "required"}


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def level_to_number(value: Any, default: int = 2) -> int:
    if value is None:
        return default
    text = str(value).strip().lower()
    if text in LOW_MED_HIGH:
        return LOW_MED_HIGH[text]
    try:
        numeric = int(float(text))
    except ValueError:
        return default
    return max(0, min(5, numeric))


def level_to_risk_score(value: Any) -> float:
    level = level_to_number(value)
    return {
        0: 0.0,
        1: 20.0,
        2: 50.0,
        3: 80.0,
        4: 95.0,
        5: 100.0,
    }.get(level, 50.0)


def level_to_inverse_score(value: Any) -> float:
    return 100.0 - level_to_risk_score(value)


def one_to_five_score(value: Any) -> float:
    numeric = clamp(safe_float(value, 3.0), 1.0, 5.0)
    return (numeric / 5.0) * 100.0


def currency(value: float) -> str:
    if value < 0:
        return f"-${abs(value):,.0f}"
    return f"${value:,.0f}"


def fmt_number(value: float, digits: int = 1) -> str:
    if abs(value - round(value)) < 0.05:
        return f"{value:,.0f}"
    return f"{value:,.{digits}f}"
