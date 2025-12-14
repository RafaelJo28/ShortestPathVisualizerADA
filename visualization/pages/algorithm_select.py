import pygame
from visualization.ui.button import Button
from visualization.pages.visualizer import Visualizer

class AlgorithmSelect:
    def __init__(self, window, selected_grid=None, grid_mode='random', seed=None):
        self.window = window
        self.selected_grid = selected_grid
        self.grid_mode = grid_mode
        self.seed = seed  # Store the seed
        self.buttons = []
        self._create_layout()
        
        # Debug: Check what we received
        print(f"DEBUG AlgorithmSelect: grid={selected_grid}, mode={grid_mode}, seed={seed}")

    def _create_layout(self):
        center_x = self.window.width // 2
        start_y = 220
        spacing = 70

        algorithms = ["BFS", "Dijkstra", "A*", "DFS"]

        for i, algo in enumerate(algorithms):
            self.buttons.append(Button(center_x - 120, start_y + i * spacing, 240, 50, algo,
                                       lambda a=algo: self.start_visualizer(a)))

        self.buttons.append(Button(center_x - 100, start_y + spacing * 4 + 40, 200, 50, "Back", self.go_back))

    def start_visualizer(self, algorithm):
        # Pass all parameters including seed
        print(f"DEBUG: Starting {algorithm} with seed={self.seed}")
        self.window.change_page(Visualizer, self.selected_grid, self.grid_mode, algorithm, self.seed)

    def go_back(self):
        from visualization.pages.grid_select import GridSelect
        self.window.change_page(GridSelect, self.grid_mode)

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((25, 25, 25))

        font = pygame.font.SysFont("arial", 50)
        text = font.render("Choose Algorithm", True, (255, 255, 255))
        screen.blit(text, (self.window.width // 2 - text.get_width() // 2, 100))

        # FIXED DISPLAY: Shows correct mode
        font2 = pygame.font.SysFont("arial", 30)
        
        # Create the display text
        if self.grid_mode == 'fixed' and self.seed is not None:
            display_text = f"Grid: {self.selected_grid} (Fixed - Seed: {self.seed})"
        else:
            display_text = f"Grid: {self.selected_grid} (Random)"
            
        sub = font2.render(display_text, True, (200, 200, 200))
        screen.blit(sub, (self.window.width // 2 - sub.get_width() // 2, 160))

        for button in self.buttons:
            button.draw(screen)
