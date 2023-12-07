import pygame

CollideLeft = [(565,542),(875,542),(975,485),(1010,424),(1010,330),(944,176),(860,163),(799,204),(749,299),(638,335),(518,299),(400,209),(276,161),(215,169),(204,205),(270,440),(395,522)]
CollideRight = [(570,650),(918,630),(1074,522),(1115,408),(1081,228),(993,119),(879,94),(756,129),(674,205),(625,220),(433,112),(278,60),(145,76),(85,224),(172,520),(283,583)]

class Road:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

    def showMinimap(self):
        oX,oY = CollideLeft[0]
        for x,y in CollideLeft[1:]:
            pygame.draw.line(self.screen,"black", (oX/4, oY/4), (x/4, y/4))
            oX,oY = x,y
        pygame.draw.line(self.screen,"black", (oX/4, oY/4), (CollideLeft[0][0]/4, CollideLeft[0][1]/4))
        

        oX,oY = CollideRight[0]
        for x,y in CollideRight[1:]:
            pygame.draw.line(self.screen,"black", (oX/4, oY/4), (x/4, y/4))
            oX,oY = x,y
        pygame.draw.line(self.screen,"black", (oX/4, oY/4), (CollideRight[0][0]/4, CollideRight[0][1]/4))

        #draw car
        pygame.draw.circle(self.screen, "red", (self.game.player.coords[0]/4, self.game.player.coords[1]/4), 3)

        #draw caméra
        pygame.draw.circle(self.screen, "blue", (self.game.camera.coords[0]/4, self.game.camera.coords[1]/4), 3)



        



