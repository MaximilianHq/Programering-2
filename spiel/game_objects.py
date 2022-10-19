import pygame, random

class Player:
    points=0
    
    #variables
    def __init__(self, type):
        self.size=30
        self.evospd=0.2
        #set random direction
        spdy=[0.1, -0.1]
        spdx=[0.2, -0.2]
        self.yspd=random.choice(spdy)
        self.xspd=random.choice(spdx)
        self.width=1280
        self.height=720
        
        self.star_duration=2500
        
        self.x=random.randint(self.size, self.width-self.size)
        self.y=random.randint(self.size, self.height-self.size)
        
        self.r=0
        self.g=0
        self.b=0
        self.color_change=10
                
        #player type
        self.type=type
        #default player properties
        #give points based on player color and propery
        if type=="white":
            self.color=255,255,255
            self.hit_p=1
        if type=="red":
            self.color=255,0,0
            self.hit_p=2
        if type=="blue":
            self.color=0,255,0
            self.hit_p=4
        if type=="green":
            self.color=0,0,255
            self.hit_p=8
        #special player properties
        if type=="star":
            self.hit_p=10
            spdy=[2, -2]
            spdx=[4, -4]
            self.yspd=random.choice(spdy)
            self.xspd=random.choice(spdx)
            #rainbow effect
            self._r = False
            self._g = False    
            self._b = True
        if type=="omega":
            self.color=0,0,0
            self.hit_p=100
            self.size=300
            self.x=self.width/2
            self.y=self.height/2
            spdy=[0.05, -0.05]
            spdx=[0.1, -0.1]
            self.yspd=random.choice(spdy)
            self.xspd=random.choice(spdx)
        if type=="bouncer":
            self.color=150,0,255
            self.hit_p=5
            self.size=10
            spdy=[4, -4]
            spdx=[8, -8]
            self.yspd=random.choice(spdy)
            self.xspd=random.choice(spdx)
            
        #sounds
        self.sounds = [pygame.mixer.Sound("./spiel/assets/boop.wav"), 
                       pygame.mixer.Sound("./spiel/assets/boop2.wav"),
                       pygame.mixer.Sound("./spiel/assets/boop3.wav")]
        self.star_sounds = [pygame.mixer.Sound("./spiel/assets/star.wav"),
                       pygame.mixer.Sound("./spiel/assets/star2.wav"),
                       pygame.mixer.Sound("./spiel/assets/star3.wav"),
                       pygame.mixer.Sound("./spiel/assets/star4.wav")]
     
    def star_sound(self):
        self.star_sound=pygame.mixer.Sound.play(self.star_sounds[random.randint(0, len(self.star_sounds)-1)])    
    #star rainbow colors
    def star_color(self):
        #RED CHECK
        if(self._r == False and self._g == False and self._b == True):
            if(self.r + self.color_change<= 255):
                self.r += self.color_change
            else:
                self._r = True
        elif(self._r == True and self._g == True):
            if(self.r - self.color_change>= 0):
                self.r -= self.color_change
            else:
                self._r = False

        #GREEN CHECK
        if(self._r == True and self._g == False and self._b == False) :
            if(self.g + self.color_change <= 255):
                self.g+=self.color_change
            else:
                self._g = True
        elif(self._b == True and self._g == True):
            if(self.g - self.color_change>= 0):
                self.g -= self.color_change
            else:
                self._g = False

        #BLUE CHECK
        if(self._r == False and self._g == True and self._b == False ):
            if(self.b + self.color_change<= 255):
                    self.b += self.color_change
            else:
                self._b = True
        elif(self._b == True and self._r == True):
            if(self.b - self.color_change>= 0):
                self.b -= self.color_change
            else:
                self._b = False
    
        self.color=self.r,self.g,self.b
    #star player properties
    def star(self):
        Player.star_color(self)
        #subtract duration
        self.star_duration-=1
        #"delete" star
        if self.star_duration==0:
            self.size=0
            self.yspd=0
            self.xspd=0
            #stop star sound
            self.star_sound.stop()
            
    #move function
    def move(self, dir):
        if dir=="x":
            self.x += self.xspd
        if dir=="y":
            self.y += self.yspd
            
    #set transformation coordinates / limits
    def flipDir(self, dir):
        #change direction on hit
        if(dir=="x"):
            self.xspd = -self.xspd
        if(dir=="y"):
            self.yspd = -self.yspd
            
        #give and display points based on color
        Player.points+=self.hit_p
        print(Player.points)
        #play star soundtrack
        pygame.mixer.Sound.play(self.sounds[random.randint(0, len(self.sounds)-1)])
        
    #draw up border when hit
    def border_hit(self, screen):
        #y top
        if self.y < 0+self.size:
            pygame.draw.line(screen, (self.color), [0, 0], [self.width, 0], 16)
        #x right
        if self.x > self.width-self.size:
            pygame.draw.line(screen, (self.color), [self.width, 0], [self.width, self.height], 20)
        #y bottom 
        if self.y > self.height-self.size:
            pygame.draw.line(screen, (self.color), [self.width, self.height], [0, self.height], 20)
        #x left 
        if self.x < 0+self.size:
            pygame.draw.line(screen, (self.color), [0, self.height], [0, 0], 16) 
 
    #player attributes
    def draw(self, screen):
        pygame.draw.circle(screen,(self.color),(self.x, self.y), self.size)