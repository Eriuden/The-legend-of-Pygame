import pygame
from Settings import *


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

    def flame(self):
        pass