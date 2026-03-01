# Function to place queens column by column
def solve(n, col, board):
    
    # If all queens placed → solution found
    if col == n:
        return True
    
    # Try placing queen in every row of current column
    for row in range(n):
        
        # Check if this position is safe
        if safe(board, row, col, n):
            
            # PLACE queen
            board[row][col] = 1
            
            # Recursively place next queen in next column
            if solve(n, col + 1, board):
                return True
            
            # BACKTRACK → remove queen if solution not found
            board[row][col] = 0
    
    # No safe position found in this column
    return False



# Function to check if queen placement is safe
def safe(board, row, col, n):
    
    # -------- CHECK LEFT ROW --------
    # No queen should be in same row (left side)
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # -------- CHECK UPPER DIAGONAL --------
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # -------- CHECK LOWER DIAGONAL --------
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    # Safe to place queen
    return True



# -------- INPUT --------
n = int(input("N: "))

# Create NxN chessboard filled with 0
board = [[0] * n for _ in range(n)]

# Solve N-Queens
if solve(n, 0, board):
    
    # Print board (1 = queen placed)
    for row in board:
        print(row)
else:
    print("No Solution")
    
# N: 4