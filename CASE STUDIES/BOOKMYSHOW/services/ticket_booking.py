from models.ticket import Ticket , TicketStatus
from models.payment import Payment, PaymentStatus
from models.cinema_hall import HallSeat , SeatStatus
from models.show import MovieShow
from models.user import User
from typing import List
from models.repository import TicketRepository

class TicketBookingService:
    def __init__(self):
        self.ticket_repository = TicketRepository()
    
    @staticmethod
    def create_booking(self,show: MovieShow, seats: List[HallSeat] , user: User) -> Ticket:
        ticket = Ticket()
        ticket.show_id = show.id
        ticket.user_id = user.id
        ticket.payment = Payment()
        ticket.payment.status = PaymentStatus.PENDING
        ticket.amount = sum([seat.price for seat in seats])
        ticket.seats = seats
        return self.ticket_repository.create(ticket)
        
        
    @staticmethod
    def confirm_booking(self,ticket_id : int, payment: Payment) -> bool:
        ticket = self.ticket_repository.find_by_id(ticket_id)
        if payment.status == PaymentStatus.COMPLETED:
            ticket.status = TicketStatus.CONFIRMED
            for seat in ticket.seats:
                seat.status = SeatStatus.BOOKED
            self.ticket_repository.update(ticket)
            return True
        return False
    
    @staticmethod
    def cancel_booking(self,ticket_id : int) -> bool:
        ticket = self.ticket_repository.find_by_id(ticket_id)
        if ticket.status != TicketStatus.CONFIRMED:
            ticket.status = TicketStatus.CANCELLED
            for seat in ticket.seats:
                seat.status = SeatStatus.AVAILABLE
            return True
        return False
    
    def get_booking_by_id(self, ticket_id: int) -> Ticket:
        return self.ticket_repository.find_by_id(ticket_id)
    