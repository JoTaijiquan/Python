#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(100, 10)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ScreenRes = (640, 480)

FPS = 30
fpsClock = pygame.time.Clock()

DISP = pygame.display.set_mode(ScreenRes)
pygame.display.set_caption('Ghost9')

GhostImg = pygame.image.load('ghost.png').convert()
GhostImg.set_colorkey(BLACK)
GhostX = 100
GhostY = 100
RecGhost = GhostImg.get_rect()

GhostBlueImg = pygame.image.load('ghostblue.png').convert()
GhostBlueImg.set_colorkey(BLACK)
GhostBlueX = 10
GhostBlueY = 10
RecGhostBlue = GhostBlueImg.get_rect()
direction = 'right'

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

    elif key[pygame.K_F10]:
        pygame.event.post(QUIT)


    if direction == 'right':
        GhostBlueX += 5
        if GhostBlueX > 600:
            direction = 'down'
    elif direction == 'down':
        GhostBlueY += 5
        if GhostBlueY > 450:
            direction = 'left'
    elif direction == 'left':
        GhostBlueX -= 5
        if GhostBlueX < 10:
            direction = 'up'
    elif direction == 'up':
        GhostBlueY -= 5
        if GhostBlueY < 10:
            direction = 'right'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    RecGhost.topleft = (GhostX, GhostY)
    RecGhostBlue.topleft = (GhostBlueX, GhostBlueY)

    Is_Hit = RecGhost.colliderect(RecGhostBlue)
    if Is_Hit == True:
        GhostBlueX = random.randint(0, 600)
        GhostBlueY = random.randint(0, 450)

    DISP.fill(WHITE)
    DISP.blit(GhostImg, RecGhost)
    DISP.blit(GhostBlueImg, RecGhostBlue)
    pygame.display.update()
    fpsClock.tick(FPS)

'''
Ghost #9
คราวนี้ลองทำให้ผีน้ำเงินวิ่งไปวิ่งมาเองได้
'''