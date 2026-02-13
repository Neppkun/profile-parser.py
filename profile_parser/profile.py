from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .utils import parse_date


@dataclass
class Profile:
    account_id: Optional[str]
    display_name: Optional[str]
    platform_names: list[str]
    mastery_rank: Optional[int]
    preset: Optional[dict]
    loadout: dict
    intrinsics: dict
    challenge_progress: list[Any]
    guild_id: Optional[str]
    guild_name: Optional[str]
    guild_tier: Optional[int]
    guild_xp: Optional[int]
    guild_class: Optional[int]
    guild_emblem: Optional[bool]
    alliance_id: Optional[str]
    death_marks: list[str]
    harvestable: bool
    death_squadable: bool
    created: Optional[datetime]
    migrated_to_console: bool
    missions: list[Any]
    syndicates: list[Any]
    daily_standing: dict[str, Optional[int]]
    daily_focus: Optional[int]
    wish_list: Optional[list[str]]
    unlocked_operator: bool
    unlocked_alignment: bool
    operator_loadouts: Optional[list[Any]]
    alignment: Optional[dict[str, int]]

    def __init__(
        self,
        profile: dict,
        locale: str = "en",
        with_item: bool = False,
        item_lookup: Any = None,
    ) -> None:
        account = profile.get("AccountId") or {}
        guild = profile.get("GuildId") or {}
        alliance = profile.get("AllianceId") or {}

        self.account_id = account.get("$oid")
        self.display_name = profile.get("DisplayName")
        self.platform_names = profile.get("PlatformNames") or []
        self.mastery_rank = profile.get("PlayerLevel")
        self.preset = profile.get("LoadOutPreset")
        self.loadout = profile.get("LoadOutInventory") or {}
        self.intrinsics = profile.get("PlayerSkills") or {}
        self.challenge_progress = profile.get("ChallengeProgress") or []
        self.guild_id = guild.get("$oid")
        self.guild_name = profile.get("GuildName")
        self.guild_tier = profile.get("GuildTier")
        self.guild_xp = profile.get("GuildXp")
        self.guild_class = profile.get("GuildClass")
        self.guild_emblem = profile.get("GuildEmblem")
        self.alliance_id = alliance.get("$oid")
        self.death_marks = profile.get("DeathMarks") or []
        self.harvestable = bool(profile.get("Harvestable", False))
        self.death_squadable = bool(profile.get("DeathSquadable", False))
        self.created = parse_date(profile.get("Created"))
        self.migrated_to_console = bool(profile.get("MigratedToConsole", False))
        self.missions = profile.get("Missions") or []
        self.syndicates = profile.get("Affiliations") or []
        self.daily_standing = {
            "daily": profile.get("DailyAffiliation"),
            "conclave": profile.get("DailyAffiliationPvp"),
            "simaris": profile.get("DailyAffiliationLibrary"),
            "ostron": profile.get("DailyAffiliationCetus"),
            "quills": profile.get("DailyAffiliationQuills"),
            "solaris": profile.get("DailyAffiliationSolaris"),
            "ventKids": profile.get("DailyAffiliationVentkids"),
            "voxSolaris": profile.get("DailyAffiliationVox"),
            "entrati": profile.get("DailyAffiliationEntrati"),
            "necraloid": profile.get("DailyAffiliationNecraloid"),
            "holdfasts": profile.get("DailyAffiliationZariman"),
            "kahl": profile.get("DailyAffiliationKahl"),
            "cavia": profile.get("DailyAffiliationCavia"),
            "hex": profile.get("DailyAffiliationHex"),
        }
        self.daily_focus = profile.get("DailyFocus")
        self.wish_list = profile.get("Wishlist")
        self.unlocked_operator = bool(profile.get("UnlockedOperator", False))
        self.unlocked_alignment = bool(profile.get("UnlockedAlignment", False))
        self.operator_loadouts = profile.get("OperatorLoadOuts")
        self.alignment = None
        if profile.get("Alignment"):
            self.alignment = {
                "wisdom": profile["Alignment"].get("Wisdom"),
                "alignment": profile["Alignment"].get("Alignment"),
            }
