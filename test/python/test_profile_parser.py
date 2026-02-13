from __future__ import annotations

import json
from pathlib import Path

from profile_parser import ProfileParser, Stats


def load_fixture(name: str) -> dict:
    path = Path(__file__).resolve().parents[2] / "test" / "data" / name
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_profile_parser_parses_fixtures() -> None:
    data = load_fixture("OrnsteinTheSlayer.json")
    parser = ProfileParser(data)

    assert parser.profile.display_name == data["Results"][0]["DisplayName"]
    assert parser.profile.account_id == data["Results"][0]["AccountId"]["$oid"]
    assert parser.profile.created is not None
    assert parser.xp_cache_expiry_date is not None
    assert isinstance(parser.stats, Stats)

    tobiah = load_fixture("Tobiah.json")
    assert ProfileParser(tobiah).profile.display_name == tobiah["Results"][0]["DisplayName"]
