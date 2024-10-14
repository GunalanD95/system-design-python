from models.basemodel import BaseModel
from models.cinema_hall import CinemaHall
from typing import Optional 

class Theatre(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._name = None
        self._halls = Optional[CinemaHall] = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
        
    @property
    def halls(self):
        return self._halls
    
    @halls.setter
    def halls(self, value):
        self._halls = value