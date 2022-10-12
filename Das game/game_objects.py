import pygame

class Player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.size=20
        self.evospd=1
        self.xspd=10
        self.yspd=10
        self.width=400
        self.height=250
        
        
    def update(self):
        self.size+=self.speed
        if(self.size>=15 or self.size<=0):
            self.speed=-self.speed
 
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 0, 0),(self.x, self.y), self.size)
        
    def flip_dir(self, ):
        
