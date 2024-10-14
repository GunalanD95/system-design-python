from typing import Dict, List, TypeVar, Generic, Type
from models.basemodel import BaseModel
from models.cinema_hall import CinemaHall
from models.ticket import Ticket
from models.movie import Movie
from models.user import User
from models.show import MovieShow

T = TypeVar('T', bound=BaseModel)


class Repository(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self._model_class = model_class
        self._storage: Dict[int, T] = {}
        self._id_counter = 1

    def create(self, obj: T) -> T:
        obj.id = self._id_counter
        self._storage[self._id_counter] = obj
        self._id_counter += 1
        return obj

    def find_by_id(self, id: int) -> T:
        return self._storage.get(id)

    def find_all(self) -> List[T]:
        return list(self._storage.values())

    def update(self, obj: T) -> T:
        if obj.id in self._storage:
            self._storage[obj.id] = obj
            return obj
        return None

    def delete(self, id: int) -> bool:
        if id in self._storage:
            del self._storage[id]
            return True
        return False

    def find_by_attribute(self, attribute: str, value: any) -> List[T]:
        return [obj for obj in self._storage.values() if getattr(obj, attribute) == value]
    
class MovieRepository(Repository[Movie]):
    def __init__(self):
        super().__init__(Movie)

class TicketRepository(Repository[Ticket]):
    def __init__(self):
        super().__init__(Ticket)

class CinemaHallRepository(Repository[CinemaHall]):
    def __init__(self):
        super().__init__(CinemaHall)

class UserRepository(Repository[User]):
    def __init__(self):
        super().__init__(User)
        
class MovieShowRepository(Repository[MovieShow]):
    def __init__(self):
        super().__init__(MovieShow)