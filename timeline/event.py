from dataclasses import dataclass
import datetime

@dataclass
class Event:
    timestamp: datetime.datetime
    medium: str
    channel: str
    preview: str
    link: str
