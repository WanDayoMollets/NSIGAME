import pygame
import random
import os
import sys
import time
from menu import p


from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1280,960
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(window_resolution)
fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def parlez(texte,x,y,color):
    if color == 0:
        c = (255,255,255)
    if color == 1:
        c= (0,0,0)
    a = True
    b= True
    i=0
    while a:

        if b:
            i+=1
            texteP(texte,i,x,y,c)
            if i >= len(texte):    
                b=False
            time.sleep(0.03)
        if not b:
            if event.type == MOUSEBUTTONDOWN:
                if click:
                    a = False
                    click = False
            
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE) and (p > 7):
                        p = 50
        pygame.display.update()
        mainClock.tick(60)

def texteP(texte,i,x,y,c):
        draw_text(texte[:i-1], fontMenuChoice, c, screen, x,y)
    
