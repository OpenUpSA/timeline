from .github import events as github_events
import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default="~/.timeline.json")
    args = parser.parse_args()

    config_path = args.config
    config = json.load(open(os.path.expanduser(config_path), 'rb'))

    github_events(config["github"])
