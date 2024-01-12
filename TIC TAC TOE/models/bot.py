from .playertype import PlayerType
from .player import Player
from .botdifficulty import Botdifficulty
from strategies.botplayingstrategy import BotPlayingStrategy
from strategies.botstrategyfactory import BotPlayingStrategyFactory

class BotPlayer(Player):    
    def __init__(self,symbol: str , bot_diffculty : Botdifficulty) -> None:
        self.bot_diffculty = bot_diffculty
        self.bot_playing_stgy : BotPlayingStrategy = BotPlayingStrategyFactory.get_bot_strategy(bot_diffculty)
        super().__init__(symbol , PlayerType.BOT)
        
    def get_bot_diff_level(self):
        return self.bot_diffculty
    
    
    def makeMove(self,board):
        return self.bot_playing_stgy.makeMove(board)
    
    def __str__(self) -> str:
        return f"Player : Bot | {self.symbol}"