from .board import Board

class Game:
    """A game object for a computerised game of tic tac toe

            Obtains player moves, performs logic checks and checks game over conditions
        """

    def __init__(self, winning_lines, board_template, board_squares, move_map):
        """Initialize a new game instance.

            winning_lines (int list)     list of winning combinations for tic tac toe
            board_template (str)         board layout stored as a string
            board_squares (str list)     list used to store contents of squares on tic tac toe board
            move_map (dict)              used to map board references to the board_squares list
        """
        self._board = Board(winning_lines, board_template, board_squares)
        self._move_map = move_map
        
    def render_board(self):
        """Draws the board on the (console) screen"""
        self._board.render_board()

    def _get_turn(self, player_name):
        """Prompts player to enter the cell they wish to play this turn and checks it is valid"""
        print(player_name + " choose a cell (e.g. a1, b2, c3):")
        newMove = input()
        
        if newMove in self._move_map.keys():
            x = self._move_map.get(newMove)
            return x
        else:
            print("Please enter a valid cell!")
            return -1

    def game_turn(self, player_name, player_sym):
        """Iterates through a game turn:
            - gets player move
            - check the move is valid
            - places valid move on board
            - returns value based on check - 1: Player has won 2: The board is full 0: Carry on playing """
        playing = -1
        while playing == -1:
            move = self._get_turn(player_name)
            while move == -1:
                move = self._get_turn(player_name)
            playing = self._board.place_piece(move, player_sym)
        if self._board.check_win(player_sym) == 1:
            print(player_name + " wins the match")
            return 1
        elif self._board.check_full_board() == -1:
            print("The board is full")
            return 2
        else:
            return 0
        





