import pygame, random

class Player:
    
    
    #variables
    def __init__(self, rgb):
        self.size=19
        self.evospd=0.2
        self.speed = 30
        spdy=[0.5, -0.5]
        spdx=[1, -1]
        self.yspd=random.choice(spdy)
        self.xspd=random.choice(spdx)
        self.width=410
        self.height=235
        
        self.star_d=1000
        
        self.x=random.randint(self.size, self.width-self.size)
        self.y=random.randint(self.size, self.height-self.size)
        
        self.rgb=rgb
        if rgb=="white":
            self.color=255,255,255
            self.give_p=0
        if rgb=="red":
            self.color=255,0,0
            self.give_p=1
        if rgb=="blue":
            self.color=0,255,0
            self.give_p=2
        if rgb=="green":
            self.color=0,0,255
            self.give_p=3
        if rgb=="star":
            self.color=0,0,0
            self.give_p=5
            spdy=[5, -5]
            spdx=[10, -10]
            self.yspd=random.choice(spdy)
            self.xspd=random.choice(spdx)
            
        
        self.sounds = [pygame.mixer.Sound("boop.wav"), 
                       pygame.mixer.Sound("boop2.wav"),
                       pygame.mixer.Sound("boop3.wav")]
        
    def star(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        self.color=r,g,b
        
        self.star_d-=1

        if self.star_d==0:
            self.size=0
            self.yspd=0
            self.xspd=0
            
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
        if(dir=="y"):
            self.yspd = -self.yspd
            
        #give and display points based on color
        Player.points+=self.give_p
        print(Player.points)
        
        
        pygame.mixer.Sound.play(self.sounds[random.randint(0, len(self.sounds)-1)])
        
    #light up border when hit
    def border_hit(self, screen):
        #y top
        if self.y < 0+self.size:
            pygame.draw.line(screen, (self.color), [0, 0], [self.width, 0], 8)
        #x right
        if self.x > self.width-self.size:
            pygame.draw.line(screen, (self.color), [self.width, 0], [self.width, self.height], 12)
        #y bottom 
        if self.y > self.height-self.size:
            pygame.draw.line(screen, (self.color), [self.width, self.height], [0, self.height], 12)
        #x left 
        if self.x < 0+self.size:
            pygame.draw.line(screen, (self.color), [0, self.height], [0, 0], 8) 
 
    #player attributes
    def draw(self, screen):
        pygame.draw.circle(screen,(self.color),(self.x, self.y), self.size)