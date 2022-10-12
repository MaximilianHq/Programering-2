import pygame, sys
from pygame.locals import QUIT

import game_objects

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
    clock.tick(15)
    #player.update()
    DISPLAYSURF.fill((255, 255, 255))
    #display
    player.draw(DISPLAYSURF)

    player.move(player.x, player.xSpeed)
    player.move(player.y, player.ySpeed)

    if(player.x > player.width-player.size or player.x < 0+player.size):
        player.flipDir("x")
        player.randomColor()
    
    if(player.y > player.height-player.size or player.y < 0+player.size):
        player.flipDir("y")
        player.randomColor()