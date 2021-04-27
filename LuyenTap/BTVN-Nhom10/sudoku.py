
def input_sudoku():
    Ask = []
    for i in range(9):
        t = []
        t = list(map(int, input().split()))
        Ask.append(t)
    return Ask
def print_sudoku(s):
    for i in range(len(s)):
        if (i % 3 == 0 and i != 0): print("- "*11)
        for j in range(len(s)):
            if (j % 3 == 0 and j != 0): print("| ", end = "")
            if (j == 8):
                print(s[i][j])
            else:
                print(str(s[i][j]) + " ", end = "")

def find(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if (s[i][j] == 0):
                return i, j
    return None

def check(s, value, row, colum):
    for i in range(len(s)):
        if (s[i][colum] == value):
            return False
    for i in range(len(s[0])):
        if (s[row][i] == value):
            return False
    for i in range(int(row/3)*3, int(row/3)*3 + 3):
        for j in range(int(colum/3)*3, int(colum/3)*3 + 3):
            if (s[i][j] == value):
                return False
    return True

def Solve_Sudoku(s):
    x = find(s)
    if (x == None): return True
    else: r, c = x 
    for i in range(1, 10):
        if (check(s, i, r, c)): 
            s[r][c] = i 
            if Solve_Sudoku(s):
                return True
            else:
                s[r][c] = 0
    return False
Ask = [[0, 0, 5, 0, 0, 8, 0, 0, 0],
       [1, 0, 6, 0, 0, 3, 0, 0, 4],
       [0, 0, 2, 0, 0, 0, 0, 0, 7],
       [0, 0, 1, 0, 0, 4, 0, 0, 0],
       [0, 0, 0, 0, 8, 0, 0, 6, 0],
       [0, 7, 0, 0, 0, 0, 0, 0, 0],
       [9, 0, 0, 5, 3, 0, 0, 0, 0],
       [0, 0, 0, 6, 0, 0, 8, 0, 1],
       [0, 0, 0, 0, 2, 0, 0, 4, 9]]
print_sudoku(Ask)
Solve_Sudoku(Ask)
print("Loi giai")
print_sudoku(Ask)
