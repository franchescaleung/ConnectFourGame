#console only user interface
#console only version
import connectfour
import connectfour_same_actions

def start_game() -> None:
    '''asks user if want to start game, if yes, return new game board else return none'''
    while True:
        answer = input("Do you want to start a new game? Please type yes or no.").lower()
        if answer.strip() == "yes":
            game_loop()
            break
        elif answer.strip() == "no":
            print("Ok.")
            break
        else:
            print("Please answer yes or no.")


def game_loop() -> None:
    '''plays the game on same computer'''
    game_state = connectfour_same_actions.start_new_gameboard()
    while True:
        connectfour_same_actions.display_board(game_state)
        if game_state.turn == connectfour.RED:
            print("Red, please choose a move.")
        elif game_state.turn == connectfour.YELLOW:
            print("Yellow, please choose a move.")

        move = connectfour_same_actions.choose_your_move()
        col = connectfour_same_actions.choose_column()
        game_state = connectfour_same_actions.place_move(move, col, game_state)

        if connectfour.winner(game_state) == connectfour.RED:
            connectfour_same_actions.display_board(game_state)
            print("Red has won!")
            break
        if connectfour.winner(game_state) == connectfour.YELLOW:
            connectfour_same_actions.display_board(game_state)
            print("Yellow has won!")
            break
        
if __name__ == '__main__':
    start_game()
    
    

