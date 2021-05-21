import pygame
import random
import os
import sys
import time


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
        
        mx, my = pygame.mouse.get_pos()

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
            
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
        pygame.display.update()
        mainClock.tick(60)

def texteP(texte,i,x,y,c):
        draw_text(texte[:i], fontMenuChoice, c, screen, x,y)

#test
"""
def main():    
    while True:
        screen.fill((0,0,0))
        draw_text("Prof Chen", fontMenu, (255,255,255), screen, x*0.345,y*0.2)
    
        mx, my = pygame.mouse.get_pos()

        dialogue = pygame.Rect(x*0.2,y*0.5,x*0.2,y*0.125)
        if dialogue.collidepoint((mx,my)):
            if click:
                parlez(texte,300,400)
        pygame.draw.rect(screen, (255,0,0), dialogue)
        draw_text("Parlez", fontMenuChoice, (255,255,255), screen, x*0.27,y*0.55)

        click = False
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
        pygame.display.update()
        mainClock.tick(60)


texte= 'Salut petite merde !'
main()
        
"""        

    
