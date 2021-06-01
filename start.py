import pygame
import random
import os
import sys
import time
import threading
import menu
from dialogue import *
import threading



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
    bgp = pygame.image.load('Design/Interface/profHouse.png')
    profIMG = pygame.image.load('Design/character/profchencrayon.png').convert_alpha()
    profIMG = pygame.transform.scale(profIMG, (700, 500))
    box = pygame.image.load('Design/Interface/DialogueBox.png').convert_alpha()
    box = pygame.transform.scale(box, (800, 500))
    skip = pygame.image.load('Design/Interface/Backreturn.png').convert_alpha()
    skip = pygame.transform.scale(skip, (80, 80))
    p = 0
    lines = []
    with open('prof.txt') as f:
        lines = f.readlines()
    
    while True:
        screen.blit(bgp, (0, 0))
        click = False
        screen.blit(profIMG,(-200,00))
        screen.blit(box,(240,580))
        pygame.display.flip()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        while p < len(lines):
                            screen.blit(box,(240,580))
                            draw_text("Pr. Brindille", fontMenuChoice, (0,0,0), screen, 310,710)
                            parlez(lines[p],300,800,1)
                    
                            if p == 2:
                                screen.blit(box,(240,580))
                                name = demande()
                                screen.blit(bgp, (0, 0))
                                screen.blit(profIMG,(-200,00))
                                    
                                
                            if p == 4:
                                screen.blit(box,(240,580))
                                dresseur = choix()
                                screen.blit(bgp, (0, 0))
                                screen.blit(profIMG,(-200,00))
                                dresseurR = pygame.transform.flip(dresseur, True, False)
                                screen.blit(dresseurR,(845,200))
                            if p ==6:
                                Poke = choixP()
                                screen.blit(box,(240,580))
                                screen.blit(bgp, (0, 0))
                                screen.blit(profIMG,(-200,00))
                                screen.blit(dresseurR,(845,200))
                            if p > 7:
                                draw_text("Press", fontMenuChoice, (128,128,128), screen, 1045,850)
                                draw_text("Space", fontMenuChoice, (128,128,128), screen, 1045,870)
                                draw_text("To", fontMenuChoice, (128,128,128), screen, 1045,890)
                                draw_text("Skip", fontMenuChoice, (128,128,128), screen, 1045,910)
                    
                                
                            p+=1

        draw_text("Pr. Brindille", fontMenuChoice, (0,0,0), screen, 310,710)
        draw_text("Clique pour parlez", fontMenuChoice, (0,0,0), screen, 310,800)

        pygame.display.update()
        mainClock.tick(60)

def demande():
    string = ""
    bgn = pygame.image.load('Design/Interface/Backname.png')
    screen.blit(bgn, (0, 0))
    a = True
    b = False
    box = pygame.image.load('Design/Interface/DialogueBox.png').convert_alpha()
    box = pygame.transform.scale(box, (800, 500))
    while a:
        screen.blit(box,(240,200))
        click = False
        pygame.display.flip()
        
        draw_text("Ton nom :", fontMenuChoice, (0,0,0), screen, 330,330)
        draw_text("Entre 3 et 12 caractères | Entrez pour valider", fontMenuChoice, (255,255,255), screen, 420,590)
        while b is False:
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
                        print(string)
                        screen.blit(box,(240,200))
                        draw_text("Ton nom :", fontMenuChoice, (0,0,0), screen, 330,330)
                        draw_text("Entre 3 et 12 caractères | Entrez pour valider", fontMenuChoice, (255,255,255), screen, 420,590)
                    elif event.key == pygame.K_RETURN and len(string) > 3 and len(string) < 12:
                        print(string)
                        b= True
                        a= False
                        
            
                draw_text(string, fontMenu, (0,0,0), screen, 460,450)
        
        
            pygame.display.update()
            mainClock.tick(60)
        pygame.display.update()
        mainClock.tick(60)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def choix():
    bgn = pygame.image.load('Design/Interface/BackVS.png')
    screen.blit(bgn, (0, 0))
    dresseur1 = pygame.image.load('Design/character/trainer1.png').convert_alpha()
    dresseur1 = pygame.transform.scale(dresseur1, (700, 500))
    dresseur2 = pygame.image.load('Design/character/trainer2.png').convert_alpha()
    dresseur2 = pygame.transform.scale(dresseur2, (700, 500))
    button1 = pygame.image.load('Design/interface/redClick.png').convert_alpha()
    button1 = pygame.transform.scale(button1, (500, 300))
    button2 = pygame.image.load('Design/interface/greenClick.png').convert_alpha()
    button2 = pygame.transform.scale(button2, (500, 300))
    a = True
    screen.blit(dresseur1,(0,150))
    screen.blit(dresseur2,(400,150))
    b1 = screen.blit(button1,(190,610))
    b2 = screen.blit(button2,(600,610))
    draw_text("CAMPAGNARD", fontMenuChoice, (207,33,33), screen, 370,750)
    draw_text("RACAILLE", fontMenuChoice, (66, 174, 70), screen, 800,750)
    click = False
    time.sleep(0.1)
    while a:
        mx, my = pygame.mouse.get_pos()
        pygame.display.update()
        mainClock.tick(60)
        if b1.collidepoint((mx,my)):
            if click:
                click = False
                print('Red player')
                return dresseur1
        if b2.collidepoint((mx,my)):
            if click:
                click = False
                print('Green player')
                return dresseur2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def choixP():
    bgc = pygame.image.load('Design/Interface/choix.png')
    screen.blit(bgc, (0, 0))
    a = True
    button1 = pygame.image.load('Design/interface/redClick.png').convert_alpha()
    button1 = pygame.transform.scale(button1, (500, 300))
    button2 = pygame.image.load('Design/interface/greenClick.png').convert_alpha()
    button2 = pygame.transform.scale(button2, (500, 300))
    button3 = pygame.image.load('Design/interface/blueClick.png').convert_alpha()
    button3 = pygame.transform.scale(button3, (500, 300))
    b1 = screen.blit(button1,(400,650))
    b2 = screen.blit(button2,(800,650))
    b3 = screen.blit(button3,(0,650))
    click = False
    while a:

        mx, my = pygame.mouse.get_pos()
        pygame.display.update()
        mainClock.tick(60)
        
        if b1.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop2')
                break
                
        if b2.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop3')
                
        if b3.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop1')
        
        click = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def space():
    a = True
    while a:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print('es')
                key = pygame.key.name(event.key)
                if key == "backspace":
                    print('10')
                    a = False
                    return True
                else :
                    return False
        
start()
