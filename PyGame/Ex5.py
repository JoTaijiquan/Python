#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)

FPS = 30
fpsClock = pygame.time.Clock()

DISP = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ghost4')

GhostImg = pygame.image.load('ghost.png')
GhostX = 100
GhostY = 100

while True:
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        GhostX -= 5
    elif key[pygame.K_RIGHT]:
        GhostX += 5
    elif key[pygame.K_UP]:
        GhostY -= 5
    elif key[pygame.K_DOWN]:
        GhostY += 5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISP.fill(WHITE)
    DISP.blit(GhostImg, (GhostX, GhostY))
    pygame.display.update()
    fpsClock.tick(FPS)

"""
    Ghost#4
    เพิ่มการปรับอัตราการวาดบนหน้าจอ ลองปรับค่า FPS=30 เป็นค่าอื่นๆ ดู
"""