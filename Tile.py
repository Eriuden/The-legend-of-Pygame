import pygame
from Settings import *

class tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)

        self.image = pygame.image.load("../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.image = pygame.image.load("../graphics/test/rock.png")
        self.rect = self.image.get_rect(topleft = position)

