"""
Main entry point for the Shortest Path Visualizer application.
"""
import pygame
from visualization.window import Window


def main():
    """Run the application."""
    window = Window(width=1200, height=800, title="Shortest Path Visualizer")
    window.run()


if __name__ == "__main__":
    main()
