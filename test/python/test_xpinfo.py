from __future__ import annotations

from profile_parser import XpInfo


def test_xpinfo_item_lookup() -> None:
    data = {
        "ItemType": "/Lotus/Weapons/Grineer/LongGuns/GrineerAssaultRifle/TwinGrakatas",
        "XP": 785691,
    }

    def lookup(unique_name: str, locale: str = "en") -> dict:
        assert locale == "en"
        return {"unique_name": unique_name, "name": "Twin Grakatas"}

    xp = XpInfo(data, locale="en", with_item=True, item_lookup=lookup)

    assert xp.unique_name == data["ItemType"]
    assert xp.item["name"] == "Twin Grakatas"
