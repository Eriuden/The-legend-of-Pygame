import pygame
from Settings import *

class Level:
    def __init__(self):

        #surface d'affichage
        self.display_surface = pygame.display.get_surface()
        
        #Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    # le MASSIF array de la world map a faire plus tard en settings...
    # enumerate est conseillé pour indexer un array
    # en énumerant ainsi les lignes, on peut faire la même avec les colonnes,
    # contenues justement dans les lignes comme dans un array
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                #ca semble trompeur, mais c'est logique
                # x pour les colonnes car celle tout à gauche, puis la seconde à 
                # gauche, etc
                # et y car les lignes sont empilées de haut en bas
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col


    def run(self):
        #mise à jour du jeu
        pass