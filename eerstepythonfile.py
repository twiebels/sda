#python code template

#1a
import pygame
from pygame.locals import *
import sys

#2
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#3
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4
pygame.image.load('ball.jpeg')

#5


#6
while True:
    #7
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #9

    window.fill(BLACK)

    #10
    #11
    pygame.display.update()

    #12
    clock.tick(FRAMES_PER_SECOND)