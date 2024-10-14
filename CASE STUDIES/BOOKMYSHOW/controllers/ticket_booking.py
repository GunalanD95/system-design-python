from services.ticket_booking import TicketBookingService
from services.movie import MovieService
from models.ticket import Ticket
from models.payment import Payment
from models.user import User
from typing import List


class BookingController:
    def __init__(self):
        self.booking_service = TicketBookingService()
        self.movie_service   = MovieService()
        
    def create_booking(self, show_id: int, seat_ids: List[int], user_id: int) -> Ticket:
        show = self.movie_service.get_show_by_id(show_id)
        user = User(user_id)
        seats = [show.get_seat_by_id(seat_id) for seat_id in seat_ids]
        return self.booking_service.create_booking(show, seats, user)

    def confirm_booking(self, booking_id: int, payment: Payment) -> bool:
        return self.booking_service.confirm_booking(booking_id, payment)

    def cancel_booking(self, booking_id: int) -> bool:
        return self.booking_service.cancel_booking(booking_id)

    def get_booking(self, booking_id: int) -> Ticket:
        return self.booking_service.get_booking_by_id(booking_id)