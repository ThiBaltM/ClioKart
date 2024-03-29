import pygame
from listeChainee import Liste
from random import choice
from classCar import Car
from classRoad import Road
from classCamera import Camera
import math
     


class Game:
    def __init__(self, screen):
        

        #autre variables
        self.screen = screen
        self.compteur = 0
        self.player = Car(self.screen, self)
        self.pressed = {pygame.K_LEFT : False,pygame.K_RIGHT : False, pygame.K_UP : False,pygame.K_DOWN : False}
        self.road = Road(self)
        self.camera = Camera(self.screen, self)

        ##### camera paramaters #####
        self.horizon=1/3*self.screen.get_height()
        self.horizonZoom = 1.5
        self.frontZoom = 3

        #background
        self.background=pygame.transform.scale(pygame.image.load("assets/background.png"),(self.screen.get_width(),self.screen.get_height()/2))
                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        pygame.draw.rect(self.screen, (210, 211, 156), pygame.Rect(0,0,self.screen.get_width(), self.screen.get_height()))
        self.camera.update()
        self.player.update()
        self.screen.blit(self.background,(0,0))
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


    def calculPosForCameraDisplay(self,x,y):
        top_scale = 1  # Plus les points sont en haut, plus ils seront resserrés
        bottom_scale = 0.3  # Plus les points sont en bas, moins ils seront resserrés

        if(y> self.screen.get_height()):
            y = self.screen.get_height()
        """
        normalized_y = -abs(y - self.screen.get_height()) / (self.screen.get_height() * (1 - 1/3))
        scaling_factor = top_scale + (bottom_scale - top_scale) * y
        """
        coef = self.horizonZoom + (self.screen.get_height() - y) * ((self.frontZoom - self.horizonZoom) / self.screen.get_height())

        nx = self.screen.get_width() / 2 + x * coef
        ny = y * self.horizon / self.screen.get_height() #* scaling_factor

        return nx, self.screen.get_height() * (5 / 6) - ny