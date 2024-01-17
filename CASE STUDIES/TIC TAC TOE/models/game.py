from typing import List, Optional
from .board import Board
from .player import Player
from .move import Move
from .cell import Cell , CellState
from .gamestatus import GameStatus

class Game:
    def __init__(self):
        self.moves: List[Move] = []
        self.board: Board = None # Assuming Board class is defined elsewhere
        self.players: List[Player] = []
        self.current_player: Optional[int] = 0
        self.winning_strategies: List[str] = []
        self.game_status: GameStatus = GameStatus.IN_PROGRESS
        self.winner: Optional[int] = None  # Change to None initially
        self.currentMovePlayerIndex = 0

    def print_result(self):
        if self.game_status == GameStatus.PLAYER_WON:
            print("Game has Ended")
            print(f"Winner is {self.winner}") 
        else:
            print("Game has Ended in Draw")
        
        print('******')
        self.printboard()
        
    def printboard(self):
        self.board.print_board()
        

    def validate_move(self, cell : Cell):
        row = cell.row
        col = cell.col 

        
        if row < 0 and col < 0 and row  >= self.board.dimension and col  >= self.board.dimension:
            return False 
                
        cell = self.board.board[row][col]
        return True if cell.cell_state == CellState.FREE else False
    
    
    def undo(self):
        
        if len(self.moves) == 0:
            print("No moves to undo....")
            return
        
        last_move = self.moves[-1]
        
        for winning_strategy in self.winning_strategies:
            winning_strategy.handleUndo(self.board, last_move)

        cell_in_board = last_move.cell
        cell_in_board.cell_state = CellState.FREE
        cell_in_board.symbol = ''
        cell_in_board.player = None
        
        self.moves.pop()

        # unmarking the current player index 
        self.currentMovePlayerIndex -= 1
        self.currentMovePlayerIndex += len(self.players)
        self.currentMovePlayerIndex %= len(self.players)
       
    def check_player_won(self,current_player , move):
        for wing_stg in self.winning_strategies:
            if wing_stg.check_winner(self.board, move):
                self.winner = current_player
                self.game_status = GameStatus.PLAYER_WON
                return True
        return False  
    
    def check_draw(self):
        dimension = self.board.dimension
        if len(self.moves)  >= dimension * dimension:
            self.game_status = GameStatus.DRAW
            return True 
        return False 
        
    def makemove(self):
        current_player = self.players[self.currentMovePlayerIndex]

        print(f"Player Turn : {current_player}")
        
        proposedCell = current_player.makeMove(self.board)
        row , col    = proposedCell.row , proposedCell.col

        if not self.validate_move(proposedCell):
            print("Invalid move. Retry.")
            return 

        print(' ')
        
        print(f"Current Player {current_player} is made new move at row: {row} and col: {col}")
     
        cell_in_board = self.board.board[row][col]
        cell_in_board.player = current_player
        cell_in_board.cell_state = CellState.OCCUPIED
        cell_in_board.symbol = current_player.symbol
        
        move = Move(current_player,cell_in_board)
        
        self.moves.append(move)
        
        if self.check_player_won(current_player , move):
            return 
        
        if self.check_draw():
            self.game_status = GameStatus.DRAW
            return

        self.currentMovePlayerIndex += 1
        self.currentMovePlayerIndex %= len(self.players)
        
        
    

class GameBuilder:
    def __init__(self) -> None:
        self.game = Game()  # Initialize with default values, you may need to adjust this based on your requirements

    def set_dimension(self, dimension: int) -> 'GameBuilder':  # Return GameBuilder for method chaining
        self.game.board = Board(dimension)
        return self

    def set_players(self, players: List[Player]) -> 'GameBuilder':
        self.game.players = players
        return self

    def set_winning_strategies(self, winning_strategies: List[str]) -> 'GameBuilder':
        self.game.winning_strategies = winning_strategies
        return self

    def build(self) -> Game:
        return self.game
