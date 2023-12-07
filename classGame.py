import pygame
from listeChainee import Liste
from random import choice
from classCar import Car
from classRoad import Road
from classCamera import Camera
     


class Game:
    def __init__(self, screen):
        

        #autre variables
        self.screen = screen
        self.compteur = 0
        self.player = Car(self.screen, self)
        self.pressed = {pygame.K_LEFT : False,pygame.K_RIGHT : False}
        self.road = Road(self)
        self.camera = Camera(self.screen, self)

                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        pygame.draw.rect(self.screen, "white", pygame.Rect(0,0,self.screen.get_width(), self.screen.get_height()))
        self.player.update()
        self.camera.update()
        if self.pressed[pygame.K_LEFT]:
            self.player.left()
        if(self.pressed[pygame.K_RIGHT]):
            self.player.right()

        self.road.showMinimap()
        




        self.compteur += 1




        
        