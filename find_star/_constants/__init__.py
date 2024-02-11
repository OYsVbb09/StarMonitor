from . import discord, osrsportal, star_parameters, probe_delays
from .debug import DEBUG, VERBOSE

EXTERNAL_CONNECTION_TIMEOUT = 30

__all__ = (
    "DEBUG",
    "VERBOSE",
    "discord",
    "osrsportal",
    "star_parameters",
    "probe_delays",
)
