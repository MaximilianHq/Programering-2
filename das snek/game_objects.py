import pygame, random

class Player:
    
    def __init__(self):
        self.speed=1
        self.width=1280
        self.height=720
        self.multiplier=32
        self.x=random.randint(0, 40)*self.multiplier
        self.y=random.randint(0, 22)*self.multiplier
        self.dir="none"
        
    def move(self, dir):
        speed=32
        if self.dir=="none":
            self.speed=0
        if dir=="up" and self.dir!="down" or dir=="left" and self.dir!="right":
            self.speed=-speed
        if dir=="down" and self.dir!="up" or dir=="right" and self.dir!="left":
            self.speed=speed
        self.dir=dir
        
    def update(self):
        pygame.time.Clock().tick(5)
        #keep snake moving
        if self.dir=="up" or self.dir=="down":
            self.y+=self.speed
        elif self.dir=="left" or self.dir=="right":
            self.x+=self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen,(255,255,255), \
            pygame.Rect(self.x+3, self.y+3, 26, 26))    
    def draw_border(self, screen):
        pygame.draw.rect(screen,(255,0,0), \
            pygame.Rect(self.x, self.y, self.multiplier, self.multiplier))
        
class Loot:
    
    def __init__(self):
        self.width=1280
        self.height=720
        self.multiplier=32
        self.x=random.randint(0, 40)*self.multiplier
        self.y=random.randint(0, 20)*self.multiplier
        
    def draw(self, screen):
        pygame.draw.rect(screen,(255,0,0), \
            pygame.Rect(self.x, self.y, self.multiplier, self.multiplier)) 