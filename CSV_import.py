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
    id_attack = random.randint(0,702)
    with open('BDD/moves.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == str(id_attack):
                attack = list(row)
    return attack

def PokeCSV(id_poke):

    Stats = CSV(id_poke)
    
    stat = attack()
    
    attack1 = moves.Move(str(stat[0]),stat[1],stat[3],stat[4],str(stat[5]),str(stat[6]),str(stat[7]))
    stat = attack()
    
    attack2 = moves.Move(str(stat[0]),stat[1],stat[3],stat[4],str(stat[5]),str(stat[6]),str(stat[7]))
    stat = attack()
    
    attack3 = moves.Move(str(stat[0]),stat[1],stat[3],stat[4],str(stat[5]),str(stat[6]),str(stat[7]))
    stat = attack()
                         
    attack4 = moves.Move(str(stat[0]),stat[1],stat[3],stat[4],str(stat[5]),str(stat[6]),str(stat[7]))
    stat = attack()
                        
    test_poke = pokemon.Pokemon(str(Stats[0]),Stats[1],Stats[2],Stats[3],str(Stats[4]),str(Stats[5]),str(Stats[6]),str(Stats[7]),str(Stats[8]),str(Stats[9]),bool(Stats[10]),[attack1,attack2,attack3,attack4])

    return test_poke



