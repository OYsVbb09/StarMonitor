from os import getenv

__all__ = (
    "DISCORD_WEBHOOK_ENDPOINT",
    "STARHUNTER_ROLE_ID",
    "DISCORD_MESSAGE_SPEC",
)

DISCORD_WEBHOOK_ENDPOINT = getenv(
    "DISCORD_WEBHOOK_ENDPOINT",
)

STARHUNTER_ROLE_ID = getenv("STARHUNTER_ROLE_ID", "StarHunters")

DISCORD_MESSAGE_SPEC = """
{world:d}<@&%(role_id)s> T{tier:d} Star at '{loc:s}
> ~<t:{time:d}:R> by {scout:s} on [osrsportal.com](https://osrsportal.com/shooting-stars-tracker)
""".strip() % {
    "role_id": STARHUNTER_ROLE_ID
}
