import pygame
import math
     


class Car:
    def __init__(self, screen, game):
        #autre variables
        self.screen = screen
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load("assets/clio.png"),(100,100))
        self.coords = [564,595]
        self.angle = 0
        self.speed =5



                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        self.screen.blit(self.image, (self.screen.get_width() /2 - self.image.get_width()/2,600))
        self.coords[0] = self.coords[0] + math.cos(self.angle)*self.speed
        self.coords[1] = self.coords[1] + math.sin(self.angle)*-self.speed


    def left(self):
        self.angle += math.pi/128

    def right(self):
        self.angle -= math.pi/128
    
    def accelerate(self):
        if(self.speed < 5):
            self.speed +=0.1
    
    def brake(self):
        if(self.speed>0):
            self.speed -=0.2
            if(self.speed < 0):
                self.speed = 0
        




        
        