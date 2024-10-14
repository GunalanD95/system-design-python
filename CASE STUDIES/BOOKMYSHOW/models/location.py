from models.basemodel import BaseModel
from typing import Optional 


class Location(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._name: Optional[str] = None
        self._latitude: Optional[float] = None
        self._longitude: Optional[float] = None
        self._address: Optional[str] = None


    @property
    def name(self):
        return self._name

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def address(self):
        return self._address
    
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @latitude.setter
    def latitude(self, value):
        self._latitude = value
        
    @longitude.setter
    def longitude(self, value):
        self._longitude = value
        
    @address.setter
    def address(self, value):
        self._address = value
        
    
    
    