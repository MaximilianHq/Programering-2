import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,720))

#initiations
clock=pygame.time.Clock()
player=game_objects.Player()
player_border=game_objects.Player()
loot=game_objects.Loot()

body=[]
body.append(player)
body_border=[]
body_border.append(player)

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
            
    for i,loot in enumerate(food):
        if player.x==loot.x and player.y==loot.y:
            loot.color=0,0,0
            food.pop(i)
            food.append(game_objects.Loot())
            loot.locations=[]
        loot.draw(DISPLAYSURF)
            
    pygame.display.update()
    clock.tick(60)
    
    player.update()

    #display player
    player.draw_border(DISPLAYSURF)
    player.draw(DISPLAYSURF)