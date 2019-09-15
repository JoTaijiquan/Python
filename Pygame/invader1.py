#Python 3.7.4
#Pygame 1.9.6
#Example invader1

import pygame, sys,random
from pygame.locals import *


SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Space Invader"
FPS = 50
WHITE = (255, 255, 255)
BLACK = (0,0,0)

def load_image (name,colorkey=None):
    image = pygame.image.load(name)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image,image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("bullet.png",-1)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("plane.png",-1)
        self.x = 0
        self.y = 0
        self.rect.center = (400,SCREEN_SIZE[1]-40)


    def move(self,key):
        if key[pygame.K_LEFT]:
            self.direction = "LEFT"
            if self.rect.x > 0:
                self.rect.move_ip(-5,0)
            
        elif key[pygame.K_RIGHT]:
            self.direction = "RIGHT"
            if self.rect.x+64 < SCREEN_SIZE[0]:
                self.rect.move_ip(5,0)

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