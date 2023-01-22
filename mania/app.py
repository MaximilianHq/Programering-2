import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,640))

#initiations
clock=pygame.time.Clock()
player=game_objects.Player()

while True:
    key=pygame.key.get_pressed()
    #input detection
    for event in pygame.event.get():
        if key[pygame.K_a]:
            player.tap(1)
        if key[pygame.K_s]:
            player.tap(2)
        if key[pygame.K_k]:
            player.tap(3)
        if key[pygame.K_l]:
            player.tap(4)
        #generate notes
        if key[pygame.K_LEFT]:
            player.generate(1)
        if key[pygame.K_UP]:
            player.generate(2)
        if key[pygame.K_DOWN]:
            player.generate(3)
        if key[pygame.K_RIGHT]:
            player.generate(4)
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)
    
    player.update()

    DISPLAYSURF.fill((0,0,0))

    #display player
    player.draw(DISPLAYSURF)