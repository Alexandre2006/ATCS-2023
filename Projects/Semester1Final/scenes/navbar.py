import pygame
import globals

class Navbar:
    screen = None

    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        # Navigate to: Kitchen - Dining Room - Store (write as text)

        # Draw text (black font)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Kitchen", True, (0, 0, 0))
        self.screen.blit(text, (0, 0))
        text = font.render("Dining Room", True, (0, 0, 0))
        self.screen.blit(text, (0, 32))
        text = font.render("Store", True, (0, 0, 0))
        self.screen.blit(text, (0, 64))

        # Draw Cash
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Cash: $" + str(globals.money), True, (0, 150, 0))
        self.screen.blit(text, (640, 0))
        
        