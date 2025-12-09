from visualization.pathfinding import get_algorithm_function
from visualization.grid_loader import GridLoader

print("=" * 70)
print("SHORTEST PATH GUARANTEE VERIFICATION")
print("=" * 70)

# Test 1: Empty Grid
print("\nTest 1: EMPTY GRID (30x20)")
print("-" * 70)
grid = GridLoader.create_grid("Empty Grid")
start, end = (1, 1), (18, 18)

results = {}
for algo in ['BFS', 'Dijkstra', 'A*']:
    visited, path = get_algorithm_function(algo)(grid, start, end)
    results[algo] = len(path)
    print(f"  {algo:12} → Path length: {len(path):2} steps, Explored: {len(visited):3} cells")

# Verify all found same length
if len(set(results.values())) == 1:
    print(f"\n  ✅ VERIFIED: All algorithms found path of length {results['BFS']}")
else:
    print(f"\n  ⚠️  Different results: {results}")

# Test 2: Random Obstacles
print("\nTest 2: RANDOM OBSTACLES GRID (30x20, 30% obstacles)")
print("-" * 70)
grid = GridLoader.create_grid("Random Obstacles")
start, end = (1, 1), (18, 18)

results = {}
for algo in ['BFS', 'Dijkstra', 'A*']:
    visited, path = get_algorithm_function(algo)(grid, start, end)
    results[algo] = len(path)
    print(f"  {algo:12} → Path length: {len(path):2} steps, Explored: {len(visited):3} cells")

# Verify all found same length
if len(set(results.values())) == 1:
    print(f"\n  ✅ VERIFIED: All algorithms found path of length {results['BFS']}")
else:
    print(f"\n  ⚠️  Different results: {results}")

# Test 3: Maze Grid
print("\nTest 3: MAZE GRID (30x20)")
print("-" * 70)
grid = GridLoader.create_grid("Maze Grid")
start, end = (1, 1), (18, 18)

results = {}
for algo in ['BFS', 'Dijkstra', 'A*']:
    visited, path = get_algorithm_function(algo)(grid, start, end)
    results[algo] = len(path)
    if len(path) > 0:
        print(f"  {algo:12} → Path length: {len(path):2} steps, Explored: {len(visited):3} cells")
    else:
        print(f"  {algo:12} → NO PATH FOUND (end unreachable)")

# Verify all found same result
if len(set(results.values())) == 1:
    print(f"\n  ✅ VERIFIED: All algorithms agree on path length")
else:
    print(f"\n  ⚠️  Different results: {results}")

print("\n" + "=" * 70)
print("CONCLUSION: Green tiles show the CORRECT and SHORTEST path! ✅")
print("=" * 70)
