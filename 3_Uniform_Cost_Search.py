# heapq is used to create a priority queue (min-heap)
import heapq

# Uniform Cost Search function
def ucs(graph, start, goal):
    
    # Priority queue stores (cost, current_node, path_so_far)
    pq = [(0, start, [])]
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Loop until priority queue becomes empty
    while pq:
        
        # Pop node with minimum cost
        cost, node, path = heapq.heappop(pq)
        
        # Skip if already visited
        if node in visited:
            continue
        
        # Mark node as visited
        visited.add(node)
        
        # Add node to path
        path = path + [node]
        
        # If goal reached → return total cost and path
        if node == goal:
            return cost, path
        
        # Explore neighbours
        for neigh, w in graph[node]:
            
            # Push neighbour into priority queue with updated cost
            heapq.heappush(pq, (cost + w, neigh, path))
    
    # If goal not reachable
    return None, None


# -------- INPUT SECTION --------

# Number of vertices
n = int(input("Vertices: "))

# Number of edges
m = int(input("Edges: "))

# Create adjacency list for weighted graph
graph = {i: [] for i in range(n)}

# Input edges with weight
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Undirected graph

# Input source and destination
s = int(input("Source: "))
d = int(input("Destination: "))

# Call UCS function
cost, path = ucs(graph, s, d)

# Print result
print("Cost:", cost, "Path:", path if path else "No Path")

# Vertices: 5
# Edges: 6
# 0 1 2
# 0 2 4
# 1 3 7
# 2 3 1
# 3 4 3
# 2 4 5
# Source: 0
# Destination: 4