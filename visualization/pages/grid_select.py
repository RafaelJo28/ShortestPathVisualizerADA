import pygame
from visualization.ui.button import Button
from visualization.pages.algorithm_select import AlgorithmSelect


class GridSelect:
    DEFAULT_FIXED_SEED = 42  # reproducible grid seed

    def __init__(self, window, grid_mode='random'):
        self.window = window
        self.buttons = []
        self.selected_grid = None
        self.grid_mode = grid_mode  # 'random' or 'fixed'
        self.mode_button = None
        self._create_layout()

    def _create_layout(self):
        center_x = self.window.width // 2
        start_y = 200
        spacing = 70

        # Updated grid presets (matches GridLoader)
        grid_types = [
            "Empty Grid",
            "Random Obstacles",
            "Maze Grid",
            "Weighted Grid",
            "Terrain Grid",     # NEW
        ]

        # Mode toggle button (Random vs Fixed)
        mode_label = "Mode: Fixed" if self.grid_mode == 'fixed' else "Mode: Random"
        btn_w, btn_h = 160, 40
        self.mode_button = Button(
            self.window.width - btn_w - 20,
            20,
            btn_w,
            btn_h,
            mode_label,
            self.toggle_mode
        )
        self.buttons.append(self.mode_button)

        # Grid buttons
        for i, grid_name in enumerate(grid_types):
            self.buttons.append(
                Button(
                    center_x - 120,
                    start_y + i * spacing,
                    240,
                    50,
                    grid_name,
                    lambda name=grid_name: self.select_grid(name)
                )
            )

        self.buttons.append(
            Button(
                center_x - 100,
                start_y + spacing * len(grid_types) + 40,
                200,
                50,
                "Back",
                self.go_back
            )
        )

    def select_grid(self, grid_name):
        """
        Pass grid type + mode + seed to next page
        """
        self.selected_grid = grid_name

        # Decide seed based on mode
        seed = self.DEFAULT_FIXED_SEED if self.grid_mode == 'fixed' else None

        # Pass everything forward
        self.window.change_page(
            AlgorithmSelect,
            grid_name,
            seed
        )

    def toggle_mode(self):
        # Flip between 'random' and 'fixed'
        self.grid_mode = 'fixed' if self.grid_mode == 'random' else 'random'

        # Update button label
        if self.mode_button:
            self.mode_button.text = (
                "Mode: Fixed" if self.grid_mode == 'fixed' else "Mode: Random"
            )

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
        screen.blit(
            text,
            (self.window.width // 2 - text.get_width() // 2, 100)
        )

        for button in self.buttons:
            button.draw(screen)
