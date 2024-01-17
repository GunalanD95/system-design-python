from models.cell  import Cell  , CellState
from models.board import Board
from abc import ABC , abstractclassmethod , abstractmethod

class BotPlayingStrategy:
    @abstractmethod
    def makeMove(self, board : Board) -> Cell:
        pass 
    
class EasyBotPlayingStrategy(BotPlayingStrategy):
    def makeMove(self, board : Board) -> Cell:
        for row in board:
            for cell in row:
                if cell.cell_state == CellState.FREE:
                    return cell 
                
        return None
    
    

class MediumBotPlayingStrategy(BotPlayingStrategy):
    def makeMove(self, board : Board) -> Cell:
        for row in board:
            for cell in row:
                if cell.cell_state == CellState.FREE:
                    return cell 
                
        return None
    
    

class HardBotPlayingStrategy(BotPlayingStrategy):
    def makeMove(self, board : Board) -> Cell:
        for row in board:
            for cell in row:
                if cell.cell_state == CellState.FREE:
                    return cell 
                
        return None