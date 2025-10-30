from .board import Board

class Game:

    def __init__(self, winning_lines, board_template, board_squares, move_map):
        self._board = Board(winning_lines, board_template, board_squares)
        self._move_map = move_map
        
    def render_board(self):
        self._board.render_board()

    def _get_turn(self, player_name):
        print(player_name + " choose a cell (e.g. a1, b2, c3):")
        newMove = input()
        
        if newMove in self._move_map.keys():
            x = self._move_map.get(newMove)
            return x
        else:
            print("Please enter a valid cell!")
            return -1

    def game_turn(self, player_name, player_sym):
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
        





