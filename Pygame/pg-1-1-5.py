#Python 3.7.3
#Pygame 1.9.6
#Example PG-1-1-5

import pygame, sys
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Ghost Run"
FPS = 50
WHITE = (255, 255, 255)


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)

class Ghost:
    def LoadImage(self,img_name,x=0,y=0):
        self.img = pygame.image.load(img_name).convert_alpha()
        self.x = x
        self.y = y

def mainloop(View):
    ghostRED = Ghost()
    ghostRED.LoadImage("ghost.png",100,100)
    ghostBLUE = Ghost()
    ghostBLUE.LoadImage("ghostblue.png",200,200)

    fpsClock = pygame.time.Clock()
    while True:
        key = pygame.key.get_pressed()    
        if key[pygame.K_LEFT]:
            ghostRED.x -=5
        elif key[pygame.K_RIGHT]:
            ghostRED.x +=5
        elif key[pygame.K_UP]:
            ghostRED.y -=5
        elif key[pygame.K_DOWN]:
            ghostRED.y +=5

        if key[pygame.K_a]:
            ghostBLUE.x -= 5
        elif key[pygame.K_d]:
            ghostBLUE.x +=5
        elif key[pygame.K_w]:
            ghostBLUE.y -=5
        elif key[pygame.K_s]:
            ghostBLUE.y += 5

        if key[pygame.K_F10]:
            pygame.event.post(QUIT)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        View.fill(WHITE)
        View.blit(ghostRED.img, (ghostRED.x, ghostRED.y))
        View.blit(ghostBLUE.img, (ghostBLUE.x, ghostBLUE.y))
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    mainloop(app.view)

'''
Ghost #5
มีผีสองตัวบังคับให้วิ่งไปมาได้ ตัวสีแดงจะบังคับด้วยแป้นลูกศร ตัวสีน้ำเงินใช้คีย์ w-s a-d ในการบังคับทิศทาง สำหรับ osx เขียนแค่นี้จะบังคับผีสองตัวให้วิ่งพร้อมๆ กันได้
แต่บน pc มันอาจจะวิ่งได้ทีละตัว คือถ้าคนหนึ่งกดค้างไว้อีกคนจะกดไม่ได้ ต้องแก้ไขด้วยโปรแกรม Ex6-1
'''