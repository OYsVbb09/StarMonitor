from os import getenv

__all__ = (
    "DISCORD_WEBHOOK_ENDPOINT",
    "STARHUNTER_ROLE_ID",
    "DISCORD_MESSAGE_SPEC",
    "DISCORD_MESSAGE_USERNAME",
    "DISCORD_MESSAGE_EMBEDS",
    "DISCORD_WEBHOOK_PAYLOAD",
)

DISCORD_WEBHOOK_ENDPOINT = getenv(
    "DISCORD_WEBHOOK_ENDPOINT",
)

STARHUNTER_ROLE_ID = getenv("STARHUNTER_ROLE_ID")

DISCORD_MESSAGE_USERNAME = "OSRS Star Watcher"

DISCORD_MESSAGE_SPEC = """
T{tier:d} Star at '{loc:s}' in {world:d}
> ~<t:{time:%s}:R> by {scout:s} on [osrsportal.com](https://osrsportal.com/shooting-stars-tracker)'
""".strip()


if STARHUNTER_ROLE_ID:
    DISCORD_MESSAGE_SPEC = f"<@&{STARHUNTER_ROLE_ID}> " + DISCORD_MESSAGE_SPEC

DISCORD_MESSAGE_EMBEDS = [
    {
        "title": "OSRS Star Tracker",
        "url": "https://osrsportal.com/shooting-stars-tracker",
        "footer": {
            "text": "No affiliation",
        },
    },
]

DISCORD_WEBHOOK_PAYLOAD = {
    "username": DISCORD_MESSAGE_USERNAME,
    # the SPEC Will be formatted when posting to Discord
    "content": DISCORD_MESSAGE_SPEC,
    "embeds": DISCORD_MESSAGE_EMBEDS,
}
