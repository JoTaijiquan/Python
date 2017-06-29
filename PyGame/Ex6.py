#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
ScreenRes = (640, 480)

FPS = 30
fpsClock = pygame.time.Clock()

DISP = pygame.display.set_mode(ScreenRes)
pygame.display.set_caption('Ghost5')

GhostImg = pygame.image.load('ghost.png')
GhostX = 100
GhostY = 100

GhostBlueImg = pygame.image.load('ghostblue.png')
GhostBlueX = 200
GhostBlueY = 200

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

    DISP.fill(WHITE)
    DISP.blit(GhostImg, (GhostX, GhostY))
    DISP.blit(GhostBlueImg, (GhostBlueX, GhostBlueY))
    pygame.display.update()
    fpsClock.tick(FPS)

'''
Ghost #5
มีผีสองตัวบังคับให้วิ่งไปมาได้ ตัวสีแดงจะบังคับด้วยแป้นลูกศร ตัวสีน้ำเงินใช้คีย์ w-s a-d ในการบังคับทิศทาง สำหรับ osx เขียนแค่นี้จะบังคับผีสองตัวให้วิ่งพร้อมๆ กันได้
แต่บน pc มันอาจจะวิ่งได้ทีละตัว คือถ้าคนหนึ่งกดค้างไว้อีกคนจะกดไม่ได้ ต้องแก้ไขด้วยโปรแกรม Ex6-1
'''