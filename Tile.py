import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/rock.png")
        self.rect = self.image.get_rect(topleft = position)
