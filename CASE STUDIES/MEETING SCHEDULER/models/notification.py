from models.base import BaseModel
from models.meeting import Meeting
from models.user import User


class Notification(BaseModel):
    def __init__(self, meeting: Meeting, user: User):
        self.meeting = meeting
        self.user = user

    def send_invite(self):
        pass
    
    def send_reminder(self):
        pass 
    
    def send_cancellation(self):
        pass
    
    