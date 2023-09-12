#1a
import pygame
from pygame.locals import *
import sys

#1b
class ball():

#1c
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
    
        self.image = pygame.image.load('ball.jpeg')
#2
        ballRect = self.image.get_rect()

        self.maxWidth = windowWidth - self.width 

#3
        self.x = random.randrange(0, self.maxWidth)

#4
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)

#4  
    def update(self):
    
#5
    def draw(self):