# board

board = ["_" , "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# display board

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#if game is still going

game_still_going = True

#who won or tie
winner = None

#whos tunr is it
current_player = "X"

# play game

def play_game():

    #display initial board
    display_board()

    while game_still_going:

        #handle a single turn of an arbitary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

    #the game has ended
    if winner == "X" or winner == "O":
        print(winner + "won.")
    elif winner == None:
        print("Tie.")

  
def handle_turn(player):

    print(player + "'s turn.")
    position= input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1" , "2" , "3" ,"4", "5", "6", "7", "8","9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "_":
        valid =True
    else:
        print("YOu can't go there.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():

    global winner
    #check rows
    row_winner = check_rows()
    #check colimns
    column_winner = check_column()
    #check diagonals
    diagonals_winner = check_diagonals()
    if row_winner:
        #theres is a winner
        winner = row_winner
    elif column_winner:
        #there is  a winner
        winner = column_winner
    elif diagonals_winner:
        winner  = diagonals_winner
    else:
        #there is a win
        winner = None
    return

def check_rows():
        #set up global variab;es
    global game_still_going
    #check if any of the rows have all the same value 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None 

def check_column():
    #set up global variab;es
    global game_still_going
    #check if any of the rows have all the same value 
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:    
        return None

def check_diagonals():
        #set up global variab;es
    global game_still_going
    #check if any of the diagonal have all the same value 
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2 :
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[4]
    

    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
        
    return

def flip_player():

    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return



play_game()
# handle turns
# check win
 # check rows
 # check columns
 # check diagonals
# check tie
# flip player 

