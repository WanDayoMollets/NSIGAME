import pokemon
import csv
import random
import moves


def CSV(id_poke):
    """Ouvre le CSV des pokemons et retourne les caracteristiques du pokemon sous forme de liste"""
    poke = [] #creer une liste vide
    with open('BDD/pokemon.csv') as csv_file: #ouvre le fichier pokemon.csv
        csv_reader = csv.reader(csv_file, delimiter=',') #place les lignes du csv dans une variable
        for row in csv_reader: #parcours des lignes du csv
            if row[0] == str(id_poke): #si l'id de la ligne = id du pokemon
                poke = list(row) #variable = ligne correspondante dans le csv
    return(poke) #retourne une liste avec les caracteristiques du poke

def attack():
    """Ouvre le CSV des attaque et retourne les caracteristiques de l'attaque sous forme de liste"""
    id_attack = random.randint(1,702) #prend l'id d'une attaque random
    with open('BDD/moves.csv') as csv_file: #ouvre le fichier moves.csv
        csv_reader = csv.reader(csv_file, delimiter=',') #place les lignes du csv dans une variable
        for row in csv_reader: #parcours des lignes du csv
            if row[0] == str(id_attack): #si l'id de la ligne = id de l'attaque
                attack = list(row) #variable = ligne correspondante dans le csv
    return attack #retourne une liste avec les caracteristiques de l'attaque

def PokeCSV(id_poke):
    """Retourne le pokemon correspondant à l'ID donné avec des attaques random"""
    Stats = CSV(id_poke) #ajoute les caracteristiques d'un pokemon dans une variable
    noneAttaque = moves.Move(0,"None","","",0,0,0) #creation d'une attaque vide
    attacks = [noneAttaque,noneAttaque,noneAttaque,noneAttaque] #creation d'un moveset d'attaques vides

    for i in range(len(attacks)): #boucle for de longueur 4
        while attacks[i].get_name() == "None": #tant que le nom de l'attaque est None
            try: #verifie si l'attaque peut correctement être initialisée
                attackStats = attack() #enregistre les caracteristiques de l'attaque dans une variable

                #remplace les attaques vides par l'attaque dernierement initialisée
                attacks[i] = moves.Move(int(attackStats[0]),str(attackStats[1]),str(attackStats[3]),str(attackStats[4]),int(attackStats[5]),int(attackStats[6]),int(attackStats[7]))
            except:
                print("echec de l'importation de l'attaque. Nouvelle tentative")
                
    #creer un objet pokemon à partir de la liste de ses caracteristiques et en lui ajoutant les attaques precedemment initialisées                   
    outputPokemon = pokemon.Pokemon(int(Stats[0]),str(Stats[1]),str(Stats[2]),str(Stats[3]),int(Stats[5]),int(Stats[6]),int(Stats[7]),int(Stats[8]),int(Stats[9]),int(Stats[10]),int(Stats[11]),bool(Stats[12]),[attacks[0],attacks[1],attacks[2],attacks[3]])

    return outputPokemon #retourne un pokemon avec des attaques random



