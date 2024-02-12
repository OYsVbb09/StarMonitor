"""OSRS Portal monitor and notifier"""

from __future__ import annotations

import sys
import logging as logger


from time import sleep
from math import floor
from datetime import datetime, timedelta

from typing import TYPE_CHECKING

from .osrsportal import get_osrsportal_stars

from ._constants import VERBOSE
from ._constants.probe_delays import PER_TIER_DELAY, SEARCH_DELAY
from ._constants.star_parameters import (
    MAXIMAL_AGE,
    MINIMAL_TIER,
    MINING_LEVEL,
    WORLD_BLACKLIST,
    REGION_BLACKLIST,
)


if TYPE_CHECKING:
    from typing import (
        Optional,
        Union,
        Callable,
        Iterable,
        ParamSpec,
        NoReturn,
        Tuple,
    )

    P = ParamSpec("P")

    from .osrsportal import Star


class StarMonitor:
    worlds: Tuple[int]
    max_age: int
    min_tier: int
    mining_lvl: int
    __star_getter: "Callable"

    def __init__(
        self,
        *worlds,
        max_age: int = MAXIMAL_AGE,
        min_tier: int = MINIMAL_TIER,
        mining_lvl: int = MINING_LEVEL,
        star_getter: "Union[Iterable[Star], Callable[[], Iterable[Star]]]" = get_osrsportal_stars,
    ):
        if not worlds:
            worlds = list(range(300, 600))
        self.worlds = worlds
        self.max_age = max_age
        self.min_tier = min_tier
        self.mining_lvl = mining_lvl
        self.__star_getter = star_getter

    def __find_suitable_star(self, stars: "Iterable[Star]") -> "Optional[Star]":
        """Find star within specified parameters

        Arguments:
        *worlds: int
            Eligible worlds
            examples:
                - 'find_suitable_star(444,445,446)'
                - 'find_suitable_star(*range(300,600))'
        Key-Word Arguments
        ------------------
        max_age: int
            Maximal scout age in approximate minutes
        min_size: int
            Minimal star 'tier'
        mining_lvl: int
            mining skill level
            (tier * 10 == required mining level)

        """
        eligible_star = {}

        for star in iter(stars):
            if not star["world"] in self.worlds or star["world"] in WORLD_BLACKLIST:
                # Skip star if we failed the world check
                continue

            if star["region"].lower() in [i.lower() for i in REGION_BLACKLIST]:
                continue
            if (
                star["time"].timestamp()
                < (datetime.now() - timedelta(minutes=self.max_age)).timestamp()
            ):
                # Skip star if the scout is too 'old'
                continue
            if self.min_tier > star["tier"] > floor(self.mining_lvl / 10):
                # skip star if it fails the 'size' check
                continue
            if eligible_star:
                # If a 'compatible' star was already found, check if this star is 'better'
                if star["tier"] < eligible_star["tier"]:
                    continue
                if star["time"].timestamp() > eligible_star["time"].timestamp():
                    continue

            eligible_star = star
        return eligible_star or None

    @staticmethod
    def calculate_star_duration(tier: int) -> int:
        return (tier * PER_TIER_DELAY)

    def get_star(self) -> "Optional[Star]":
        return self.__find_suitable_star(self.__star_getter())

    def background_notify(
        self,
        __notification_hook: "Callable[[Star]]",
    ) -> "NoReturn":
        """Loop and notify on star in specified worlds

        Arguments
        ---------
            *worlds: int
                worlds to find stars in
            notification_hook: Callable[[Star], ...]
                notifier to call with 'eligible star'
        """
        while True:
            try:
                star = self.get_star()
                if star:
                    logger.info("Found star: %r", star)
                    __notification_hook(star)
                    tier = star["tier"]
                    idle_time = self.calculate_star_duration(tier)
                    sleep(idle_time)
                    continue
                sleep(SEARCH_DELAY)  # 60 seconds
            except KeyboardInterrupt as _e:
                logger.debug("Caught exit signal %s, exiting...", _e)
                sys.exit(130)
            except TimeoutError as _e:
                logger.error("Connection failure: %s", _e, stack_info=VERBOSE)
                sleep(30)
            except Exception as _e:
                logger.error("Unexpected: %r", _e)
                raise
