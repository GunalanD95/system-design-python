from enum import Enum

class CellState(Enum):
    FREE = 'Free'
    OCCUPIED = 'Occupied'

class Cell:
    def __init__(self, row, col,player = None) -> None:
        self.row = row
        self.col = col
        self.symbol: str = ''
        self.cell_state: CellState = CellState.FREE
        self.player = player

    def __repr__(self) -> str:
        return f'Cell(row={self.row}, col={self.col}, symbol={self.symbol}, state={self.cell_state.value})'
