from algorithms.dfs import dfs
from algorithms.astar import astar

# Dummy Node class
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

# Dummy Grid class
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
    print("Start = (0, 0), End = (4, 4), # = Obstacle, D = Delayed, * = Path, v = Visited")

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
                label = "D"
            else:
                label = "."

            row_str += f"({r},{c}){label}  "
        print(row_str)
    print()

# Build test grid
grid = Grid(5, 5)

# Add obstacles (vertical wall)
grid.set_obstacle(1, 2)
grid.set_obstacle(2, 2)
grid.set_obstacle(3, 2)

start = grid.get_node(0, 0)
end = grid.get_node(4, 4)

# Add a delay node
grid.get_node(2, 3).delay = 5

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