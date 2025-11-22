# === visualization/pages/visualizer.py ===
import pygame
from visualization.ui.button import Button


class Visualizer:
def __init__(self, window, selected_grid, algorithm):
self.window = window
self.selected_grid = selected_grid
self.algorithm = algorithm
self.buttons = []
self.finished = False
self.visited_nodes = []
self.path_nodes = []
self.grid = None # loaded later based on selected_grid


self._create_layout()
self._load_grid()
self._run_algorithm()


def _create_layout(self):
self.buttons.append(Button(20, 20, 150, 40, "Back", self.go_back))


def _load_grid(self):
# Placeholder for loading different grid types
# Later replaced with core/grid generators
width, height = 30, 20
self.grid = [[0 for _ in range(width)] for _ in range(height)]


def _run_algorithm(self):
# Placeholder animation logic
# In final version: call core.algorithm_runner
import random
for _ in range(100):
self.visited_nodes.append((random.randint(0, 29), random.randint(0, 19)))
self.path_nodes = [(i, i) for i in range(10)]
self.finished = True


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
screen.fill((20, 20, 20))


# Draw grid
cell_size = 25
for r in range(len(self.grid)):
for c in range(len(self.grid[0])):
pygame.draw.rect(screen, (50, 50, 50), (c * cell_size + 200, r * cell_size + 80, cell_size, cell_size), 1)


# Draw visited nodes
for (x, y) in self.visited_nodes:
pygame.draw.rect(screen, (0, 120, 255), (x * cell_size + 200, y * cell_size + 80, cell_size, cell_size))


# Draw final path
for (x, y) in self.path_nodes:
pygame.draw.rect(screen, (255, 200, 0), (x * cell_size + 200, y * cell_size + 80, cell_size, cell_size))


# Draw UI elements
for button in self.buttons:
button.draw(screen)


# Draw labels
font = pygame.font.SysFont("arial", 32)
title = font.render(f"{self.algorithm} on {self.selected_grid}", True, (255, 255, 255))
screen.blit(title, (self.window.width//2 - title.get_width()//2, 20))