
import sys

sys.path.insert(0, 'C:\\Users\\admin\\Desktop\\system-design-python\\TIC TAC TOE')


from models.game import  GameBuilder
from typing import List 
from models.player import Player 

# Builder to create a Game Object

class GameController:
    
    def __init__(self) -> None:
        self.gamebuilder = GameBuilder()
        
    
    def create_game(self, dimension : int , players : List[Player] ,  winning_strategies: List[str] ):
        return self.gamebuilder.set_dimension(dimension).set_players(players).set_winning_strategies(winning_strategies).build()
    
    def displayBoard(self,game):
        game.printboard()

    def undo(self,game):
        game.undo()

    def makeMove(self,game):
        game.makemove()

    def getGameStatus(self,game):
        game.getGameStatus()

    def printResult(self,game):
        game.print_result()
        
        
        