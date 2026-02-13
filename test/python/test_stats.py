from __future__ import annotations

import json
from pathlib import Path

from profile_parser import Stats


def load_fixture(name: str) -> dict:
    path = Path(__file__).resolve().parents[2] / "test" / "data" / name
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_stats_handles_fixtures() -> None:
    data = load_fixture("OrnsteinTheSlayer.json")
    stats = Stats(data["Stats"])

    assert stats.guild_name == data["Stats"].get("GuildName")
    assert isinstance(stats.lunaro, dict)
    assert len(stats.weapons) == len(data["Stats"].get("Weapons", []))

    tobiah = load_fixture("Tobiah.json")
    assert Stats(tobiah["Stats"]).missions_completed == tobiah["Stats"].get(
        "MissionsCompleted",
        0,
    )
