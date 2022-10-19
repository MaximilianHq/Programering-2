import pygame, sys, game_objects, random
from pygame.locals import QUIT

pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((1280,720))
bg=pygame.image.load("./spiel/assets/background.png").convert()
pygame.display.set_caption('K-OS')

#initiations
clock=pygame.time.Clock()
player=game_objects.Player("white")

splits=[]
splits.append(player)

DISPLAYSURF.blit(bg, (8, 8))
 
while True:
    
    for event in pygame.event.get():
        key=pygame.key.get_pressed()
        
        #user input
        if event.type == pygame.KEYDOWN:
            #default players
            if key[pygame.K_1]:
                player=game_objects.Player("red")
            elif key[pygame.K_2]:
                player=game_objects.Player("blue")
            elif key[pygame.K_3]:
                player=game_objects.Player("green")
            #special players
            elif key[pygame.K_q]:
                player=game_objects.Player("star")
                player.star_sound()
            elif key[pygame.K_w]:
                player=game_objects.Player("omega")
            elif key[pygame.K_e]:
                player=game_objects.Player("bouncer")
                
            #add player to list
            splits.append(player)
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(1000)
    
    for n in splits:
        #star update
        if n.type=="star":
            if n.star_duration>0:
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