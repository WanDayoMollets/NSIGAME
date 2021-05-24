import pygame
import random
import os
import sys
import time
import threading
import player
import pokemon
import moves

from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1280,960
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Nomékop")
screen = pygame.display.set_mode(window_resolution)
fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False
lose = False
IAlose = False 

def draw_text(text,font,color,surface,x,y):
    """permet d'afficher un texte"""
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu():
    """Menu principal -> Jouer, Options, Quitter"""
    while True:
        screen.fill((0,0,0))
        draw_text("Nomékop", fontMenu, (255,255,255), screen, x*0.345,y*0.2)

        mx, my = pygame.mouse.get_pos()

        play = pygame.Rect(x*0.2,y*0.5,x*0.2,y*0.125)
        #bouton jouer
        if play.collidepoint((mx,my)):
            if click:
                #intro toussatoussa
                init_game()
                battle()
        options = pygame.Rect(x*0.6,y*0.5,x*0.2,y*0.125)
        #bouton options
        if options.collidepoint((mx,my)):
            if click:
                optionsMenu()
        leave = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        #bouton quitter
        if leave.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        #affiche tous les boutons et le texte
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
    """Menu des options"""
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text("Options", fontMenu, (255,255,255), screen, x*0.345,y*0.2)

        mx, my = pygame.mouse.get_pos()

        back = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        #bouton retour
        if back.collidepoint((mx,my)):
            if click:
                running = False
        #affiche tous les boutons et le texte
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
    """fenetre principale lors d'un combat : attaquer/sac/pokemons"""
    running = True
    global IAlose
    IAlose = False
    while running:
        screen.fill((0,0,0))

        if lose == True or IAlose == True:
            running = False

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        attackButton = pygame.Rect(x*0.1,y*0.7,x*0.3,y*0.2)
        #bouton pour attaquer, ouvre le menu d'attaque
        if attackButton.collidepoint((mx,my)):
            if click:
                attackMenu()
        #affiche tous les boutons et le texte
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
    """Menu d'attaque, affiche les 4 attaques dispo"""
    click = False
    attackMenuRunning = True
    while attackMenuRunning:

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)

        attack1Button = pygame.Rect(x*0.05,y*0.625,x*0.35,y*0.125)
        if attack1Button.collidepoint((mx,my)):
            if click: 
                tourJeu = threading.Thread(target = tour, args = (1,))
                tourJeu.start()
                block_user_control(tourJeu)
                attackMenuRunning = False
        attack2Button = pygame.Rect(x*0.45,y*0.625,x*0.35,y*0.125)
        if attack2Button.collidepoint((mx,my)):
            if click:
                tourJeu = threading.Thread(target = tour, args = (2,))
                tourJeu.start()
                block_user_control(tourJeu)
                attackMenuRunning = False
        attack3Button = pygame.Rect(x*0.05,y*0.825,x*0.35,y*0.125)
        if attack3Button.collidepoint((mx,my)):
            if click:
                tourJeu = threading.Thread(target = tour, args = (3,))
                tourJeu.start()
                block_user_control(tourJeu)
                attackMenuRunning = False
        attack4Button = pygame.Rect(x*0.45,y*0.825,x*0.35,y*0.125)
        if attack4Button.collidepoint((mx,my)):
            if click:
                tourJeu = threading.Thread(target = tour, args = (4,))
                tourJeu.start()
                block_user_control(tourJeu)
                attackMenuRunning = False
        returnButton = pygame.Rect(x*0.91,y*0.8745,x*0.064,y*0.1)
        #retourne sur la fenetre de combat
        if returnButton.collidepoint((mx,my)):
            if click:
                attackMenuRunning = False
        #affiche tous les boutons et le texte
        pygame.draw.rect(screen, (255,255,255),menuBackground)
        pygame.draw.rect(screen, (255,0,0),attack1Button)
        pygame.draw.rect(screen, (255,0,0),attack2Button)
        pygame.draw.rect(screen, (255,0,0),attack3Button)
        pygame.draw.rect(screen, (255,0,0),attack4Button)
        pygame.draw.rect(screen, (255,0,0), returnButton)
        draw_text("back", fontMenuChoice, (0,0,0), screen, x*0.92,y*0.91)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(1)}", fontMenuChoice, (0,0,0), screen, x*0.15,y*0.65)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(2)}", fontMenuChoice, (0,0,0), screen, x*0.5,y*0.65)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(3)}", fontMenuChoice, (0,0,0), screen, x*0.15,y*0.9)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(4)}", fontMenuChoice, (0,0,0), screen, x*0.5,y*0.9)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                #augmente de 1 lvl le pokemon actu
                if event.key == pygame.K_KP1:
                    joueur.get_currentPokemon().level_up(joueur.get_currentPokemon().get_level()+1)
                    print(f"{joueur.get_currentPokemon().get_level()}")
                    print(f"{joueur.get_currentPokemon().get_attack()}")
                #augmente de 5 lvl le pokemon actu
                if event.key == pygame.K_KP5:
                    joueur.get_currentPokemon().level_up(joueur.get_currentPokemon().get_level()+5)
                    print(f"{joueur.get_currentPokemon().get_level()}")
                if event.key == pygame.K_KP2:
                    p = pokemon.Pokemon(28,"pokemonAdd","eau","psy",55,42,63,35,28,14,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])
                    joueur.set_pokemon(2,p)

        pygame.display.update()
        mainClock.tick(60)

def block_user_control(tourJeu):
    blockedCommand=True
    while blockedCommand:
        blockMenu = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        pygame.draw.rect(screen, (255,255,255),blockMenu)
        if not tourJeu.is_alive():
            blockedCommand = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def tourIA():
    attaque = random.randint(0,3)
    print(f"{IA.get_currentPokemon().get_name()} de {IA.get_name()} utilise {IA.get_currentPokemon().get_pokemon_move(attaque+1)}")
    IA.get_currentPokemon().attack_target(joueur.get_currentPokemon(),IA.get_currentPokemon().moveSet[attaque])
    print(f"il reste {joueur.get_currentPokemon().get_hp()} à {joueur.get_currentPokemon().get_name()}")
    time.sleep(1)
    print(f"oof, ça fait mal")
    time.sleep(0.5)

def tourJoueur(numAttaque):
    print(f"vie de l'adversaire avant attaque : {IA.get_currentPokemon().get_hp()}")
    joueur.get_currentPokemon().attack_target(IA.get_currentPokemon(),joueur.get_currentPokemon().moveSet[numAttaque-1])
    print(f"vie de l'adversaire après attaque : {IA.get_currentPokemon().get_hp()}")

def tour(numAttaqueJoueur):
    if joueur.get_currentPokemon().get_speed() >= IA.get_currentPokemon().get_speed():
        tourJoueur(numAttaqueJoueur)
        check_death()
        if not is_dead(IA.get_currentPokemon()):
            tourIA()
            check_death()     
    else:
        tourIA()
        check_death()
        if not is_dead(joueur.get_currentPokemon()):
            tourJoueur(numAttaqueJoueur)
            check_death()

def check_death():
    if is_dead(IA.get_currentPokemon()):
        print(f"{IA.get_currentPokemon().get_name()} de {IA.get_name()} est mort")
        IA.set_pokemon(IA.get_currentPokemon_position()+1,notPokemon)
        if IA.has_pokemon_remaining() == False:
            print(f"{IA.get_name()} a Perdu!")
            global IAlose
            IAlose = True
            #fin combat
        else:
            #L'IA envoie un autre pokemon, défini pour le moment
            IA.set_currentPokemon(IA.get_pokemon(2))
            print(f"{IA.get_name()} envoie {IA.get_currentPokemon().get_name()}")
    if is_dead(joueur.get_currentPokemon()):
        print(f"{joueur.get_currentPokemon().get_name()} est mort")
        joueur.set_pokemon(joueur.get_currentPokemon_position()+1,notPokemon)
        if joueur.has_pokemon_remaining() == False:
            print("Perdu!")
            global lose
            lose = True
        else:
            #choisir un autre pokemon
            pass

def is_dead(pokemon):
    if pokemon.get_hp() <= 0:
        return True
    return False

notPokemon = pokemon.Pokemon(0,"None","","",0,0,0,0,0,0,False,[])

def init_game():
    global joueur
    attaqueP1 = moves.Move(1,"attack1","feu","Special",100,100,15)
    attaqueP2 = moves.Move(2,"attack2","sol","Physical",100,100,10)
    attaqueP3 = moves.Move(2,"attack3","sol","Physical",80,100,10)
    attaqueP4 = moves.Move(2,"attack4","sol","Special",80,100,10)
    global lose
    lose = False
    #animation + explications du prof
    #input nom du joueur
    inputPlayer = "joueur test"
    #choix du starter
    Pokemon1 = pokemon.Pokemon(12,"yes","feu","vol",55,60,63,35,28,14,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])
    Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6 = notPokemon, notPokemon, notPokemon, notPokemon, notPokemon
    joueur = player.Player(inputPlayer,[Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6],[])


#tests

attaqueP1 = moves.Move(1,"attack1","feu","Special",100,100,15)
attaqueP2 = moves.Move(2,"attack2","sol","Physical",100,100,10)
attaqueP3 = moves.Move(2,"attack3","sol","Physical",80,100,10)
attaqueP4 = moves.Move(2,"attack4","sol","Special",80,100,10)

test = pokemon.Pokemon(12,"yes","feu","vol",55,42,63,35,28,14,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])
test2 = pokemon.Pokemon(14,"no","feu","vol",68,35,65,36,35,13,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])

IA = player.Player("IA",[test2,test],[])

main_menu()
