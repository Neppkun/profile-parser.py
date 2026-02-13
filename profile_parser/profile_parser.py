from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Optional

from .profile import Profile
from .stats import Stats
from .utils import parse_date


@dataclass
class ProfileParser:
    profile: Profile
    tech_projects: list[Any]
    xp_components: list[Any]
    xp_cache_expiry_date: Optional[datetime]
    ceremony_reset_date: Optional[datetime]
    stats: Stats

    def __init__(
        self,
        data: dict,
        locale: str = "en",
        with_item: bool = False,
        item_lookup: Optional[Callable[..., Any]] = None,
    ) -> None:
        results = data.get("Results") or []
        profile_data = results[0] if results else {}
        self.profile = Profile(
            profile_data,
            locale=locale,
            with_item=with_item,
            item_lookup=item_lookup,
        )
        self.tech_projects = data.get("TechProjects") or []
        self.xp_components = data.get("XpComponents") or []
        self.xp_cache_expiry_date = parse_date(data.get("XpCacheExpiryDate"))
        self.ceremony_reset_date = parse_date(data.get("CeremonyResetDate"))
        self.stats = Stats(data.get("Stats", {}))
