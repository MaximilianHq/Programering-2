import pygame, random, sys

class Player:
    
    def __init__(self):
        self.speed=1
        self.width=1280
        self.height=720
        self.multiplier=32
        self.dir="none"
        self.timer=0
        self.position=pygame.math.Vector2\
            (random.randint(0, 40)*self.multiplier, \
                random.randint(0, 22)*self.multiplier)
        self.cords=[]
        self.length=1
    
    #detect if snake collides with itself
        
    #toggle snake direction
    def direction(self, dir):
        #how far snake travels
        speed=32
        if self.dir=="none":
            self.speed=0
        if dir=="up" and self.dir!="down" or dir=="left" and self.dir!="right":
            self.speed=-speed
        if dir=="down" and self.dir!="up" or dir=="right" and self.dir!="left":
            self.speed=speed
        self.dir=dir
        
    def collide(self):
        #look for recurring coordinates
        for n,i in enumerate(self.cords):
            #if so, QUIT
            if self.cords[n]==pygame.math.Vector2(self.position.x, self.position.y):
                pygame.quit()
                sys.exit()
        #save previous coordinates
        self.cords.append(pygame.math.Vector2\
            (self.position.x, self.position.y))
            
    def delete(self, screen):
        if len(self.cords)>self.length+2:
            #delete last snake tile
            self.cords.pop(-len(self.cords))
            #overlap last snake tile
            pygame.draw.rect(screen,(0,0,0), pygame.Rect(self.cords[-len(self.cords)].x, \
                self.cords[-len(self.cords)].y, self.multiplier, self.multiplier))
        print(self.cords[-len(self.cords)]) #TODO self.cords[-2]=self.cords[-1]. börja längst bak! kolla bild
        
    #snake movement
    def move(self, screen):
        #keep snake moving
        if self.dir=="up" or self.dir=="down":
            self.position.y+=self.speed
        elif self.dir=="left" or self.dir=="right":
            self.position.x+=self.speed
        
    def update(self, screen):
        if self.dir!="none":
            if self.timer==0:
                Player.move(self, screen)
                #detect if snake collides with itself
                Player.collide(self)
                Player.delete(self, screen)
                #decide snake speed (higher values = slower movement)
                self.timer=15

            self.timer-=1

    def draw(self, screen):
        #snake border
        pygame.draw.rect(screen,(255,0,0), \
            pygame.Rect(self.position.x, self.position.y, \
                self.multiplier, self.multiplier))
        #snake
        pygame.draw.rect(screen,(255,255,255), \
            pygame.Rect(self.position.x+3, self.position.y+3, 26, 26))
        
class Loot:
    
    def __init__(self):
        self.width=1280
        self.height=720
        self.multiplier=32
        self.color=255,0,0
        self.position=pygame.math.Vector2\
            (random.randint(0, 40)*self.multiplier, \
                random.randint(0, 20)*self.multiplier)
        
    def draw(self, screen):
        pygame.draw.rect(screen,(self.color), \
            pygame.Rect(self.position.x, self.position.y, \
                self.multiplier, self.multiplier)) 