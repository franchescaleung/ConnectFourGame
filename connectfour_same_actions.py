import connectfour
def display_board(game_state: connectfour.GameState) -> None:
    '''displays gane board'''
    for i in range(connectfour.BOARD_COLUMNS):
        print(i+1, end = " ")
    print()
    for j in range(connectfour.BOARD_ROWS):
        for k in range(connectfour.BOARD_COLUMNS):
            if game_state.board[k][j] == connectfour.NONE:
                print(".", end = " ")
            elif game_state.board[k][j] == connectfour.RED:
                print("R", end = " ")
            elif game_state.board[k][j] == connectfour.YELLOW:
                print("Y", end = " ")
            else:
                print(".", end = " ")
        print()


def start_new_gameboard():
    game_state = connectfour.new_game()
    return game_state
                   
        

def choose_your_move() -> str:
    '''ask user whether to pop or drop a game piece'''
    while True:
        move = input("Would you like to 'pop' a game piece or 'drop' one?")
        if move == 'pop':
            return "pop"
        elif move == 'drop':
            return 'drop'

def choose_column() -> int:
    '''asks user to choose column'''
    while True:
        try:
            place = int(input("Please choose a column by typing a number between 1 and 7."))
            if 0 < place < 8:
                return place
            else:
                print("Please type a column between 1 to 7")
        except ValueError:
            print("Please type a number.")
def place_move(move_type:
               str, col: int, state: connectfour.GameState) -> connectfour.GameState:
    '''place moves given move type and col'''
    while True:
        try:
            if move_type == 'pop':
                return connectfour.pop(state, col-1)
            elif move_type == 'drop':
                return connectfour.drop(state, col-1)
        except connectfour.InvalidMoveError:
            print("\nPlease try another move.")
            return state
        except connectfour.GameOverError:
            print("The game is over.")
            return state
        except TypeError:
            print("Please try again")

