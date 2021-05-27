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
    while True:
        screen.fill((0,0,0))
        click = False
        pygame.display.flip()
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()

        if len(key) == 1:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                string += key.upper()
            else:
                pass
                """https://www.reddit.com/r/pygame/comments/205i05/get_user_input/"""
        
        

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    

start()
