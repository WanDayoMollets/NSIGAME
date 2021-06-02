import pygame
import random
import os
import urllib.request

x,y=1000,640
window_resolution = (x,y)
launched = True

pygame.init()
pygame.display.set_caption("Music")
window_surface = pygame.display.set_mode(window_resolution)
def playMusique(event):
    a = True
    if event == "battle":

        selectMusique=int(input("Entrez l'id d'un pokémon : ")) #id du pokemon à la place de l'input
        if selectMusique <= 151:
            Musique=f"Gen1_{random.randint(1,1)}.ogg"
        elif selectMusique <= 251:
            Musique=f"Gen2_{random.randint(1,3)}.ogg"
        elif selectMusique <= 386:
            Musique=f"Gen3_{random.randint(1,2)}.ogg"
        elif selectMusique <= 493:
            Musique=f"Gen4_{random.randint(1,7)}.ogg"
        elif selectMusique <= 649:
            Musique=f"Gen5_{random.randint(1,3)}.ogg"
        else:
            print("pas bon")
        pygame.mixer.music.load("musiques/WildBattle/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
    if event == "pause":
        Musique=f"Gen4_{random.randint(1,4)}.ogg"
        pygame.mixer.music.load("musiques/Pause/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        print(Musique)
    if event == "intro":
        Musique=f"Gen{random.randint(4,4)}.ogg"
        pygame.mixer.music.load("musiques/Intro/"+Musique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        print(Musique)
    
    while a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                a = False
    

playMusique("battle")
