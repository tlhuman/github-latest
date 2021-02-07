import sys
import json

import requests

base_url = "https://api.github.com/"
# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    try:
        username = sys.argv[1]
    except IndexError:
        username = "tlhuman"

    resp_uid = requests.get(base_url + f"users/{username}")

    events_url = resp_uid.json()['events_url'].split("{")[0]
    resp_event = requests.get(events_url)

    event = resp_event.json()[0]
    created_at = event['created_at']

    print(f"{username} event at {created_at}")


