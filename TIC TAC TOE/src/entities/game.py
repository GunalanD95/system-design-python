from .player import Player , PlayerBuilder
from .board  import Board

class Game:    
    def __init__(self,player1: Player , player2: Player , board : Board) -> None:
        self.p1      = player1
        self.p2      = player2
        self.board   = board
        
        
class GamerBuilder:
    def __init__(self,player1=None , player2=None , board=None) -> None:
        self.p1      = player1
        self.p2      = player2
        self.board   = board

    def create_player1(self , player_name : str , symbol = 'x'):
        pb = PlayerBuilder()
        self.p1 = pb.set_name(player_name).set_symbol(symbol).build()
        return self

    def create_player2(self , player_name : str , symbol = 'o'):
        pb = PlayerBuilder()
        self.p2 = pb.set_name(player_name).set_symbol(symbol).build()
        return self
    
    def build(self) -> Game:
        if not self.p1 or not self.p2:
            raise Exception('Players are not created!! Create players before starting the game')
        return Game(self.p1,self.p2,Board())