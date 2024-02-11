import sys
import json
import logging

from ._constants import VERBOSE

if VERBOSE:
    logging.basicConfig(level=logging.DEBUG)

from .find_star import StarMonitor
from .discord import DiscordNotifier
from .cli_arguments import cli_arguments

from ._constants.discord import DISCORD_WEBHOOK_ENDPOINT

if not DISCORD_WEBHOOK_ENDPOINT:
    logging.error("Unset manditory variable: DISCORD_WEBHOOK_ENDPOINT")
    sys.exit(1)


message_handler = DiscordNotifier(DISCORD_WEBHOOK_ENDPOINT)
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

if VERBOSE:
    logging.basicConfig(level=logging.DEBUG)

star = monitor.get_star()
if not star:
    logging.info("No Star in requested world")
    sys.exit(1)

star["time"] = star["time"].isoformat()
json.dump(star, sys.stdout)
sys.exit(0)
