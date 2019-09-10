#Python 3.7.3
#Pygame 1.9.6
#Example PG-1-1-2

import pygame, sys
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "One Ghost"

def init():
    pygame.init()
    pygame.display.set_caption(SCREEN_CAPTION)
    return pygame.display.set_mode(SCREEN_SIZE) 

class Ghost:
    def LoadImage(self,img_name,x=0,y=0):
        self.img = pygame.image.load(img_name)
        self.x = x
        self.y = y

def mainloop(View):
    ghost1 = Ghost()
    ghost1.LoadImage("ghost.png",100,100)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        View.blit(ghost1.img, (ghost1.x, ghost1.y))
        pygame.display.update()

if __name__ == "__main__":
    View = init()
    mainloop(View)

"""
    Ghost #1
    แสดงภาพผีหนึ่งตัวขึ้นมากลางจอ โผล่มาเฉยๆ งั้น ทำอะไรไม่ได้
"""
