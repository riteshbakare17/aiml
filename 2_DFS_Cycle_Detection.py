# DFS function to detect cycle in an undirected graph
def dfs(graph, node, visited, parent):
    
    # Mark current node as visited
    visited.add(node)
    
    # Visit all neighbours of current node
    for neigh in graph[node]:
        
        # If neighbour not visited → continue DFS
        if neigh not in visited:
            # If cycle found deeper in recursion → return True
            if dfs(graph, neigh, visited, node):
                return True
        
        # If neighbour already visited AND not parent → cycle found
        elif parent != neigh:
            return True
    
    # No cycle found from this node
    return False


# -------- INPUT SECTION --------

# Number of vertices
n = int(input("Vertices: "))

# Number of edges
m = int(input("Edges: "))

# Create adjacency list
graph = {i: [] for i in range(n)}

# Input edges (undirected graph)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Set to track visited nodes
visited = set()

# Variable to store result
cycle = False

# Run DFS for each component (important for disconnected graph)
for i in range(n):
    if i not in visited:
        if dfs(graph, i, visited, -1):
            cycle = True

# Print result
print("Cycle Detected" if cycle else "No Cycle")


# Vertices: 4
# Edges: 4
# 0 1
# 1 2
# 2 3
# 3 0

# Vertices: 4
# Edges: 3
# 0 1
# 1 2
# 2 3