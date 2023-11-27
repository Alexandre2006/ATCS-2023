import pygame

class Block(pygame.sprite.Sprite):
    WALL = 0
    BRICK = 1
    MONEY = 2
    BOOSTER = 3

    def __init__(self, x=50, y=50, wall_type=0):
        super().__init__()

        filepath = "assets/images/"

        # Load the image
        if wall_type == self.WALL:
            self.image = pygame.image.load(filepath+"wall.png")
        elif wall_type == self.BRICK:
            self.image = pygame.image.load(filepath+"brick.png")
        elif wall_type == self.MONEY:
            self.image = pygame.image.load(filepath+"money.png")
        elif wall_type == self.BOOSTER:
            self.image = pygame.image.load(filepath+"booster.png")

        self.type = wall_type
        
        # Set the position to be the center of the image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        