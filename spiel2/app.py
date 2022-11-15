import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,720))

#initiations
clock=pygame.time.Clock()
player=game_objects.Player()

while True:
    key=pygame.key.get_pressed()
    
    for event in pygame.event.get():        
        if key[pygame.K_SPACE]:
            player.visibility()
        if key[pygame.K_b]:
            player.brush()
        if key[pygame.K_LSHIFT]:
            player.brush_size("+")
        if key[pygame.K_LCTRL]:
            player.brush_size("-")

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    if key[pygame.K_w]:
        player.move("up")
    if key[pygame.K_s]:
        player.move("down")
    if key[pygame.K_a]:
        player.move("left")
    if key[pygame.K_d]:
        player.move("right")
    if key[pygame.K_r]:
        DISPLAYSURF.fill((0,0,0))
            
    pygame.display.update()
    clock.tick(1000)

    #display player
    player.draw(DISPLAYSURF)
