from models.base import BaseModel   
from models.meeting import Meeting
from typing import List

class Calendar(BaseModel):
    def __init__(self):
        self.__meetings : List[Meeting] = []
        
        
    @property
    def meetings(self):
        return self.__meetings
    
    @meetings.setter
    def meetings(self, value):
        self.__meetings = value
        
        
    def add_meeting(self, meeting):
        self.__meetings.append(meeting)