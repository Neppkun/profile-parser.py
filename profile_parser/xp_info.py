from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class XpInfo:
    unique_name: str
    xp: int
    item: Optional[Any] = None

    def __init__(
        self,
        info: dict,
        locale: str = "en",
        with_item: bool = False,
        item_lookup: Optional[Callable[..., Any]] = None,
    ) -> None:
        self.unique_name = info.get("ItemType")
        self.xp = info.get("XP", 0)
        self.item = None
        if with_item and item_lookup:
            try:
                self.item = item_lookup(self.unique_name, locale)
            except TypeError:
                self.item = item_lookup(self.unique_name)
