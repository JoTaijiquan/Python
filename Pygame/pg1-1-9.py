#Python 3.7.3
#Pygame 1.9.6
#Example PG-1-1-9

'ยังไม่เสร็จ'



import pygame, sys,random
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Ghost Run"
FPS = 50
WHITE = (255, 255, 255)
BLACK = (0,0,0)

def load_image (name,colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image,image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprite.png",-1)
        self.x = 0
        self.y = 0
        #self.image.rect = (0,0,32,48)
        self.rect.center = (400,200)
    
    def move(self,key):
        if key[pygame.K_LEFT] and self.rect.x>0: 
            self.x-=1
        elif key[pygame.K_RIGHT] and self.rect.x<SCREEN_SIZE[0]:
            self.x+=1 


    def update(self):
         self.rect.move_ip(self.x,self.y)




class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(100, 10)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)

def mainloop(View):
    allsprites = pygame.sprite.Group()
    player1 = Player()
    allsprites.add(player1)

    fpsClock = pygame.time.Clock()
    while True:
        key = pygame.key.get_pressed() 
        player1.move(key)   
        
        if key[pygame.K_F10]:
            pygame.event.post(QUIT)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        View.fill(WHITE)
        #View.blit(wall.img,(wall.x,wall.y))
        #View.blit(ghostRED.img, (ghostRED.x, ghostRED.y))
        #View.blit(ghostBLUE.img, (ghostBLUE.x, ghostBLUE.y))
        
        allsprites.update()
        allsprites.draw(View)

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    mainloop(app.view)

'''
เพิ่มหลายคำสั่งเลย รวมทั้งมี import random เพิ่มขึ้นด้วย
โปรแกรมนี้ ถ้าผีวิ่งชนกัน ตัวสีน้ำเงินจะเด้งออกไป
'''