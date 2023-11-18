import pygame
from Settings import *

class Upgrade:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player 
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys)
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        self.selection_index = 0
        self.selection_time = None 
        self.can_move = True
        
    def input(self):
        keys = pygame.key.pygame.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_number:
                self.selection_index += 1 
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            elif keys[pygame.K_LEFT]and self.selection_index > self.attribute_number:
                self.selection_index -=1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False 
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True 

    def create_items(self):
        self.item_list = []

        #horizontal
        for item, increment in enumerate (range(self.attribute_number)):
            full_width = self.display_surface.get_size()[0]
            increment - full_width // self.attribute_number
            left = (item * increment) + (increment - self.width) // 2
        #vertical
        top = self.display_surface.get_size()[1] * 0.1

        #création objet
        item = Item(left,top,self.width,self.height,self.index,self.font)
        self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):

            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface,self.selection_index,name,value,max_value,cost)

class Item:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index 
        self.font = font 

    def display_name(self,surface,name,cost,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        #titre
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_Rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        #coût
        cost_surface = self.font.render(f"{int(cost)}", False, TEXT_COLOR)
        cost_rect = cost_surface.get_Rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))
        
        surface.blit(title_surface, title_rect)
        surface.blit(cost_surface,cost_rect)

    def display_bar(self,surface,value,max_value,selected):
        top = self.rect.midtop + pygame.math.Vector2(0,60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
        color = BAR_COLOR_ACTIVE if selected else BAR_COLOR

        full_heigth = bottom[1] - top[1]
        relative_number = (value / max_value) * full_heigth
        value_rect = pygame.Rect(top[0] - 15, bottom[0] - relative_number, 30, 10)
        
        pygame.draw.line(surface,color,top,bottom, 5)
        pygame.draw.rect(surface,color, value_rect)
    
    def trigger(self,player):
        upgrade_attribute = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4
        
        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self,surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num:
            pygame.draw.rect(surface, UI_BORDERCOLOR_ACTIVE , self.rect)
            pygame.draw.rect(surface, UI_BORDERCOLOR, self.rect, 4)
        else :
            pygame.draw.rect(surface, UI_BGCOLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDERCOLOR, self.rect, 4)

        self.display_name(surface,name,cost,self.index == selection_num)
        self.display_bar(surface, value, max_value, self.index == selection_num)