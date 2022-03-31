import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
from datetime import datetime, timezone
import argparse

MESSAGE_PREVIEW_LENGTH = 50
CHANNEL_PREVIEW_LENGTH = 10

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default="~/.timeline.json")
    args = parser.parse_args()

    config_path = args.config
    config = json.load(open(os.path.expanduser(config_path), 'rb'))

    app = App(token=config["slack"]["user_token"])

    response = app.client.search_messages(query="from:jd after:February", sort="timestamp")
    for match in response["messages"]["matches"]:
        timestamp = datetime.fromtimestamp(float(match['ts']), timezone.utc)
        message = match['text']
        message.replace("\n", " ")
        print((
            f"{ timestamp.astimezone() } "
            f"#{ match['channel']['name'][:CHANNEL_PREVIEW_LENGTH].ljust(CHANNEL_PREVIEW_LENGTH) } "
            f"{ message[:MESSAGE_PREVIEW_LENGTH].ljust(MESSAGE_PREVIEW_LENGTH) } "
            f"{ match['permalink'] } "
        ))
