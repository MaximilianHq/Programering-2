import pygame, random, sys

class Player:
    
    def __init__(self):
        self.speed=1
        self.width=1280
        self.height=640
        self.multiplier=32
        self.dir="none"
        self.timer=0
        self.length=1

        #TODO skapa array med delar av kroppen
        self.snake=[]
        coord=pygame.math.Vector2
        self.snake.append(coord(32*20, 32*11))
        self.snake.append(coord(32*19, 32*11))
        self.snake.append(coord(32*18, 32*12))
        self.snake_head=self.snake[0]#first
        self.snake_tail=self.snake[-1]#last
  
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
        
        #TODO den kan fortfarande döda sigsjälv. Måste se till att rörelse sker på bild så att den inte  togglar riktning 2 ggr
        
    #snake movement
    def move(self):
        #move body
        v=len(self.snake)-1
        for n in range(0, v):
            self.snake[v-n].x=self.snake[v-n-1].x
            self.snake[v-n].y=self.snake[v-n-1].y
        #move snake head
        if self.dir=="up" or self.dir=="down":
            self.snake_head.y+=self.speed
        elif self.dir=="left" or self.dir=="right":
            self.snake_head.x+=self.speed

    #grow snake
    def grow(self):
        #spawn new tile at snake end
        xy=self.snake[len(self.snake)-1].x, self.snake[len(self.snake)-1].y
        self.snake.append(pygame.math.Vector2(xy))

    #snake collision
    def crash(self):
        x=self.snake_head.x
        y=self.snake_head.y
        kill=False
        #body impact
        c=self.snake.count(self.snake_head)
        #whilst head coordinates are only detected one time
        if c>1:
            kill=True
        #wall impact
        elif x<0 or y<0 or x>self.width-self.multiplier \
            or y>self.height-self.multiplier:
            kill=True
        if kill==True:
            pygame.quit()
            sys.exit()

    def update(self):
        if self.dir!="none":
            Player.move(self)
            Player.crash(self)

    #draw snake
    def draw(self, screen):
        for n,i in enumerate(self.snake):
            #snake border
            pygame.draw.rect(screen,(255,0,0), \
                pygame.Rect(self.snake[n].x, self.snake[n].y, \
                    self.multiplier, self.multiplier))
            #snake
            pygame.draw.rect(screen,(255,255,255), \
                pygame.Rect(self.snake[n].x+3, self.snake[n].y+3, 26, 26))
            
class Loot:
    
    def __init__(self):
        self.width=1280
        self.height=720
        self.multiplier=32
        self.color=255,0,0
        x=random.randint(0, 40)*self.multiplier
        y=random.randint(0, 20)*self.multiplier
        self.position=pygame.math.Vector2(x, y)
        
    #draw food
    def draw(self, screen):
        pygame.draw.rect(screen,(self.color), \
            pygame.Rect(self.position.x, self.position.y, \
                self.multiplier, self.multiplier)) 