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

#TODO skapa array med delar av kroppen se bild

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
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #detect if snake collides with LOOT
    for i,loot in enumerate(food):
        if player.position.x==loot.position.x and \
            player.position.y==loot.position.y: #TODO position==position
            loot.color=0,0,0
            food.pop(i)
            food.append(game_objects.Loot())
            loot.locations=[]
            player.length+=1
        loot.draw(DISPLAYSURF)
            
    pygame.display.update()
    clock.tick(60)#TODO gör mig till rätt tick
    player.update(DISPLAYSURF)

    #display player
    player.draw_border(DISPLAYSURF)
    player.draw(DISPLAYSURF)