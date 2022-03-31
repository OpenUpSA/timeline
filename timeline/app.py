import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
from datetime import datetime, timezone


config = json.load(open(os.path.expanduser("~/.timeline.json"), 'rb'))

app = App(token=config["user_token"])

if __name__ == "__main__":
    response = app.client.search_messages(query="from:jd after:February", sort="timestamp")
    for match in response["messages"]["matches"]:
        timestamp = datetime.fromtimestamp(float(match['ts']), timezone.utc)
        print((
            f"{ timestamp.astimezone() } "
            f"{ match['permalink'] } "
            f"#{ match['channel']['name'][:15].ljust(15) } "
            f"{ match['text'][:100] }"
        ))
