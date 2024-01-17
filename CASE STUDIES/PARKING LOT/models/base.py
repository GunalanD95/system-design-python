from datetime import datetime
from typing import Optional

class BaseModel:
    def __init__(self) -> None:
        self._id: Optional[int] = None
        self._created_at: Optional[datetime] = None
        self._last_updated: Optional[datetime] = None

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        self._id = value

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at

    @property
    def last_updated(self) -> Optional[datetime]:
        return self._last_updated

    def set_created_at(self) -> None:
        """
        Set the created_at timestamp to the current datetime.
        """
        self._created_at = datetime.now()

    def set_last_updated(self) -> None:
        """
        Set the last_updated timestamp to the current datetime.
        """
        self._last_updated = datetime.now()
