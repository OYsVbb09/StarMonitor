from __future__ import annotations

import logging as logger

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import requests

from .data_structure import Star
from .auth_header import osrs_portal_auth_header

from .._constants import EXTERNAL_CONNECTION_TIMEOUT, DEBUG
from .._constants.osrsportal import ACTIVE_STARS_ENDPOINT

if TYPE_CHECKING:
    from typing import Iterable

__all__ = ("get_osrsportal_stars",)


def get_osrsportal_stars(
    endpoint: str = ACTIVE_STARS_ENDPOINT,
) -> "Iterable[Star]":
    """Fetch stars from osrsportal

    arguments
    ---------
    endpoint: str
        osrs portal 'internal' json get endpoint
    """
    headers = {
        "host": "osrsportal.com",
        "Referer": "https://osrsportal.com/shooting-stars",
        "Authorization": osrs_portal_auth_header(),
    }
    ret = requests.get(endpoint, headers=headers,
                       timeout=EXTERNAL_CONNECTION_TIMEOUT)
    if ret.status_code != 200:
        logger.error("Failed to make request, status: %d", ret.status_code)
        return []
    stars = ret.json()

    if DEBUG:
        logger.debug("All stars: '\n%r\n'", stars)

    for star in stars:
        time = datetime.now() - timedelta(minutes=star["time"])
        star["time"] = time
        yield star
