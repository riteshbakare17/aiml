# heapq is used to implement priority queue (min heap)
import heapq

# A* Search Function
def astar(graph, heuristic, start, goal):
    
    # Priority queue stores:
    # (f = g + h, g = path cost so far, current node, path)
    pq = [(heuristic[start], 0, start, [])]
    
    # To keep track of visited nodes
    visited = set()
    
    # Loop until queue becomes empty
    while pq:
        
        # Pop node with smallest f(n)
        f, g, node, path = heapq.heappop(pq)
        
        # Skip if already visited
        if node in visited:
            continue
        
        visited.add(node)
        
        # Add node to path
        path = path + [node]
        
        # If goal reached → return cost and path
        if node == goal:
            return g, path
        
        # Explore neighbours
        for neigh, w in graph[node]:
            
            # g = current cost + edge weight
            # f = g + heuristic(neighbour)
            heapq.heappush(
                pq,
                (g + w + heuristic[neigh],  # f(n)
                 g + w,                     # g(n)
                 neigh,
                 path)
            )
    
    # If path not found
    return None, None


# -------- INPUT SECTION --------

n = int(input("Vertices: "))
m = int(input("Edges: "))

# Create weighted graph
graph = {i: [] for i in range(n)}

# Input edges with weights
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Undirected graph

# Input heuristic values
heuristic = {}
print("Enter heuristic values:")
for i in range(n):
    heuristic[i] = int(input(f"h({i}): "))

# Start and Goal
s = int(input("Start: "))
g = int(input("Goal: "))

# Run A*
cost, path = astar(graph, heuristic, s, g)

print("Cost:", cost, "Path:", path if path else "No Path")

# Vertices: 5
# Edges: 6
# 0 1 2
# 0 2 4
# 1 3 5
# 2 3 1
# 3 4 3
# 2 4 7
# Enter heuristic values:
# h(0): 7
# h(1): 6
# h(2): 2
# h(3): 1
# h(4): 0
# Start: 0
# Goal: 4