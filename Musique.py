import pygame
import random
import os

x,y=1000,640
window_resolution = (x,y)
launched = True

pygame.init()
pygame.display.set_caption("Test musique jeu NSI")
window_surface = pygame.display.set_mode(window_resolution)


selectMusique=int(input("Entrez l'id d'un pokémon : ")) #id du pokemon à la place de l'input
if selectMusique <= 151:
    Musique=f"Gen1_{random.randint(1,1)}.ogg"
elif selectMusique <= 251:
    Musique=f"Gen2_{random.randint(1,3)}.ogg"
elif selectMusique <= 386:
    Musique=f"Gen3_{random.randint(1,2)}.ogg"
elif selectMusique <= 493:
    Musique=f"Gen4_{random.randint(1,3)}.ogg"
elif selectMusique <= 649:
    Musique=f"Gen5_{random.randint(1,3)}.ogg"
elif selectMusique <= 721:
    Musique=f"Gen6_{random.randint(1,2)}.ogg"
elif selectMusique <= 809:
    Musique=f"Gen7_{random.randint(1,3)}.ogg"
elif selectMusique <= 898:
    Musique=f"Gen8_{random.randint(1,1)}.ogg"
else:
    print("pas bon")

print(Musique)


"""

song = pygame.mixer.Sound("Gen1.ogg")
song.set_volume(0.1)
song.play(0,0,1000)
"""
#pygame.mixer.init(22050,16,2,4096)
pygame.mixer.music.load("musiques/WildBattle/"+Musique) #musiques/WildBattle/+Musique
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

"""
charger id random pour le combat
regarder le nom du pokemon lié à cet id
charger le nom du pokemon/png 
si n'existe pas charger le nom du pokemon/jpg
si n'existe pas charger image notexture
"""
pokemonRandom="bidoof.png"

pokemonj=pygame.image.load("images/alakazam.png").convert_alpha()
pokemonP=pygame.transform.flip(pokemonj,True,False)
pokemonIA=pygame.image.load("images/"+pokemonRandom).convert_alpha()



while launched:
    window_surface.blit(pokemonP,(0.2*x,0.3*y)) 
    window_surface.blit(pokemonIA,(0.7*x,0.1*y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    pygame.display.flip()