from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
from Settings import *
from Tile import tile
from Player import player
from Debug import debug
from Support import *

class Level:
    def __init__(self):

        #surface d'affichage
        self.display_surface = ySortCameraGroup()
        
        #Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    # le MASSIF array de la world map a faire plus tard en settings...
    # enumerate est conseillé pour indexer un array
    # en énumerant ainsi les lignes, on peut faire la même avec les colonnes,
    # contenues justement dans les lignes comme dans un array
    def create_map(self):

        layouts = {
            "boundary": import_csv_layout("../map/map_FloorBlcoks.csv")
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(WORLD_MAP):
                for col_index, col in enumerate(row):
                    #ca semble trompeur, mais c'est logique
                    # x pour les colonnes car celle tout à gauche, puis la seconde à 
                    # gauche, etc
                    # et y car les lignes sont empilées de haut en bas
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE

                    if style == "boundary":
                        tile((x,y), [self.visible_sprites, self.obstacles_sprites], "invisible")
                if col == "x" :
                    tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if col =="p" :
                    # si on ne mets pas en array les obstacles, c'est car le joueur
                    # contrairement aux visibles, ne peut aller dedans
                    # ils ne correspondent aux paramètres groups
                    # qui de par son nom nous laisse deviner l'array, et sont un autre paramètre
                    self. player = player((2000,1400), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        #mise à jour du jeu
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class ySortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        # gestion de la caméra au propre
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        #Sol
        self.floor_surface = pygame.image.load("../graphics/tilemap.ground.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def custom_draw(self):
        # La caméra suit l'avancée du perso
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_position = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_position)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
    


        