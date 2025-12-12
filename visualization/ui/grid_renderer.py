import pygame


class GridRenderer:
    """Handles rendering of grid cells with different states."""
    
    # Color definitions
    COLORS = {
        'background': (20, 20, 20),
        'grid_line': (50, 50, 50),
        'empty': (240, 240, 240),
        'obstacle': (30, 30, 30),
        'visited': (52, 152, 219),      # Blue
        'path': (46, 204, 113),          # Green
        'start': (155, 89, 182),         # Purple
        'end': (230, 126, 34),           # Orange
        'waypoint': (241, 196, 15),      # Yellow
        'grid_border': (100, 100, 100),
    }
    
    def __init__(self, grid_offset_x=200, grid_offset_y=80, cell_size=25):
        """
        Initialize the grid renderer.
        
        Args:
            grid_offset_x: X coordinate offset for grid rendering
            grid_offset_y: Y coordinate offset for grid rendering
            cell_size: Size of each cell in pixels
        """
        self.grid_offset_x = grid_offset_x
        self.grid_offset_y = grid_offset_y
        self.cell_size = cell_size
    
    def draw_background(self, screen):
        """Draw the background."""
        screen.fill(self.COLORS['background'])
    
    def draw_grid(self, screen, grid):
        """Draw grid lines and empty cells."""
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        for r in range(rows):
            for c in range(cols):
                x = self.grid_offset_x + c * self.cell_size
                y = self.grid_offset_y + r * self.cell_size
                
                # Draw cell background
                pygame.draw.rect(
                    screen,
                    self.COLORS['empty'],
                    (x, y, self.cell_size, self.cell_size)
                )
                
                # Draw cell border
                pygame.draw.rect(
                    screen,
                    self.COLORS['grid_line'],
                    (x, y, self.cell_size, self.cell_size),
                    1
                )
    
    def draw_obstacles(self, screen, grid):
        """Draw obstacles on the grid."""
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        for r in range(rows):
            for c in range(cols):
                node = grid[r][c]
                if hasattr(node, 'is_obstacle') and node.is_obstacle:
                    x = self.grid_offset_x + c * self.cell_size
                    y = self.grid_offset_y + r * self.cell_size
                    pygame.draw.rect(
                        screen,
                        self.COLORS['obstacle'],
                        (x, y, self.cell_size, self.cell_size)
                    )
                    # Draw border
                    pygame.draw.rect(
                        screen,
                        self.COLORS['grid_line'],
                        (x, y, self.cell_size, self.cell_size),
                        1
                    )
    
    def draw_visited_nodes(self, screen, visited_nodes):
        """Draw visited nodes."""
        for (row, col) in visited_nodes:
            x = self.grid_offset_x + col * self.cell_size
            y = self.grid_offset_y + row * self.cell_size
            pygame.draw.rect(
                screen,
                self.COLORS['visited'],
                (x, y, self.cell_size, self.cell_size)
            )
            pygame.draw.rect(
                screen,
                self.COLORS['grid_line'],
                (x, y, self.cell_size, self.cell_size),
                1
            )
    
    def draw_path(self, screen, path_nodes):
        """Draw the final path."""
        for (row, col) in path_nodes:
            x = self.grid_offset_x + col * self.cell_size
            y = self.grid_offset_y + row * self.cell_size
            pygame.draw.rect(
                screen,
                self.COLORS['path'],
                (x, y, self.cell_size, self.cell_size)
            )
            pygame.draw.rect(
                screen,
                self.COLORS['grid_line'],
                (x, y, self.cell_size, self.cell_size),
                1
            )
    
    def draw_start_node(self, screen, start_node):
        """Draw the start node."""
        if start_node:
            row, col = start_node if isinstance(start_node, tuple) else (start_node.row, start_node.col)
            x = self.grid_offset_x + col * self.cell_size
            y = self.grid_offset_y + row * self.cell_size
            pygame.draw.rect(
                screen,
                self.COLORS['start'],
                (x, y, self.cell_size, self.cell_size)
            )
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x, y, self.cell_size, self.cell_size),
                3
            )
    
    def draw_end_node(self, screen, end_node):
        """Draw the end node."""
        if end_node:
            row, col = end_node if isinstance(end_node, tuple) else (end_node.row, end_node.col)
            x = self.grid_offset_x + col * self.cell_size
            y = self.grid_offset_y + row * self.cell_size
            pygame.draw.rect(
                screen,
                self.COLORS['end'],
                (x, y, self.cell_size, self.cell_size)
            )
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x, y, self.cell_size, self.cell_size),
                3
            )
    
    def draw_waypoints(self, screen, waypoints):
        """Draw waypoints."""
        for waypoint in waypoints:
            row, col = waypoint if isinstance(waypoint, tuple) else (waypoint.row, waypoint.col)
            x = self.grid_offset_x + col * self.cell_size
            y = self.grid_offset_y + row * self.cell_size
            pygame.draw.rect(
                screen,
                self.COLORS['waypoint'],
                (x, y, self.cell_size, self.cell_size)
            )
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x, y, self.cell_size, self.cell_size),
                2
            )
    
    def draw_title(self, screen, window_width, title_text):
        """Draw title text."""
        font = pygame.font.SysFont("arial", 32, bold=True)
        title_surf = font.render(title_text, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(window_width // 2, 20))
        screen.blit(title_surf, title_rect)
    
    def draw_grid_border(self, screen, grid):
        """Draw border around the entire grid."""
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        x1 = self.grid_offset_x
        y1 = self.grid_offset_y
        x2 = self.grid_offset_x + cols * self.cell_size
        y2 = self.grid_offset_y + rows * self.cell_size
        
        pygame.draw.rect(
            screen,
            self.COLORS['grid_border'],
            (x1, y1, cols * self.cell_size, rows * self.cell_size),
            3
        )
    
    def draw_stats(self, screen, stats_dict):
        """Draw statistics on screen."""
        font = pygame.font.SysFont("arial", 14)
        y_offset = 10
        
        for key, value in stats_dict.items():
            text_surf = font.render(f"{key}: {value}", True, (200, 200, 200))
            screen.blit(text_surf, (10, y_offset))
            y_offset += 25

    def draw_stats_bottom(self, screen, stats_dict, window_width, window_height, grid):
        """Draw statistics centered below the grid area.

        Args:
            screen: pygame surface
            stats_dict: dict of stats to draw
            window_width: width of the window
            window_height: height of the window
            grid: the grid (2D list) used to compute bottom position
        """
        font = pygame.font.SysFont("arial", 14)

        # Compute grid area
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        grid_x = self.grid_offset_x
        grid_y = self.grid_offset_y
        grid_w = cols * self.cell_size
        grid_h = rows * self.cell_size

        # Start drawing a little below the grid
        start_y = grid_y + grid_h + 10

        # Draw each stat centered under the grid
        y_offset = start_y
        for key, value in stats_dict.items():
            text = f"{key}: {value}"
            text_surf = font.render(text, True, (200, 200, 200))
            text_x = grid_x + (grid_w // 2) - (text_surf.get_width() // 2)
            screen.blit(text_surf, (text_x, y_offset))
            y_offset += 20
