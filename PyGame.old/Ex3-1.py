#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((640, 480),0,32)
pygame.display.set_caption('Ghost2')

GhostImg = pygame.image.load('ghost.png').convert_alpha()
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

DISP = pygame.display.set_mode((640, 480),0,32)
0 (default) flag มี option ดังนี้
    FULLSCREEN  แสดงผลเต็มจอ
    DOUBLEBUF   ใช้ร่วมกับ HWSURFACE หรือ OPENGL
    HWSURFACE   ให้ hardware accelerated ใช้ร่วมกับ FULLSSCREEN
    OPENGL      ใช้ระบบ openGL
    RESIZABLE   
    NOFRAME
    ใช้ร่วมกันได้ เช่น FULLSCREEN | HWSURFACE
32  Bit depth มี 8,15,16,24,32

คำสั่ง pygame.image.load('ghost.png') จะเลือกชนิดไฟล์ภาพโดยอัตโนมัต

pygame.image.load('ghost.png').convert() จะเป็นการ copy surface มา ทำให้วาดได้เร็วขึ้น

pygame.image.load('ghost.png').convert_alpha() สำหรับ .png เพื่อทำ transparency


"""