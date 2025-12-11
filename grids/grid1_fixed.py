from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.dijkstra import dijkstra
import random

# Node class
class Node:
    def __init__(self, row, col, is_obstacle=False, cost=1, delay=0):
        self.row = row
        self.col = col
        self.is_obstacle = is_obstacle
        self.cost = cost
        self.delay = delay

    def __repr__(self):
        return f"({self.row},{self.col})"

    # Needed for sets & dict keys
    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

# Grid class
class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        # Create 2D array of nodes
        self.grid = [
            [Node(r, c) for c in range(cols)]
            for r in range(rows)
        ]

    def get_node(self, row, col):
        return self.grid[row][col]

    def set_obstacle(self, row, col):
        self.grid[row][col].is_obstacle = True

    def get_neighbors(self, node):
        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        neighbors = []
        for dr, dc in directions:
            r = node.row + dr
            c = node.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbors.append(self.grid[r][c])

        return neighbors

# Print Grid
def print_grid(grid, start, end, path=None, visited=None):
    print("\nGrid Layout:")
    print("Start = (0, 0), End = (50, 50), # = Obstacle, D = Delayed, * = Path, v = Visited")

    for r in range(grid.rows):
        row_str = ""
        for c in range(grid.cols):
            node = grid.get_node(r, c)

            label = ""

            if path and node in path:
                label = "*"
            elif visited and visited is not None and node in visited:
                label = "v"
            elif node == start:
                label = "S"
            elif node == end:
                label = "E"
            elif node.is_obstacle:
                label = "#"
            elif node.delay > 0:
                label = "D:{node.delay}"
            else:
                label = "."

            row_str += f"({r},{c}){label}  "
        print(row_str)
    print()

# Build grid
grid = Grid(40, 40)

# Add obstacles
# Vertical walls
for r in range(5, 30):
    grid.set_obstacle(r, 5)

for r in range(0, 25):
    grid.set_obstacle(r, 10)

for r in range(10, 35):
    grid.set_obstacle(r, 20)

# Horizontal walls
for c in range(3, 30):
    grid.set_obstacle(8, c)

for c in range(12, 35):
    grid.set_obstacle(15, c)

for c in range(5, 20):
    grid.set_obstacle(25, c)

# Box obstacles
for r in range(30, 35):
    for c in range(30, 35):
        grid.set_obstacle(r, c)

# Another box
for r in range(18, 22):
    for c in range(2, 7):
        grid.set_obstacle(r, c)

# Diagonal-style blockers (zig-zag)
for i in range(8, 20):
    grid.set_obstacle(i, i)

for i in range(22, 35):
    grid.set_obstacle(i, 39 - i)

start = grid.get_node(0, 0)
end = grid.get_node(39, 39)

# Make sure the start and end remain open
start.is_obstacle = False
end.is_obstacle = False

# Add delay nodes to all nodes
for r in range(40):
    for c in range(40):
        node = grid.get_node(r, c)
        if node != start and node != end:
            node.delay = (r + c) % 8

# Print initial grid
print_grid(grid, start, end)

# Run DFS
print("=== DFS ===")
visited_dfs, path_dfs = dfs(grid, start, end)
print("Visited:", visited_dfs)
print("Path:", path_dfs)

print("\nDFS Path Visualization:")
print_grid(grid, start, end, path=path_dfs, visited=visited_dfs)

# Run A*
print("\n=== A* ===")
visited_astar, path_astar = astar(grid, start, end)
print("Visited:", visited_astar)
print("Path:", path_astar)

print("\nA* Path Visualization:")
print_grid(grid, start, end, path=path_astar, visited=visited_astar)

# Run BFS
print("=== BFS ===")
visited_bfs, path_bfs = bfs(grid, start, end)
print("Visited:", visited_bfs)
print("Path:", path_bfs)

print("\nBFS Path Visualization:")
print_grid(grid, start, end, path=path_bfs, visited=visited_bfs)

# Run Dijkstra
print("\n=== Dijkstra ===")
visited_dijkstra, path_dijkstra = dijkstra(grid, start, end)
print("Visited:", visited_dijkstra)
print("Path:", path_dijkstra)

print("\nDijkstra Path Visualization:")
print_grid(grid, start, end, path=path_dijkstra, visited=visited_dijkstra)