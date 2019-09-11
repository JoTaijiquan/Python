#Python 3.7.3
#Pygame 1.9.6
#Example PG-1-1-8

import pygame, sys,random
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Ghost Run"
FPS = 50
WHITE = (255, 255, 255)
BLACK = (0,0,0)

class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(100, 10)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)

class Ghost:
    def LoadImage(self,img_name,x=0,y=0):
        self.img = pygame.image.load(img_name).convert_alpha()
        self.img.set_colorkey(BLACK)

        self.x = x
        self.y = y
        self.ox = x
        self.oy = y
        self.rect = self.img.get_rect()
        self.rect[0] =x
        self.rect[1] =y


def mainloop(View):
    #width = View.get_width()
    #height = View.get_height()
    width,height = View.get_size()

    ghostRED = Ghost()
    ghostRED.LoadImage("ghost.png",500,500)
    ghostBLUE = Ghost()
    ghostBLUE.LoadImage("ghostblue.png",200,200)
    wall = Ghost()
    wall.LoadImage("wall.png",300,300)

    fpsClock = pygame.time.Clock()
    while True:
        ghostRED.ox = ghostRED.rect[0]
        ghostRED.oy = ghostRED.rect[1]

        key = pygame.key.get_pressed()    
        if key[pygame.K_LEFT]:
            ghostRED.rect[0] -=5
        elif key[pygame.K_RIGHT]:
            ghostRED.rect[0] +=5
        elif key[pygame.K_UP]:
            ghostRED.rect[1] -=5
        elif key[pygame.K_DOWN]:
            ghostRED.rect[1] +=5

        if key[pygame.K_a]:
            ghostBLUE.rect[0] -=5
        elif key[pygame.K_d]:
            ghostBLUE.rect[0] +=5
        elif key[pygame.K_w]:
            ghostBLUE.rect[1] -=5
        elif key[pygame.K_s]:
            ghostBLUE.rect[1] +=5
        
        if key[pygame.K_F10]:
            pygame.event.post(QUIT)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #ghostRED.rect.topleft = (ghostRED.x,ghostRED.y)
        #ghostBLUE.rect.topleft = (ghostBLUE.x,ghostBLUE.y)
        #wall.rect.topleft = (wall.x,wall.y)

        is_Hit = ghostRED.rect.colliderect(ghostBLUE.rect)
        if is_Hit==True:
            ghostBLUE.rect[0] = random.randint(0,width)
            ghostBLUE.rect[1] = random.randint(0,height)


        is_Wall = ghostRED.rect.colliderect(wall.rect)
        if is_Wall == True:
            ghostRED.rect[0] = ghostRED.ox
            ghostRED.rect[1] = ghostRED.oy

        View.fill(WHITE)
        View.blit(wall.img,wall.rect)
        View.blit(ghostRED.img, ghostRED.rect)
        View.blit(ghostBLUE.img, ghostBLUE.rect)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    mainloop(app.view)

'''
เพิ่มหลายคำสั่งเลย รวมทั้งมี import random เพิ่มขึ้นด้วย
โปรแกรมนี้ ถ้าผีวิ่งชนกัน ตัวสีน้ำเงินจะเด้งออกไป
'''