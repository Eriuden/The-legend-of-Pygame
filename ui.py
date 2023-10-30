import pygame
from Settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #gauche, haut, largeur, hauteur
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 30, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self,current, max, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BGCOLOR, bg_rect)

        #Voilà donc comment on crée une jauge de vie qui s'adapte aux HP
        # le ratio agira donc sur la largueur par un effet de pourcentage
        ratio = current / max
        current_width = bg_rect.width * ratio 
        current_rect = bg_rect.copy()
        current_rect_width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.drax.rect(self.display_surface, UI_BORDERCOLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surface.get_rect(bottomright = (x,y))

        self.display_surface.blit(text_surface, text_rect)

    def display(self,player):
        #pygame.draw.rect(self.display_surface, "black", self.health_bar_rect)
        self.show_bar(player.healt, player.stats["health"], self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect,ENERGY_COLOR)

        self.show_exp(player.exp)