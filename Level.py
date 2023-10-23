import pygame

class Level:
    def __init__(self):

        #surface d'affichage
        self.display_surface = pygame.display.get_surface()
        
        #Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        #mise à jour du jeu
        pass