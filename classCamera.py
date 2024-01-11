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
        self.distanceWithCar = 50
        



                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        
        
        self.coords = self.game.player.coords[0] - math.cos(self.game.player.angle)*self.distanceWithCar, self.game.player.coords[1] + math.sin(self.game.player.angle)*self.distanceWithCar

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
            pygame.draw.line(self.screen,(99, 84, 44), self.game.calculPosForCameraDisplay(oX, oY), self.game.calculPosForCameraDisplay(x, y), 5)
            oX,oY = x,y
        pygame.draw.line(self.screen,(99, 84, 44), self.game.calculPosForCameraDisplay(oX, oY), self.game.calculPosForCameraDisplay(newCollideLeft[0][0], newCollideLeft[0][1]),5)

        oX,oY = newCollideRight[0]
        for x,y in newCollideRight[1:]:
            pygame.draw.line(self.screen,(99, 84, 44), self.game.calculPosForCameraDisplay(oX, oY), self.game.calculPosForCameraDisplay(x, y),5)
            oX,oY = x,y
        pygame.draw.line(self.screen,(99, 84, 44), self.game.calculPosForCameraDisplay(oX, oY), self.game.calculPosForCameraDisplay(newCollideRight[0][0], newCollideRight[0][1]),5)