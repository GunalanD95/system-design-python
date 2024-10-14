from models.basemodel import BaseModel
from datetime import datetime
from typing import Optional , List
from models.movie import Movie , Language
from models.theatre import Theatre
from models.cinema_hall import CinemaHall , HallSeat , SeatStatus


class MovieShow(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._movie: Optional[Movie] = None
        self._theatre: Optional[Theatre] = None
        self._cinema_hall: Optional[CinemaHall] = None
        self._show_time: Optional[datetime] = None
        self._show_date: Optional[datetime] = None
        self._price: Optional[int] = None
        self._language: Optional[Language] = None
        self._seats: List['HallSeat'] = []

    @property
    def id(self):
        return self._id
    
    @property
    def movie(self):
        return self._movie
    
    @property
    def theatre(self):
        return self._theatre
    
    @property
    def cinema_hall(self):
        return self._cinema_hall
    
    @property
    def show_time(self):
        return self._show_time
    
    @property
    def show_date(self):
        return self._show_date
    
    @property
    def price(self):
        return self._price
    
    @property
    def language(self):
        return self._language
    
    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, seats):
        self._seats = seats
    
    @movie.setter
    def movie(self, movie):
        self._movie = movie
        
    @theatre.setter
    def theatre(self, theatre):
        self._theatre = theatre
        
        
    @cinema_hall.setter
    def cinema_hall(self, cinema_hall):
        self._cinema_hall = cinema_hall
        
    @show_time.setter
    def show_time(self, show_time):
        self._show_time = show_time
        
    @show_date.setter
    def show_date(self, show_date):
        self._show_date = show_date
        
    @price.setter
    def price(self, price):
        self._price = price
        
    @language.setter
    def language(self, language):
        self._language = language
        
    def show_available_seats(self) -> List['HallSeat']:
        return [seat for seat in self._seats if seat.status == SeatStatus.AVAILABLE]
    
    def get_seat_by_id(self, seat_id) -> 'HallSeat':
        for seat in self._seats:
            if seat.id == seat_id:
                return seat
        return None
        

        
    
    
    