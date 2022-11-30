import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,640))

#initiations
clock=pygame.time.Clock()
player=game_objects.Player()
loot=game_objects.Loot()

food=[]
food.append(game_objects.Loot())

while True:
    key=pygame.key.get_pressed()
    #input detection
    for event in pygame.event.get():
        if key[pygame.K_w]:
            player.direction("up")
        if key[pygame.K_s]:
            player.direction("down")
        if key[pygame.K_a]:
            player.direction("left")
        if key[pygame.K_d]:
            player.direction("right")
 #TODO detect any key press and in dir == "none" move always right
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #detect if snake collides with LOOT
    for i,loot in enumerate(food):
        if player.snake_head==loot.position:
            loot.color=0,0,0
            food.pop(i)
            food.append(game_objects.Loot()) #TODO mat spawnar i snake !
            player.grow()
        loot.draw(DISPLAYSURF)
            
    pygame.display.update()
    clock.tick(60)

    if player.timer==0:
        DISPLAYSURF.fill((0,0,0))
        player.update()
        player.timer=15
        print(player.snake)
    player.timer-=1

    #display player
    player.draw(DISPLAYSURF)


    