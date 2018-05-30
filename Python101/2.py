#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *


    
        
class View:
    def __init__(self,mode=(640,480),caption="Hello"):
        pygame.init()
        DISP = pygame.display.set_mode(mode)
        pygame.display.set_caption(caption)
    
    

class Controller:
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update
                    

V = View
C = Controller
C.main()
