from models.base import BaseModel
from models.user import User
from models.interval import Interval
from models.meetingroom import MeetingRoom

class Meeting(BaseModel):
    def __init__(self):
        self.__meeting_id : int = None 
        self.__participants : list[User] = []
        self.__interval : Interval = None
        self.__meetting_rom : MeetingRoom = None
        self.__subject : str = ''
        
        
    @property
    def meeting_id(self):
        return self.__meeting_id
    
    @property
    def participants(self):
        return self.__participants
    
    @property
    def interval(self):
        return self.__interval
    
    @property
    def meeting_room(self):
        return self.__meetting_rom
    
    @property
    def subject(self):
        return self.__subject
    
    @meeting_id.setter
    def meeting_id(self, value):
        self.__meeting_id = value
        
    @participants.setter
    def participants(self, value):
        self.__participants = value
        
    @interval.setter
    def interval(self, value):
        self.__interval = value
        
    @meeting_room.setter
    def __meetting_rom(self, value):
        self.__meetting_rom = value
        
    @subject.setter
    def subject(self, value):
        self.__subject = value