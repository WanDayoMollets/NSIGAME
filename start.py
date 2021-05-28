import pygame
import random
import os
import sys
import time
import threading
from dialogue import *



from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1280,960
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Nomekop")
screen = pygame.display.set_mode(window_resolution)
fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False
blockedCommand = False
tourIA_finished = False


def start():
    bg = pygame.image.load('Design/Interface/BackGroundLogo.png')
    while True:
        
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        draw_text("Press space to continue", fontMenuChoice, (80,150,200), screen, 540,630)
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    prof()
                    
                    

        pygame.display.update()
        mainClock.tick(60)


def prof():
    profIMG = pygame.image.load('Design/character/profchencrayon.png').convert_alpha()
    profIMG = pygame.transform.scale(profIMG, (900, 680))
    box = pygame.image.load('Design/Interface/DialogueBox.png').convert_alpha()
    p = 0
    lines = []
    with open('prof.txt') as f:
        lines = f.readlines()
    
    while True:
        screen.fill((0,0,0))
        click = False
        screen.blit(profIMG,(200,-50))
        screen.blit(box,(0,400))
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if p <= len(lines):   
                            parlez(lines[p],300,800,1)
                            if p == 2:
                                name = demande()  
                            p+=1


        
                        

        pygame.display.update()
        mainClock.tick(60)

def demande():
    string = ""
    screen.fill((0,0,0))
    a = True
    while a:
        
        click = False
        pygame.display.flip()
        
        

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                print(key)
                if len(key) == 1:
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        string += key.upper()
                    else:
                        string += key
                elif key == "backspace":
                    string = string[:len(string) - 1]
                elif event.key == pygame.K_RETURN and len(string) > 3:
                    print(string)
                    a= False
            
        draw_text("Ton nom :", fontMenuChoice, (255,255,255), screen, 540,550)
        draw_text(string, fontMenuChoice, (255,255,255), screen, 540,630)
        
        
        pygame.display.update()
        mainClock.tick(60)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    

start()
