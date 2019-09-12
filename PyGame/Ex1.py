#Python 3.6.5, Pygame 1.9.3 haha ad
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption('Hello World')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

"""
1. import pygame, sys
จากนี้ทุกโปรแกรมที่เขียนด้วย pygame เราจะต้องมีโค้ดบรรทัดนี้อยู่ด้วยเสมอ เพื่อเป็นการบอกภาษา python ว่าเราจะขอเอา pygame module และ sys module มาใช้

2. from pygame.locals import *
ปกติแล้ว การเรียกใช้โมดูลในภาษา python เราจะเขียนเป็น modulename.functionname() แต่เมื่อเราสั่ง from modulename import * จะทำให้เราเรียกชื่อฟังก์ชั่นในโมดูลนั้นได้โดยตรงโดยไม่ต้องใช้ชื่อ modulename. นำหน้า
ทีนี้บรทัดนี้เราจะ import เฉพาะในโมดูล pygame.locals เพราะใน pygame.locals เก็บค่าคงที่ที่มีประโยชน์สำหรับ pygame ไว้เยอะแยะ

3. pygame.init()
คำสั่งภาคบังคับสำหรับ pygame

4. DISP=pygame.display.setmode ((640,480))
กำหนดขนาดหน้าจอที่จะใช้ ให้กับตัวแปร DISP ซึ่งหลังจากนี้การอ้างถึงหน้าจอ เราจะใช้ตัวแปร DISP นี้แทน

5. pygame.display.set_caption ('Hello World')
ใส่ชื่อให้กับ window ที่สร้างขึ้น

"""
