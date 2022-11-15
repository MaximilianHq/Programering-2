import pygame, random

class Player:

    def __init__(self):
        self.size=30
        self.width=1280
        self.height=720
        self.speed=0
        self.mspeed=0.3
        self.x=self.width/2
        self.y=self.height/2
        self.color=255,255,255
        self.dir="right"
        self.dir_toggle=1
        
    def move(self, dir):
        #set directional velocity
        self.mspeed+=0.05
        self.dir=dir
        if dir=="up" or dir=="left":
            self.speed=-self.mspeed
        if dir=="down" or dir=="right":
            self.speed=self.mspeed
            
    def animation(self):
        multi=0.1
        if self.dir=="up" and self.dir_toggle>=0 or self.dir=="down" and self.dir_toggle>=0:
            self.x+=multi
            self.dir_toggle+=1
        if self.dir=="up" and self.dir_toggle<0 or self.dir=="down" and self.dir_toggle<0:
            self.x-=multi
            self.dir_toggle+=1
        if self.dir=="left" and self.dir_toggle>=0 or self.dir=="right" and self.dir_toggle>=0:
            self.y+=multi
            self.dir_toggle+=1
        if self.dir=="left" and self.dir_toggle<0 or self.dir=="right" and self.dir_toggle<0:
            self.y-=multi
            self.dir_toggle+=1
            
        if self.dir_toggle>75:
            self.dir_toggle=-self.dir_toggle

    def update(self):
        #keep snake moving
        if self.dir=="up" or self.dir=="down":
            self.y+=self.speed
        elif self.dir=="left" or self.dir=="right":
            self.x+=self.speed
        #if border is hit
        if self.dir=="up" and self.y-self.size<=0 \
            or self.dir=="down" and self.size+self.y>=self.height \
            or self.dir=="left" and self.x-self.size<=0 \
            or self.dir=="right" and self.size+self.x>=self.width:
            pygame.quit()
            print("GAME OVER")
            
        self.animation()
    
    def shift(self):
        r=random.randint(0,256)
        g=random.randint(0,256)
        b=random.randint(0,256)
        self.color=r,g,b
        
    def draw(self, screen):
        pygame.draw.circle(screen,(self.color),(self.x, self.y), self.size)

class Loot:
    def __init__(self):
        self.size=30
        self.width=1280
        self.height=720
        self.x=random.randint(0+self.size, self.width-self.size)
        self.y=random.randint(0+self.size, self.height-self.size)
        self.color=255,0,0
        self.timer=1000

    def draw(self, screen):
        pygame.draw.circle(screen,(self.color),(self.x, self.y), self.size)
        self.timer-=1