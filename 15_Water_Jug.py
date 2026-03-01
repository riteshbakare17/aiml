from collections import deque   # used for BFS queue


# Function to solve Water Jug problem
def water_jug(a, b, target):
    
    # visited set to avoid revisiting same states
    visited = set()
    
    # Queue for BFS → start from (0,0) both jugs empty
    q = deque([(0, 0)])
    
    # BFS loop
    while q:
        x, y = q.popleft()   # current state
        
        # If target achieved in any jug → success
        if x == target or y == target:
            print("Reached:", (x, y))
            return
        
        # Skip if already visited
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        # Generate all possible next states
        q.extend([
            (a, y),   # Fill Jug1 completely
            (x, b),   # Fill Jug2 completely
            (0, y),   # Empty Jug1
            (x, 0),   # Empty Jug2
            
            # Pour Jug1 → Jug2
            (x - min(x, b - y), y + min(x, b - y)),
            
            # Pour Jug2 → Jug1
            (x + min(y, a - x), y - min(y, a - x))
        ])
    
    # If BFS ends → no solution
    print("No Solution")


# -------- INPUT --------
a = int(input("Jug1: "))
b = int(input("Jug2: "))
t = int(input("Target: "))

# Run BFS solver
water_jug(a, b, t)

# Jug1: 4
# Jug2: 3
# Target: 2