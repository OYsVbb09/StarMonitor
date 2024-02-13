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
from datetime import timedelta
from typing import TYPE_CHECKING

import requests

from .._constants import DEBUG
from .._constants.discord import DISCORD_PAYLOAD, EXTRA_FORMAT_ARGS
from .._constants.external_probes import EXTERNAL_CONNECTION_TIMEOUT


if TYPE_CHECKING:
    from typing import Optional, Dict, Any
    from ..osrsportal.data_structure import Star

__all__ = ("DiscordNotifier",)


def same_star(new_star: Star, old_star: Star = None):
    if not old_star:
        return False
    if old_star["world"] != new_star["world"]:
        return False
    if old_star["loc"] == new_star["loc"]:
        return (old_star["time"] + timedelta(minutes=90)).timestamp() > new_star[
            "time"
        ].timestamp()
    return False


class DiscordNotifier:
    """Discord notifier

    NOTE, the developer doesn't use or plan on using Discord

    As such, this class is untested
    """

    headers: "Dict[str, str]" = {"Content-Type": "application/json"}
    payload: "Dict[str, Any]" = DISCORD_PAYLOAD
    __endpoint: str
    __last_star: "Optional[Star]" = None

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
        if not __endpoint:
            raise ValueError("Missing Discord webhook endpoint")
        self.__endpoint = __endpoint

    def __call__(self, __star_info: "Star") -> "Optional[requests.Response]":
        """Send notification to Discord"""
        if same_star(__star_info, self.__last_star):
            if DEBUG:
                logger.debug("Already posted star to Discord, skipping")
            return
        format_args = {
            k: v.format(**__star_info) for k, v in EXTRA_FORMAT_ARGS.items()
        }
        format_args.update(__star_info)
        payload = copy(self.payload)
        payload["content"] = (
            # Format template message with star info
            payload["content"].format(**format_args)
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
        if ret.status_code in [200, 201, 204, 404]:
            self.__last_star = __star_info
            return
        logger.error(
            "Failed to post message to discord (status=%d)", ret.status_code)
        if DEBUG:
            logger.debug(
                "Send to discord: \n\t%r\nAnd received:\n\t%r",
                ret.request.body,
                ret.text,
            )
