from models.cell import Cell
from models.board import Board
from models.botdifficulty import Botdifficulty 
from .botplayingstrategy import BotPlayingStrategy, EasyBotPlayingStrategy, MediumBotPlayingStrategy, HardBotPlayingStrategy

class BotPlayingStrategyFactory:

    @staticmethod
    def get_bot_strategy(difficulty: Botdifficulty) -> BotPlayingStrategy:
        if difficulty == Botdifficulty.EASY:
            return EasyBotPlayingStrategy()
        elif difficulty == Botdifficulty.MEDIUM:
            return MediumBotPlayingStrategy()
        elif difficulty == Botdifficulty.HARD:
            return HardBotPlayingStrategy()
        else:
            raise ValueError("Invalid difficulty level")
