marks = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def display_board():
    board = f'''
  0     1     2 
0  {marks[0][0]} |  {marks[0][1]}  |  {marks[0][2]}
- - -|- - -|- - -
1  {marks[1][0]} |  {marks[1][1]}  |  {marks[1][2]}
- - -|- - -|- - -
2  {marks[2][0]} |  {marks[2][1]}  |  {marks[2][2]}

'''
    print(board)

def player_input(player):
    global marks
    while True:
        print(f"Player {player} input. . .")
        row = int(input("Enter row "))
        column = int(input("Enter column "))

        if marks[row][column] == " ":
            marks[row][column] = player
            break
        else:
            print("Choose another cell!")
            
    display_board()

def check_win():
    for i in range(3):
        if marks[i][0] == marks[i][1] == marks[i][2] != " ":
            return True
        elif marks[0][i] == marks[1][i] == marks[2][i] != " ":
            return True
        
        if marks[0][0] == marks[1][1] == marks[2][2] != " " or marks[0][2] == marks[1][1] == marks[2][0] != " ":
            return True
    return False

def is_draw():
    for row in range(3):
        for column in range(3):
            if marks[row][column] == " ":
                return False
    return True

def play():
    display_board()
    player = "X"

    while True:
        player_input(player)
        
        if check_win():
            print(f"Player {player} won!")
            break

        if is_draw():
            print("Its a tie!")
            break
        
        if player == "X":
            player = "O"
        else:
            player = "X"

play()