import pygame
from Settings import *

class Upgrade:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player 
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        
    def input(self):
        keys = pygame.key.pygame.get_pressed()

        if keys[pygame.K_RIGHT]:
            pass 
        elif keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_SPACE]:
            pass


    def display(self):
        self.display_surface.fill("black")