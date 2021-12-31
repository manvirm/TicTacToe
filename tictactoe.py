# Board for playing game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Print out board
def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    current_player = "X"
    tie = False
    Winner = None
    show_board()

    while(not(Winner) and not(tie)):
        play_turn(current_player)
        Winner = check_game_over(Winner)
        tie = check_tie()
        current_player = switch_player(current_player)
    if(Winner):
        print(Winner + " has won!")
    elif(tie):
        print("Tie.")

# Player chooses which position they want to insert X or O
def play_turn(player):

    # position is to compare the string
    position = input("Choose a number between 1 and 9: ")

    # User has to choose a valid input (1-9)
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a number between 1 and 9: ")

    # positionInt is to check the spot in the board
    positionInt = int(position) - 1

    # User has to choose spot that isnt already taken (cannot replace spot taken by X with O)
    while board[positionInt] != "-":

        position = input("Spot is taken. Choose a number between 1 and 9: ")

        # User has to choose a valid input (1-9)
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a number between 1 and 9: ")

        positionInt = int(position)-1

    board[positionInt] = player
    show_board()

# Check if there is a winner, which means game is over
def check_game_over(Winner):
    rowWinner = check_row()
    columnWinner = check_column()
    diagonalWinner = check_diagonal()

    if(rowWinner):
        Winner = rowWinner
    elif(columnWinner):
        Winner = columnWinner
    elif(diagonalWinner):
        Winner=diagonalWinner
    return Winner

def check_row():
    if board[0] == board[1] == board[2] != '-':
        return board[0]
    if board[3] == board[4] == board[5] != "-":
        return board[3]
    if board[6] == board[7] == board[8] != "-":
        return board[6]
    else: return

def check_column():
    if board[0] == board[3] == board[6] != '-':
        return board[0]
    if board[1] == board[4] == board[7] != "-":
        return board[1]
    if board[2] == board[5] == board[8] != "-":
        return board[2]
    else:
        return

def check_diagonal():
    if board[0] == board[4] == board[8] != '-':
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]

    else:
        return

def check_tie():
    if "-" not in board:
        return True
    return

# Swap from player X to O, vice versa
def switch_player(player):
    if player == "X":
        return "O"
    if player == "O":
        return "X"


play_game()