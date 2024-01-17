from typing import List, Optional , Tuple
from .cell import Cell

class Board:
    
    def __init__(self , dimension: int ) -> None:
        self.dimension = dimension
        self.board: List[List[Cell]] = [[Cell(i, j) for j in range(dimension)] for i in range(dimension)]
        
        
    def print_board(self):
        for row in self.board:
            for cell in row:
                print(' | ' + cell.symbol + ' | ', end=' ')
            print('')
            print('-' * (len(row) * 6 + 1))

        