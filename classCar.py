import pygame
import math
     


class Car:
    def __init__(self, screen, game):
        #autre variables
        self.screen = screen
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load("assets/clio.png"),(100,100))
        self.coords = (564,595)
        self.angle = math.pi/4
        self.speed =0



                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        self.screen.blit(self.image, (self.screen.get_width() /2 - self.image.get_width()/2,500))

    def left(self):
        pass

    def right(self):
        pass
        




        
        