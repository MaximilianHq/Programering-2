import random
from re import X
import pygame

class Player:
    def __init__(self, x, y,):
        self.x=x
        self.y=y
        self.size=20
        self.speed=10
        self.xSpeed = 10
        self.ySpeed = 20
        self.width = 400
        self.height = 250

        self.r = 255
        self.g = 0
        self.b = 0                  

        
    def update(self):
        self.size+=self.speed
        if(self.size>=100 or self.size<=0):
            self.speed= -self.speed

    def flipDir(self, dir):
        if(dir=="x"):
            self.xSpeed = -self.xSpeed
        elif(dir=="y"):
            self.ySpeed = -self.ySpeed

    def move(self, player, moveSpeed):
        player += moveSpeed

    def randomColor(self):
        self.r = random.randint(-1, 256)
        self.g = random.randint(-1, 256)
        self.b = random.randint(-1, 256)
        

    def draw(self, screen):
        self.x += self.xSpeed
        self.y += self.ySpeed

        print(self.x)
        pygame.draw.circle(screen,(0, 0, 0),(self.x, self.y), self.size)
