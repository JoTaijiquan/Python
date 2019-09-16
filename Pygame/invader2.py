#Python 3.7.4
#Pygame 1.9.6
#Example invader2

import pygame, sys,random
from pygame.locals import *

SCREEN_SIZE = (800,600)
SCREEN_CAPTION = "Space Invader"

IMG_NAME = {'plane':'plane.png',
            'bullet':'bullet16x48.png', 
            'invader1':'invader64x64.png'
}

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0,0,0)

def load_image (name,colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((1,1))
        image.set_colorkey(colorkey,RLEACCEL)
    return image,image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(IMG_NAME['plane'],-1)
        self.rect.center = (400,SCREEN_SIZE[1]-40)

    def move(self,direction):
        if direction == "LEFT" and self.rect.x>0:
            self.rect.move_ip(-5,0)
        elif direction == "RIGHT" and self.rect.x+64<SCREEN_SIZE[0]:
            self.rect.move_ip(5,0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet,self).__init__()
        self.image, self.rect = load_image(IMG_NAME['bullet'],-1)
        self.rect.center = (x+30,y)
        self.velocity = 16
        self.delay = 0
    
    def update(self):
        self.delay +=1
        self.rect.move_ip(0,self.velocity*-1)
        if self.rect.y < 0:
            self.kill()

class Invader(pygame.sprite.Sprite):
    def __init__(self):
        super(Invader,self).__init__()
        self.image, self.rect = load_image(IMG_NAME['invader1'],-1)
        self.rect.center = (SCREEN_SIZE[0]/2,20)
    
    def __del__(self):
        self.rect.center = (0,0)

class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10,100)
        pygame.display.set_caption(SCREEN_CAPTION)
        self.view = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.allsprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def app_update(self):
        self.view.fill(WHITE)

        self.allsprites.update()
        self.allsprites.draw(self.view)
        self.bullets.update()
        self.bullets.draw(self.view)

        self.clock.tick(FPS)
        pygame.display.update()

def mainloop(app):
    player1 = Player()
    app.allsprites.add(player1)
    bullet = ""

    invader1 = Invader()
    app.allsprites.add(invader1)

    while True:    
        key = pygame.key.get_pressed() 
        if key[pygame.K_LEFT]:
            player1.move("LEFT")
        elif key[pygame.K_RIGHT]:
            player1.move("RIGHT")

        if key[pygame.K_SPACE]:
            if bullet == "":
                delay = 1000
            else:
                delay = bullet.delay
            
            if delay>5:
                bullet = Bullet(player1.rect.x, player1.rect.y)
                bullet.delay = 0
                app.bullets.add(bullet)
                #app.allsprites.add(bullet)
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        hits = pygame.sprite.spritecollide(invader1,app.bullets,True)
        if hits != []:
            print (hits)  

        app.app_update()
        
if __name__ == "__main__":
    app = App()
    mainloop(app)