import math   # used for +infinity and -infinity values

# Tic-Tac-Toe board (1D list of 9 cells)
board = [" "] * 9


# Function to check if player has won
def win(b, p):
    # All possible winning combinations (rows, columns, diagonals)
    wins = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]
    
    # Check if any winning pattern is fully occupied by player p
    return any(all(b[i] == p for i in w) for w in wins)


# Minimax Algorithm
def minimax(b, isMax):
    
    # Terminal states (game over conditions)
    if win(b, "X"): return 1    # AI wins → best score
    if win(b, "O"): return -1   # Opponent wins → worst score
    if " " not in b: return 0   # Draw
    
    # Maximizing player (AI → X)
    if isMax:
        best = -math.inf   # start with lowest possible score
        
        for i in range(9):
            if b[i] == " ":     # if cell empty
                b[i] = "X"      # try move
                best = max(best, minimax(b, False))  # recursive call
                b[i] = " "      # undo move (backtracking)
        
        return best
    
    # Minimizing player (Opponent → O)
    else:
        best = math.inf   # start with highest possible score
        
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(best, minimax(b, True))
                b[i] = " "
        
        return best


print("Minimax Ready")