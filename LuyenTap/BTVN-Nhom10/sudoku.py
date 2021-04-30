def get_sudoku_board():
    game_board = []
    for _ in range(9):
        line = list(map(int, input().split()))
        game_board.append(line)
    return game_board
    
def print_sudoku(board):
    for row in range(len(board)):
        if (row % 3 == 0 and row != 0): print("- "*11)
        for col in range(len(board)):
            if (col % 3 == 0 and col != 0): print("| ", end = "")
            if (col == 8):
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end = "")

def find_blank_box(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return row, col
    return None

def check(board, value, row, col):
    for r in range(len(board)):
        if (board[r][col] == value):
            return False
    for c in range(len(board[0])):
        if (board[row][c] == value):
            return False
    for r in range(int(row/3)*3, int(row/3)*3 + 3):
        for c in range(int(col/3)*3, int(col/3)*3 + 3):
            if (board[r][c] == value):
                return False
    return True

def solve_sudoku(board):
    blank_box = find_blank_box(board)

    if (blank_box is None):
        return True
    else:
        row, col = blank_box 
    
    for number in range(1, 10):
        if (check(board, number, row, col)): 
            board[row][col] = number 
            if solve_sudoku(board):
                return True
            else:
                board[row][col] = 0
        
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
