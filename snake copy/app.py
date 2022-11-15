import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,720))
DISPLAYSURF.fill((50,50,50))

#initiations
clock=pygame.time.Clock()
player=game_objects.Player()
loot=game_objects.Loot()

food=[]
food.append(game_objects.Loot())

while True:
    key=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if key[pygame.K_w]:
            player.move("up")
        if key[pygame.K_s]:
            player.move("down")
        if key[pygame.K_a]:
            player.move("left")
        if key[pygame.K_d]:
            player.move("right")

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    player.update()
    for i,loot in enumerate(food):
        if player.size>player.x-loot.x>-player.size \
            and player.size>player.y-loot.y>-player.size:
            print("kjsdhf")
            player.shift()
            loot.color=0,0,0
            loot.draw(DISPLAYSURF)
            food.pop(i)
            
            food.append(game_objects.Loot())
            
    pygame.display.update()
    clock.tick(1000)

    #display player
    player.draw(DISPLAYSURF)
