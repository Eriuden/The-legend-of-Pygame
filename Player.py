import pygame
from pygame.sprite import _Group
from Settings import *

class player(pygame.sprite.Sprite):

    #rappel, init, c'est là où on inscrit les "variables" de self
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        # L'on est obligé de faire en deux variantes if du au else
        # celui ci sert à stopper le mouvement si on arrête d'actionner
        # mais comme il arrête le if statement, on en fait un pour chaque dimension

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)