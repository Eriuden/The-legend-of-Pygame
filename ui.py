import pygame
from Settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #gauche, haut, largeur, hauteur
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 30, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        #conversion de la liste des armes

        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.spell_graphics = []
        for spell in spell_data.values():
            path = spell["graphic"]
            spell = pygame.image.load(spell["graphic"]).convert_alpha()
            self.spell_graphics.append(spell)

    def show_bar(self,current, max, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BORDERCOLOR, bg_rect,3)

        #Voilà donc comment on crée une jauge de vie qui s'adapte aux HP
        # le ratio agira donc sur la largueur par un effet de pourcentage
        ratio = current / max
        current_width = bg_rect.width * ratio 
        current_rect = bg_rect.copy()
        current_rect_width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDERCOLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surface.get_rect(bottomright = (x,y))

        self.display_surface.blit(text_surface, text_rect)

    def selection_box(self,left,top, switched):
        bg_rect = pygame.Rect(left,top, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BGCOLOR, bg_rect)
        if switched:
            pygame.drax.rect(self.display_surface, UI_BORDERCOLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.drax.rect(self.display_surface, UI_BORDERCOLOR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self,weapon_index,switched):
        bg_rect = self.selection_box(10,630,switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(bg_rect.center)

        self.display_surface.blit(weapon_surf,weapon_rect)

    def spell_overlay(self,spell_index,switched):
        bg_rect = self.selection_box(80,630,switched)
        spell_surf = self.spell_graphics[spell_index]
        spell_rect = spell_surf.get_rect(bg_rect.center)
        
        self.display_surface.blit(spell_surf,spell_rect)

    def display(self,player):
        #pygame.draw.rect(self.display_surface, "black", self.health_bar_rect)
        self.show_bar(player.healt, player.stats["health"], self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect,ENERGY_COLOR)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.spell_overlay(player.spell_index, not player.can_switch_spell)

        self.selection_box(10,650) #l'arme
        self.selection_box(80,635) #le sort
