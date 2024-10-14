from models.basemodel import BaseModel
from typing import Optional , List
from enum import Enum

class CinemaHall(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._name = None
        self._location = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = value
    
class SeatStatus(Enum):
    BOOKED = 1
    AVAILABLE = 2
    OUT_OF_SERVICE = 3
    
class SeatType(Enum):
    NORMAL = 1
    PREMIUM = 2
    BALCONY = 3
        
class HallSeat(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._hall_id = None
        self._row = None
        self._column = None
        self._status : SeatStatus = None
        self._price = None
        self._seat_type : SeatType = None
        
    @property
    def seat_type(self):
        return self._seat_type
    
    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value
        
    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, value):
        self._row = value
        
    @property
    def column(self):
        return self._column
    
    @column.setter
    def column(self, value):
        self._column = value
        
        
    