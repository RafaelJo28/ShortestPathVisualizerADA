"""Grid loader utility for loading different grid types."""
import random


class Node:
    """Grid node class."""
    def __init__(self, row, col, is_obstacle=False, cost=1):
        self.row = row
        self.col = col
        self.is_obstacle = is_obstacle
        self.cost = cost
    
    def __repr__(self):
        return f"({self.row},{self.col})"
    
    def __hash__(self):
        return hash((self.row, self.col))
    
    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)


class GridLoader:
    """Loads different types of grids."""
    
    GRID_DIMENSIONS = {
        "Empty Grid": (30, 20),
        "Random Obstacles": (30, 20),
        "Maze Grid": (30, 20),
        "Weighted Grid": (30, 20),
    }
    
    @staticmethod
    def create_grid(grid_type, rows=None, cols=None, seed=None):
        """
        Create a grid based on type.
        
        Args:
            grid_type: Type of grid to create
            rows: Number of rows (if None, uses default)
            cols: Number of columns (if None, uses default)
        
        Returns:
            2D list of Node objects
        """
        if rows is None or cols is None:
            cols, rows = GridLoader.GRID_DIMENSIONS.get(grid_type, (30, 20))

        # If a seed is provided, temporarily seed the global RNG
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
            else:
                return GridLoader._create_empty_grid(rows, cols)
        finally:
            if state is not None:
                random.setstate(state)
    
    @staticmethod
    def _create_empty_grid(rows, cols):
        """Create an empty grid."""
        return [[Node(r, c) for c in range(cols)] for r in range(rows)]
    
    @staticmethod
    def _create_random_obstacles_grid(rows, cols):
        """Create a grid with random obstacles."""
        grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]
        
        # Add random obstacles (30% of cells)
        for r in range(rows):
            for c in range(cols):
                if random.random() < 0.3:
                    grid[r][c].is_obstacle = True
        
        return grid
    
    @staticmethod
    def _create_maze_grid(rows, cols):
        """Create a maze-like grid using recursive backtracking."""
        grid = [[Node(r, c, is_obstacle=True) for c in range(cols)] for r in range(rows)]
        
        # Simple maze generation: create paths
        def carve_path(r, c):
            grid[r][c].is_obstacle = False
            
            # Randomize directions
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc].is_obstacle:
                    # Carve wall between cells
                    grid[r + dr // 2][c + dc // 2].is_obstacle = False
                    carve_path(nr, nc)
        
        carve_path(0, 0)
        return grid
    
    @staticmethod
    def _create_weighted_grid(rows, cols):
        """Create a grid with weighted cells."""
        grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]
        
        # Add some obstacles and varied costs
        for r in range(rows):
            for c in range(cols):
                if random.random() < 0.15:
                    grid[r][c].is_obstacle = True
                elif random.random() < 0.3:
                    grid[r][c].cost = random.randint(2, 5)
        
        return grid


class GridDefaults:
    """Default grid configurations."""
    
    @staticmethod
    def get_start_position(rows, cols):
        """Get default start position."""
        return (1, 1)
    
    @staticmethod
    def get_end_position(rows, cols):
        """Get default end position."""
        return (rows - 2, cols - 2)
    
    @staticmethod
    def get_waypoints(rows, cols):
        """Get default waypoints (empty by default)."""
        return []
