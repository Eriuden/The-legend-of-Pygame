import pygame
from Settings import *

class tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)

        self.image = pygame.image.load("../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        #inflate permet de réduire la hitbox pour une collision plus propre
        # par exemple, avoir quand même la tête face à l'obstacle en haut
        self.hitbox = self.rect.inflate(0,-10)

