import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
<<<<<<< HEAD
        self.image = pygame.image.load("../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
=======
        self.image = pygame.image.load("../graphics/test/rock.png")
        self.rect = self.image.get_rect(topleft = position)
>>>>>>> 414ec96781445ec4561bcadb54cbe7e475c245c4
