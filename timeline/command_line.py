from .github import get_events as github_events
from .slack import get_events as slack_events
import argparse
import json
import os

MEDIUM_LENGTH = 10
CHANNEL_LENGTH = 30
PREVIEW_LENGTH = 50


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default="~/.timeline.json")
    args = parser.parse_args()

    config_path = args.config
    config = json.load(open(os.path.expanduser(config_path), 'rb'))

    events = []
    events += github_events(config["github"])
    events += slack_events(config["slack"])

    events = sorted(events, key=lambda e: e.timestamp)
    events.reverse()

    for event in events:
        print((
            f"{ event.timestamp.astimezone().strftime('%Y-%m-%d %H:%M') } "
            f"{ event.medium[:MEDIUM_LENGTH].ljust(MEDIUM_LENGTH) } "
            f"{ event.channel[:CHANNEL_LENGTH].ljust(CHANNEL_LENGTH) } "
            f"{ event.preview[:PREVIEW_LENGTH].ljust(PREVIEW_LENGTH) } "
            f"{ event.link }"
        ))
