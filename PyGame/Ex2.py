#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ghost1')

GhostImg = pygame.image.load('ghost.png')
GhostX = 100
GhostY = 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISP.blit(GhostImg, (GhostX, GhostY))
    pygame.display.update()

"""
    Ghost #1
    แสดงภาพผีหนึ่งตัวขึ้นมากลางจอ โผล่มาเฉยๆ งั้น ทำอะไรไม่ได้
"""
