import pygame
import sys
from pygame.locals import *
import string

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 80, 255,  80)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 255)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (255, 255,  50)



WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = RED







LEFT=1
CENTER=0
RIGHT=2


class Windows:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(100, 100)
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 15)
        BIGFONT = pygame.font.Font('freesansbold.ttf', 60)
        MYFONT = pygame.font.Font('/usr/lib/jvm/jdk-7-oracle-armhf/jre/lib/fonts/LucidaTypewriterBold.ttf',40)
        DJVFONT = pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',40)
        self.DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Ghelfa")    
        

        
    def showTextScreen(self, text,LN, COLOR, Side):
        titleSurf, titleRect = Windows.makeTextObjs(self, text, self.BASICFONT, COLOR)
        if Side==0:
                h=titleRect.height*(LN-1) + titleRect.height/2
                titleRect.center = (int(WINDOWWIDTH / 2), int(h))
        else:
                h=titleRect.height*(LN-1) + titleRect.height/2
                if Side==1:
                    titleRect.center = (int(titleRect.width/2), int(h))
                else:
                    titleRect.center = (int(WINDOWWIDTH - titleRect.width), int(h))
                
        pygame.draw.rect (self.DISPLAYSURF,BGCOLOR,titleRect)
        self.DISPLAYSURF.blit(titleSurf, titleRect)
        pygame.display.update()
      

    def makeTextObjs(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()
