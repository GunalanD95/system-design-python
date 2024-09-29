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
        
        
class MyCalendar:

    def __init__(self):
        self.events = []
        
    def search_insert_position(self, event):
        low, high = 0, len(self.events) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_st, mid_e = self.events[mid]
            
            if event[0] <= mid_e and mid_st <= event[1]:
                return -1  # If overlap is found, return -1 (or handle as needed)
            
            
            if mid_e < event[0]:
                low = mid + 1
            # Otherwise, move left
            else:
                high = mid - 1

        # Return the correct position to insert the new event
        return low
                

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events = [[start,end-1]]
            return True
        
        idx = self.search_insert_position([start,end-1])
        if idx == -1:
            return False
        self.events.insert(idx,[start,end-1])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)