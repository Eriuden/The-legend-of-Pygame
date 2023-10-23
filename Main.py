import pygame, sys
from Settings import *
from Debug import debug

class Game:
    def __init__(self):
        pygame.init()
        # comment créer l'écran de l'appli
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            #Fonction pour quitter l'appli
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            debug("")
            pygame.display.update()
            self.clock.tick(FPS)

if __name__== "__main__":
    game = Game()
    game.run()