import requests
from requests.auth import HTTPBasicAuth


def events(config):
    start_date = "2022-04-01"
    username = config['username']
    access_token = config['access_token']

    session = requests.Session()
    session.headers.update({"Accept": "application/vnd.github.v3+json"})
    session.auth = HTTPBasicAuth(username, access_token)

    page = 1
    events = []
    page_events = None

    while page_events != []:
        params = {"page": page}
        print(f"Fetching page {page}")
        r = session.get(f"https://api.github.com/users/{username}/events/public", params=params)
        if r.status_code == 403:
            print(r.headers)
        r.raise_for_status()
        page_events = r.json()

        for event in page_events:
            if event["created_at"] >= start_date:
                # Only add events from start_date
                events += [event]
            else:
                break

        page += 1

        if page_events and page_events[-1]["created_at"] < start_date:
            # Stop fetching when we've reached past start_date
            break


    print(len(events))

    for event in events:
        print(event["created_at"])
