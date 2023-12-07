import pygame
from classGame import Game

#initialisation valeurs plateau
largeurEcran, hauteurEcran = (1280, 720)
#paramétrage de l'affichage
screen = pygame.display.set_mode((largeurEcran,hauteurEcran))

clock = pygame.time.Clock()
FPS = 60

isRunning = True

game = Game(screen)

while isRunning:

    clock.tick(FPS)
    #gestion des touches
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.QUIT: #fermeture de la page
            isRunning = False
    game.update()
    pygame.display.flip()

