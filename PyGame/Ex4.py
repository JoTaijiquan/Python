#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)

DISP = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ghost3')

GhostImg = pygame.image.load('ghost.png')
GhostX = 100
GhostY = 100

while True:
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        GhostX -= 2
    elif key[pygame.K_RIGHT]:
        GhostX += 2
    elif key[pygame.K_UP]:
        GhostY -= 2
    elif key[pygame.K_DOWN]:
        GhostY += 2
    elif key[pygame.K_F10]:
        pygame.event.post(QUIT)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISP.fill(0)
    DISP.blit(GhostImg, (GhostX, GhostY))
    pygame.display.update()

"""
Ghost#3
เพิ่ม background สีขาวไปก่อนจะวาดผีลงบนจอ ทำให้ไม่มีปื้นสีแดงๆละ
"""