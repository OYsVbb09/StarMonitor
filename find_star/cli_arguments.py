from __future__ import annotations

import argparse

from typing import TypedDict, Sequence

from ._constants.star_parameters import MAXIMAL_AGE, MINIMAL_TIER, MINING_LEVEL

__all__ = (
    "CliArguments",
    "cli_arguments",
)


class CliArguments(TypedDict):
    max_age: int
    min_tier: int
    mining_lvl: int
    worlds: Sequence[int]
    daemon: bool


def cli_arguments(name: str = "StarMonitor"):
    parser = argparse.ArgumentParser(name)

    parser.add_argument(
        "--max-age",
        default=MAXIMAL_AGE,
        type=int,
        help="maximal star scout age in minutes",
    )
    parser.add_argument(
        "--min-tier",
        default=MINIMAL_TIER,
        type=int,
        choices=list(range(1, 10)),
        help="Minimal Star tier",
    )
    parser.add_argument(
        "--mining-lvl",
        default=MINING_LEVEL,
        type=int,
        help="Target mining lvl (lvl 80 does not get T9 stars)",
    )
    parser.add_argument("--daemon", action="store_true", default=False)
    parser.add_argument("worlds", nargs="+", type=int, help="World to scout")
    args = parser.parse_args()
    return CliArguments(
        {
            "max_age": args.max_age,
            "min_tier": args.min_tier,
            "mining_lvl": args.mining_lvl,
            "worlds": args.worlds,
            "daemon": args.daemon,
        }
    )
