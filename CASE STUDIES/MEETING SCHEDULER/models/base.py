from typing import Optional
from datetime import datetime

class BaseModel():
    def __init__(self):
        self._created_at: Optional[datetime] = None
        self._last_updated: Optional[datetime] = None

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value: Optional[datetime]):
        self._created_at = value

    @property
    def last_updated(self):
        return self._last_updated