import pygame
from visualization.ui.button import Button
from visualization.pages.visualizer import Visualizer

class AlgorithmSelect:
    def __init__(self, window, selected_grid=None):
        self.window = window
        self.selected_grid = selected_grid
        self.buttons = []
        self._create_layout()

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
        self.window.change_page(Visualizer, self.selected_grid, algorithm)

    def go_back(self):
        from visualization.pages.grid_select import GridSelect
        self.window.change_page(GridSelect)

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

        font2 = pygame.font.SysFont("arial", 30)
        sub = font2.render(f"Grid: {self.selected_grid}", True, (200, 200, 200))
        screen.blit(sub, (self.window.width // 2 - sub.get_width() // 2, 160))

        for button in self.buttons:
            button.draw(screen)
