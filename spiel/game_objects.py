import pygame, random

class Player:
    score_value=0
    
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
        #set star duration(frames)
        self.star_duration=2500
        #randomize coordinates
        self.x=random.randint(self.size, self.width-self.size)
        self.y=random.randint(self.size, self.height-self.size)
        #star color
        self.r=0
        self.g=0
        self.b=0
        self.color_change=10
        #score
        self.textX=10
        self.textY=10
        self.font=pygame.font.Font("freesansbold.ttf",32)
                
        #player type
        self.type=type
        #default player properties
        #give points based on player color and propery
        if type=="white":
            self.color=255,255,255
            self.hit_p=1
            self.cords=1300,20
            self.cost=0
            self.btn=""
        if type=="red":
            self.color=255,0,0
            self.hit_p=2
            self.cords=1300,80
            self.cost=5
            self.btn="1"
        if type=="blue":
            self.color=0,255,0
            self.hit_p=4
            self.cords=1300,140
            self.cost=7.5
            self.btn="2"
        if type=="green":
            self.color=0,0,255
            self.hit_p=8
            self.cords=1300,200
            self.cost=10
            self.btn="3"
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
            self.cords=1300,260
            self.cost=20
            self.btn="q"
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
            self.cords=1300,320
            self.cost=30
            self.btn="w"
        if type=="bouncer":
            self.color=150,0,255
            self.hit_p=5
            self.size=10
            spdy=[4, -4]
            spdx=[8, -8]
            self.yspd=random.choice(spdy)
            self.xspd=random.choice(spdx)
            self.cords=1300,380
            self.cost=50
            self.btn="e"
        if type=="nuke":
            self.color=0,0,0
            self.size=300
            self.x=self.width/2
            self.y=self.height/2
            self.xspd=0
            self.yspd=0
            self.cords=1300,440
            self.cost=1
            self.btn="g"
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
            
    def bomb_drop(self):
        print("s")
    
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
        Player.score_value+=self.hit_p
        #play star soundtrack
        pygame.mixer.Sound.play(self.sounds[random.randint(0, len(self.sounds)-1)])
        
    def show_score(self, screen):
        score=self.font.render("Score: " + str(Player.score_value),True, (255,255,255))
        #text background
        pygame.draw.line(screen, (0,0,0), [10,25], [250,25], 34)
        screen.blit(score, (8,10))
    
    def show_price(self, screen):
        price=self.font.render(str(self.btn+" "+self.type+" ") + str(str(self.cost)+"$"),True, (255,255,255))
        screen.blit(price, (self.cords))
        
    #confirm there is sufficient money
    def validate_score(self):
        if Player.score_value-self.cost>0:
            Player.score_value-=self.cost
            return True
    
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