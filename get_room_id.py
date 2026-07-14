"""
Run this once to find the roomId of the space you added the bot to.

Usage:
    export WEBEX_BOT_TOKEN="your-bot-token-here"
    python get_room_id.py
"""

import os
import requests

WEBEX_TOKEN = os.environ["WEBEX_BOT_TOKEN"]

resp = requests.get(
    "https://webexapis.com/v1/rooms",
    headers={"Authorization": f"Bearer {WEBEX_TOKEN}"},
    timeout=15,
)
resp.raise_for_status()

rooms = resp.json()["items"]
if not rooms:
    print("No rooms found. Make sure the bot has been added to a space.")
else:
    print("Rooms this bot can see:\n")
    for room in rooms:
        print(f"  {room['title']!r}  ->  roomId: {room['id']}")
