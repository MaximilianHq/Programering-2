import pygame, sys, game_objects
from pygame.locals import QUIT

pygame.init()
#screen size
DISPLAYSURF = pygame.display.set_mode((400,250))
pygame.display.set_caption('Das Game')

#initiations
clock=pygame.time.Clock()
player=game_objects.Player(200, 150)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #clear window
    pygame.display.update()
    #update
    clock.tick(2)
    player.update()
    #display
    DISPLAYSURF.fill((255, 255, 255))
    player.draw(DISPLAYSURF)
    
    player.move(player.x, )