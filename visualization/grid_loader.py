import random


class Node:
    def __init__(self, row, col, is_obstacle=False, cost=1, terrain="normal"):
        self.row = row
        self.col = col
        self.is_obstacle = is_obstacle
        self.cost = cost
        self.terrain = terrain  # normal, sand, water, road

    def __repr__(self):
        return f"({self.row},{self.col})"

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)


class GridLoader:

    GRID_DIMENSIONS = {
        "Empty Grid": (30, 20),
        "Random Obstacles": (30, 20),
        "Maze Grid": (30, 20),
        "Weighted Grid": (30, 20),
        "Terrain Grid": (30, 20),
    }

    @staticmethod
    def create_grid(grid_type, rows=None, cols=None, seed=None):
        if rows is None or cols is None:
            cols, rows = GridLoader.GRID_DIMENSIONS.get(grid_type, (30, 20))

        state = None
        if seed is not None:
            state = random.getstate()
            random.seed(seed)

        try:
            if grid_type == "Empty Grid":
                return GridLoader._create_empty_grid(rows, cols)
            elif grid_type == "Random Obstacles":
                return GridLoader._create_random_obstacles_grid(rows, cols)
            elif grid_type == "Maze Grid":
                return GridLoader._create_maze_grid(rows, cols)
            elif grid_type == "Weighted Grid":
                return GridLoader._create_weighted_grid(rows, cols)
            elif grid_type == "Terrain Grid":
                return GridLoader._create_terrain_grid(rows, cols)
            else:
                return GridLoader._create_empty_grid(rows, cols)
        finally:
            if state is not None:
                random.setstate(state)

    # --------------------------------------------------
    # BASIC GRIDS
    # --------------------------------------------------

    @staticmethod
    def _create_empty_grid(rows, cols):
        return [[Node(r, c) for c in range(cols)] for r in range(rows)]

    @staticmethod
    def _create_random_obstacles_grid(rows, cols):
        grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if random.random() < 0.3:
                    grid[r][c].is_obstacle = True

        return grid

    @staticmethod
    def _create_maze_grid(rows, cols):
        grid = [[Node(r, c, is_obstacle=True) for c in range(cols)] for r in range(rows)]

        def carve_path(r, c):
            grid[r][c].is_obstacle = False
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc].is_obstacle:
                    grid[r + dr // 2][c + dc // 2].is_obstacle = False
                    carve_path(nr, nc)

        carve_path(0, 0)
        return grid

    # --------------------------------------------------
    # WEIGHTED / TERRAIN GRIDS
    # --------------------------------------------------

    @staticmethod
    def _create_weighted_grid(rows, cols):
        grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                roll = random.random()

                if roll < 0.15:
                    grid[r][c].is_obstacle = True
                elif roll < 0.45:
                    grid[r][c].cost = random.randint(2, 5)

        return grid

    @staticmethod
    def _create_terrain_grid(rows, cols):
        """
        FULLY DETERMINISTIC TERRAIN GRID
        - No randomness
        - Same layout every run
        """

        grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):

                # Solid border walls
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    grid[r][c].is_obstacle = True
                    continue

                # Deterministic pattern based on position
                value = (r * 7 + c * 11) % 10

                if value < 2:
                    grid[r][c].is_obstacle = True

                elif value < 4:
                    grid[r][c].terrain = "water"
                    grid[r][c].cost = 5

                elif value < 6:
                    grid[r][c].terrain = "sand"
                    grid[r][c].cost = 3

                else:
                    grid[r][c].terrain = "road"
                    grid[r][c].cost = 1

        return grid


# --------------------------------------------------
# GRID UTILITIES
# --------------------------------------------------

class GridUtils:

    @staticmethod
    def in_bounds(grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    @staticmethod
    def get_neighbors(grid, node):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = node.row + dr, node.col + dc
            if GridUtils.in_bounds(grid, nr, nc):
                if not grid[nr][nc].is_obstacle:
                    neighbors.append(grid[nr][nc])

        return neighbors

    @staticmethod
    def grid_statistics(grid):
        total = len(grid) * len(grid[0])
        obstacles = sum(n.is_obstacle for row in grid for n in row)
        weighted = sum(n.cost > 1 for row in grid for n in row)

        return {
            "total_cells": total,
            "obstacles": obstacles,
            "weighted_cells": weighted
        }


class GridDefaults:

    @staticmethod
    def get_start_position(rows, cols):
        return (1, 1)

    @staticmethod
    def get_end_position(rows, cols):
        return (rows - 2, cols - 2)

    @staticmethod
    def get_waypoints(rows, cols):
        return []
