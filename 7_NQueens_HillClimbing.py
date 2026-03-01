import random   # used to generate random initial state

# Function to count number of conflicts in N-Queens board
def conflicts(state):
    n = len(state)   # number of queens
    c = 0            # conflict counter
    
    # Compare every pair of queens
    for i in range(n):
        for j in range(i+1, n):
            
            # Same row OR same diagonal → conflict
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                c += 1
    
    return c


# Hill Climbing algorithm
def hill_climb(n):
    
    # Generate random initial board state
    # state[i] = row position of queen in column i
    state = [random.randint(0, n-1) for _ in range(n)]
    
    while True:
        
        # Count current conflicts
        curr = conflicts(state)
        
        # If no conflicts → solution found
        if curr == 0:
            return state
        
        neighbors = []
        
        # Generate all neighbour states
        for col in range(n):
            for row in range(n):
                
                new = state.copy()   # copy current state
                new[col] = row       # move queen in column to new row
                
                # store (conflicts, state)
                neighbors.append((conflicts(new), new))
        
        # Choose neighbour with minimum conflicts
        best = min(neighbors, key=lambda x: x[0])
        
        # If no improvement → stuck in local maxima
        if best[0] >= curr:
            return None
        
        # Move to better state
        state = best[1]


# -------- INPUT --------
n = int(input("N: "))

# Run hill climbing
sol = hill_climb(n)

# Print solution
print("Solution:", sol if sol else "No Solution")


# N: 4