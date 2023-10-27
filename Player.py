import pygame
from pygame.sprite import _Group
from Settings import *

class player(pygame.sprite.Sprite):

    #rappel, init, c'est là où on inscrit les "variables" de self
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0,-25)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        # L'on est obligé de faire en deux variantes if du au else
        # celui ci sert à stopper le mouvement si on arrête d'actionner
        # mais comme il arrête le if statement, on en fait un pour chaque dimension

        #mouvement basiques
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
        #attaques, à noter, pygame ne semble pas avoir pensé aux boutons de la souris...
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            # le get ticks de cooldown fonctionnant indéfiniment, il pourra recharger celui ci, censé fonctionner qu'une fois à la base
            self.attack_time = pygame.time.get_ticks()
        #sorts
        if keys[pygame.K_LSHIFT]and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")

        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")

        self.rect.center = self.hitbox.center

    def collision(self,direction):
        # Donc si un sprite du joueur rentre en collision avec celui d'un obstacle
        # si il va vers la droite, on le renvoie vers la gauche, et vice versa
        if direction == "horizontal":
            for sprite in self.obstacle_sprites :
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right 
        
        if direction =="vertical":
            for sprite in self.obstacle_sprites :
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def update(self):
        self.input()
        self.cooldown()
        self.move(self.speed)