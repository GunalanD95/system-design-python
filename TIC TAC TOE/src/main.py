from entities.board import Board  
from entities.game import Game , GamerBuilder
from entities.player import Player 

game_builder = GamerBuilder()

print('Welcome to tic tac toe Game!')
print('-----------------------------')

print('Enter Player1 Name and Symbol (x):')
game = game_builder.create_player1('gunalan','x').create_player2('guhan','o').build()


total_moves = 9

while total_moves > 0:
    