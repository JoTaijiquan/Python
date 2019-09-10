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
pygame.display.set_caption('Ghost8')

GhostImg = pygame.image.load('ghost.png').convert()
GhostImg.set_colorkey(BLACK)
GhostX = 100
GhostY = 100
RecGhost = GhostImg.get_rect()

GhostBlueImg = pygame.image.load('ghostblue.png').convert()
GhostBlueImg.set_colorkey(BLACK)
GhostBlueX = 200
GhostBlueY = 200
RecGhostBlue = GhostBlueImg.get_rect()

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

    if key[pygame.K_a]:
        GhostBlueX -= 5
    elif key[pygame.K_d]:
        GhostBlueX += 5
    elif key[pygame.K_w]:
        GhostBlueY -= 5
    elif key[pygame.K_s]:
        GhostBlueY += 5

    elif key[pygame.K_F10]:
        pygame.event.post(QUIT)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    RecGhost.topleft = (GhostX, GhostY)
    RecGhostBlue.topleft = (GhostBlueX, GhostBlueY)

    Is_Hit = RecGhost.colliderect(RecGhostBlue)
    if Is_Hit == True:
        GhostBlueX = random.randint(0, 600)
        GhostBlueY = random.randint(0, 420)

    DISP.fill(WHITE)
    DISP.blit(GhostImg, RecGhost)
    DISP.blit(GhostBlueImg, RecGhostBlue)
    pygame.display.update()
    fpsClock.tick(FPS)

'''
Ghost #8

ปรับปรุงความเร็วให้เพิ่มขึ้น ถ้าเกมที่มีภาพน้อยๆ จะยังเห็นไม่ชัดเจน
'''