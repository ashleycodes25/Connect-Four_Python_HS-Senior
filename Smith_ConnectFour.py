def board(game_board, rows):
    for rows in game_board:
        print(rows)
    
def win(board, player):
    for row in range(rows):
        for col in range(cols-3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for row in range(rows - 3):
        for col in range(cols):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(rows - 3):
        for col in range(cols - 3):
            for col in range(cols - 3):
                if all(board[row + i][col + i] == player for i in range(4)):
                    return True
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False       

playing_game = True
playing_round = True
red_player = "R"
blue_player = "B"
rows, cols = (6, 7)
while playing_game:
    game_board = [["_" for column in range(cols)] for row in range(rows)]
    dictionary = {1 : 5, 2 : 5, 3 : 5, 4 : 5, 5 : 5, 6 : 5, 7 : 5}
    col_full = []
    choosing_column = True
    print("Welcome to Connect 4!")
    while playing_round:
        print("Here is the current board")
        board(game_board, rows)
        print("Red Player: Choose a column number to drop your token!")
        choosing_column = True
        while(choosing_column):
            red_col = int(input())
            if not (red_col in col_full):
                game_board[dictionary.get(red_col)][red_col-1] = "R"
                dictionary.update({red_col : dictionary.get(red_col)-1})
                if dictionary.get(red_col) == -1:
                    col_full.append(red_col)
                choosing_column = False
            else:
                print("That column is full! Please choose a different column!")
        if win(game_board, red_player):
            print("Congratulations red player! You won!")
            playing_round = False
            break
        print("Blue Player: Choose a column number to drop your token!")
        choosing_column = True
        while choosing_column:
            blue_col = int(input())
            if not blue_col in col_full:
                game_board[dictionary.get(blue_col)][blue_col-1] = "B"
                dictionary.update({blue_col : dictionary.get(blue_col)-1})
                if dictionary.get(blue_col) == -1:
                    col_full.append(blue_col)
                choosing_column = False
            else:
                print("That column is full! Please choose a different column!")
        if win(game_board, blue_player):
            print("Congratulations blue player! You won!")
            playing_round = False
    print("Would you like to play again?")
    answer = input().lower()
    if answer == "yes":
        print("Awesome! Good luck in the next game!")
        playing_round = True
    if answer == "no":
        print("Thanks for playing! Have a good day!")
        playing_game = False
        
        
    


