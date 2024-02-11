from __future__ import annotations

from datetime import datetime
from typing import TypedDict

__all__ = ("Star",)


class Star(TypedDict):
    """OSRSPortal star index data structure"""

    scout: str
    time: datetime
    tier: int
    world: int
    loc: str
    region: str
