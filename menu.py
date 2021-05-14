import pygame
import random
import os
import sys
import player
import pokemon
import moves

from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1000,640
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Nomékop")
screen = pygame.display.set_mode(window_resolution)
fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill((0,0,0))
        draw_text("Nomékop", fontMenu, (255,255,255), screen, x*0.345,y*0.2)

        mx, my = pygame.mouse.get_pos()

        play = pygame.Rect(x*0.2,y*0.5,x*0.2,y*0.125)
        if play.collidepoint((mx,my)):
            if click:
                battle()
        options = pygame.Rect(x*0.6,y*0.5,x*0.2,y*0.125)
        if options.collidepoint((mx,my)):
            if click:
                optionsMenu()
        leave = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        if leave.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255,0,0), play)
        pygame.draw.rect(screen, (255,0,0), options)
        pygame.draw.rect(screen, (255,0,0), leave)
        draw_text("Jouer", fontMenuChoice, (0,0,0), screen, x*0.27,y*0.55)
        draw_text("Options", fontMenuChoice, (0,0,0), screen, x*0.66,y*0.55)
        draw_text("Quitter", fontMenuChoice, (0,0,0), screen, x*0.9,y*0.925)

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
    
def optionsMenu():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text("Options", fontMenu, (255,255,255), screen, x*0.345,y*0.2)

        mx, my = pygame.mouse.get_pos()

        back = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        if back.collidepoint((mx,my)):
            if click:
                running = False
        pygame.draw.rect(screen, (255,0,0), back)
        draw_text("Retour", fontMenuChoice, (0,0,0), screen, x*0.9,y*0.925)

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

def battle():
    running = True
    currentPokemon = j1.team[0]
    while running:
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        attackButton = pygame.Rect(x*0.1,y*0.7,x*0.3,y*0.2)
        if attackButton.collidepoint((mx,my)):
            if click:
                attackMenu()
        pygame.draw.rect(screen, (255,255,255),menuBackground)
        pygame.draw.rect(screen, (255,0,0), attackButton)
        draw_text("Attaquer", fontMenuChoice, (0,0,0), screen, x*0.21,y*0.78)

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

def attackMenu():
    click = False
    currentPokemon = j1.team[0]
    attackMenuRunning = True
    while attackMenuRunning:

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        attack1Button = pygame.Rect(x*0.05,y*0.625,x*0.35,y*0.125)
        if attack1Button.collidepoint((mx,my)):
            if click:
                print(f"{currentPokemon.get_pokemon_move(1)}")
        attack2Button = pygame.Rect(x*0.45,y*0.625,x*0.35,y*0.125)
        if attack2Button.collidepoint((mx,my)):
            if click:
                print(f"{currentPokemon.get_pokemon_move(2)}")
        attack3Button = pygame.Rect(x*0.05,y*0.825,x*0.35,y*0.125)
        if attack3Button.collidepoint((mx,my)):
            if click:
                print(f"{currentPokemon.get_pokemon_move(3)}")
        attack4Button = pygame.Rect(x*0.45,y*0.825,x*0.35,y*0.125)
        if attack4Button.collidepoint((mx,my)):
            if click:
                print(f"{currentPokemon.get_pokemon_move(4)}")
        returnButton = pygame.Rect(x*0.91,y*0.8745,x*0.064,y*0.1)
        if returnButton.collidepoint((mx,my)):
            if click:
                attackMenuRunning = False
        pygame.draw.rect(screen, (255,255,255),menuBackground)
        pygame.draw.rect(screen, (255,0,0),attack1Button)
        pygame.draw.rect(screen, (255,0,0),attack2Button)
        pygame.draw.rect(screen, (255,0,0),attack3Button)
        pygame.draw.rect(screen, (255,0,0),attack4Button)
        pygame.draw.rect(screen, (255,0,0), returnButton)
        draw_text("back", fontMenuChoice, (0,0,0), screen, x*0.92,y*0.91)
        draw_text(f"{currentPokemon.get_pokemon_move(1)}", fontMenuChoice, (0,0,0), screen, x*0.15,y*0.65)
        draw_text(f"{currentPokemon.get_pokemon_move(2)}", fontMenuChoice, (0,0,0), screen, x*0.5,y*0.65)
        draw_text(f"{currentPokemon.get_pokemon_move(3)}", fontMenuChoice, (0,0,0), screen, x*0.15,y*0.9)
        draw_text(f"{currentPokemon.get_pokemon_move(4)}", fontMenuChoice, (0,0,0), screen, x*0.5,y*0.9)

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


attaqueP1 = moves.Move(1,"feuuu","feu","Special",100,100,15)
attaqueP2 = moves.Move(2,"boom","sol","Physical",80,100,10)
attaqueP3 = moves.Move(2,"tagada","sol","Physical",80,100,10)
attaqueP4 = moves.Move(2,"yaouh","sol","Physical",80,100,10)

test = pokemon.Pokemon(12,"yes","feu","vol",55,42,63,35,28,14,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])
test2 = pokemon.Pokemon(14,"no","feu","vol",55,42,63,35,28,14,False,[attaqueP1])

j1 = player.Player("TestPlayer",[test,test2],[])
main_menu()