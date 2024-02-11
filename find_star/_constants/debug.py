from os import getenv

__all__ = (
    "DEBUG",
    "VERBOSE",
)

_true_strings = (
    "true",
    "yes",
    "y",
    "on",
    "1",
)

DEBUG = getenv("DEBUG", "false").lower() in _true_strings
VERBOSE = DEBUG or getenv("VERBOSE", "false").lower() in _true_strings
