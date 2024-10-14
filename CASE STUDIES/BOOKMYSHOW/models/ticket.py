from models.basemodel import BaseModel
from models.payment import Payment
from models.cinema_hall import HallSeat
from typing import List
from enum import Enum

class TicketStatus(Enum):
    CONFIRMED = 1
    PENDING = 2
    CANCELLED = 3
    

class Ticket(BaseModel):
    def __init__(self):
        super().__init__()
        self._payment_id: int = None
        self._show_id: int = None
        self._user_id: int = None
        self._payment : Payment = None
        self._amount : int = None
        self._status : TicketStatus = None
        self._seats : List['HallSeat'] = []
        
    @property
    def payment_id(self):
        return self._payment_id
    
    @property
    def show_id(self):
        return self._show_id
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def payment(self):
        return self._payment
    
    @payment.setter
    def payment(self, value: Payment):
        self._payment = value
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value: int):
        self._amount = value
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value: TicketStatus):
        self._status = value
        
    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, seats):
        self._seats = seats
        