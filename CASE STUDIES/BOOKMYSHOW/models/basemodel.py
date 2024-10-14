from typing import Optional
from datetime import datetime

class BaseModel:
    def __init__(self):
        self._id: Optional[int] = None
        self._created_at: Optional[datetime] = None
        self._last_updated: Optional[datetime] = None
        
    def save(self):
        if not self._id:
            self._created_at = datetime.now()
        else:
            self._last_updated = datetime.now()