from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .utils import parse_races


@dataclass
class Stats:
    guild_name: Optional[str] = None
    missions_completed: int = 0
    missions_quit: int = 0
    missions_failed: int = 0
    missions_interrupted: int = 0
    missions_dumped: int = 0
    pickup_count: int = 0
    weapons: list[dict] = field(default_factory=list)
    enemies: list[dict] = field(default_factory=list)
    excavation_event_score_max: Optional[int] = None
    forest_event_score_max: Optional[int] = None
    forest_event_score_sum: Optional[int] = None
    melee_kills: int = 0
    abilities: list[dict] = field(default_factory=list)
    ciphers_solved: int = 0
    ciphers_failed: int = 0
    income: int = 0
    time_played_sec: int = 0
    cipher_time: int = 0
    rating: int = 0
    rank: int = 0
    deaths: int = 0
    player_level: int = 0
    missions: list[dict] = field(default_factory=list)
    heal_count: int = 0
    breed_grounds: Optional[dict[str, int]] = None
    gradivus_dilemma: Optional[dict[str, int]] = None
    scans: list[dict] = field(default_factory=list)
    revive_count: int = 0
    fomorian_event_score: Optional[int] = None
    pvp: list[dict] = field(default_factory=list)
    lunaro: dict[str, int] = field(default_factory=dict)
    dojo_obstacle_score: int = 0
    pvp_games_pending_mask: int = 0
    dedicated_server_games_completed: int = 0
    pacifism_defect: Optional[int] = None
    ambulas_reborn: Optional[int] = None
    sentinel_game_score: Optional[int] = None
    amalgam_event_score_max: Optional[int] = None
    scarlet_spear: Optional[dict[str, int]] = None
    orphix_venom_score: Optional[int] = None
    happy_zephyr_score: int = 0
    k_drive_races: list[dict[str, Optional[int]]] = field(default_factory=list)
    gate_crash: Optional[int] = None
    false_profit_mission_score: Optional[int] = None
    false_profit_event_score: Optional[int] = None
    shadow_debt_event_score: Optional[int] = None
    rathuum_event_score: Optional[int] = None
    hallowed_flame_score_max: Optional[int] = None
    survival_weekend_event_score: Optional[int] = None
    infested_event_score: Optional[int] = None

    def __init__(self, stats: dict) -> None:
        self.excavation_event_score_max = None
        self.forest_event_score_max = None
        self.forest_event_score_sum = None
        self.breed_grounds = None
        self.gradivus_dilemma = None
        self.fomorian_event_score = None
        self.pacifism_defect = None
        self.ambulas_reborn = None
        self.sentinel_game_score = None
        self.amalgam_event_score_max = None
        self.scarlet_spear = None
        self.orphix_venom_score = None
        self.gate_crash = None
        self.false_profit_mission_score = None
        self.false_profit_event_score = None
        self.shadow_debt_event_score = None
        self.rathuum_event_score = None
        self.hallowed_flame_score_max = None
        self.survival_weekend_event_score = None
        self.infested_event_score = None

        self.guild_name = stats.get("GuildName")
        self.missions_completed = stats.get("MissionsCompleted", 0)
        self.missions_quit = stats.get("MissionsQuit", 0)
        self.missions_failed = stats.get("MissionsFailed", 0)
        self.missions_interrupted = stats.get("MissionsInterrupted", 0)
        self.missions_dumped = stats.get("MissionsDumped", 0)
        self.pickup_count = stats.get("PickupCount", 0)
        self.weapons = stats.get("Weapons", [])
        self.enemies = stats.get("Enemies", [])
        if stats.get("ExcavationEventScoreMax"):
            self.excavation_event_score_max = stats.get("ExcavationEventScoreMax")
        if stats.get("ForestEventScoreMax"):
            self.forest_event_score_max = stats.get("ForestEventScoreMax")
        if stats.get("ForestEventScoreSum"):
            self.forest_event_score_sum = stats.get("ForestEventScoreSum")
        self.melee_kills = stats.get("MeleeKills", 0)
        self.abilities = stats.get("Abilities", [])
        self.ciphers_solved = stats.get("CiphersSolved", 0)
        self.ciphers_failed = stats.get("CiphersFailed", 0)
        self.income = stats.get("Income", 0)
        self.time_played_sec = stats.get("TimePlayedSec", 0)
        self.cipher_time = stats.get("CipherTime", 0)
        self.rating = stats.get("Rating", 0)
        self.rank = stats.get("Rank", 0)
        self.deaths = stats.get("Deaths", 0)
        self.player_level = stats.get("PlayerLevel", 0)
        self.missions = stats.get("Missions", [])
        self.heal_count = stats.get("HealCount", 0)
        if stats.get("HiveEventScore") or stats.get("HiveEventScoreSum"):
            self.breed_grounds = {
                "personal_score": stats.get("HiveEventScore", 0),
                "clan_score": stats.get("HiveEventScoreSum", 0),
            }
        if stats.get("InvasionEventGrineerScore") or stats.get(
            "InvasionEventCorpusScore"
        ):
            self.gradivus_dilemma = {
                "grineer": stats.get("InvasionEventGrineerScore", 0),
                "corpus": stats.get("InvasionEventCorpusScore", 0),
            }
        self.scans = stats.get("Scans") or []
        self.revive_count = stats.get("ReviveCount", 0)
        if stats.get("FomorianEventScore"):
            self.fomorian_event_score = stats.get("FomorianEventScore")
        self.pvp = stats.get("PVP") or []
        self.lunaro = {
            "ties": stats.get("PVPSpeedballTies", 0) or 0,
            "checks": stats.get("PVPSpeedballChecks", 0) or 0,
            "goals": stats.get("PVPSpeedballGoals", 0) or 0,
            "interceptions": stats.get("PVPSpeedballInterceptions", 0) or 0,
            "steals": stats.get("PVPSpeedballSteals", 0) or 0,
            "points": stats.get("PVPSpeedballPoints", 0) or 0,
            "losses": stats.get("PVPSpeedballLosses", 0) or 0,
            "assists": stats.get("PVPSpeedballAssists", 0) or 0,
            "wins": stats.get("PVPSpeedballWins", 0) or 0,
            "saves": stats.get("PVPSpeedballSaves", 0) or 0,
            "passes": stats.get("PVPSpeedballPasses", 0) or 0,
        }
        self.dojo_obstacle_score = stats.get("DojoObstacleScore", 0) or 0
        self.pvp_games_pending_mask = stats.get("PvpGamesPendingMask", 0) or 0
        self.dedicated_server_games_completed = (
            stats.get("DedicatedServerGamesCompleted", 0) or 0
        )
        if stats.get("ColonistRescueEventScoreMax"):
            self.pacifism_defect = stats.get("ColonistRescueEventScoreMax")
        if stats.get("AmbulasEventScoreMax"):
            self.ambulas_reborn = stats.get("AmbulasEventScoreMax")
        if stats.get("SentinelGameScore"):
            self.sentinel_game_score = stats.get("SentinelGameScore")
        if stats.get("AmalgamEventScoreMax"):
            self.amalgam_event_score_max = stats.get("AmalgamEventScoreMax")
        if stats.get("FlotillaEventScore"):
            self.scarlet_spear = {
                "event_score": stats.get("FlotillaEventScore", 0),
                "condrix_tier1": stats.get("FlotillaGroundBadgesTier1", 0),
                "condrix_tier2": stats.get("FlotillaGroundBadgesTier2", 0),
                "condrix_tier3": stats.get("FlotillaGroundBadgesTier3", 0),
                "murex_tier1": stats.get("FlotillaSpaceBadgesTier1", 0),
                "murex_tier2": stats.get("FlotillaSpaceBadgesTier2", 0),
                "murex_tier3": stats.get("FlotillaSpaceBadgesTier3", 0),
            }
        if stats.get("MechSurvivalScoreMax"):
            self.orphix_venom_score = stats.get("MechSurvivalScoreMax")
        self.happy_zephyr_score = stats.get("ZephyrScore", 0) or 0
        self.k_drive_races = parse_races(stats.get("Races"))
        if stats.get("PortalEventScore"):
            self.gate_crash = stats.get("PortalEventScore")
        if stats.get("RiotMoaEventScore"):
            self.false_profit_mission_score = stats.get("RiotMoaEventScore")
        if stats.get("RiotMoaEventScoreMax"):
            self.false_profit_event_score = stats.get("RiotMoaEventScoreMax")
        if stats.get("ProjectSinisterEventScore"):
            self.shadow_debt_event_score = stats.get("ProjectSinisterEventScore")
        if stats.get("KelaEventBonusScoreMax"):
            self.rathuum_event_score = stats.get("KelaEventBonusScoreMax")
        if stats.get("Halloween19ScoreMax"):
            self.hallowed_flame_score_max = stats.get("Halloween19ScoreMax")
        if stats.get("SurvivalEventScore"):
            self.survival_weekend_event_score = stats.get("SurvivalEventScore")
        if stats.get("InfestedEventScore"):
            self.infested_event_score = stats.get("InfestedEventScore")
