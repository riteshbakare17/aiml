import math   # provides +infinity and -infinity using math.inf

# Create Tic-Tac-Toe board with 9 empty cells
board = [" "] * 9
# Index positions:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8


# Function to check if a player has won the game
def win(b, p):
    
    # All possible winning combinations in Tic-Tac-Toe
    wins = [
        [0,1,2],  # row 1
        [3,4,5],  # row 2
        [6,7,8],  # row 3
        [0,3,6],  # column 1
        [1,4,7],  # column 2
        [2,5,8],  # column 3
        [0,4,8],  # diagonal
        [2,4,6]   # diagonal
    ]
    
    # any() → checks if ANY winning combination is true
    # all() → checks if ALL positions in that combination have same player symbol
    return any(all(b[i] == p for i in w) for w in wins)



# Alpha-Beta pruning algorithm
def alphabeta(b, depth, alpha, beta, isMax):
    
    # -------- TERMINAL CONDITIONS --------
    
    # If AI (X) wins → best score
    if win(b, "X"): 
        return 1
    
    # If Opponent (O) wins → worst score
    if win(b, "O"): 
        return -1
    
    # If board full → draw
    if " " not in b: 
        return 0
    
    
    # -------- MAXIMIZING PLAYER (AI = X) --------
    if isMax:
        
        # Start with worst possible value
        value = -math.inf
        
        # Try placing X in every empty cell
        for i in range(9):
            if b[i] == " ":
                
                # MAKE MOVE (simulate)
                b[i] = "X"
                
                # Recursively evaluate opponent move
                value = max(value,
                            alphabeta(b, depth+1, alpha, beta, False))
                
                # UNDO MOVE (Backtracking)
                b[i] = " "
                
                # Update alpha (best value for maximizer so far)
                alpha = max(alpha, value)
                
                # -------- PRUNING STEP --------
                # If alpha becomes >= beta → no need to explore further
                if alpha >= beta:
                    break   # cut the branch
        
        return value
    
    
    # -------- MINIMIZING PLAYER (Opponent = O) --------
    else:
        
        # Start with worst possible value for minimizer
        value = math.inf
        
        # Try placing O in every empty cell
        for i in range(9):
            if b[i] == " ":
                
                # MAKE MOVE
                b[i] = "O"
                
                # Recursively evaluate AI move
                value = min(value,
                            alphabeta(b, depth+1, alpha, beta, True))
                
                # UNDO MOVE
                b[i] = " "
                
                # Update beta (best value for minimizer so far)
                beta = min(beta, value)
                
                # -------- PRUNING STEP --------
                if alpha >= beta:
                    break   # cut the branch
        
        return value


print("Alpha-Beta Ready")