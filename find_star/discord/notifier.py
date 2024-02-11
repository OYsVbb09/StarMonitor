"""Discord Notification sender

Environment variables
---------------------

Required:

DISCORD_WEBHOOK_ENDPOINT

Optional:

STARHUNTER_ROLE_ID: number (default=None)
    Prefix a role with '&' '&<role_id>'
    or '<user_id>' without '&' prefix for a user id

"""

from __future__ import annotations

import json
import logging as logger

from copy import copy
from typing import TYPE_CHECKING

import requests

from .._constants import EXTERNAL_CONNECTION_TIMEOUT, DEBUG, VERBOSE
from .._constants.discord import DISCORD_MESSAGE_SPEC

if TYPE_CHECKING:
    from typing import Dict, Any
    from ..osrsportal.data_structure import Star

__all__ = ("DiscordNotifier",)


class DiscordNotifier:
    """Discord notifier

    NOTE, the developer doesn't use or plan on using Discord

    As such, this class is untested
    """

    headers: "Dict[str, str]" = {"Content-Type": "application/json"}
    payload: "Dict[str, Any]" = {
        "username": "OSRS Star Watcher",
        "content": DISCORD_MESSAGE_SPEC,  # Will be formatted when posting to Discord
        "embeds": [
            {
                "title": "OSRS Star Tracker",
                "url": "https://osrsportal.com/shooting-stars-tracker",
                "footer": {
                    "text": "No affiliation",
                },
            },
        ],
    }

    __endpoint: str

    def __init__(
        self,
        __endpoint: str,
    ):
        """
        Arguments
        ---------

        __endpoint: str
            Discord webhook 'uri'
        """
        self.__endpoint = __endpoint

    def __call__(self, __star_info: "Star") -> "requests.Response":
        """Send notification to Discord"""
        star = __star_info
        _scout_time = star["time"]
        star["time"] = round(_scout_time.timestamp())
        payload = copy(self.payload)
        payload["content"] = (
            # Format tempate message with star info
            payload["content"].format(**star)
        )
        if DEBUG:
            logger.debug(
                "Sending the following message to Discord:\n%r", payload)
        ret = requests.post(
            self.__endpoint,
            data=json.dumps(payload),
            headers=self.headers,
            timeout=EXTERNAL_CONNECTION_TIMEOUT,
        )
        if ret.status_code not in [200, 201, 204]:
            logger.error(
                "Failed to post message to discord (status=%d)", ret.status_code
            )
            if VERBOSE:
                logger.debug("Send to discord: \n\t%r\nAnd received:\n\t%r",
                             ret.request.body, ret.text)
        return ret
