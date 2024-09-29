from player import GamePlayer
from typing import List
from enum import Enum

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GameStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    DRAW = "Draw"
    PLAYER_WON = "Player Won"

class Game(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__game_id : int = 0
        self.__players : List[GamePlayer] = []
        self.__cur_player : GamePlayer = None
        self.__winner : GamePlayer = None
        self.__deck_of_cards : List[int] = []
        self.__game_status : GameStatus = GameStatus.NOT_STARTED
        
    # Getters
    def get_game_id(self) -> int:
        return self.__game_id

    def get_players(self) -> List[GamePlayer]:
        return self.__players

    def get_cur_player(self) -> GamePlayer:
        return self.__cur_player

    def get_winner(self) -> GamePlayer:
        return self.__winner

    def get_deck_of_cards(self) -> List[int]:
        return self.__deck_of_cards
    
    def get_game_status(self) -> GameStatus:
        return self.__game_status

    # Setters
    def set_game_id(self, game_id : int) -> None:
        self.__game_id = game_id

    def set_players(self, players : List[GamePlayer]) -> None:
        self.__players = players

    def set_cur_player(self, cur_player : GamePlayer) -> None:
        self.__cur_player = cur_player
        
    def set_game_status(self, game_status : GameStatus) -> None:
        self.__game_status = game_status