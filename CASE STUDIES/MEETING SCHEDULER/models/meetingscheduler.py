from models.base import BaseModel
from models.meeting import Meeting
from models.user import User
from models.calendar import Calendar
from models.meetingroom import MeetingRoom
from models.interval import Interval
from typing import List
from enum import Enum

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MeetingStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2
    OUT_OF_SERVICE = 3

class MeetingScheduler(BaseModel, metaclass=SingletonMeta):
    def __init__(self):
        self.__calendar : Calendar = None
        self.__organizer : User = None 
        self.__rooms : List[MeetingRoom] = []
        self.__status : MeetingStatus = None
        
    @property
    def calendar(self):
        return self.__calendar

    @calendar.setter
    def calendar(self, value):
        self.__calendar = value

    @property
    def organizer(self):
        return self.__organizer

    @organizer.setter
    def organizer(self, value):
        self.__organizer = value

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        self.__rooms = value
        
        
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
        