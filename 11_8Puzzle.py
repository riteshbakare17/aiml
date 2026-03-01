# deque is used as queue for BFS
from collections import deque

# Goal state of 8-puzzle
goal = "123456780"
# 0 represents blank tile

# Possible moves of blank tile: Up, Down, Left, Right
moves = [(-1,0), (1,0), (0,-1), (0,1)]


# Function to generate all possible next states
def neighbors(state):
    
    # Find position of blank tile (0)
    idx = state.index("0")
    
    # Convert index into row and column
    x, y = divmod(idx, 3)
    
    res = []   # store neighbour states
    
    # Try all four moves
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        
        # Check if new position is inside board
        if 0 <= nx < 3 and 0 <= ny < 3:
            
            # Convert new row, col back to index
            ni = nx * 3 + ny
            
            # Convert string → list (to swap tiles)
            lst = list(state)
            
            # Swap blank with neighbour tile
            lst[idx], lst[ni] = lst[ni], lst[idx]
            
            # Convert list back to string and store
            res.append("".join(lst))
    
    return res



# Take starting state input
start = input("Enter start state (e.g., 123456780): ")

# BFS Queue → stores (current_state, path)
q = deque([(start, [])])

# Set to avoid revisiting states
visited = set([start])


# BFS Loop
while q:
    
    # Remove state from front of queue
    state, path = q.popleft()
    
    # If goal reached → print moves
    if state == goal:
        print("Moves:", len(path))
        break
    
    # Generate next possible states
    for n in neighbors(state):
        if n not in visited:
            visited.add(n)
            q.append((n, path + [n]))
            
            
# Enter start state (e.g., 123456780): 123456708