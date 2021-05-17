import pygame
import random
import os
import sys


from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1000,640
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Dialogue")
screen = pygame.display.set_mode(window_resolution)
fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def parlez():
    a = True
    while a:
        screen.fill((0,0,0))

        draw_text("Prof Chen", fontMenu, (255,255,255), screen, x*0.345,y*0.2)
        mx, my = pygame.mouse.get_pos()
        dialogue = pygame.Rect(x*0.5,y*0.5,x*0.2,y*0.125)
        pygame.draw.rect(screen, (0,0,255), dialogue)
        draw_text("Hello", fontMenuChoice, (0,255,0), screen, x*0.27,y*0.55)

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

def main():    
    while True:
        screen.fill((0,0,0))
        draw_text("Prof Chen", fontMenu, (255,255,255), screen, x*0.345,y*0.2)
    
        mx, my = pygame.mouse.get_pos()

        dialogue = pygame.Rect(x*0.2,y*0.5,x*0.2,y*0.125)
        if dialogue.collidepoint((mx,my)):
            if click:
                parlez()
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
    

main()
