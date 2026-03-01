import random   # used to generate random paths and swaps


# Function to calculate total distance of a path
def cost(path, dist):
    
    # Sum distance between consecutive cities in the path
    return sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))


# -------- INPUT --------

# Number of cities
n = int(input("Cities: "))

# Distance matrix (n x n)
# dist[i][j] = distance from city i → city j
dist = [list(map(int, input().split())) for _ in range(n)]

# Create initial path [0,1,2,...,n-1]
path = list(range(n))

# Shuffle to create random starting solution
random.shuffle(path)

# Calculate cost of initial path
best = cost(path, dist)


# Hill Climbing loop (1000 iterations)
for _ in range(1000):
    
    # Pick two random cities to swap
    i, j = random.sample(range(n), 2)
    
    # Create neighbour solution by swapping cities
    new = path.copy()
    new[i], new[j] = new[j], new[i]
    
    # Calculate new path cost
    c = cost(new, dist)
    
    # If new path is better → move to it (hill climbing step)
    if c < best:
        path, best = new, c


# Print best path found
print("Best Path:", path, "Cost:", best)\
    
# Cities: 4
# 0 10 15 20
# 10 0 35 25
# 15 35 0 30
# 20 25 30 0