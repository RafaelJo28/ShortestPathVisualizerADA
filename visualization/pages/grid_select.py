import pygame
from visualization.ui.button import Button
from visualization.pages.algorithm_select import AlgorithmSelect
from visualization.pages.visualizer import Visualizer

class GridSelect:
    def __init__(self, window):
        self.window = window
        self.buttons = []
        self.selected_grid = None
        self._create_layout()

    def _create_layout(self):
        center_x = self.window.width // 2
        start_y = 200
        spacing = 70

        # Example grid presets (you will add more later)
        grid_types = ["Empty Grid", "Random Obstacles", "Maze Grid", "Weighted Grid"]

        for i, grid_name in enumerate(grid_types):
            self.buttons.append(Button(center_x - 120, start_y + i * spacing, 240, 50, grid_name,
                                       lambda name=grid_name: self.select_grid(name)))

        self.buttons.append(Button(center_x - 100, start_y + spacing * 4 + 40, 200, 50, "Back", self.go_back))

    def select_grid(self, grid_name):
        self.selected_grid = grid_name
        self.window.change_page(AlgorithmSelect, grid_name)

    def go_back(self):
        from visualization.pages.main_menu import MainMenu
        self.window.change_page(MainMenu)

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((25, 25, 25))

        font = pygame.font.SysFont("arial", 50)
        text = font.render("Choose Grid", True, (255, 255, 255))
        screen.blit(text, (self.window.width // 2 - text.get_width() // 2, 100))

        for button in self.buttons:
            button.draw(screen)
