# Function to solve Sudoku using Backtracking
def solve(board):

    # Traverse entire 9x9 board
    for i in range(9):
        for j in range(9):

            # If cell is empty (0 means empty)
            if board[i][j] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):

                    # Check if placing number is valid
                    if valid(board, i, j, num):

                        # PLACE number (make move)
                        board[i][j] = num

                        # Recursively try to solve remaining board
                        if solve(board):
                            return True

                        # BACKTRACK (undo move if not solved)
                        board[i][j] = 0

                # If no number works → backtrack
                return False

    # If no empty cell left → puzzle solved
    return True



# Function to check if number placement is valid
def valid(b, r, c, num):

    # -------- CHECK ROW & COLUMN --------
    for i in range(9):
        # If number already in row OR column → invalid
        if b[r][i] == num or b[i][c] == num:
            return False

    # -------- CHECK 3x3 SUBGRID --------
    # Find starting index of 3x3 box
    sr, sc = 3 * (r // 3), 3 * (c // 3)

    # Traverse the 3x3 box
    for i in range(3):
        for j in range(3):
            if b[sr + i][sc + j] == num:
                return False

    # If no conflicts → valid placement
    return True



# -------- INPUT SECTION --------

board = []

print("Enter 9x9 Sudoku (0 for empty):")

# Take 9 rows as input
for _ in range(9):
    board.append(list(map(int, input().split())))

# Solve Sudoku
if solve(board):

    # Print solved board
    for row in board:
        print(row)
else:
    print("No Solution")
    
    
# Enter 9x9 Sudoku (0 for empty):
# 5 3 0 0 7 0 0 0 0
# 6 0 0 1 9 5 0 0 0
# 0 9 8 0 0 0 0 6 0
# 8 0 0 0 6 0 0 0 3
# 4 0 0 8 0 3 0 0 1
# 7 0 0 0 2 0 0 0 6
# 0 6 0 0 0 0 2 8 0
# 0 0 0 4 1 9 0 0 5
# 0 0 0 0 8 0 0 7 9