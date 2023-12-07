import pygame
import math
from classRoad import CollideLeft, CollideRight
     


class Camera:
    def __init__(self, screen, game):
        #autre variables
        self.screen = screen
        self.game = game
        self.coords = (0,0)
        self.angle = 0



                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        self.coords = self.game.player.coords[0] - math.cos(self.game.player.angle)*100, self.game.player.coords[1] + math.sin(self.game.player.angle)*100
        self.screen.blit(self.game.player.image, (self.screen.get_width() /2 - self.game.player.image.get_width()/2,500))

        ####################" affichage" ########################
        """Trouver distance entre les 2 points, calculer angle + trigonométrie"""
        #distance entre caméra et points
        for point in CollideLeft:
            a = self.coords[0] - point[0]
            b = self.coords[1] - point[1]
            d = math.sqrt(a*a+b*b)
            

        
    









        
        