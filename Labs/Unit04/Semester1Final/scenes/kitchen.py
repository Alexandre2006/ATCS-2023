# Kitchen Scene (extends Scene)
# Written by all members

import pygame
from utils.scene import Scene
from utils.fsm import *
from scenes.navbar import Navbar
from obj.crepe import Crepe
import globals

class Kitchen(Scene):
    current_crepe = Crepe()
    kitchen_layout = []
    screen = pygame.display.set_mode((768, 512))
    navbar = Navbar(screen)
    topping_map = [[
        "apple", "banana", "blueberry", "chocolate", "strawberry", "whip"
    ], [
        "cheese", "ham", "mushroom", "spinach", "tomato", "bacon"
    ]]

    # Crepe Sprites
    crepe_png = pygame.image.load("sprites/crepe/raw_crepe.png")
    crepe_png.set_colorkey((255, 255, 255))
    crepe_burned_png = pygame.image.load("sprites/crepe/burnt_crepe.png")
    crepe_burned_png.set_colorkey((255, 255, 255))
    crepe_cooked_png = pygame.image.load("sprites/crepe/cooked_crepe.png")
    crepe_cooked_png.set_colorkey((255, 255, 255))
    
    # Kitchen Sprites
    cooker_png = pygame.image.load("sprites/kitchen/cooker.png")
    tile_png = pygame.image.load("sprites/kitchen/tile.png")
    counter_png = pygame.image.load("sprites/kitchen/counter.png")
    drawers_png = pygame.image.load("sprites/kitchen/drawers.png")
    plate_png = pygame.image.load("sprites/kitchen/plate.png")
    trash_png = pygame.image.load("sprites/kitchen/trash.png")

    # Sweet Toppings
    apple_png = pygame.image.load("sprites/toppings/sweet/apple.png")
    apple_png.set_colorkey((255, 255, 255))
    banana_png = pygame.image.load("sprites/toppings/sweet/banana.png")
    banana_png.set_colorkey((255, 255, 255))
    blueberry_png = pygame.image.load("sprites/toppings/sweet/blueberry.png")
    blueberry_png.set_colorkey((255, 255, 255))
    chocolate_png = pygame.image.load("sprites/toppings/sweet/chocolate.png")
    chocolate_png.set_colorkey((255, 255, 255))
    strawberry_png = pygame.image.load("sprites/toppings/sweet/strawberry.png")
    strawberry_png.set_colorkey((255, 255, 255))
    whip_png = pygame.image.load("sprites/toppings/sweet/whip.png")
    whip_png.set_colorkey((255, 255, 255))

    # Savory Toppings
    cheese_png = pygame.image.load("sprites/toppings/savory/cheese.png")
    cheese_png.set_colorkey((255, 255, 255))
    ham_png = pygame.image.load("sprites/toppings/savory/ham.png")
    ham_png.set_colorkey((255, 255, 255))
    mushroom_png = pygame.image.load("sprites/toppings/savory/mushroom.png")
    mushroom_png.set_colorkey((255, 255, 255))
    spinach_png = pygame.image.load("sprites/toppings/savory/spinach.png")
    spinach_png.set_colorkey((255, 255, 255))
    tomato_png = pygame.image.load("sprites/toppings/savory/tomato.png")
    tomato_png.set_colorkey((255, 255, 255))
    bacon_png = pygame.image.load("sprites/toppings/savory/bacon.png")
    bacon_png.set_colorkey((255, 255, 255))



    def __init__(self):
        # Load kitchen layout from kitchen.txt
        with open("kitchen.txt", "r") as f:
            self.kitchen_layout = [list(line.strip()) for line in f.readlines()]
        
        self.current_crepe.crepe_fsm.run_transition("cook")


    def render(self):
        # Render Background
        for i in range(len(self.kitchen_layout)):
            for j in range(len(self.kitchen_layout[i])):
                if self.kitchen_layout[i][j] == "A":
                    self.screen.blit(self.cooker_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "B":
                    self.screen.blit(self.tile_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "C":
                    self.screen.blit(self.counter_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "D":
                    self.screen.blit(self.drawers_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "E":
                    self.screen.blit(self.plate_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "F":
                    self.screen.blit(self.trash_png, (j * 128, i * 128))
                elif self.kitchen_layout[i][j] == "G":
                    self.screen.blit(self.plate_png, (j * 128, i * 128))
                    if globals.available_crepes > 0:
                        self.screen.blit(self.crepe_png, (j * 128, (i * 128) - 4))
                    # Render text of crepe count available
                    font = pygame.font.SysFont("Arial", 24)
                    text = font.render(str(globals.available_crepes), True, (0, 0, 0))
                    self.screen.blit(text, (j * 128, (i * 128) - 4))
        
        # Render Toppings on wall (sweet)
        self.screen.blit(self.apple_png, (64*3, 64))
        self.screen.blit(self.banana_png, (64*4, 64))
        self.screen.blit(self.blueberry_png, (64*5, 64))
        self.screen.blit(self.chocolate_png, (64*6, 64))
        self.screen.blit(self.strawberry_png, (64*7, 64))
        self.screen.blit(self.whip_png, (64*8, 64))

        # Render Toppings on wall (savory)
        self.screen.blit(self.cheese_png, (64*3, 64*2))
        self.screen.blit(self.ham_png, (64*4, 64*2))
        self.screen.blit(self.mushroom_png, (64*5, 64*2))
        self.screen.blit(self.spinach_png, (64*6, 64*2))
        self.screen.blit(self.tomato_png, (64*7, 64*2))
        self.screen.blit(self.bacon_png, (64*8, 64*2))
        
        # Render Crepes
        if self.current_crepe.crepe_fsm.current_state == "uncooked":
            pass # No crepe to render
        elif self.current_crepe.crepe_fsm.current_state == "cooking":
            self.screen.blit(self.crepe_png, (64*4, (256) - 2))
        elif self.current_crepe.crepe_fsm.current_state == "cooked":
            self.screen.blit(self.crepe_cooked_png, (64*4, (256) - 2))
        elif self.current_crepe.crepe_fsm.current_state == "burned":
            self.screen.blit(self.crepe_burned_png, (64*4, (256) - 2))
        elif self.current_crepe.crepe_fsm.current_state == "plated":
            self.screen.blit(self.crepe_cooked_png, (64*8, (256) - 2))
        
        # Render Toppings on Crepe
        offset = 0
        if self.current_crepe.crepe_fsm.current_state == "plated":
            offset = 8.5
        else:
            offset = 4.5
        for i in range(len(self.current_crepe.toppings)):
            topping = self.current_crepe.toppings[i]
            if topping == "apple":
                self.screen.blit(self.apple_png, (64*offset, (256) + 32))
            elif topping == "banana":
                self.screen.blit(self.banana_png, (64*offset, (256) + 32))
            elif topping == "blueberry":
                self.screen.blit(self.blueberry_png, (64*offset, (256) + 32))
            elif topping == "chocolate":
                self.screen.blit(self.chocolate_png, (64*offset, (256) + 32))
            elif topping == "strawberry":
                self.screen.blit(self.strawberry_png, (64*offset, (256) + 32))
            elif topping == "whip":
                self.screen.blit(self.whip_png, (64*offset, (256) + 32))
            elif topping == "cheese":
                self.screen.blit(self.cheese_png, (64*offset, (256) + 32))
            elif topping == "ham":
                self.screen.blit(self.ham_png, (64*offset, (256) + 32))
            elif topping == "mushroom":
                self.screen.blit(self.mushroom_png, (64*offset, (256) + 32))
            elif topping == "spinach":
                self.screen.blit(self.spinach_png, (64*offset, (256) + 32))
            elif topping == "tomato":
                self.screen.blit(self.tomato_png, (64*offset, (256) + 32))
            elif topping == "bacon":
                self.screen.blit(self.bacon_png, (64*offset, (256) + 32))
        
        # Render Navbar
        self.navbar.draw()

            

    def on_switch_to(self):
        pass

    def on_switch_from(self):
        pass

    def handle_events(self, events):
        # Check for mouse clicks
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Find letter pressed
                    x, y = event.pos
                    x = x // 128
                    y = y // 128
                    letter = self.kitchen_layout[y][x]

                    # Check if letter is trash, plate, or crepe
                    if letter == "F":
                            self.current_crepe.toppings = []
                            self.current_crepe.crepe_fsm.run_transition("throw")
                    elif letter == "E":
                        if self.current_crepe.crepe_fsm.current_state == "cooked":
                            self.current_crepe.crepe_fsm.run_transition("plate")
                        elif self.current_crepe.crepe_fsm.current_state == "plated" and globals.customer != None and globals.customer.customer_fsm.current_state == "waiting_for_order":
                            globals.customer.grade(self.current_crepe)
                            self.current_crepe.crepe_fsm.run_transition("serve")
                    elif letter == "G":
                        if globals.available_crepes > 0 and self.current_crepe.crepe_fsm.current_state == "uncooked":
                            self.current_crepe.crepe_fsm.run_transition("cook")
                            globals.available_crepes -= 1
                    
                    # Check if position is on a topping (32x32 tiles, starting at 32 y and 96 x)
                    x, y = event.pos
                    x = x // 64
                    y = y // 64
                    
                    if y >= 1 and y < 3 and x >= 3 and x < 9:
                        if self.current_crepe.crepe_fsm.current_state != "uncooked":
                            x -= 3
                            y -= 1
                            topping = self.topping_map[y][x]
                            if topping not in self.current_crepe.toppings:
                                self.current_crepe.add_topping(topping)
        # Navbar
        self.navbar.handle_events(events)
                    

                    
        pass
    

