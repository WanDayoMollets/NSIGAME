import pokemon
import csv
import random
import moves


def CSV(id_poke):
    poke = []
    with open('BDD/pokemon.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == str(id_poke):
                poke = list(row)
    return(poke)

def attack():
    id_attack = random.randint(1,702)
    with open('BDD/moves.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == str(id_attack):
                attack = list(row)
    return attack

def PokeCSV(id_poke):

    Stats = CSV(id_poke)
    noneAttaque = moves.Move(0,"None","","",0,0,0)
    attacks = [noneAttaque,noneAttaque,noneAttaque,noneAttaque]

    for i in range(len(attacks)):
        attackStats = attack()
        attacks[i] = moves.Move(int(attackStats[0]),str(attackStats[1]),str(attackStats[3]),str(attackStats[4]),int(attackStats[5]),int(attackStats[6]),int(attackStats[7]))
                        
    outputPokemon = pokemon.Pokemon(int(Stats[0]),str(Stats[1]),str(Stats[2]),str(Stats[3]),int(Stats[5]),int(Stats[6]),int(Stats[7]),int(Stats[8]),int(Stats[9]),int(Stats[10]),int(Stats[11]),bool(Stats[12]),[attacks[0],attacks[1],attacks[2],attacks[3]])

    return outputPokemon



