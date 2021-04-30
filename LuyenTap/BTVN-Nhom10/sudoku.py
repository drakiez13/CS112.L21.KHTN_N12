def get_sudoku_board():
    game_board = []
    for _ in range(9):
        line = list(map(int, input().split()))
        game_board.append(line)
    return game_board
    
def print_sudoku(s):
    for i in range(len(s)):
        if (i % 3 == 0 and i != 0): print("- "*11)
        for j in range(len(s)):
            if (j % 3 == 0 and j != 0): print("| ", end = "")
            if (j == 8):
                print(s[i][j])
            else:
                print(str(s[i][j]) + " ", end = "")

def find_blank_box(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return i, j
    return None

def check(board, value, row, colum):
    for i in range(len(board)):
        if (board[i][colum] == value):
            return False
    for i in range(len(board[0])):
        if (board[row][i] == value):
            return False
    for i in range(int(row/3)*3, int(row/3)*3 + 3):
        for j in range(int(colum/3)*3, int(colum/3)*3 + 3):
            if (board[i][j] == value):
                return False
    return True

def solve_sudoku(board):
    blank_box = find_blank_box(board)

    if (blank_box is None):
        return True
    else:
        row, column = blank_box 
    
    for number in range(1, 10):
        if (check(board, number, row, column)): 
            board[row][column] = number 
            if solve_sudoku(board):
                return True
            else:
                board[row][column] = 0
        
    return False

game_board = [[0, 0, 5, 0, 0, 8, 0, 0, 0],
       [1, 0, 6, 0, 0, 3, 0, 0, 4],
       [0, 0, 2, 0, 0, 0, 0, 0, 7],
       [0, 0, 1, 0, 0, 4, 0, 0, 0],
       [0, 0, 0, 0, 8, 0, 0, 6, 0],
       [0, 7, 0, 0, 0, 0, 0, 0, 0],
       [9, 0, 0, 5, 3, 0, 0, 0, 0],
       [0, 0, 0, 6, 0, 0, 8, 0, 1],
       [0, 0, 0, 0, 2, 0, 0, 4, 9]]

print_sudoku(game_board)
solve_sudoku(game_board)
print("Loi giai:")
print_sudoku(game_board)
