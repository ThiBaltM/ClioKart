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
        self.horizon=1/3*self.screen.get_height()
        self.horizonZoom = 1.5
        self.frontZoom = 6



                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        def calculPosForCameraDisplay(x,y):
            coef = self.horizonZoom+ (self.screen.get_height()-y)*((self.frontZoom - self.horizonZoom)/self.screen.get_height())

            nx = self.screen.get_width()/2 + x*coef
            ny = y*self.horizon/self.screen.get_height()
            return nx,self.screen.get_height()-ny
        
        self.coords = self.game.player.coords[0] - math.cos(self.game.player.angle)*100, self.game.player.coords[1] + math.sin(self.game.player.angle)*100

        ####################" affichage "########################
        #distance entre caméra et points
        newCollideLeft = []
        for point in CollideLeft:
            a = self.coords[0] - point[0]
            b = self.coords[1] - point[1]
            d = math.sqrt(a*a+b*b)

            angleEntreOrdonneeEtDroite = math.atan2(a,b)

            angle = (angleEntreOrdonneeEtDroite - self.game.player.angle + math.pi) % (2 * math.pi)
            oppose = math.sin(angle)*(d)
            adjacent = math.cos(angle)*(d)
            newCollideLeft.append((adjacent, oppose))
        
        newCollideRight = []
        for point in CollideRight:
            a = point[0] - self.coords[0]
            b = point[1]-self.coords[1]
            d = math.sqrt(a*a+b*b)

            angleEntreOrdonneeEtDroite = math.atan2(a,b)

            angle = (angleEntreOrdonneeEtDroite - self.game.player.angle) % (2 * math.pi)
            oppose = math.sin(angle)*(d)
            adjacent = math.cos(angle)*(d)
            newCollideRight.append((adjacent, oppose))

        #affichage de la carte
        oX,oY = newCollideLeft[0]
        for x,y in newCollideLeft[1:]:
            pygame.draw.line(self.screen,"blue", calculPosForCameraDisplay(oX, oY), calculPosForCameraDisplay(x, y))
            oX,oY = x,y
        pygame.draw.line(self.screen,"blue", calculPosForCameraDisplay(oX, oY), calculPosForCameraDisplay(newCollideLeft[0][0], newCollideLeft[0][1]))

        oX,oY = newCollideRight[0]
        for x,y in newCollideRight[1:]:
            pygame.draw.line(self.screen,"red", calculPosForCameraDisplay(oX, oY), calculPosForCameraDisplay(x, y))
            oX,oY = x,y
        pygame.draw.line(self.screen,"red", calculPosForCameraDisplay(oX, oY), calculPosForCameraDisplay(newCollideRight[0][0], newCollideRight[0][1]))