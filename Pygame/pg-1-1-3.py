#Python 3.7.3
#Pygame 1.9.6
#Example PG-1-1-3

import pygame, sys
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Ghost Run"
FPS = 50

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)

class Ghost:
    def LoadImage(self,img_name,x=0,y=0):
        self.img = pygame.image.load(img_name)
        self.x = x
        self.y = y

def mainloop(View):
    ghost1 = Ghost()
    ghost1.LoadImage("plane.png",100,100)
    fpsClock = pygame.time.Clock()

    while True:
        key = pygame.key.get_pressed()    
        if key[pygame.K_LEFT]:
            ghost1.x -=5
        elif key[pygame.K_RIGHT]:
            ghost1.x +=5
        elif key[pygame.K_UP]:
            ghost1.y -=5
        elif key[pygame.K_DOWN]:
            ghost1.y +=5
            
        if key[pygame.K_F10]:
            pygame.event.post(QUIT)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        View.blit(ghost1.img, (ghost1.x, ghost1.y))
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    mainloop(app.view)

"""
Ghost #2
เพิ่มคำสั่งบังคับผีให้วิ่งไปมาตามแป้นลูกศรได้ แต่เวลาวิ่งมันดันแดงพืดซะงั้น

self.view = pygame.display.set_mode(SCREEN_SIZE,0,32)
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
