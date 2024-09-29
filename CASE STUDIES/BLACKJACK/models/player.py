from abc import ABC, abstractmethod
from models.user import User
from models.game import Game


class GamePlayer(ABC):
    
    def __init__(self):
        self.__player_id = 0
        self.__game_id = 0
        self.__cur_points = 0
        self.__cur_cards = []
        
    @abstractmethod
    def get_game_id(self) -> int:
        pass
    
    @abstractmethod
    def get_player_id(self) -> int:
        pass
    
    @abstractmethod
    def get_cur_points(self) -> int:
        pass
    
    @abstractmethod
    def get_cur_cards(self) -> list:
        pass
    
    @abstractmethod
    def set_game_id(self, game_id : int) -> None:
        pass
    
    @abstractmethod
    def set_player_id(self, player_id : int) -> None:
        pass
    
    @abstractmethod
    def set_cur_points(self, cur_points : int) -> None:
        pass
    
    @abstractmethod 
    def set_cur_cards(self, cur_cards : list) -> None:
        pass
    
    @abstractmethod
    def hit(self, deck) -> None:
        pass
    
    @abstractmethod
    def stand(self) -> None:
        pass
        

class Dealer(GamePlayer):
    def __init__(self):
        self.__dealer_id : int = 0
        self.__playing_strategy : str = None

class BlackJackPlayer(GamePlayer):
    def __init__(self):
        self.__user : User = None
        self.__bet : int =  0
        self.__total_cash : int = 0
        
    @property
    def user(self) -> User:
        return self.__user
    
    @user.setter
    def user(self, user : User):
        self.__user = user
        
        
    @property
    def bet(self) -> int:
        return self.__bet
    
    @bet.setter
    def bet(self, bet : int):
        self.__bet = bet
        
    @property
    def total_cash(self) -> int:
        return self.__total_cash
    
    @total_cash.setter
    def total_cash(self, total_cash : int):
        self.__total_cash = total_cash
        
        
    def place_bet(self, bet : int) -> None:
        self.__bet = bet