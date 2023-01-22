import pygame, random, sys

class Player:
    points=0
    
    def __init__(self):
        self.speed=1
        self.size=35
        self.scrspd=26/2
        self.lnr=0
        self.delay=1
        
        self.border=[]
        self.border.append(pygame.math.Vector2(200, 500))
        self.border.append(pygame.math.Vector2(300, 500))
        self.border.append(pygame.math.Vector2(400, 500))
        self.border.append(pygame.math.Vector2(500, 500))
        
        self.note=[]
    
    def tap(self, b):
        for n,i in enumerate(self.note):
            margin=self.size*2
            math=self.border[0].y-margin<(self.border[0].y+self.note[n].y)/2<self.border[0].y+margin
            if b==1 and math and self.note[n].x==200:
                Player.points+=1
                self.note.pop(n)
            if b==2 and math and self.note[n].x==300:
                Player.points+=1
                self.note.pop(n)
            if b==3 and math and self.note[n].x==400:
                Player.points+=1
                self.note.pop(n)
            if b==4 and math and self.note[n].x==500:
                Player.points+=1
                self.note.pop(n)
                
    def generate(self, b):
        n1=pygame.math.Vector2(200, 50)
        n2=pygame.math.Vector2(300, 50)
        n3=pygame.math.Vector2(400, 50)
        n4=pygame.math.Vector2(500, 50)
        
        if b==1:
            self.note.append(n1)
        if b==2:
            self.note.append(n2)
        if b==3:
            self.note.append(n3)
        if b==4:
            self.note.append(n4)      
            
    def noting(self):
        file=open('mania/song1.txt')
        content=file.readlines()
        n=content[self.lnr]
        
        n1=pygame.math.Vector2(200, 50)
        n2=pygame.math.Vector2(300, 50)
        n3=pygame.math.Vector2(400, 50)
        n4=pygame.math.Vector2(500, 50)
        
        print(n)
        
        if n=="n1":
            self.note.append(n1)
        if n=="n2":
            self.note.append(n2)
        if n=="n3":
            self.note.append(n3)
        if n=="n4":
            self.note.append(n4)
            
        self.lnr+=2
        self.delay+=2
        
    def update(self):
        #move notes downward
        for n,i in enumerate(self.note):
            self.note[n].y+=self.scrspd
            
            #pop missed notes
            if self.note[n].y>600:
                self.note.pop(n)
                
        Player.noting(self)
                
        print(Player.points)
        
    def draw(self, screen):
        #display hit-area
        for n,i in enumerate(self.border):
            pygame.draw.circle(screen,(50,50,50),\
                (self.border[n].x ,self.border[n].y), self.size)
            pygame.draw.circle(screen,(0,0,0),\
                (self.border[n].x ,self.border[n].y), self.size-7)
        #display notes
        for n,i in enumerate(self.note):
            pygame.draw.circle(screen,(255,0,0),\
                (self.note[n].x ,self.note[n].y), self.size)