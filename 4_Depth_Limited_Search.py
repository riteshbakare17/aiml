# Depth Limited Search function
def dls(graph, node, goal, limit):
    
    # If current node is goal → success
    if node == goal:
        return True
    
    # If depth limit reached → stop searching
    if limit <= 0:
        return False
    
    # Explore neighbours with reduced depth
    for neigh in graph[node]:
        if dls(graph, neigh, goal, limit - 1):
            return True
    
    # Goal not found within depth limit
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

# Input start, goal and depth limit
s = int(input("Start: "))
g = int(input("Goal: "))
limit = int(input("Depth Limit: "))

# Run DLS
print("Found" if dls(graph, s, g, limit) else "Not Found")

# Vertices: 5
# Edges: 5
# 0 1
# 1 2
# 2 3
# 3 4
# 0 2
# Start: 0
# Goal: 4
# Depth Limit: 3