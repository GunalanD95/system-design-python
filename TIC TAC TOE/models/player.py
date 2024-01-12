from typing import AnyStr
from abc    import ABC , abstractmethod
from .playertype import PlayerType
from .cell  import Cell

class Player(ABC):
    def __init__(self , symbol: str  , player_type : PlayerType ) -> None:
        self.symbol = symbol
        self.player_type = player_type
    
    @abstractmethod   
    def makeMove(self,board):
        pass 
        
        
class HumanPlayer(Player):
    def __init__(self,name : str , symbol: str) -> None:
        self.name   = name
        super().__init__(symbol , PlayerType.HUMAN)
        

    def makeMove(self,board):
        row_num = int(input('Please tell the row number starting from 0 : '))
        col_num = int(input('Please tell the col number starting from 0 : ')) 
        
        return Cell(row_num, col_num)
        
    def __str__(self) -> str:
        return f"Player : {self.name} | {self.symbol}"
        
        
        
