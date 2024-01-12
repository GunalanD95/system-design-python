from enum import Enum

class GameStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    DRAW = "Draw"
    PLAYER_WON = "Player Won"