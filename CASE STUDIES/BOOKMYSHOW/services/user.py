from models.user import User
from models.repository import UserRepository
from models.basemodel import BaseModel
from typing import List
from models.payment import Payment
from models.ticket import Ticket
from models.cinema_hall import HallSeat
from models.show import MovieShow
from models.movie import Movie


class UserService(BaseModel):
    def __init__(self):
        self.repo = UserRepository()

    def get_all_users(self) -> List[User]:
        return self.repo.find_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.repo.find_by_id(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.repo.find_by_attribute("email", email)
    
    def create_user(self, name: str, email: str, password: str) -> User:
        user = User(None, name, email, password)
        return self.repo.create(user)
    
    def update_user(self,name, email, password):
        user = self.repo.find_by_attribute("email", email)
        if not user:
            return ValueError("User not found")
        user.name = name
        user.password = password
        return self.repo.update(user)