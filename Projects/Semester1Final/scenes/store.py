# Kitchen Scene (extends Scene)
# Written by all members

import pygame
from utils.scene import Scene
from utils.fsm import *
from scenes.navbar import Navbar
import globals

class Store(Scene):
    screen = pygame.display.set_mode((768, 512))
    navbar = Navbar(screen)

    # Crepe Sprites
    crepe_png = pygame.image.load("sprites/crepe/raw_crepe.png")
    crepe_png = pygame.transform.scale(crepe_png, (crepe_png.get_width() * 2, crepe_png.get_height() * 2))
    crepe_png.set_colorkey((255, 255, 255))

    def __init__(self):
        pass

    def render(self):
        # Clear screen
        self.screen.fill((255, 255, 255))

        # Draw Store Sign (Background)
        pygame.draw.rect(self.screen, (50, 50, 50), (64, 16, 640, 72))

        # Draw Store Sign (Text)
        font = pygame.font.SysFont("Arial", 38)
        text = font.render("Store", True, (255, 255, 255))
        self.screen.blit(text, (340, 32))

        # Draw Crepe (Background)
        pygame.draw.rect(self.screen, (50, 50, 50), (64, 104, 640, 384))

        # Draw Crepe (Image)
        self.screen.blit(self.crepe_png, (256, 160))

        # Draw Crepe (Title)
        font = pygame.font.SysFont("Arial", 38)
        text = font.render("Additional Crepes", True, (255, 255, 255))
        self.screen.blit(text, (228, 104))

        # Draw Crepe (Owned)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Owned: " + str(globals.available_crepes), True, (0, 0, 0))
        self.screen.blit(text, (320, 276))

        # Draw Crepe Purchase Button (background)
        pygame.draw.rect(self.screen, (0, 200, 0), (240, 420, 288, 48))

        # Draw Crepe Purchase Button (text)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Purchase Crepes 5x ($10)", True, (255, 255, 255))
        self.screen.blit(text, (245, 430))

        # Draw navbar
        self.navbar.draw()
        






    def on_switch_to(self):
        pass

    def on_switch_from(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Purchase Crepes
                    if event.pos[0] >= 240 and event.pos[0] <= 528 and event.pos[1] >= 420 and event.pos[1] <= 468:
                        if globals.money >= 10:
                            globals.money -= 10
                            globals.available_crepes += 5
                    # Return to Kitchen
                    elif event.pos[0] >= 0 and event.pos[0] <= 128 and event.pos[1] >= 0 and event.pos[1] <= 32:
                        globals.current_scene = "kitchen"
        # Navbar
        self.navbar.handle_events(events)
    

