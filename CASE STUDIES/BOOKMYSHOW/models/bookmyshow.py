from models.basemodel import BaseModel


class BookMyShow(BaseModel):
    def __init__(self):
        super().__init__()
        self.__theaters = []
        self.__movies   = []
        