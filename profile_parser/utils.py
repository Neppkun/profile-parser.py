from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional


def parse_date(raw: Any) -> Optional[datetime]:
    """Parse Mongo extended JSON dates or epoch milliseconds into datetime."""
    if raw is None:
        return None
    if isinstance(raw, datetime):
        return raw
    if isinstance(raw, dict):
        if "$date" in raw:
            return parse_date(raw["$date"])
        if "$numberLong" in raw:
            return parse_date(raw["$numberLong"])
    if isinstance(raw, (int, float)):
        return datetime.fromtimestamp(raw / 1000, tz=timezone.utc)
    if isinstance(raw, str):
        try:
            return datetime.fromtimestamp(int(raw) / 1000, tz=timezone.utc)
        except (ValueError, TypeError):
            try:
                return datetime.fromisoformat(raw.replace("Z", "+00:00"))
            except ValueError:
                return None
    return None


def parse_races(races: Optional[dict]) -> list[dict[str, Optional[int]]]:
    if not races:
        return []
    parsed: list[dict[str, Optional[int]]] = []
    for name, details in races.items():
        high_score = None
        if isinstance(details, dict):
            high_score = details.get("highScore", 0)
        parsed.append({"unique_name": name, "high_score": high_score})
    return parsed
