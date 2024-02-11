from __future__ import annotations

import json
import base64

from math import floor
from datetime import datetime
from typing import TYPE_CHECKING

from .._constants import EXTERNAL_CONNECTION_TIMEOUT
from .._constants.osrsportal import BEARER_FORMAT_SPEC

if TYPE_CHECKING:
    from typing import Dict, Any

__all__ = ("osrs_portal_auth_header",)


def _json_b64encode(__value: "Dict[str, Any]") -> str:
    """Base64 encode a JSON compatible dictionary"""
    value = json.dumps(__value).encode("utf-8")
    base_64 = base64.b64encode(value)
    return base_64.decode("utf-8")


def osrs_portal_auth_header(token_expiration: int = EXTERNAL_CONNECTION_TIMEOUT) -> str:
    """osrs_portal_auth_header

    Arguments
    ---------

    token_expiration: int
        Token lifetime, i.e. with the default, 5 min after the call of this function
    """
    spec = _json_b64encode(
        {
            "alg": "none",
            "typ": "JWT",
        }
    )
    data = _json_b64encode(
        {
            "data": "osrs_stars",
            "exp": floor(datetime.now().timestamp() + token_expiration),
        }
    )
    return BEARER_FORMAT_SPEC.format(spec=spec, data=data)
