# Import libraries
import random 

# Declare variables
playerOneName = ''
playerTwoName = ''

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
CROSS = ' X'
CIRCLE = 'O'
squares = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

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


def getName(playerNum):
    print("Please enter name for player " + str(playerNum) + ":")
    name = input()
    return name


def renderBoard():
    print(BOARD_TEMPLATE.format(*squares))


def getTurn(playerName):
    print(playerName + " choose a cell (e.g. a1, b2, c3):")
    newMove = input()
    # TODO: Make this into a dictionary lookup table
    if newMove in MOVE_MAP.keys():
        x = MOVE_MAP.get(newMove)
        return x
    else:
        print("Please enter a valid cell!")
        return -1


def checkWin(symbol):
    for line in WINNING_LINES:
        if all(squares[line[i]] == symbol for i in range(3)):
            return 1
    return 0


def checkMove(theMove, piece):
    if squares[theMove] == '  ':
        squares[theMove] = piece
        return 1
    else:
        print("This space is already taken")
        return - 1


# Main Program Loop

# Get names of players and store them

playerOneName = getName(1)
playerTwoName = getName(2)

# Randomise who gets to go first

# TODO: Print player 1 name below.

print("""
      Player 1 select a coin face:
      1: Heads
      2: Tails""")

# TODO: Enacapsulate in a try statement.

coinSelect = input()


random.seed()
coinLand = random.randint(1, 2)
if coinLand == 1:
    print("The coin landed on heads!")
else:
    print("The coin landed on Tails!")

if coinSelect == coinLand:
    print(playerOneName + " you go first!")
    firstPlayer = playerOneName
    secondPlayer = playerTwoName
else:
    print(playerTwoName + " you go first!")
    firstPlayer = playerTwoName
    secondPlayer = playerOneName

# TODO: Game event logging
# TODO: Finish game loop and logic

playing = True
currentPlayer = firstPlayer
currentPiece = CIRCLE

while playing:
    move = -1
    while move == -1 and playing:                   # Value returned by getTurn
        renderBoard()
        move = getTurn(currentPlayer)
        move = checkMove(move, currentPiece)
        has_won = checkWin(currentPiece)
        if has_won == 1:
            print(currentPlayer + " has won")
            playing = False
            break
        if all(cell != '  ' for cell in squares):
            print("It's a draw!")
            playing = False
            break
        if currentPlayer == firstPlayer:
            currentPlayer = secondPlayer
            currentPiece = CROSS
        else:
            currentPlayer = firstPlayer
            currentPiece = CIRCLE
    move = -1
