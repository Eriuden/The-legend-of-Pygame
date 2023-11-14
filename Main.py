import pygame, sys
from Settings import *
from Debug import debug
from Level import level 
class Game:
    def __init__(self):
        pygame.init()
        # comment créer l'écran de l'appli
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #set caption est basiquement le nom de l'appli
        pygame.display.set_caption("The legend of Williams")
        self.clock = pygame.time.Clock()

        self.level = level()

    def run(self):
        while True:
            #Fonction pour quitter l'appli
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level(self.toggle_menu())

            self.screen.fill("black")
            self.level.run()
            debug("")
            pygame.display.update()
            self.clock.tick(FPS)

if __name__== "__main__":
    game = Game()
    game.run()