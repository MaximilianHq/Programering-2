import pygame, random

class Player:
    
    #variables
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.size=19
        self.evospd=0.1
        self.yspd=1
        self.xspd=2
        self.width=400
        self.height=250
        
        self.r=0
        self.g=0
        self.b=0
        
        self.crash_sound = pygame.mixer.Sound("boop.wav")
        
    #player transformation
    def update(self):
        self.size += self.evospd
        if(self.size >= 20 or self.size <= 17.5):
            self.evospd = -self.evospd
            
    #move function
    def move(self, dir):
        if dir=="x":
            self.x += self.xspd
        if dir=="y":
            self.y += self.yspd
            
    #set transformation coordinates / limits
    def flipDir(self, dir):
        if(dir=="x"):
            self.xspd = -self.xspd
        elif(dir=="y"):
            self.yspd = -self.yspd
        
        pygame.mixer.Sound.play(self.crash_sound)
        
    #light up border when hit
    def border_hit(self, screen):
        rgbr=self.r, self.g, self.b
        #y top
        if self.y < 0+self.size:
            pygame.draw.line(screen, (rgbr), [0, 0], [self.width, 0], 10)
        #x right
        elif self.x > self.width-self.size:
            pygame.draw.line(screen, (rgbr), [self.width, 0], [self.width, self.height], 10)
        #y bottom 
        elif self.y > self.height-self.size:
            pygame.draw.line(screen, (rgbr), [self.width, self.height], [0, self.height], 10)
        #x left 
        elif self.x < 0+self.size:
            pygame.draw.line(screen, (rgbr), [0, self.height], [0, 0], 10) 
         
    #randomize rgb values   
    def color_shift(self, n):
        if n=="true":
            self.r=random.randint(0,255)
            self.g=random.randint(0,255)
            self.b=random.randint(0,255)
 
    #player attributes
    def draw(self, screen):
        pygame.draw.circle(screen,(self.r, self.g, self.b),(self.x, self.y), self.size)