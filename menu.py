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
import shutil
import music

from pygame.rect import Rect
from pygame.sprite import collide_rect

from pygame.constants import MOUSEBUTTONDOWN

x,y=1280,960
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode(window_resolution)
pygame.init()
pygame.display.set_caption("Nomékop")

fontMenu = pygame.font.SysFont(None, 100)
fontMenuChoice = pygame.font.SysFont(None, 30)
click = False
lose = False
IAlose = False 

def start():
    """Affiche l'écran de démarrage"""
    bg = pygame.image.load('Design/Interface/BackGroundLogo.png')
    # music.playMusique("intro")
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
                    init_game()
                    prof()
                    
                    

        pygame.display.update()
        mainClock.tick(60)



def prof():
    """Lance le dialogue avec le prof"""
    bgp = pygame.image.load('Design/Interface/profHouse.png')
    profIMG = pygame.image.load('Design/character/profchencrayon.png').convert_alpha()
    profIMG = pygame.transform.scale(profIMG, (700, 500))
    box = pygame.image.load('Design/Interface/DialogueBox.png').convert_alpha()
    box = pygame.transform.scale(box, (800, 500))
    skip = pygame.image.load('Design/Interface/Backreturn.png').convert_alpha()
    skip = pygame.transform.scale(skip, (80, 80))
    global p
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

        if lose == True:
            break
        
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
                                global name
                                name = demande()
                                joueur.set_name(name)
                                screen.blit(bgp, (0, 0))
                                screen.blit(profIMG,(-200,00))
                                with open('prof.txt') as f:
                                    lines = f.readlines()
                                    
                                
                            if p == 4:
                                screen.blit(box,(240,580))
                                global dresseur
                                dresseur = choix()
                                screen.blit(bgp, (0, 0))
                                screen.blit(profIMG,(-200,00))
                                dresseurR = pygame.transform.flip(dresseur, True, False)
                                screen.blit(dresseurR,(845,200))

                            if p == 5:
                                draw_text("Cliquez une fois", fontMenuChoice, (128,128,128), screen, 1045,850)
                                draw_text("Et attendez", fontMenuChoice, (128,128,128), screen, 1045,870)

                            if p ==6:
                                global Poke
                                choixP()
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
                    
        if p >= len(lines):
            waiting_menu()

        draw_text("Pr. Brindille", fontMenuChoice, (0,0,0), screen, 310,710)
        draw_text("Clique pour parlez", fontMenuChoice, (0,0,0), screen, 310,800)

        pygame.display.update()
        mainClock.tick(60)

def parlez(texte,x,y,color):
    """Permet de faire defiler le texte"""
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
                    global p
                    if (event.key == pygame.K_SPACE) and (p > 7):
                        p = 50
        pygame.display.update()
        mainClock.tick(60)

def texteP(texte,i,x,y,c):
    """Permet d'écrire une phrase du texte, sans le retour à la ligne"""
    draw_text(texte[:i-1], fontMenuChoice, c, screen, x,y)

def demande():
    """Lance une interface qui demande le nom du Joueur"""
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
                        with open("prof.txt", "r") as p:
                            lines = p.readlines()
                            with open("prof.txt", "w") as p:
                                for line in lines:
                                    if "Bonne chance" not in line:
                                        p.write(line)

                        txtP = open("prof.txt","a")
                        txtP.write("Bonne chance "+ str(string)+" !\n")
                        txtP.close()
                        
            
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
    """Lance une interface qui demandera au joueur de faire un choix entre deux personnages"""
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
    """Lance une interface qui demande au joueur de choisir un Nomekop parmis 3 autres"""
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
    init_IA("start")
    image_update("start")
    click = False
    while a:

        screen.blit(pokeChoice1,(50,220))
        screen.blit(pokeChoice2,(450,220))
        screen.blit(pokeChoice3,(850,220))

        draw_text(IA.get_pokemon(1).get_name(), fontMenuChoice, (33,96,207), screen, 200,790)
        draw_text(IA.get_pokemon(2).get_name(), fontMenuChoice, (207,33,33), screen, 600,790)
        draw_text(IA.get_pokemon(3).get_name(), fontMenuChoice, (66,174,70), screen, 1000,790)

        mx, my = pygame.mouse.get_pos()
        pygame.display.update()
        mainClock.tick(60)

        if b1.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop2')
                joueur.set_pokemon(1,IA.team[1])
                a = False
                
        if b2.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop3')
                joueur.set_pokemon(1,IA.team[2])
                a = False
                
        if b3.collidepoint((mx,my)):
            if click:
                click = False
                print('NomeKop1')
                joueur.set_pokemon(1,IA.team[0])
                a = False
        
        click = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def draw_text(text,font,color,surface,x,y):
    """Ecrit du texte sur l'écran"""
    """permet d'afficher un texte"""
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

    
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
    click = False
    joueur.set_currentPokemon(joueur.get_pokemon(1))
    IA.set_currentPokemon(IA.get_pokemon(1))
    image_update("joueur")
    image_update("IA")
    button1 = pygame.image.load('Design/interface/redClick.png').convert_alpha()
    button1 = pygame.transform.scale(button1, (700, 500))
    button2 = pygame.image.load('Design/interface/blueClick.png').convert_alpha()
    button2 = pygame.transform.scale(button2, (500, 300))
    bgf = pygame.image.load('Design/Interface/fight.png')
    menuBackground = pygame.image.load('Design/Interface/acier.png')
    HP = pygame.image.load('Design/interface/HP.png').convert_alpha()
    HP = pygame.transform.scale(HP, (400, 200))
    while running:
        screen.blit(bgf,(0,0))

        if lose == True or IAlose == True:
            running = False
        
        screen.blit(currentPokemonJoueur,(128,230))
        screen.blit(currentPokemonIA,(770,-30))
        b1 = screen.blit(button1,(20,525))
        b2 = screen.blit(button2,(700,550))
        hp = screen.blit(HP,(820,450))
        hp2 = screen.blit(HP,(820,-60))

        mx, my = pygame.mouse.get_pos()
        screen.blit(menuBackground,(32,590))
        attackButton = screen.blit(button1,(20,525))
        teamButton = screen.blit(button2,(700,550))
        #bouton pour attaquer, ouvre le menu d'attaque
        if attackButton.collidepoint((mx,my)):
            if click:
                click = False
                attackMenu()
        if teamButton.collidepoint((mx,my)):
            if click:
                click =False
                teamMenu("battle")
        #affiche tous les boutons et le texte
        draw_text("Attaquer", fontMenu, (207,33,33), screen, 210,730)
        draw_text("NoméKops", fontMenuChoice, (33,96,207), screen, 900,690)
        draw_text(f"{joueur.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,540)
        draw_text(f"{joueur.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,540)
        draw_text(f"{joueur.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,540)

        draw_text(f"{IA.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,30)
        draw_text(f"{IA.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,30)
        draw_text(f"{IA.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,30)


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
    menuBackground = pygame.image.load('Design/Interface/acier.png')
    screen.blit(menuBackground,(32,590))

    while attackMenuRunning:

        mx, my = pygame.mouse.get_pos()
        button = pygame.image.load('Design/interface/redClick.png').convert_alpha()
        button = pygame.transform.scale(button, (500, 270))
        

        attackb1 = screen.blit(button,(30,550))
        attackb2 = screen.blit(button,(600,550))
        attackb3 = screen.blit(button,(30,710))
        attackb4 = screen.blit(button,(600,710))


        if attackb1.collidepoint((mx,my)):
            if click:
                #tourJeu = threading.Thread(target = tour, args = (1,))
                #tourJeu.start()
                #block_user_control(tourJeu)
                tour(1)
                attackMenuRunning = False
    
        if attackb2.collidepoint((mx,my)):
            if click:
                #tourJeu = threading.Thread(target = tour, args = (2,))
                #tourJeu.start()
                #block_user_control(tourJeu)
                tour(2)
                attackMenuRunning = False
        
        if attackb3.collidepoint((mx,my)):
            if click:
                #tourJeu = threading.Thread(target = tour, args = (3,))
                #tourJeu.start()
                #block_user_control(tourJeu)
                tour(3)
                attackMenuRunning = False
        
        if attackb4.collidepoint((mx,my)):
            if click:
                #tourJeu = threading.Thread(target = tour, args = (4,))
                #tourJeu.start()
                #block_user_control(tourJeu)
                tour(4)
                attackMenuRunning = False
        returnButton = pygame.Rect(x*0.91,y*0.8745,x*0.064,y*0.1)
        #retourne sur la fenetre de combat
        if returnButton.collidepoint((mx,my)):
            if click:
                click = False
                attackMenuRunning = False
        #affiche tous les boutons et le texte
        
        pygame.draw.rect(screen, (249, 82, 82), returnButton)
        draw_text("back", fontMenuChoice, (207,33,33), screen, x*0.92,y*0.91)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(1)}", fontMenuChoice, (207,33,33), screen,210,670)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move_category(1)} | {joueur.get_currentPokemon().get_pokemon_move_power(1)}", fontMenuChoice, (207,33,33), screen,220,700)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(2)}", fontMenuChoice, (207,33,33), screen, 780,670)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move_category(2)} | {joueur.get_currentPokemon().get_pokemon_move_power(2)}", fontMenuChoice, (207,33,33), screen,790,700)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(3)}", fontMenuChoice, (207,33,33), screen, 210,840)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move_category(3)} | {joueur.get_currentPokemon().get_pokemon_move_power(3)}", fontMenuChoice, (207,33,33), screen,220,870)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move(4)}", fontMenuChoice, (207,33,33), screen, 780,840)
        draw_text(f"{joueur.get_currentPokemon().get_pokemon_move_category(4)} | {joueur.get_currentPokemon().get_pokemon_move_power(4)}", fontMenuChoice, (207,33,33), screen,790,870)

        draw_text(f"{joueur.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,540)
        draw_text(f"{joueur.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,540)
        draw_text(f"{joueur.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,540)

        draw_text(f"{IA.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,30)
        draw_text(f"{IA.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,30)
        draw_text(f"{IA.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,30)

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

def teamMenu(condition): #en combat ou pause
    """Menu de gestion de l'équipe pokemon"""
    click = False
    global teamMenuRunning
    teamMenuRunning = True
    menuBackground = pygame.image.load('Design/Interface/MenuBack.png')
    Button = pygame.image.load('Design/Interface/woodB.png')
    returnButton = pygame.Rect(1140,850,x*0.064,y*0.08)
    while teamMenuRunning:
        
        mx, my = pygame.mouse.get_pos()
        
        screen.blit(menuBackground,(32,590))
        
        
        if condition != "death":
            pygame.draw.rect(screen, (183,160,75), returnButton)
            draw_text("back", fontMenuChoice, (245,209,75), screen, 1160,880)
        Poke1 = screen.blit(Button,(x*0.05,y*0.65))
        Poke2 = screen.blit(Button,(x*0.33,y*0.65))
        Poke3 = screen.blit(Button,(x*0.61,y*0.65))
        Poke4 = screen.blit(Button,(x*0.05,y*0.85))
        Poke5 = screen.blit(Button,(x*0.33,y*0.85))
        Poke6 = screen.blit(Button,(x*0.61,y*0.85))
        #retourne sur la fenetre de combat
        if returnButton.collidepoint((mx,my)):
            if click:
                teamMenuRunning = False
        if Poke1.collidepoint((mx,my)) and joueur.team[0].get_name() != "None":
            if click:
                select_pokemon(1,condition)
        if Poke2.collidepoint((mx,my)) and joueur.team[1].get_name() != "None":
            if click:
                select_pokemon(2,condition)
        if Poke3.collidepoint((mx,my)) and joueur.team[2].get_name() != "None":
            if click:
                select_pokemon(3,condition)
        if Poke4.collidepoint((mx,my)) and joueur.team[3].get_name() != "None":
            if click:
                select_pokemon(4,condition)
        if Poke5.collidepoint((mx,my)) and joueur.team[4].get_name() != "None":
            if click:
                select_pokemon(5,condition)
        if Poke6.collidepoint((mx,my)) and joueur.team[5].get_name() != "None":
            if click:
                select_pokemon(6,condition)
        display_pokemon_in_menu()
        if condition == "battle":
            draw_text(f"{joueur.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,540)
            draw_text(f"{joueur.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,540)
            draw_text(f"{joueur.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,540)

            draw_text(f"{IA.get_currentPokemon().get_name()}", fontMenuChoice, (255,255,255), screen,850,30)
            draw_text(f"{IA.get_currentPokemon().get_hp()}", fontMenuChoice, (255,255,255), screen,1050,30)
            draw_text(f"{IA.get_currentPokemon().get_level()}", fontMenuChoice, (255,255,255), screen,1150,30)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    teamMenuRunning = False

        pygame.display.update()
        mainClock.tick(60)

def switchMenu(): 
    """Menu de switch pokemon"""
    click = False
    global teamMenuRunning
    switchMenuRunning = True
    Button = pygame.image.load('Design/Interface/woodB.png')
    menuBackground = pygame.image.load('Design/Interface/MenuBack.png')
    while switchMenuRunning:

        mx, my = pygame.mouse.get_pos()
        screen.blit(menuBackground,(32,590))

        Poke1 = screen.blit(Button,(x*0.05,y*0.65))
        Poke2 = screen.blit(Button,(x*0.33,y*0.65))
        Poke3 = screen.blit(Button,(x*0.61,y*0.65))
        Poke4 = screen.blit(Button,(x*0.05,y*0.85))
        Poke5 = screen.blit(Button,(x*0.33,y*0.85))
        Poke6 = screen.blit(Button,(x*0.61,y*0.85))
        if Poke1.collidepoint((mx,my)):
            if click:
                if (joueur.team[0].get_name() == switchPokemon[0].get_name()) or joueur.team[0].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[0])
                    joueur.set_pokemon(1,switchPokemon[0])
                    switchMenuRunning = False
        if Poke2.collidepoint((mx,my)):
            if click:
                if (joueur.team[1].get_name() == switchPokemon[0].get_name()) or joueur.team[1].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[1])
                    joueur.set_pokemon(2,switchPokemon[0])
                    switchMenuRunning = False
        if Poke3.collidepoint((mx,my)):
            if click:
                if (joueur.team[2].get_name() == switchPokemon[0].get_name()) or joueur.team[2].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[2])
                    joueur.set_pokemon(3,switchPokemon[0])
                    switchMenuRunning = False
        if Poke4.collidepoint((mx,my)):
            if click:
                if (joueur.team[3].get_name() == switchPokemon[0].get_name()) or joueur.team[3].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[3])
                    joueur.set_pokemon(4,switchPokemon[0])
                    switchMenuRunning = False
        if Poke5.collidepoint((mx,my)):
            if click:
                if (joueur.team[4].get_name() == switchPokemon[0].get_name()) or joueur.team[4].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[4])
                    joueur.set_pokemon(5,switchPokemon[0])
                    switchMenuRunning = False
        if Poke6.collidepoint((mx,my)):
            if click:
                if (joueur.team[5].get_name() == switchPokemon[0].get_name()) or joueur.team[5].get_name() == "None":
                    switchMenuRunning = False
                else:
                    joueur.set_pokemon(switchPokemon[1],joueur.team[5])
                    joueur.set_pokemon(6,switchPokemon[0])
                    switchMenuRunning = False
        #affiche tous les boutons et le texte
        draw_text("Choisissez un pokemon à échanger", fontMenuChoice, (221,190,76), screen, 50,600)
        display_pokemon_in_menu()

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

def select_pokemon(pokemonNb,condition):
    """Fenetre pour changer de place de Nomekop dans l'équipe""" #condition : en combat ou après une mort (battle,pause)
    click = False
    select_pokemonRunning = True
    mxWhenClicked,myWhenClicked = pygame.mouse.get_pos()
    while select_pokemonRunning:

        mx, my = pygame.mouse.get_pos()

        options = pygame.Rect(mxWhenClicked,myWhenClicked,75,100)
        pygame.draw.rect(screen, (0,255,255), options)
        switch = pygame.Rect(mxWhenClicked,myWhenClicked,75,50)
        pygame.draw.rect(screen, (219,187,66), switch)
        equip = pygame.Rect(mxWhenClicked,myWhenClicked+50,75,50)
        pygame.draw.rect(screen, (245,209,75), equip)
        if condition == "battle" or condition == "death":
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
                if condition == "battle" and joueur.get_currentPokemon().get_name() == joueur.team[pokemonNb-1].get_name():
                    print(f"{joueur.get_currentPokemon().get_name()} est déjà en combat")
                    select_pokemonRunning = False
                elif (condition == "battle" or condition == "death") and joueur.team[pokemonNb-1].get_name() == "None":
                    print("Ceci n'est pas un pokémon")
                elif condition == "battle" or condition == "death":
                    joueur.set_currentPokemon(joueur.team[pokemonNb-1])
                    image_update("joueur")
                    IA_tour = threading.Thread(target = tourIA(), args = ())
                    IA_tour.start()
                    block_user_control(IA_tour)
                    global teamMenuRunning
                    teamMenuRunning = False
                    select_pokemonRunning = False
                elif condition == "pause":
                    global switchPokemon
                    switchPokemon = [joueur.team[pokemonNb-1],pokemonNb] #Pokemon / position dans la team
                    switchMenu()
                    joueur.set_currentPokemon(joueur.get_pokemon(1))
                    select_pokemonRunning = False
                    
        display_pokemon_in_menu()         
        
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
    """Interface qui permet au joueur de réorganiser son équipe, de continuer la partie, ou de la quitter"""
    shutil.rmtree("cache/start")
    click = False
    gameRunning = True
    bgw = pygame.image.load('Design/Interface/gestionback.png')
    Sign1 = pygame.image.load('Design/Interface/continuer.png').convert_alpha()
    Sign2 = pygame.image.load('Design/Interface/equipe.png').convert_alpha()
    
    """Menu d'attente -> organiser son équipe"""
    while gameRunning:
        pygame.display.flip()
        screen.blit(bgw,(0,0))
        s1 = screen.blit(Sign1,(700,330))
        s2 = screen.blit(Sign2,(130,280))
        if lose == True:
            gameRunning = False
        
        draw_text(f"STAGE : {joueur.get_stage()}", fontMenu, (229,192,57), screen, 450,500)
        draw_text("Clique sur les panneaux", fontMenuChoice, (229,192,57), screen, 500,930)
        mx, my = pygame.mouse.get_pos()

        #bouton next
        
        if s1.collidepoint((mx,my)):
            if click:
                #prochain combat
                joueur.save_team()
                init_IA("wild")
                IA.team[0].level_up(joueur.get_stage())
                joueur.team[0].level_up(joueur.get_stage())
                battle()
                joueur.reset_team()
                joueur.update_team()
                joueur.set_stage(joueur.get_stage()+1)
        
        if s2.collidepoint((mx,my)):
            if click:
                #ouvre l'équipe du joueur
                teamMenu("pause")

        
        leave = pygame.Rect(x*0.87,y*0.89,x*0.125,y*0.1)
        #bouton quitter
        
        if leave.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        #affiche tous les boutons et le texte
        pygame.draw.rect(screen, (96,191,40), leave)
        draw_text("Quitter", fontMenuChoice, (133,222,81), screen, x*0.9,y*0.925)

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

def block_user_control(wait):
    """Bloque les commandes du joueur pendant le tour de l'adversaire"""
    blockedCommand=True
    while blockedCommand:
        blockMenu = pygame.Rect(x*0.025,y*0.6,x*0.95,y*0.375)
        pygame.draw.rect(screen, (255,255,255),blockMenu)
        if not wait.is_alive():
            blockedCommand = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def tourIA():
    """IA lance une attaque sur le joueur"""
    attaque = random.randint(0,3)
    IA.get_currentPokemon().attack_target(joueur.get_currentPokemon(),IA.get_currentPokemon().moveSet[attaque])
    print(f"{IA.get_name()} utilise {IA.get_currentPokemon().moveSet[attaque]}")
    time.sleep(0.5)

def tourJoueur(numAttaque):
    """Le joueur lance une attaque sur l'adversaire (IA)"""
    joueur.get_currentPokemon().attack_target(IA.get_currentPokemon(),joueur.get_currentPokemon().moveSet[numAttaque-1])
    print(f"{joueur.get_name()} utilise {joueur.get_currentPokemon().moveSet[numAttaque-1]}")
def tour(numAttaqueJoueur):
    """Regarde la vie des deux adversaire et en informe le joueur"""

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
    """Regarde s'il reste des Nomekop en vie dans l'équipe"""
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
            for i in range(len(IA.team)):
                if IA.get_pokemon(i+1).get_name() != "None":
                    IA.set_currentPokemon(IA.get_pokemon(i+1))
            print(f"{IA.get_name()} envoie {IA.get_currentPokemon().get_name()}")
            image_update("IA")
    elif is_dead(joueur.get_currentPokemon()):
        print(f"{joueur.get_currentPokemon().get_name()} est mort")
        joueur.set_pokemon(joueur.get_currentPokemon_position()+1,notPokemon)
        if joueur.has_pokemon_remaining() == False:
            print("Perdu!")
            global lose
            lose = True
            dead()
        else:
            joueur.sort_team()
            teamMenu("death")
            image_update("joueur")

def is_dead(pokemon):
    """Regarde si un NomeKop est mort"""
    if pokemon.get_hp() <= 0:
        return True
    return False


notPokemon = pokemon.Pokemon(0,"None","","",0,0,0,0,0,0,0,False,[])

def init_game():
    """Initialise les équipes des deux cotés"""
    global joueur
    global lose
    lose = False
    #Pokemon1 = Poke
    #inputPlayer = "joueur test"
    #Pokemon1 = CSV_import.PokeCSV(random.randint(1,649))
    Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6 = notPokemon, notPokemon, notPokemon, notPokemon, notPokemon, notPokemon
    #Pokemon2 = CSV_import.PokeCSV(random.randint(1,649))
    Pokemon3 = CSV_import.PokeCSV(random.randint(1,649))
    joueur = player.Player("notDefined",[Pokemon1, Pokemon2, Pokemon3, Pokemon4, Pokemon5, Pokemon6],[])
    joueur.update_team()

def init_IA(typeIA): #IAtype wild / trainer / etc...
    """Defini le type d'IA"""
    global IA
    if typeIA == "start":
        IA = player.Player("IA",[CSV_import.PokeCSV(random.randint(1,649)),CSV_import.PokeCSV(random.randint(1,649)),CSV_import.PokeCSV(random.randint(1,649))],[])
    elif typeIA == "wild":
        IA = player.Player("IA",[CSV_import.PokeCSV(random.randint(1,649))],[])
    elif typeIA == "trainer":
        IA = player.Player("IA",[CSV_import.PokeCSV(random.randint(1,649)),CSV_import.PokeCSV(random.randint(1,649))],[])
    IA.update_team()

def image_update(player):
    """Permet d'associer le Nomekop avec son image"""
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
    elif player == "start":
        if not os.path.exists("cache/start"):
            os.makedirs("cache/start")
        imageImport.importPokemonImage(IA.team[0].get_name().lower(),player)
        imageImport.importPokemonImage(IA.team[1].get_name().lower(),player)
        imageImport.importPokemonImage(IA.team[2].get_name().lower(),player)
        global pokeChoice1 , pokeChoice2, pokeChoice3
        pokeChoice1 = pygame.image.load("cache/start/"+IA.team[0].get_name()+".png").convert_alpha()
        pokeChoice2 = pygame.image.load("cache/start/"+IA.team[1].get_name()+".png").convert_alpha()
        pokeChoice3 = pygame.image.load("cache/start/"+IA.team[2].get_name()+".png").convert_alpha()
        pokeChoice1 = pygame.transform.scale(pokeChoice1, (360, 360))
        pokeChoice2 = pygame.transform.scale(pokeChoice2, (360, 360))
        pokeChoice3 = pygame.transform.scale(pokeChoice3, (360, 360))

def display_pokemon_in_menu():
    """Affiche le nom du Nomekop"""
    xCoords = [125,525,925,125,525,925]
    yCoords = [650,650,650,850,850,850]
    for i in range(len(joueur.team)):
        if joueur.team[i].get_name() != "None":
            draw_text(f"{joueur.team[i].get_name()}", fontMenuChoice, (0,0,0), screen, xCoords[i],yCoords[i])

def dead():
    bg = pygame.image.load('Design/Interface/death.png')
    a = True
    while a :

        pygame.display.flip()
        screen.blit(bg, (0, 0))
        draw_text("Press space to continue", fontMenuChoice, (255,255,255), screen, 100,800)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a = False
                    
                    

        pygame.display.update()
        mainClock.tick(60)

        
start()
