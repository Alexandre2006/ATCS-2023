import pygame
import sys
from block import Block
from mazebot import MazeBot

class MangoGame:
    # Constants
    START_X, START_Y = 24, 24
    SPACING = 50
    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self):
        self.DEBUG = True

        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.ghost_timer = 8000

        # Paths
        self.txt_grid = []
        self.grid = []

        # sprites
        self.blocks = pygame.sprite.Group()
        self.mango = None

        # Load the game level and available paths
        self.load_level(3)

        self.HEIGHT = len(self.txt_grid) * self.SPACING
        self.WIDTH = len(self.txt_grid[0]) * self.SPACING

        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Mango FSM")

    def load_level(self, maze_number=1):
        filepath = "assets/mazes/maze" + str(maze_number) + ".txt"
        row = 0
        with open(filepath, "r") as file:
            line = file.readline().strip()
            while line:
                txt_row = []
                for col in range(len(line)):
                    pos_x = self.START_X + (self.SPACING * col)
                    pos_y = self.START_Y + (self.SPACING * row)
                    txt_row.append(line[col])
                    if line[col] == '#':
                        self.blocks.add(Block(pos_x, pos_y))
                    elif line[col] == 'X':
                        self.blocks.add(Block(pos_x, pos_y, Block.BRICK))
                    elif line[col] == '$':
                        self.blocks.add(Block(pos_x, pos_y, Block.MONEY))
                    elif line[col] == 'B':
                        self.blocks.add(Block(pos_x, pos_y, Block.BOOSTER))
                    elif line[col] == 'M':
                        self.mango = MazeBot(self, pos_x, pos_y)

                self.txt_grid.append(txt_row)
                line = file.readline()
                row += 1

    def run(self):
        # Main game loop
        running = True

        # Draw the initial screen
        self.screen.fill(self.BACKGROUND_COLOR)
        self.blocks.draw(self.screen)
        self.mango.draw(self.screen)
        
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)

            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Only update every 120 fps
            if self.dt > 120:
                self.dt = 0
                self.mango.update()

                # Draw to the screen
                self.screen.fill(self.BACKGROUND_COLOR)
                self.blocks.draw(self.screen)
                self.mango.draw(self.screen)

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = MangoGame()
    pm.run()
