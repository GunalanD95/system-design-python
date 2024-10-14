from models.movie import Movie
from typing import List
from models.repository import MovieRepository , MovieShowRepository
from models.show import MovieShow

class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()
        self.show_repository = MovieShowRepository()

    def add_movie(self, movie: Movie) -> Movie:
        saved_movie = self.movie_repository.create(movie)
        return saved_movie
    
    def add_show(self, show: MovieShow) -> MovieShow:
        saved_show = self.show_repository.create(show)
        return saved_show

    def get_movie_by_id(self, movie_id: int) -> Movie:
        return self.movie_repository.find_by_id(movie_id)
    
    def get_show_by_id(self, show_id: int) -> MovieShow:
        return self.show_repository.find_by_id(show_id)
    
    def get_movie_by_name(self, name: str) -> List[Movie]:
        return self.movie_repository.find_by_attribute("name", name)

    def search_movies(self, criteria: str, value: str) -> List[Movie]:
        if criteria == "title":
            return self.movie_repository.find_by_attribute("title", value)
        elif criteria == "language":
            return self.movie_repository.find_by_attribute("language", value)
        elif criteria == "genre":
            return self.movie_repository.find_by_attribute("genre", value)
        elif criteria == "release_date":
            return self.movie_repository.find_by_attribute("release_date", value)
        else:
            return []