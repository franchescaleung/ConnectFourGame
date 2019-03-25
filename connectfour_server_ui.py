import connectfour
import connectfour_same_actions
import connectfour_server_handling


def _starting_game(connection: connectfour_server_handling.GameConnection):
    '''asks player if they want to start game'''
    while True:
        
        answer = input("Do you want to start a game? Please type yes or no.").lower()
        if answer == 'yes':
            connectfour_server_handling.write_line(connection, "AI_GAME")
            break
        elif answer == "no":
            print("Ok. Goodbye")
            return "no"
        


def sending_moves_to_server(connection: connectfour_server_handling.GameConnection, move_type: str) -> int:
    '''sends moves to server'''
    col = str(connectfour_same_actions.choose_column())
    if move_type == 'drop':
        message = 'DROP ' + col
    elif move_type == 'pop':
        message = 'POP ' + col
    connectfour_server_handling.write_line(connection, message)
    return int(col)


def translating_moves(connection: connectfour_server_handling.GameConnection, game_state: connectfour.GameState) -> connectfour.GameState:
    '''translate from server'''
    while True:

        message_from_server = connectfour_server_handling.read_line(connection)
        if message_from_server.startswith("DROP") or message_from_server.startswith("POP"):
            intended_move_from_server = message_from_server.split()
            move = str(intended_move_from_server[0]).lower()
            col = int(intended_move_from_server[-1])
            return connectfour_same_actions.place_move(move, col, game_state)
        elif message_from_server.startswith("INVALID"):
            return game_state
        elif message_from_server == "WINNER_RED":
            return  game_state
        elif message_from_server == "WINNER_YELLOW":
            return game_state

        


def _connecting_to_server() -> connectfour_server_handling.GameConnection:
    '''starts game'''
    connection = connectfour_server_handling.connect()
    connectfour_server_handling.connect_username(connection)
    answer = _starting_game(connection)
    if answer == "no":
        return "no"
    return connection


def game_loop():
    '''plays game with machine'''
    connection = _connecting_to_server()
    if connection == "no":
        return
    else:
        print("Welcome to Connect Four! You are player Red.")
        game_state = connectfour_same_actions.start_new_gameboard()
        connectfour_same_actions.display_board(game_state)
        while True:
            move = connectfour_same_actions.choose_your_move()
            col = sending_moves_to_server(connection, move)
            game_state = connectfour_same_actions.place_move(move, col, game_state)
            connectfour_same_actions.display_board(game_state)
            game_state = translating_moves(connection, game_state)
            if connectfour.winner(game_state) == connectfour.RED:
                connectfour_same_actions.display_board(game_state)
                print("You've won!")
                connectfour_server_handling.close_socket(connection)
                break
            if connectfour.winner(game_state)  == connectfour.YELLOW:
                connectfour_same_actions.display_board(game_state)
                print("YELLOW has won!")
                connectfour_server_handling.close_socket(connection)
                break
            connectfour_same_actions.display_board(game_state)
            
        
        
            
        
    
    
if __name__ == '__main__':
    game_loop()
    
