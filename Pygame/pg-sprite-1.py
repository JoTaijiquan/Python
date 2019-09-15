#Python 3.7.3
#Pygame 1.9.6
#Example PG-sprite-1
import pygame, sys,random
from pygame.locals import *


SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Ghost Run"
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0,0,0)

class SpriteSheet():
    def __init__(self,img_name):
        self.sprite_sheet = pygame.image.load(img_name).convert()
    
    def get_sprite(self,x,y,w,h):
        image = pygame.Surface((w,h)).convert()
        image.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        image.set_colorkey(image.get_at((0,0)),RLEACCEL)
        return image    


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sheet = SpriteSheet("sprite32x48.png")
        
        self.images = []
        for i in range(4):
            for j in range(4):
                self.images.append(sheet.get_sprite(j*32,i*48,32,48))
        'down 0-3, up 4-7, left 8-11, right 12-15'
        self.index = 0
        self.direction = "DOWN"
        self.image = self.images[self.index]
        #self.image.rect = (0,0,32,48)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.center = (400,200)

    def move(self,key):
        if key[pygame.K_LEFT]:
            self.direction = "LEFT"
            self.index-=1
            if self.index < 8 or self.index >11:
                self.index = 11
            
            self.rect.move_ip(-3,0)
            self.image = self.images[self.index]
            
        elif key[pygame.K_RIGHT]:
            self.direction = "RIGHT"
            self.index+=1
            if self.index < 12 or self.index >15:
                self.index = 12
            
            self.rect.move_ip(3,0)
            self.image = self.images[self.index]

    def update(self):
        pass            

class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(100, 10)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.allsprites = pygame.sprite.Group()
    
    def app_update(self):
        self.view.fill(WHITE)

        self.allsprites.update()
        self.allsprites.draw(self.view)

        self.clock.tick(FPS)
        pygame.display.update()

def mainloop(app):
    #allsprites = pygame.sprite.Group()
    player1 = Player()
    app.allsprites.add(player1)

    while True:
        key = pygame.key.get_pressed() 
        player1.move(key)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #allsprites.update()
        #allsprites.draw(app.view)
        app.app_update()
        
if __name__ == "__main__":
    app = App()
    mainloop(app)