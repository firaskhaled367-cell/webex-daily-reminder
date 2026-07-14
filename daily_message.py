"""
Sends today's short Islamic reminder to a Webex space.

Requires two environment variables:
    WEBEX_BOT_TOKEN  - your bot's access token
    WEBEX_ROOM_ID    - the roomId of the target space (see get_room_id.py)
"""

import os
import json
from datetime import date
from pathlib import Path

import requests

WEBEX_TOKEN = os.environ["WEBEX_BOT_TOKEN"]
ROOM_ID = os.environ["WEBEX_ROOM_ID"]

CONTENT_PATH = Path(__file__).parent / "content.json"


def load_messages():
    with open(CONTENT_PATH, encoding="utf-8") as f:
        return json.load(f)


def pick_message(messages):
    # Deterministic by day-of-year, so it rotates through the whole list
    # before repeating, and running it twice in one day sends the same text.
    idx = date.today().toordinal() % len(messages)
    return messages[idx]


def send_message(text: str):
    resp = requests.post(
        "https://webexapis.com/v1/messages",
        headers={"Authorization": f"Bearer {WEBEX_TOKEN}"},
        json={"roomId": ROOM_ID, "markdown": text},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    messages = load_messages()
    text = pick_message(messages)
    result = send_message(text)
    print("Sent message id:", result.get("id"))
