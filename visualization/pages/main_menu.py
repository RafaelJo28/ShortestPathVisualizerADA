import pygame
from visualization.ui.button import Button
from visualization.pages.algorithm_select import AlgorithmSelect
from visualization.pages.grid_select import GridSelect

class MainMenu:
    def __init__(self, window):
        self.window = window
        self.buttons = []
        self._create_layout()

    def _create_layout(self):
        center_x = self.window.width // 2
        start_y = 250
        spacing = 80

        self.buttons.append(Button(center_x - 100, start_y, 200, 50, "Choose Grid", self.go_to_grid_select))
        self.buttons.append(Button(center_x - 100, start_y + spacing, 200, 50, "Choose Algorithm", self.go_to_algorithm_select))
        self.buttons.append(Button(center_x - 100, start_y + spacing * 2, 200, 50, "Quit", self.quit_app))

    def go_to_algorithm_select(self):
        self.window.change_page(AlgorithmSelect)

    def go_to_grid_select(self):
        self.window.change_page(GridSelect)

    def quit_app(self):
        self.window.running = False

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))

        title_font = pygame.font.SysFont("arial", 60)
        title_surf = title_font.render("Shortest Path Visualizer", True, (255, 255, 255))

        screen.blit(title_surf, (self.window.width // 2 - title_surf.get_width() // 2, 120))

        for button in self.buttons:
            button.draw(screen)
