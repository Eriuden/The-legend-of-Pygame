import pygame
from pygame.sprite import _Group
from Settings import *

class player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)