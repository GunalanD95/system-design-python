from services.movie import MovieService
from models.payment import Payment
from models.cinema_hall import HallSeat
from models.show import MovieShow
from models.movie import Movie
from models.user import User
from typing import List


class MovieController:
    def __init__(self, service: MovieService) -> None:
        self.service = service

    def get_movie_by_id(self, movie_id: int) -> Movie:
        if not movie_id:
            return ValueError("Movie id is required")
        movie = self.service.get_movie_by_id(movie_id)
        if not movie:
            return ValueError("Movie not found")
        return {"movie": movie}

    def get_movies_by_name(self, name: str) -> List[Movie]:
        if not name:
            return ValueError("Movie name is required")
        movies = self.service.get_movie_by_name(name)
        if not movies:
            return ValueError("Movie not found")
        return {"movies": movies}      
    
    def add_movie(self, movie: Movie) -> Movie:
        if not movie:
            return ValueError("Movie is required")
        saved_movie = self.service.add_movie(movie)
        return {"movie": saved_movie}  