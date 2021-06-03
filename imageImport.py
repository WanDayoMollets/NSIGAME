import requests
import shutil

def importPokemonImage(pokemonName,playerType): 
    """Importe le sprite d'un pokemon en fonction de son nom, il est enregistré dans un dossier différent en fonction du type de joueur"""
    replaceChar = " " #indique que le caractere à remplacer est l'espace
    pokemonName = pokemonName.replace(replaceChar,"-") #remplace les espaces dans le nom d'un pokemon par des tirets 
    if playerType == "joueur": #si le type de joueur est joueur
        image_url = "https://img.pokemondb.net/sprites/black-white/back-normal/"+pokemonName+".png" #indique l'url de l'image en fonction du nom du pokemon
        filename = "cache/joueur/currentPokemon.png" #indique qu'il faut enregistrer le sprite dans le cache du joueur
    elif playerType == "IA": #si le type de joueur est IA
        image_url = "https://img.pokemondb.net/sprites/black-white/normal/"+pokemonName+".png" #indique l'url de l'image en fonction du nom du pokemon
        filename = "cache/IA/currentPokemon.png" #indique qu'il faut enregistrer le sprite dans le cache de l'IA
    elif playerType == "start": #si le type de joueur est start
        image_url = "https://img.pokemondb.net/sprites/black-white/normal/"+pokemonName+".png" #indique l'url de l'image en fonction du nom du pokemon
        filename = "cache/start/"+pokemonName+".png" #indique qu'il faut enregistrer le sprite dans le cache du start

    r = requests.get(image_url, stream = True) #creer une requete pour recuperer l'image

    if r.status_code == 200: #si l'image peut-être décodée
        r.raw.decode_content = True #décode l'image 

        with open(filename,'wb') as f: #ouvre l'image
            shutil.copyfileobj(r.raw, f) #copie de l'image dans le dossier
            
        print("L'image a été correctement téléchargée :",filename)
    else: #si l'image ne peut-être décodée
        print("L'image ne peut pas être téléchargée")