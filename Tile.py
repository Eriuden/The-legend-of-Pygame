import pygame
from Settings import *

class tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface = pygame.surface((TILESIZE, TILESIZE))):
        super().__init__(groups)

        self.image = surface
        self.sprite_type = sprite_type

        if sprite_type == "object":
            self.rect = self.image.get_rect(topleft = (position[0],position[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = position)
            
        #inflate permet de réduire la hitbox pour une collision plus propre
        # par exemple, avoir quand même la tête face à l'obstacle en haut
        self.hitbox = self.rect.inflate(0,-10)

