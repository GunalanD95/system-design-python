from models.meeting import Meeting
from models.user import User
from models.calendar import Calendar
from models.meetingroom import MeetingRoom
from models.interval import Interval
from typing import List
from models.meetingscheduler import MeetingScheduler
from models.notification import Notification


class MeetingSchedulerService:
    def __init__(self):
        self.__scheduler : MeetingScheduler = MeetingScheduler()


    def create_scheduler(self, calendar: Calendar, organizer: User, rooms: List[MeetingRoom]):
        self.__scheduler.calendar = calendar
        self.__scheduler.organizer = organizer
        self.__scheduler.rooms = rooms
        
    
    def schedule_meeting(self,users: List[User], interval: Interval) -> Notification:
        pass 
    
    def cancel_meeting(self, meeting: Meeting) -> Notification:
        pass
    
    def book_room(self, meeting: Meeting) -> Notification:
        pass
    
    def release_room(self,meetingroom: MeetingRoom, interval: Interval) -> Notification:
        pass
    
    def check_availability(self, meetingroom: MeetingRoom, interval: Interval) -> bool:
        pass