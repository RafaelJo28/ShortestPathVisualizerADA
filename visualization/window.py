import pygame
from visualization.pages.main_menu import MainMenu

class Window:
    def __init__(self, width=800, height=600, title="Shortest Path Visualizer"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Current page object
        self.current_page = MainMenu(self)
        self.clock = pygame.time.Clock()
        self.running = True

    def change_page(self, new_page_class, *args):
        """Switch to a different page class."""
        self.current_page = new_page_class(self, *args)

    def run(self):
        """Main loop controlling page rendering and event handling."""
        while self.running:
            dt = self.clock.tick(60) / 1000
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Delegate handling to current page
            self.current_page.handle_events(events)
            self.current_page.update(dt)
            self.current_page.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
