__all__ = (
    "SEARCH_DELAY",
    "PER_TIER_DELAY",
)

# WARNING-start
SEARCH_DELAY = 45
# lowering this only marginally increase notification speed,
# what lowering it will do is send excessive requests to an
# unaffiliated endpoint, which they may not appreciate!
# WARNING-end

_minute = 60

PER_TIER_DELAY = _minute * 7  # 7 minutes wait per tier on found star
