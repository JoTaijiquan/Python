#Python3.6 + Pygame
# -*- coding: utf-8 -*-


import pygame, sys
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ghost2')

GhostImg = pygame.image.load('ghost.png')
GhostX = 100
GhostY = 100

while True:
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        GhostX = GhostX - 5
    elif key[pygame.K_RIGHT]:
        GhostX = GhostX + 5
    elif key[pygame.K_UP]:
        GhostY = GhostY - 5
    elif key[pygame.K_DOWN]:
        GhostY = GhostY + 5
    elif key[pygame.K_F10]:
        pygame.event.post(QUIT)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISP.blit(GhostImg, (GhostX, GhostY))
    pygame.display.update()

"""
Ghost #2
เพิ่มคำสั่งบังคับผีให้วิ่งไปมาตามแป้นลูกศรได้ แต่เวลาวิ่งมันดันแดงพืดซะงั้น
กด F10 เพื่อจบ
"""