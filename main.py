import random
from game.game import Game
from game.player import Player

# Create variables required by game
# Create Board variable

BOARD_TEMPLATE = """"
     a      b     c
   |     |     |     |
1  | {}  | {}  | {}  |
   |_____|_____|_____|
   |     |     |     |
2  | {}  | {}  | {}  |
   |_____|_____|_____|
   |     |     |     |
3  | {}  | {}  | {}  |
   |     |     |     |
"""

SQUARES = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

# Dictionary based lookup table for all possible moves

MOVE_MAP = {
    "a1": 0, "b1": 1, "c1": 2,
    "a2": 3, "b2": 4, "c2": 5,
    "a3": 6, "b3": 7, "c3": 8
}

# Create a list of possible winning combinations

WINNING_LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def get_name(player_order):
    print("Please enter name for " + player_order + " player:")
    name = input()
    return name

def main():
    player_one = get_name("first")
    player_two = get_name("second") 

    print("""
      Player 1 select a coin face:
      1: Heads
      2: Tails""")


    coin_select = input()

    random.seed()
    coin_land = random.randint(1, 2)
    if coin_land == 1:
        print("The coin landed on heads!")
    else:
        print("The coin landed on Tails!")

    if coin_select == coin_land:
        print(player_one + " you go first!")
        first_player = Player(player_one, ' X')
        first_player = Player(player_two, 'O ')
    else:
        print(player_two + " you go first!")
        first_player = Player(player_two, ' X')
        second_player = Player(player_one, 'O')

    #Create the game instance, now we have all required data

    ttt_game = Game(WINNING_LINES, BOARD_TEMPLATE, SQUARES, MOVE_MAP)

    #Start the game loop

    playing = True
    current_player = first_player.get_name()
    current_piece = first_player.get_symbol()

    while playing:
        ttt_game.render_board()
        game_turn = ttt_game.game_turn(current_player, current_piece)
        if game_turn == 1 or game_turn == 2:
            playing = False
        if current_player == first_player.get_name():
            current_player = second_player.get_name()
            current_piece = second_player.get_symbol()
        else:
            current_player = first_player.get_name()
            current_piece = first_player.get_symbol() 

if __name__ == "__main__":
    main()