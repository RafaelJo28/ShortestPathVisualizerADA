import pygame
import random
from visualization.ui.button import Button
from visualization.ui.grid_renderer import GridRenderer
from visualization.ui.animator import Animator
from visualization.grid_loader import GridLoader, GridDefaults
from visualization.pathfinding import get_algorithm_function


class Visualizer:
    """Main visualizer page for displaying pathfinding algorithms."""
    
    def __init__(self, window, selected_grid, algorithm):
        self.window = window
        self.selected_grid = selected_grid
        self.algorithm = algorithm
        self.buttons = []
        
        # Grid and visualization data
        self.grid = None
        self.start_node = None
        self.end_node = None
        self.waypoints = []
        self.visited_nodes = []
        self.path_nodes = []
        
        # Rendering and animation
        self.renderer = GridRenderer(grid_offset_x=200, grid_offset_y=80, cell_size=25)
        self.animator = None
        self.is_running = False
        
        # Initialize
        self._create_layout()
        self._load_grid()
        self._generate_algorithm_data()
    
    def _create_layout(self):
        """Create UI buttons for visualization control."""
        # Control buttons on the left
        self.buttons.append(Button(10, 40, 90, 40, "Start", self.start_animation))
        self.buttons.append(Button(10, 90, 90, 40, "Pause", self.pause_animation))
        self.buttons.append(Button(10, 140, 90, 40, "Reset", self.reset_animation))
        self.buttons.append(Button(10, 190, 90, 40, "Skip", self.skip_animation))
        self.buttons.append(Button(10, 240, 90, 40, "Speed+", self.increase_speed))
        self.buttons.append(Button(10, 290, 90, 40, "Speed-", self.decrease_speed))
        self.buttons.append(Button(10, 340, 90, 40, "Back", self.go_back))
    
    def _load_grid(self):
        """Load the selected grid type."""
        self.grid = GridLoader.create_grid(self.selected_grid)
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        # Set start and end positions
        self.start_node = GridDefaults.get_start_position(rows, cols)
        self.end_node = GridDefaults.get_end_position(rows, cols)
        self.waypoints = GridDefaults.get_waypoints(rows, cols)
        
        # Ensure start and end are not obstacles
        start_r, start_c = self.start_node
        end_r, end_c = self.end_node
        self.grid[start_r][start_c].is_obstacle = False
        self.grid[end_r][end_c].is_obstacle = False
    
    def _generate_algorithm_data(self):
        """Generate visited and path nodes using the selected algorithm."""
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        # Get the algorithm function
        algorithm_func = get_algorithm_function(self.algorithm)
        
        # Run the algorithm to get visited nodes and path
        self.visited_nodes, self.path_nodes = algorithm_func(
            self.grid,
            self.start_node,
            self.end_node
        )
        
        # Initialize animator with the data
        self.animator = Animator(
            visited_nodes=self.visited_nodes,
            path_nodes=self.path_nodes,
            animation_speed=0.05
        )
    
    def start_animation(self):
        """Start the animation."""
        if self.animator:
            self.animator.resume()
            self.is_running = True
    
    def pause_animation(self):
        """Pause the animation."""
        if self.animator:
            self.animator.pause()
            self.is_running = False
    
    def reset_animation(self):
        """Reset the animation."""
        if self.animator:
            self.animator.reset()
            self.is_running = False
    
    def skip_animation(self):
        """Skip to the end of animation."""
        if self.animator:
            self.animator.skip_to_end()
            self.is_running = False
    
    def increase_speed(self):
        """Increase animation speed."""
        if self.animator:
            self.animator.set_speed(self.animator.animation_speed * 0.8)
    
    def decrease_speed(self):
        """Decrease animation speed."""
        if self.animator:
            self.animator.set_speed(self.animator.animation_speed * 1.2)
    
    def go_back(self):
        """Return to main menu."""
        from visualization.pages.main_menu import MainMenu
        self.window.change_page(MainMenu)
    
    def handle_events(self, events):
        """Handle user input."""
        mouse_pos = pygame.mouse.get_pos()
        
        for event in events:
            for button in self.buttons:
                button.update(mouse_pos)
                button.handle_event(event)
    
    def update(self, dt):
        """Update animation state."""
        if self.animator:
            self.animator.update(dt)
    
    def draw(self, screen):
        """Draw the visualization."""
        # Draw background
        self.renderer.draw_background(screen)
        
        # Draw grid base
        self.renderer.draw_grid(screen, self.grid)
        
        # Draw obstacles
        self.renderer.draw_obstacles(screen, self.grid)
        
        # Draw visited nodes
        if self.animator:
            visited = self.animator.get_current_visited()
            self.renderer.draw_visited_nodes(screen, visited)
        
        # Draw path
        if self.animator:
            path = self.animator.get_current_path()
            self.renderer.draw_path(screen, path)
        
        # Draw special nodes
        self.renderer.draw_start_node(screen, self.start_node)
        self.renderer.draw_end_node(screen, self.end_node)
        self.renderer.draw_waypoints(screen, self.waypoints)
        
        # Draw grid border
        self.renderer.draw_grid_border(screen, self.grid)
        
        # Draw title
        title = f"{self.algorithm} on {self.selected_grid}"
        self.renderer.draw_title(screen, self.window.width, title)
        
        # Draw statistics
        stats = {
            "Visited": len(self.visited_nodes),
            "Path": len(self.path_nodes),
        }
        if self.animator:
            stats["Progress"] = f"{self.animator.get_progress()}%"
            stats["Status"] = "Finished" if self.animator.is_finished else ("Paused" if self.animator.is_paused else "Running")

        # Add algorithm complexity info
        complexities = {
            "BFS": ("O(V+E)", "O(V)"),
            "Dijkstra": ("O((V+E) log V)", "O(V)"),
            "A*": ("O(E) worst-case, typically faster", "O(V)"),
            "DFS": ("O(V+E)", "O(V)"),
        }

        time_c, space_c = complexities.get(self.algorithm, ("O(V+E)", "O(V)"))
        stats["Time Complexity"] = time_c
        stats["Space Complexity"] = space_c

        # Draw stats below the grid instead of on the left
        self.renderer.draw_stats_bottom(screen, stats, self.window.width, self.window.height, self.grid)
        
        # Draw buttons
        for button in self.buttons:
            button.draw(screen)