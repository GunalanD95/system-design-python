from enum import Enum
from typing import Optional
from models.base import BaseModel


class User(BaseModel):
    def __init__(self) -> None:
        self.__user_id: Optional[int] = None
        self.__name: Optional[str] = None
        self.__email: Optional[str] = None
        self.__password: Optional[str] = None

    @property
    def user_id(self) -> Optional[int]:
        return self.__user_id

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @property
    def email(self) -> Optional[str]:
        return self.__email

    @property
    def password(self) -> Optional[str]:
        return self.__password
    
    @user_id.setter
    def user_id(self, value: Optional[int]):
        self.__user_id = value

    @name.setter
    def name(self, value: Optional[str]):
        self.__name = value

    @email.setter
    def email(self, value: Optional[str]):
        self.__email = value

    @password.setter
    def password(self, value: Optional[str]):
        self.__password = value