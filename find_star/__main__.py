
import logging
from ._constants import VERBOSE

if VERBOSE:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(filename)s.%(funcName)s: %(message)s",
    )

# pylint: disable=C0413
import sys
import json

from os import getenv

from .find_star import StarMonitor
from .discord import DiscordNotifier
from .cli_arguments import cli_arguments


def main():
    discord_endpoint = getenv("DISCORD_WEBHOOK_ENDPOINT")
    message_handler = DiscordNotifier(discord_endpoint)
    cli_args = cli_arguments()
    worlds = cli_args.pop("worlds")
    monitor = StarMonitor(
        *worlds,
        max_age=cli_args["max_age"],
        min_tier=cli_args["min_tier"],
        mining_lvl=cli_args["mining_lvl"]
    )

    logging.debug("Running with settings: %r", cli_args)
    if cli_args["daemon"]:
        monitor.background_notify(message_handler)

    star = monitor.get_star()
    if not star:
        logging.info("No Star in requested world")
        sys.exit(1)

    star["time"] = star["time"].isoformat()
    json.dump(star, sys.stdout)
    sys.exit(0)


main()
