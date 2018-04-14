#!/usr/bin/env python
# coding=utf-8

import sys

import pygame
from pygame.locals import *

pygame.init()

myfont = pygame.font.Font(None, 60)

white = 255, 255, 255
blue = 0, 0, 200

textImage = myfont.render("Hello Pygame", True, white)
screen = pygame.display.set_mode((600, 500))
# pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            # pygame.quit()
            sys.exit()

    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()
