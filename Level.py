from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
from Settings import *
from Tile import tile
from Player import player
from Debug import debug
from Support import *
from random import choice
from weapon import Weapon

class Level:
    def __init__(self):

        #surface d'affichage
        self.display_surface = ySortCameraGroup()
        
        #Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.current_attack = None

        self.create_map()
        
    # enumerate est conseillé pour indexer un array
    # en énumerant ainsi les lignes, on peut faire la même avec les colonnes,
    # contenues justement dans les lignes comme dans un array
    def create_map(self):

        layouts = {
            "boundary": import_csv_layout("../map/map_FloorBlcoks.csv"),
            "grass" :import_csv_layout("../map/map_Grass.csv"),
            "object" :import_csv_layout("../map/map_Objects.csv")
        }
        graphics = {
            "grass": import_folder("../graphics/Grass"),
            "objects": import_folder("../graphics/objects")
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    #ca semble trompeur, mais c'est logique
                    # x pour les colonnes car celle tout à gauche, puis la seconde à 
                    # gauche, etc
                    # et y car les lignes sont empilées de haut en bas
                    if col !="-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                    if style == "boundary":
                        tile((x,y), [self.obstacles_sprites], "invisible")

                    if style =="grass":
                        random_grass_image = choice(graphics["grass"])
                        tile((x,y, [self.visible_sprites, self.obstacles_sprites], "grass", random_grass_image))

                    if style =="object":
                        surface = graphics["objects"][int(col)]
                        tile((x,y),[self.visible_sprites, self.obstacles_sprites], "object", surface)
                        
                    # si on ne mets pas en array les obstacles, c'est car le joueur
                    # contrairement aux visibles, ne peut aller dedans
                    # ils ne correspondent aux paramètres groups
                    # qui de par son nom nous laisse deviner l'array, et sont un autre paramètre
        self. player = player((2000,1400), [self.visible_sprites], self.obstacles_sprites, self.attack, self.destroy_weapon)

    def attack(self):
        self.current_attack = Weapon(self. player, [self.visible_sprites])
    
    def destroy_weapon(self):
        # si une attaque est en cours, on la supprime, et valeur nulle
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
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
    


        