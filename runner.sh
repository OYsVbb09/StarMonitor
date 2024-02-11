#!/usr/bin/env bash

if [[ -f ".env" ]]; then
    . .env
fi

DISCORD_WEBHOOK_ENDPOINT=${DISCORD_WEBHOOK_ENDPOINT}    \
STARHUNTER_ROLE_ID=${STARHUNTER_ROLE_ID}                \
    python3 -m find_star --daemon --min-tier=1 444

