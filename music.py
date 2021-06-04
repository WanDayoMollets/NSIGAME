import pygame
import random
import sys
import os
import urllib.request
x,y=1280,960
window_resolution = (x,y)
launched = True
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode(window_resolution)
pygame.init()
pygame.display.set_caption("Nomékop")

def playMusique(event,idPokemon=0):
    pygame.mixer.init()
    a = True
    if pygame.mixer.get_busy() == True:
        print("yes")
    if event == "battle":
        if idPokemon <= 151:
            Musique=f"Gen1_{random.randint(1,1)}.ogg"
        elif idPokemon <= 251:
            Musique=f"Gen2_{random.randint(1,3)}.ogg"
        elif idPokemon <= 386:
            Musique=f"Gen3_{random.randint(1,2)}.ogg"
        elif idPokemon <= 493:
            Musique=f"Gen4_{random.randint(1,7)}.ogg"
        elif idPokemon <= 649:
            Musique=f"Gen5_{random.randint(1,3)}.ogg"
        else:
            print("pas bon")
        pygame.mixer.music.load("musiques/WildBattle/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
    if event == "pause":
        Musique=f"Gen4_{random.randint(1,3)}.ogg"
        pygame.mixer.music.load("musiques/Pause/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        print(Musique)
    if event == "intro":
        Musique=f"Gen4.ogg"
        pygame.mixer.music.load("musiques/Intro/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        print(Musique)
    
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()           

        pygame.display.update()
        mainClock.tick(60)
