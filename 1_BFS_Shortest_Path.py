# deque is a double ended queue used for efficient pop from left (O(1))
from collections import deque

# Function to perform BFS and return shortest path
def bfs(graph, start, goal):
    
    # Set to keep track of visited nodes so we don't visit again
    visited = set([start])
    
    # Dictionary to store parent of each node (used to reconstruct path)
    parent = {start: None}
    
    # Queue for BFS traversal, initially contains start node
    q = deque([start])
    
    # Loop until queue becomes empty
    while q:
        # Remove element from front of queue (FIFO)
        node = q.popleft()
        
        # If destination reached, reconstruct the path
        if node == goal:
            path = []
            
            # Trace back from goal to start using parent dictionary
            while node is not None:
                path.append(node)
                node = parent[node]
            
            # Reverse the path because we traced from goal → start
            return path[::-1]
        
        # Visit all neighbors of current node
        for neigh in graph[node]:
            
            # If neighbor not visited yet
            if neigh not in visited:
                visited.add(neigh)        # Mark neighbor as visited
                parent[neigh] = node      # Store parent of neighbor
                q.append(neigh)           # Add neighbor to queue
    
    # If destination not reachable
    return None


# ----------- INPUT SECTION -----------

# Number of vertices
n = int(input("Vertices: "))

# Number of edges
m = int(input("Edges: "))

# Create empty adjacency list for graph
graph = {i: [] for i in range(n)}

# Input edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)   # Because graph is undirected
    graph[v].append(u)

# Input source and destination
s = int(input("Source: "))
d = int(input("Destination: "))

# Call BFS function
res = bfs(graph, s, d)

# Print result
print("Shortest Path:", res if res else "No Path")

# output
# Vertices: 6
# Edges: 7
# 0 1
# 0 2
# 1 3
# 2 3
# 3 4
# 4 5
# 2 5
# Source: 0
# Destination: 5