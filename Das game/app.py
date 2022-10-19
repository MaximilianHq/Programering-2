import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((410,235))
bg=pygame.image.load("background.png").convert()
pygame.display.set_caption('K-OS')

#initiations
clock=pygame.time.Clock()
player=game_objects.Player("white")

splits=[]
splits.append(player)

DISPLAYSURF.blit(bg, (5, 5))
 
while True:
    
    for event in pygame.event.get():
        key=pygame.key.get_pressed()
        
        #user input
        if event.type == pygame.KEYDOWN:
            #default players
            if key[pygame.K_r]:
                player=game_objects.Player("red")
            elif key[pygame.K_g]:
                player=game_objects.Player("blue")
            elif key[pygame.K_b]:
                player=game_objects.Player("green")
            #special players
            elif key[pygame.K_s]:
                player=game_objects.Player("star")
                
            #add player to list
            splits.append(player)
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(120)
    
    for n in splits:
        #star update
        if n.rgb=="star":
            if n.star_d>0:
                n.star()
        #display players
        n.draw(DISPLAYSURF)
        #move players
        n.move("x")
        n.move("y")
        #when player hits border
        if(n.x > n.width-n.size or n.x < 0+n.size):
            n.flipDir("x")
            n.border_hit(DISPLAYSURF)
        #when player hits border
        if(n.y > n.height-n.size or n.y < 0+n.size):
            n.flipDir("y")
            n.border_hit(DISPLAYSURF)