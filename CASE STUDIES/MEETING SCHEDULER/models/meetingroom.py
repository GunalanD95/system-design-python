from models.interval import Interval
from typing import Optional

class MeetingRoom:
    def __init__(self, name: str, capacity: int) -> None:
        self.room_id : Optional[int] = None
        self.name = name
        self.capacity = capacity
        self.booked_intervals : Optional[Interval] = []