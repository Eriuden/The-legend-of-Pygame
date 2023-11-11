import pygame
from Settings import *
from random import randint


class SpellPlayer:
    def __init__(self, animation):
        self.animation = animation

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            player.health += strength 
            player.energy -= cost
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]
            self.animation.create_particles("aura", player.rect.center, groups)
            self.animation.create_particles("heal", player.rect.center + pygame.math.Vector2(0,0), groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.stats.split("_")[0] =="right":
                direction = pygame.math.Vector2(1,0)
            elif player.status.split("_")[0] =="left":
                direction = pygame.math.Vector2(-1,0)
            elif player.stats.split("_")[0] =="up":
                direction = pygame.math.Vector2(0,-1)
            else:
                direction = pygame.math.Vector2(0,1)

            for i in range(1, 6):
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation.create_particles("flame", (x,y), groups)
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx  + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = player.rect.centery + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation.create_particles("flame", (x,y), groups)