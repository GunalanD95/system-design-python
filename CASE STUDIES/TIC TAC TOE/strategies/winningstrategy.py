from abc import ABC , abstractmethod
from models.board import Board
from models.move  import Move 

class WinningStrategy:
    @abstractmethod
    def check_winner(self,board : Board, move : Move ) -> bool:
        pass
    
    @abstractmethod
    def handleUndo(self,board : Board, move : Move ):
        pass
    
    

class RowWinningStrategy(WinningStrategy):
    
    def __init__(self , size , players) -> None:
        self.rowMaps = []
        for i in range(size):
            self.rowMaps.append({})
            for player in players:
                self.rowMaps[i][player.symbol] = 0
                

    def check_winner(self,board : Board, move : Move ) -> bool:
        row    = move.cell.row 
        player = move.player 
        getMap = self.rowMaps[row]
        getMap[player.symbol] += 1
        if getMap[player.symbol] == len(self.rowMaps):
            return True 
        
        return False 
    
    
    def handleUndo(self, board : Board, move : Move):
        row    = move.cell.row 
        player = move.player 
        getMap = self.rowMaps[row]
        getMap[player.symbol] -= 1
    
    

class ColWinningStrategy(WinningStrategy):
    
    def __init__(self , size , players) -> None:
        self.colMaps = []
        for i in range(size):
            self.colMaps.append({})
            for player in players:
                self.colMaps[i][player.symbol] = 0
                

    def check_winner(self,board : Board, move : Move ) -> bool:
        col    = move.cell.col 
        player = move.player 
        getMap = self.colMaps[col]
        getMap[player.symbol] += 1
        if getMap[player.symbol] == len(self.colMaps):
            return True 
        
        return False 
    
    
    def handleUndo(self, board : Board, move : Move):
        col    = move.cell.col 
        player = move.player 
        getMap = self.colMaps[col]
        getMap[player.symbol] -= 1
    
    
class DiagonalWinningStrategy(WinningStrategy):
    
    def __init__(self ,players) -> None:
        self.leftdiagonal   = {}
        self.rightdiagonal  = {}
        
        for player in players:
            self.leftdiagonal[player.symbol] = 0
            self.rightdiagonal[player.symbol] = 0    

    def check_winner(self,board : Board, move : Move ) -> bool:
        row = move.cell.row 
        col = move.cell.col 
        player = move.player
        
        if row == col:
            self.leftdiagonal[player.symbol] += 1
            
        if row + col == len(board.board) -1:
            self.rightdiagonal[player.symbol] += 1
            
        if row == col:
            if self.leftdiagonal[player.symbol] == len(board.board):
                return True 
            
        if row + col == len(board.board) -1:    
            if self.rightdiagonal[player.symbol] == len(board.board):
                return True             
            
        return False 
    
    
    def handleUndo(self, board : Board, move : Move):
        row = move.cell.row 
        col = move.cell.col 
        player = move.player
        
        if row == col:
            self.leftdiagonal[player.symbol] -= 1
            
        if row + col == len(board.board) -1:
            self.rightdiagonal[player.symbol] -= 1
