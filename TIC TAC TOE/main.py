from controllers.gamecontroller import GameController
from models.player import Player , HumanPlayer
from models.bot import BotPlayer
from strategies.winningstrategy import RowWinningStrategy , ColWinningStrategy , DiagonalWinningStrategy
from models.gamestatus import GameStatus
from models.botdifficulty import Botdifficulty

def main():
    game_controller = GameController()
    
    print("......Creating Game......")
    
    dimension = 3
    
    players = [
        HumanPlayer('Gunalan','X'),
        HumanPlayer('Guhan'  ,'O'),
        # BotPlayer('O',Botdifficulty.EASY)
    ]
    
    winning_strategies = [
        RowWinningStrategy(dimension,players),
        ColWinningStrategy(dimension,players)
    ]
    
    game = game_controller.create_game(dimension,players,winning_strategies)
        
    print(f'......Created Game : {game.__dict__}........')

    print("-------------- Game is starting --------------")
    
    while game.game_status == GameStatus.IN_PROGRESS:
        print("This is how board looks like:")
        game_controller.displayBoard(game)

        print(' ')
        print("Does anyone want to undo? (y/n)")
            
        should_undo = input('')

        if should_undo == 'y':
            game_controller.undo(game)
        else:
            game_controller.makeMove(game)
    
    game_controller.printResult(game)
    
if __name__ == '__main__' :
    main()