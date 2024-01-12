from .cell import Cell
from .player import Player 

class Move:
    
    def __init__(self,player : Player , cell: Cell ):
        self.player = player
        self.cell   = cell
        
        
        
        
    def __str__(self) -> str:
        return f"Move : {self.player.symbol} | {self.cell}"
    
         