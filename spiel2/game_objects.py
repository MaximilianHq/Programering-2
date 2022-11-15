from tkinter import W
import pygame, random

class Player:

    def __init__(self):
        self.size=30
        self.width=1280
        self.height=720
        self.speed=0.5
        self.x=self.width/2
        self.y=self.height/2
        self.color=255,255,255
        self.toggle=1
        self.brushes="circle"
        
    def move(self, dir):
        if dir=="up" and self.y-self.size>=0:
            self.y-=self.speed
        if dir=="down" and self.size+self.y<=self.height:
            self.y+=self.speed
        if dir=="left" and self.x-self.size>=0:
            self.x-=self.speed
        if dir=="right" and self.size+self.x<=self.width:
            self.x+=self.speed
    
    def visibility(self):
        if self.toggle==1:
            self.color=0,0,0
            self.toggle=-self.toggle
        elif self.toggle==-1:
            self.color=255,255,255
            self.toggle=-self.toggle

    def brush_size(self, s):
        size=7.5
        if s=="+" and self.size<90:
            self.size+=size
        if s=="-" and self.size>size:
            self.size-=size
            
    def brush(self):
        if self.brushes=="circle":
            self.brushes="square"
        if self.brushes=="square":
            self.brushes="circle"
                
    def draw(self, screen):
        if self.brushes=="circle":
            pygame.draw.circle(screen,(self.color),(self.x, self.y), self.size)
        if self.brushes=="square": #TODO fix rect
            pygame.draw.rect(screen, (0,0,0), pygame.Rect[100,100,100,100])