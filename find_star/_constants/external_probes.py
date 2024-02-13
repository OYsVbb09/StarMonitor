__all__ = (
    "SEARCH_DELAY",
    "EXTERNAL_CONNECTION_TIMEOUT",
)

# WARNING-start
SEARCH_DELAY = 45
# lowering this only marginally increase notification speed,
# what lowering it will do is send excessive requests to an
# unaffiliated endpoint, which they may not appreciate!
# WARNING-end

EXTERNAL_CONNECTION_TIMEOUT = 30
