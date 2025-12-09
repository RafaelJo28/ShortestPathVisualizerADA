import pygame


class Animator:
    """Handles animation of algorithm visualization."""
    
    def __init__(self, visited_nodes=None, path_nodes=None, animation_speed=0.05):
        """
        Initialize animator.
        
        Args:
            visited_nodes: List of visited nodes to animate through
            path_nodes: List of path nodes to animate
            animation_speed: Delay between frames (in seconds)
        """
        self.visited_nodes = visited_nodes or []
        self.path_nodes = path_nodes or []
        self.animation_speed = animation_speed
        
        self.current_visited_index = 0
        self.current_path_index = 0
        self.time_accumulator = 0.0
        self.is_paused = False
        self.is_finished = False
    
    def update(self, dt):
        """Update animation state."""
        if self.is_paused or self.is_finished:
            return
        
        self.time_accumulator += dt
        
        if self.time_accumulator >= self.animation_speed:
            self.time_accumulator = 0.0
            
            # Animate visited nodes first
            if self.current_visited_index < len(self.visited_nodes):
                self.current_visited_index += 1
            else:
                # Then animate path
                if self.current_path_index < len(self.path_nodes):
                    self.current_path_index += 1
                else:
                    self.is_finished = True
    
    def get_current_visited(self):
        """Get nodes to display as visited up to current frame."""
        return self.visited_nodes[:self.current_visited_index]
    
    def get_current_path(self):
        """Get path nodes to display up to current frame."""
        return self.path_nodes[:self.current_path_index]
    
    def pause(self):
        """Pause animation."""
        self.is_paused = True
    
    def resume(self):
        """Resume animation."""
        self.is_paused = False
    
    def reset(self):
        """Reset animation to beginning."""
        self.current_visited_index = 0
        self.current_path_index = 0
        self.time_accumulator = 0.0
        self.is_paused = False
        self.is_finished = False
    
    def skip_to_end(self):
        """Skip animation to the end."""
        self.current_visited_index = len(self.visited_nodes)
        self.current_path_index = len(self.path_nodes)
        self.is_finished = True
    
    def set_speed(self, speed):
        """Set animation speed (0.01 = fast, 0.1 = slow)."""
        self.animation_speed = max(0.001, min(0.2, speed))
    
    def get_progress(self):
        """Get animation progress as percentage (0-100)."""
        total_frames = len(self.visited_nodes) + len(self.path_nodes)
        if total_frames == 0:
            return 100
        current_frame = self.current_visited_index + self.current_path_index
        return int((current_frame / total_frames) * 100)
