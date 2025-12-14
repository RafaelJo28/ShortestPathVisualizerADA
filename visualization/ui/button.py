import pygame


class Button:
    """Simple button UI element with hover and click effects."""
    
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.hovered = False
        
        # Colors
        self.normal_color = (70, 70, 70)
        self.hover_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        
    def handle_event(self, event):
        """Handle mouse clicks on the button."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
    
    def update(self, mouse_pos):
        """Update button state based on mouse position."""
        self.hovered = self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
        """Draw the button."""
        color = self.hover_color if self.hovered else self.normal_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        
        font = pygame.font.SysFont("arial", 18, bold=True)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
