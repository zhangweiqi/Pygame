#!/usr/bin/env python
# coding=utf-8

import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")

myfont = pygame.font.Font(None, 60)

white = 255, 255, 255
blue = 0, 0, 200
yellow = 255, 255, 0

position = 300, 250
radius = 100
width = 10

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

# pygame.draw.circle(screen, yellow, position, radius, width)

# textImage = myfont.render("Hello Pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            # pygame.quit()
            sys.exit()

    screen.fill(blue)

    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    # screen.blit(textImage, (100, 100))
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, yellow, pos, width)

    pygame.display.update()
