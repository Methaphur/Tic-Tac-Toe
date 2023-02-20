def generate_board(N):
    board = [[0 for i in range(N)] for i in range(N)]
    return board

def print_board(board):
    pieces = {0:" ","O":"O","X":"X"}
    for row in board:
        for item in row:
            if item in pieces:
                print(f'| {pieces[item]} |',end = "")
            else:
                print(f'| {item} |', end = "")
        print()
    
def is_free(row,col,board):
    if board[row][col] != 0:
        return False
    else:
        return True
    
def has_won(x,y,char,board):
    rows = 0
    columns = 0 
    l_diagonals = 0
    r_diagonals = 0

    for row in board:
        if row[y] == char:
            columns += 1
    
    if columns == len(board):
        return True

    for item in board[x]:
        if item == char:
            rows += 1
        
    if rows == len(board):
        return True
        
    for row in range(len(board)):
        if board[row][row] == char:
            l_diagonals += 1
        
    if l_diagonals == len(board):
        return True

    for row in range(len(board)):
        col = len(board)- (row+1) 
        if board[col][row] == char:
            r_diagonals += 1
        
    if r_diagonals == len(board):
        return True
    else:
        return False
        
def tie(board):
    for row in board:
        for item in row:
            if item == 0:
                return False
    return True
    
def game(board,player):
    def move_make(N):  
        board = [[(i,j) for j in range(N)] for i in range(N)]
        move = []
        for i in board:
            move += i
        moves = {i+1:move[i] for i in range(N*N)}

        return moves
    moves = move_make(len(board))
    def move(char):
        user_move = int(input(f"Enter player {player[char]}'s ({char}) move: "))
        row,column = moves[user_move]
        player_move(row,column,char,board)
        print_board(board)
        print()

        if has_won(row,column,char,board):
            print(f'Congrats {player[char]}! You Won')
            return None

        if tie(board):
            print(f' The game has been a tie')
            return None
        
        else:
            return True
    def player_move(x,y,char,board):
        if is_free(x,y,board):
            board[x][y] = char
        else:
            print("Unavailable spot !!")
            print_board(board)
            print()
            char_move = int(input("Play the move again : "))
            row,col = moves[char_move]
            player_move(row,col,char,board)
    
    flag = True
    while True:
        
        X = move("X")
        if X == None: break
        Y = move("O")
        if Y == None: break 

def instructions(N):
    sample_board = []
    k = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(k)
            k += 1
        sample_board.append(row)
    print_board(sample_board)
    print(f'The numbers represent the input for that spot')
    print(f'Each player has one move per turn ')

def play_game():
    N = int(input("Enter size of board: "))
    player_1 = input("Enter first player's name: ")
    player_2 = input("Enter second player's name: ")
    players = {"X":player_1 , "O":player_2 }
    board = generate_board(N)
    instructions(N)
    game(board,players)

play_game()
