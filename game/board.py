class Board:
        """A board object for a computerised game

            This board can be used for the Tic Tac Toe game.
            Stores the board, the pieces used on the board, 
            possible moves and winning lines.
        """


        def __init__(self,winning_lines, board_template, board_squares):
            """Initialise a new board instance

                winning_lines   (int list)    stores winning combinations
                board_template  (str)         template used for the board
                board_squares   (str list)    list used for storing board positions
            """

            self._winning_lines = winning_lines
            self._template = board_template
            self._board_squares = board_squares

        def render_board(self):
            """Draws the board on the (console) screen"""

            print(self._template.format(*self._board_squares))

        def place_piece(self, sqaure_num, player_symbol):
             """Places player symbol in square on board
                Returns 1 if successful, -1 if square is taken"""
             
             if self._board_squares[sqaure_num] == '  ':
                  self._board_squares[sqaure_num] = player_symbol
                  return 1
             else:
                  print("This space is already taken")
                  return -1

        def check_win(self, symbol):
            """Checks if game is won using specifed player symbol
                returns 1 for win, 0 if no winner(yet)"""

            for line in self._winning_lines:
                 if all(self._board_squares[line[i]] == symbol for i in range(3)):
                    return 1
            return 0

        def check_full_board(self):
             """Checks to see if there are free spaces available on the board"""
             for square in self._board_squares:
                  if square == '  ':
                       return 1
                  
             return -1                
             
            