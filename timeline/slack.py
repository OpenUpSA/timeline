from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
from datetime import datetime, timezone

MESSAGE_PREVIEW_LENGTH = 50
CHANNEL_PREVIEW_LENGTH = 10


def get_page(page_num):
    return app.client.search_messages(query="from:jd after:March", sort="timestamp", page=page_num)

def print_response(response):
    for match in response["messages"]["matches"]:
        timestamp = datetime.fromtimestamp(float(match['ts']), timezone.utc)
        message = match['text'].replace('\n', ' ')
        print((
            f"{ timestamp.astimezone().strftime('%Y-%m-%d %H:%M') } "
            f"#{ match['channel']['name'][:CHANNEL_PREVIEW_LENGTH].ljust(CHANNEL_PREVIEW_LENGTH) } "
            f"{ message[:MESSAGE_PREVIEW_LENGTH].ljust(MESSAGE_PREVIEW_LENGTH) } "
            f"{ match['permalink'] } "
        ))



    app = App(token=config["slack"]["user_token"])

    response = get_page(1)
    print_response(response)

    for page_num in range(2, response["messages"]["pagination"]["page_count"] + 1):
        print_response(get_page(page_num))