import pygame
import globals
from obj.customer import Customer

class Navbar:
    screen = None

    def __init__(self, screen):
        self.screen = screen
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if x >= 0 and x < 128 and y >= 0 and y < 32:
                        globals.current_scene = "kitchen"
                    elif x >= 0 and x < 128 and y >= 32 and y < 64:
                        globals.current_scene = "store"
                    # Check for presses on order buttons
                    elif x >= 400 and x < 640 and y >= 32 and y < 64:
                        print("YAYAYAYA")
                        if globals.customer == None:
                            globals.customer = Customer()
                        elif globals.customer.customer_fsm.current_state == "success":
                            globals.customer = Customer()
                        elif globals.customer.customer_fsm.current_state == "waiting_to_take_order":
                            globals.customer.customer_fsm.run_transition("take_order")
    
    def draw(self):
        order_map = {
            "Ha" : "Ham\n",
            "Ch" : "Cheese\n",
            "Mu" : "Mushroom\n",
            "To" : "Tomato\n",
            "Sp" : "Spinach\n",
            "Ba" : "Bacon\n",
            "St" : "Strawberry\n",
            "Bn" : "Banana\n",
            "Co" : "Chocolate\n",
            "Wh" : "Whipped Cream\n",
            "Bl" : "Blueberry\n",
            "Ap" : "Apple\n"
        }

        # Draw text (black font)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Kitchen", True, (0, 0, 0))
        self.screen.blit(text, (0, 0))
        text = font.render("Store", True, (0, 0, 0))
        self.screen.blit(text, (0, 32))

        # Draw Cash
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Cash: $" + str(globals.money), True, (0, 150, 0))
        self.screen.blit(text, (400, 0))

        # Draw Current Order
        font = pygame.font.SysFont("Arial", 24)
        text = ""
        if globals.customer == None:
            text = font.render("Current Order: Next Customer!", True, (0, 0, 0))
        elif globals.customer.customer_fsm.current_state == "waiting_to_take_order":
            text = font.render("Current Order: Take Order!", True, (0, 0, 0))
        else:
            order_as_text = ""
            # Substring every 2 characters
            for i in range(0, len(globals.customer.order), 2):
                order_as_text += order_map[globals.customer.order[i:i+2]]
            # Blit each line
            lines = order_as_text.split("\n")
            for i in range(len(lines)):
                text = font.render(lines[i], True, (0, 0, 0))
                self.screen.blit(text, (400, 32 + (i * 24)))
        self.screen.blit(text, (400, 32))
        