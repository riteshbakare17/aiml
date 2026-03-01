# Depth Limited Search (same function used inside IDS)
def dls(graph, node, goal, limit):
    
    # If goal found → return True
    if node == goal:
        return True
    
    # If depth limit reached → stop searching
    if limit <= 0:
        return False
    
    # Explore neighbours with reduced depth
    for neigh in graph[node]:
        if dls(graph, neigh, goal, limit - 1):
            return True
    
    # Goal not found at this depth
    return False


# -------- INPUT SECTION --------

# Number of vertices
n = int(input("Vertices: "))

# Number of edges
m = int(input("Edges: "))

# Create adjacency list
graph = {i: [] for i in range(n)}

# Input directed edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# Input start node, goal node and max depth to search
s = int(input("Start: "))
g = int(input("Goal: "))
max_depth = int(input("Max Depth: "))

# Iterative Deepening Loop
# Run DLS from depth = 0 to max_depth
for depth in range(max_depth + 1):
    
    # Call DLS with current depth limit
    if dls(graph, s, g, depth):
        print("Found at depth", depth)
        break

# If goal never found up to max_depth
else:
    print("Not Found")

# Vertices: 6
# Edges: 6
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 0 2
# Start: 0
# Goal: 5
# Max Depth: 5
    