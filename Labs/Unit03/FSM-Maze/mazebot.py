from time import sleep
import pygame
from fsm import FSM

class MazeBot(pygame.sprite.Sprite):

    def __init__(self, game, x=50, y=50):
        super().__init__()

        self.game = game

        # Load initial image
        self.image = pygame.image.load("assets/images/bot.png")
        self.rect = self.image.get_rect()

        # Set rectangle
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.centerx = x
        self.rect.centery = y

        # The map of the maze
        self.maze = self.game.txt_grid

        # The route the bot will take to get to the $
        self.path = []

        self.fsm = FSM("SOUTH")
        self.init_fsm()
    
    def init_fsm(self):
        dirs = ["SOUTH", "EAST", "NORTH", "WEST"]
        tiles = ["", "B", "#", "X", "$"]
                
        # Blank Space (w/o Breaker Mode On)
        self.fsm.add_transition(" ", "SOUTH", self.move_south, "SOUTH")
        self.fsm.add_transition(" ", "EAST", self.move_east, "EAST")
        self.fsm.add_transition(" ", "NORTH", self.move_north, "NORTH")
        self.fsm.add_transition(" ", "WEST", self.move_west, "WEST")

        # Blank Space (w/ Breaker Mode On)
        self.fsm.add_transition(" ", "BSOUTH", self.move_south, "BSOUTH")
        self.fsm.add_transition(" ", "BEAST", self.move_east, "BEAST")
        self.fsm.add_transition(" ", "BNORTH", self.move_north, "BNORTH")
        self.fsm.add_transition(" ", "BWEST", self.move_west, "BWEST")

        # B Breaker Mode Toggle (On)
        self.fsm.add_transition("B", "SOUTH", self.move_south, "BSOUTH")
        self.fsm.add_transition("B", "EAST", self.move_east, "BEAST")
        self.fsm.add_transition("B", "NORTH", self.move_north, "BNORTH")
        self.fsm.add_transition("B", "WEST", self.move_west, "BWEST")

        # B Breaker Mode Toggle (Off)
        self.fsm.add_transition("B", "BSOUTH", self.move_south, "SOUTH")
        self.fsm.add_transition("B", "BEAST", self.move_east, "EAST")
        self.fsm.add_transition("B", "BNORTH", self.move_north, "NORTH")
        self.fsm.add_transition("B", "BWEST", self.move_west, "WEST")

        # # Impassable Wall (w/o Breaker Mode On)
        self.fsm.add_transition("#", "SOUTH", None, "EAST")
        self.fsm.add_transition("#", "EAST", None, "NORT")
        self.fsm.add_transition("#", "NORTH", None, "WEST")
        self.fsm.add_transition("#", "WEST", None, "SOUTH")

        # # Impassable Wall (w/ Breaker Mode On)
        self.fsm.add_transition("#", "BSOUTH", None, "BEAST")
        self.fsm.add_transition("#", "BEAST", None, "BNORTH")
        self.fsm.add_transition("#", "BNORTH", None, "BWEST")
        self.fsm.add_transition("#", "BWEST", None, "BSOUTH")

        # X Passable Wall (w/o Breaker Mode On)
        self.fsm.add_transition("X", "SOUTH", None, "EAST")
        self.fsm.add_transition("X", "EAST", None, "NORTH")
        self.fsm.add_transition("X", "NORTH", None, "WEST")
        self.fsm.add_transition("X", "WEST", None, "SOUTH")

        # X Passable Wall (w/ Breaker Mode On)
        self.fsm.add_transition("X", "BSOUTH", self.move_south, "BSOUTH")
        self.fsm.add_transition("X", "BEAST", self.move_east, "BEAST")
        self.fsm.add_transition("X", "BNORTH", self.move_north, "BNORTH")
        self.fsm.add_transition("X", "BWEST", self.move_west, "BWEST")

        # $ Goal (w/o Breaker Mode On)
        self.fsm.add_transition("$", "SOUTH", self.move_south, "WIN")
        self.fsm.add_transition("$", "EAST", self.move_east, "WIN")
        self.fsm.add_transition("$", "NORTH", self.move_north, "WIN")
        self.fsm.add_transition("$", "WEST", self.move_west, "WIN")

        # $ Goal (w/ Breaker Mode On)
        self.fsm.add_transition("$", "BSOUTH", self.move_south, "WIN")
        self.fsm.add_transition("$", "BEAST", self.move_east, "WIN")
        self.fsm.add_transition("$", "BNORTH", self.move_north, "WIN")
        self.fsm.add_transition("$", "BWEST", self.move_west, "WIN")
        pass
    
    def get_state(self):
        return self.fsm.current_state
    
    def move_south(self):
        """
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.rect.centery += self.game.SPACING
        self.path.append("SOUTH")

    def move_east(self):
        """
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.rect.centerx += self.game.SPACING
        self.path.append("EAST")

    def move_north(self):
        """
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.rect.centery -= self.game.SPACING
        self.path.append("NORTH")

    def move_west(self):
        """
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.rect.centerx -= self.game.SPACING
        self.path.append("WEST")
    
    def get_next_space(self):
        """
        Uses the bot's current state to determine the next 
        space in the maze the bot would go to. The next 
        space is returned as a String from self.maze.

        Ex. If the bot is facing South, you should get 
        the character one row down from you.

        Returns:
            String: The next character in the maze the bot could go to
        """

        # This is the current x and y indices of the bot in the maze
        grid_x = self.rect.centerx // self.game.SPACING
        grid_y = self.rect.centery // self.game.SPACING


        current_state = self.get_state()
        
        if current_state in ["BSOUTH", "SOUTH"]:
            return self.maze[grid_y + 1][grid_x]
        elif current_state in ["BWEST", "WEST"]:
            return self.maze[grid_y][grid_x - 1]
        elif current_state in ["BEAST", "EAST"]:
            return self.maze[grid_y][grid_x + 1]
        elif current_state in ["BNORTH", "NORTH"]:
            return self.maze[grid_y - 1][grid_x]
    
    def update(self):
        if self.get_state() != "WIN":
            self.fsm.process(self.get_next_space())
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))
