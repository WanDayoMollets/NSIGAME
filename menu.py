import pygame
import random
import os
import sys
import time
import threading
import player
import pokemon
import moves
import CSV_import
import imageImport

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
                waiting_menu()
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
    
    image_update("joueur")
    image_update("IA")

    while running:
        screen.fill((0,0,0))


        if lose == True or IAlose == True:
            running = False

        screen.blit(currentPokemonJoueur,(0.1*x,0.25*y))
        screen.blit(currentPokemonIA,(0.6*x,0.1*y))
        

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        attackButton = pygame.Rect(x*0.1,y*0.7,x*0.3,y*0.2)
        teamButton = pygame.Rect(x*0.6,y*0.7,x*0.25,y*0.1)
        #bouton pour attaquer, ouvre le menu d'attaque
        if attackButton.collidepoint((mx,my)):
            if click:
                attackMenu()
        if teamButton.collidepoint((mx,my)):
            if click:
                teamMenu("battle")
        #affiche tous les boutons et le texte
        pygame.draw.rect(screen, (255,255,255),menuBackground)
        pygame.draw.rect(screen, (255,0,0), attackButton)
        pygame.draw.rect(screen, (0,0,255), teamButton)
        draw_text("Attaquer", fontMenuChoice, (0,0,0), screen, x*0.21,y*0.78)
        draw_text("Pokemons", fontMenuChoice, (0,0,0), screen, x*0.62,y*0.75)

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
                #augmente de 5 lvl le pokemon actu
                if event.key == pygame.K_KP5:
                    joueur.get_currentPokemon().level_up(joueur.get_currentPokemon().get_level()+5)
                    print(f"{joueur.get_currentPokemon().get_level()}")
                if event.key == pygame.K_KP2:
                    p = pokemon.Pokemon(28,"pokemonAdd","eau","psy",55,42,63,35,28,14,False,[attaqueP1,attaqueP2,attaqueP3,attaqueP4])
                    joueur.set_pokemon(2,p)

        pygame.display.update()
        mainClock.tick(60)

def teamMenu(condition): #en combat ou pause
    """Menu de gestion de l'équipe pokemon"""
    click = False
    global teamMenuRunning
    teamMenuRunning = True
    while teamMenuRunning:

        mx, my = pygame.mouse.get_pos()

        menuBackground = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)

        returnButton = pygame.Rect(x*0.91,y*0.8745,x*0.064,y*0.1)
        Poke1 = pygame.Rect(x*0.05,y*0.65,x*0.25,y*0.1)
        Poke2 = pygame.Rect(x*0.33,y*0.65,x*0.25,y*0.1)
        Poke3 = pygame.Rect(x*0.61,y*0.65,x*0.25,y*0.1)
        Poke4 = pygame.Rect(x*0.05,y*0.85,x*0.25,y*0.1)
        Poke5 = pygame.Rect(x*0.33,y*0.85,x*0.25,y*0.1)
        Poke6 = pygame.Rect(x*0.61,y*0.85,x*0.25,y*0.1)
        #retourne sur la fenetre de combat
        if returnButton.collidepoint((mx,my)):
            if click:
                teamMenuRunning = False
        if Poke1.collidepoint((mx,my)):
            if click:
                select_pokemon(1,condition)
        if Poke2.collidepoint((mx,my)):
            if click:
                select_pokemon(2,condition)
        if Poke3.collidepoint((mx,my)):
            if click:
                select_pokemon(3,condition)
        if Poke4.collidepoint((mx,my)):
            if click:
                select_pokemon(4,condition)
        if Poke5.collidepoint((mx,my)):
            if click:
                select_pokemon(5,condition)
        if Poke6.collidepoint((mx,my)):
            if click:
                select_pokemon(6,condition)
        #affiche tous les boutons et le texte
        pygame.draw.rect(screen, (255,255,255),menuBackground)
        pygame.draw.rect(screen, (255,0,0), returnButton)
        pygame.draw.rect(screen, (0,255,0), Poke1)
        pygame.draw.rect(screen, (0,255,0), Poke2)
        pygame.draw.rect(screen, (0,255,0), Poke3)
        pygame.draw.rect(screen, (0,255,0), Poke4)
        pygame.draw.rect(screen, (0,255,0), Poke5)
        pygame.draw.rect(screen, (0,255,0), Poke6)
        draw_text("back", fontMenuChoice, (0,0,0), screen, x*0.92,y*0.91)
        display_pokemon_in_menu()

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
                #augmente de 5 lvl le pokemon actu
                if event.key == pygame.K_KP5:
                    joueur.get_currentPokemon().level_up(joueur.get_currentPokemon().get_level()+5)
                    print(f"{joueur.get_currentPokemon().get_level()}")

        pygame.display.update()
        mainClock.tick(60)

def select_pokemon(pokemonNb,condition): #condition : en combat ou après une mort (battle,pause)
    click = False
    select_pokemonRunning = True
    mxWhenClicked,myWhenClicked = pygame.mouse.get_pos()
    while select_pokemonRunning:

        mx, my = pygame.mouse.get_pos()

        options = pygame.Rect(mxWhenClicked,myWhenClicked,75,100)
        pygame.draw.rect(screen, (0,255,255), options)
        switch = pygame.Rect(mxWhenClicked,myWhenClicked,75,50)
        pygame.draw.rect(screen, (255,0,255), switch)
        equip = pygame.Rect(mxWhenClicked,myWhenClicked+50,75,50)
        pygame.draw.rect(screen, (255,255,0), equip)
        if condition == "battle":
            draw_text("envoyer", fontMenuChoice, (0,0,0), screen, mxWhenClicked,myWhenClicked+10)
            draw_text("infos", fontMenuChoice, (0,0,0), screen, mxWhenClicked,myWhenClicked+60)
        elif condition == "pause":
            draw_text("echanger", fontMenuChoice, (0,0,0), screen, mxWhenClicked,myWhenClicked+10)
            draw_text("equiper", fontMenuChoice, (0,0,0), screen, mxWhenClicked,myWhenClicked+60)
        
        if not options.collidepoint((mx,my)):
            if click:
                select_pokemonRunning = False 
        
        if switch.collidepoint((mx,my)):
            if click:
                if condition == "battle":
                    switchPokemon = joueur.get_currentPokemon()
                    joueur.set_currentPokemon(joueur.team[pokemonNb-1])
                    joueur.set_pokemon(pokemonNb,switchPokemon)
                    image_update("joueur")
                    global teamMenuRunning
                    teamMenuRunning = False
                    select_pokemonRunning = False
                    
        
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

def waiting_menu():
    click = False
    gameRunning = True
    """Menu d'attente -> organiser son équipe"""
    while gameRunning:
        screen.fill((0,0,0))
        if lose == True:
            gameRunning = False
        draw_text(f"Preparez votre equipe!", fontMenu, (255,255,255), screen, x*0.345,y*0.2)
        draw_text(f"STAGE : {joueur.get_stage()}", fontMenu, (255,255,255), screen, x*0.345,y*0.3)

        mx, my = pygame.mouse.get_pos()

        next = pygame.Rect(x*0.2,y*0.5,x*0.2,y*0.125)
        #bouton next
        if next.collidepoint((mx,my)):
            if click:
                #prochain combat
                joueur.save_team()
                init_IA()
                battle()
                joueur.reset_team()
                joueur.update_team()
                joueur.set_stage(joueur.get_stage()+1)
        equipe = pygame.Rect(x*0.6,y*0.5,x*0.2,y*0.125)
        #bouton options
        if equipe.collidepoint((mx,my)):
            if click:
                #ouvre l'équipe du joueur
                pass
        leave = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        #bouton quitter
        if leave.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        #affiche tous les boutons et le texte
        pygame.draw.rect(screen, (255,0,0), next)
        pygame.draw.rect(screen, (255,0,0), equipe)
        pygame.draw.rect(screen, (255,0,0), leave)
        draw_text("Combat suivant", fontMenuChoice, (0,0,0), screen, x*0.27,y*0.55)
        draw_text("Equipe", fontMenuChoice, (0,0,0), screen, x*0.66,y*0.55)
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
    IA.get_currentPokemon().attack_target(joueur.get_currentPokemon(),IA.get_currentPokemon().moveSet[attaque])
    time.sleep(0.5)

def tourJoueur(numAttaque):
    joueur.get_currentPokemon().attack_target(IA.get_currentPokemon(),joueur.get_currentPokemon().moveSet[numAttaque-1])

def tour(numAttaqueJoueur):
    print(f"Vie du pokemon joueur : {joueur.get_currentPokemon().get_hp()}")
    print(f"Vie du pokemon IA : {IA.get_currentPokemon().get_hp()}")
    if joueur.get_currentPokemon().get_speed() >= IA.get_currentPokemon().get_speed():
        tourJoueur(numAttaqueJoueur)
        if is_dead(IA.get_currentPokemon()):
            check_death()
            return
        tourIA()
        check_death()     
    else:
        tourIA()
        if is_dead(joueur.get_currentPokemon()):
            check_death()
            return
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
            image_update("IA")
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
            #image_update("joueur")

def is_dead(pokemon):
    if pokemon.get_hp() <= 0:
        return True
    return False


notPokemon = pokemon.Pokemon(0,"None","","",0,0,0,0,0,0,0,False,[])

def init_game():
    global joueur
    global lose
    lose = False
    #animation + explications du prof
    #input nom du joueur
    inputPlayer = "joueur test"
    #choix du starter
    Pokemon1 = CSV_import.PokeCSV(random.randint(1,721))
    Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6 = notPokemon, notPokemon, notPokemon, notPokemon, notPokemon
    Pokemon2 = CSV_import.PokeCSV(random.randint(1,721))
    Pokemon6 = CSV_import.PokeCSV(random.randint(1,721))
    joueur = player.Player(inputPlayer,[Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6],[])
    joueur.update_team()

def init_IA():
    global IA
    IA = player.Player("IA",[CSV_import.PokeCSV(random.randint(1,721)),CSV_import.PokeCSV(random.randint(1,721))],[])
    IA.update_team()

def image_update(player):
    global currentPokemonJoueur
    global currentPokemonIA
    if player == "joueur":
        imageImport.importPokemonImage(joueur.currentPokemon.get_name().lower(),player)
        currentPokemonJoueur=pygame.image.load("cache/joueur/currentPokemon.png").convert_alpha()
        currentPokemonJoueur=pygame.transform.scale(currentPokemonJoueur, (360, 360))
    elif player == "IA":
        imageImport.importPokemonImage(IA.currentPokemon.get_name().lower(),player)
        currentPokemonIA=pygame.image.load("cache/IA/currentPokemon.png").convert_alpha()
        currentPokemonIA=pygame.transform.scale(currentPokemonIA, (360, 360))

def display_pokemon_in_menu():
    xCoords = [125,525,925,125,525,925]
    yCoords = [650,650,650,850,850,850]
    for i in range(len(joueur.team)):
        if joueur.team[i].get_name() != "None":
            draw_text(f"{joueur.team[i].get_name()}", fontMenuChoice, (0,0,0), screen, xCoords[i],yCoords[i])




main_menu()
