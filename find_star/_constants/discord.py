from os import getenv

__all__ = (
    "DISCORD_WEBHOOK_ENDPOINT",
    "DISCORD_PAYLOAD",
    "EXTRA_FORMAT_ARGS",
)

STARHUNTER_ROLE_ID = getenv("STARHUNTER_ROLE_ID", "000000")

DISCORD_WEBHOOK_ENDPOINT = getenv(
    "DISCORD_WEBHOOK_ENDPOINT",
)

EXTRA_FORMAT_ARGS = {
    "role_mention": f"<@&{STARHUNTER_ROLE_ID}>",
    "dynamic_ts": "<t:{time:%s}:R>",
}

DISCORD_MESSAGE_SPEC = """
**T{tier:d} Star** at **{loc:s}** {role_mention}
> {dynamic_ts:s} by {scout:s} on [osrsportal](https://osrsportal.com/shooting-stars-tracker)
""".strip()

DISCORD_EMBEDS = (
    [
        {
            "title": "#get-roles for W444 Star Notifications",
            "url": "https://discord.com/channels/1172035731837960242/1185740071488471040",
            "footer": {
                "text": "Follow the #get-roles link and react to Star Watcher to receive Discord pings",
            },
        },
    ],
)

DISCORD_USER_NAME = "Star Watcher"

DISCORD_PAYLOAD = {
    # https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
    "username": DISCORD_USER_NAME,
    "content": DISCORD_MESSAGE_SPEC,  # Will be formatted when posting to Discord
    "embeds": [
        {
            "title": "#get-roles for W444 Star Notifications",
            "url": "https://discord.com/channels/1172035731837960242/1185740071488471040",
            "footer": {
                "text": "Follow the #get-roles link and react to Star Watcher to receive Discord pings",
            },
        },
    ],
}
