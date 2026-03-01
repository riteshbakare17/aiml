# deque is used for BFS queue (FIFO)
from collections import deque

# Maze representation
# 0 = free cell
# 1 = wall / blocked cell
maze = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

# Start and Goal coordinates
start = (0,0)
goal = (2,2)

# Possible movements → Down, Up, Right, Left
dirs = [(1,0), (-1,0), (0,1), (0,-1)]


# BFS function to find shortest path in maze
def bfs():
    
    # Queue stores ((x,y), path_so_far)
    q = deque([(start, [])])
    
    # Set to keep track of visited cells
    visited = set([start])
    
    # BFS loop
    while q:
        
        # Remove front element from queue
        (x, y), path = q.popleft()
        
        # If goal reached → return full path
        if (x, y) == goal:
            return path + [(x, y)]
        
        # Explore all 4 possible directions
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            # Check valid move:
            # 1) inside grid
            # 2) not a wall
            # 3) not visited
            if (0 <= nx < 3 and 0 <= ny < 3 
                and maze[nx][ny] == 0 
                and (nx, ny) not in visited):
                
                visited.add((nx, ny))
                
                # Add new cell to queue with updated path
                q.append(((nx, ny), path + [(x, y)]))


# Print shortest path from start to goal
print("Path:", bfs())