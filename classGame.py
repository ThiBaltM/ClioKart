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
        self.pressed = {pygame.K_LEFT : False,pygame.K_RIGHT : False, pygame.K_UP : False,pygame.K_DOWN : False}
        self.road = Road(self)
        self.camera = Camera(self.screen, self)

                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        pygame.draw.rect(self.screen, "white", pygame.Rect(0,0,self.screen.get_width(), self.screen.get_height()))
        self.camera.update()
        self.player.update()
        if self.pressed[pygame.K_LEFT]:
            self.player.left()
        if(self.pressed[pygame.K_RIGHT]):
            self.player.right()
        if(self.pressed[pygame.K_UP]):
            self.player.accelerate()
        if(self.pressed[pygame.K_DOWN]):
            self.player.brake()

        self.road.showMinimap()
        




        self.compteur += 1




        
        