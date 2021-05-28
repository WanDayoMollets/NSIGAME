import requests
import shutil

def importPokemonImage(pokemonName,playerType):
    replaceChar = " "
    pokemonName = pokemonName.replace(replaceChar,"-")
    if playerType == "joueur":
        image_url = "https://img.pokemondb.net/sprites/black-white/back-normal/"+pokemonName+".png"
    elif playerType == "IA":
        image_url = "https://img.pokemondb.net/sprites/black-white/normal/"+pokemonName+".png"

    filename = "cache/"+playerType+"/currentPokemon.png"

    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')