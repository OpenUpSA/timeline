from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
from datetime import datetime, timezone
from .event import Event


def get_page(app, page_num, username):
    return app.client.search_messages(query=f"from:{ username } after:March", sort="timestamp", page=page_num)


def make_events(response):
    for match in response["messages"]["matches"]:
        timestamp = datetime.fromtimestamp(float(match['ts']), timezone.utc)
        message = match['text'].replace('\n', ' ')
        yield Event(
            timestamp,
            "slack",
            match['channel']['name'],
            message,
            match['permalink'],
        )


def get_events(config):
    app = App(token=config["user_token"])
    username = config["username"]

    response = get_page(app, 1, username)

    for page_num in range(2, response["messages"]["pagination"]["page_count"] + 1):
        for event in make_events(get_page(app, page_num, username)):
            yield event
