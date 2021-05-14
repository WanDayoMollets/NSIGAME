import random
import math
from moves import Move

class Pokemon:

    def __init__(self,pokemon_id : int,name : str,type1 : str,type2 : str,Base_hp : int,Base_attack : int,Base_defense : int,Base_sp_attack : int,Base_sp_defense : int,Base_speed : int,legendary : bool,moveset : list):
        self.pokemon_id = pokemon_id
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.Base_hp = Base_hp
        self.Base_attack = Base_attack
        self.Base_defense = Base_defense
        self.Base_sp_attack = Base_sp_attack
        self.Base_sp_defense = Base_sp_defense
        self.Base_speed = Base_speed
        self.hp = Base_hp 
        self.attack = Base_attack
        self.defense = Base_defense
        self.sp_attack = Base_sp_attack
        self.sp_defense = Base_sp_defense
        self.speed = Base_speed
        self.level = 1
        self.legendary = legendary
        self.EV_hp = random.randint(1,255)
        self.EV_attack = random.randint(1,255)
        self.EV_defense = random.randint(1,255)
        self.EV_sp_attack = random.randint(1,255)
        self.EV_sp_defense = random.randint(1,255)
        self.EV_speed = random.randint(1,255)
        self.IV_hp = random.randint(1,31)
        self.IV_attack = random.randint(1,31)
        self.IV_defense = random.randint(1,31)
        self.IV_sp_attack = random.randint(1,31)
        self.IV_sp_defense = random.randint(1,31)
        self.IV_speed = random.randint(1,31)
        self.moveSet = moveset
        
        
    def get_pokemon_move(self,moveNb):
        return self.moveSet[moveNb-1].name

    def get_pokemon_id(self):
        return self.pokemon_id

    def get_name(self):
        return self.name

    def get_type1(self):
        return self.type1

    def get_type2(self):
        return self.type2

    def get_Base_hp(self):
        return self.Base_hp

    def get_Base_attack(self):
        return self.Base_attack

    def get_Base_defense(self):
        return self.Base_defense

    def get_sp_Base_attack(self):
        return self.sp_Base_attack

    def get_sp_Base_defense(self):
        return self.sp_Base_defense

    def get_Base_speed(self):
        return self.Base_speed

    def get_EV_hp(self):
        return self.EV_hp

    def get_EV_attack(self):
        return self.EV_attack

    def get_EV_defense(self):
        return self.EV_defense

    def get_EV_sp_attack(self):
        return self.EV_sp_attack

    def get_EV_sp_defense(self):
        return self.EV_sp_defense

    def get_EV_speed(self):
        return self.EV_speed

    def get_IV_hp(self):
        return self.IV_hp

    def get_IV_attack(self):
        return self.IV_attack

    def get_IV_defense(self):
        return self.IV_defense

    def get_IV_sp_attack(self):
        return self.IV_sp_attack

    def get_IV_sp_defense(self):
        return self.IV_sp_defense

    def get_IV_speed(self):
        return self.IV_speed

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_sp_attack(self):
        return self.sp_attack

    def get_sp_defense(self):
        return self.sp_defense

    def get_speed(self):
        return self.speed
    
    def is_legendary(self):
        return self.legendary
    
    def get_level(self):
        return self.level
    
    def set_name(self,name):
        self.name = name

    def set_type1(self,type1):
        self.type1 = type1

    def set_type2(self,type2):
        self.type2 = type2

    def set_hp(self,hp):
        self.hp = hp
    
    def set_EV_hp(self,EV_hp):
        self.EV_hp = EV_hp
    
    def set_EV_attack(self,EV_attack):
        self.EV_attack = EV_attack

    def set_EV_defense(self,EV_defense):
        self.EV_defense = EV_defense
    
    def set_EV_sp_attack(self,EV_sp_attack):
        self.EV_sp_attack = EV_sp_attack
    
    def set_EV_sp_defense(self,EV_sp_defense):
        self.EV_sp_defense = EV_sp_defense
    
    def set_EV_speed(self,EV_speed):
        self.EV_speed = EV_speed
    
    def set_IV_hp(self,IV_hp):
        self.IV_hp = IV_hp
    
    def set_IV_attack(self,IV_attack):
        self.IV_attack = IV_attack

    def set_IV_defense(self,IV_defense):
        self.IV_defense = IV_defense
    
    def set_IV_sp_attack(self,IV_sp_attack):
        self.IV_sp_attack = IV_sp_attack
    
    def set_IV_sp_defense(self,IV_sp_defense):
        self.IV_sp_defense = IV_sp_defense
    
    def set_IV_speed(self,IV_speed):
        self.IV_speed = IV_speed

    def set_attack(self,attack):
        self.attack = attack

    def set_defense(self,defense):
        self.defense = defense

    def set_sp_attack(self,sp_attack):
        self.sp_attack = sp_attack

    def set_sp_defense(self,sp_defense):
        self.sp_defense = sp_defense

    def set_speed(self,speed):
        self.speed = speed

    def set_legendary(self,legendary):
        self.legendary = legendary

    def set_level(self,level):
        self.level = level

    def update_hp(self):
        self.set_hp(math.floor((int((2 * self.Base_hp + self.IV_hp + int(self.EV_hp / 4)) * self.level) / 100) + self.level + 10))

    def update_attack(self):
        self.set_attack(math.floor(int((2*self.Base_attack+self.IV_attack+int(self.EV_attack/4))*self.level)/100)+5)

    def update_defense(self):
        self.set_defense(math.floor(int((2*self.Base_defense+self.IV_defense+int(self.EV_defense/4))*self.level)/100)+5)

    def update_sp_attack(self):
        self.set_sp_attack(math.floor(int((2*self.Base_sp_attack+self.IV_sp_attack+int(self.EV_sp_attack/4))*self.level)/100)+5)

    def update_sp_defense(self):
        self.set_sp_defense(math.floor(int((2*self.Base_sp_defense+self.IV_sp_defense+int(self.EV_sp_defense/4))*self.level)/100)+5)

    def update_speed(self):
        self.set_speed(math.floor(int((2*self.Base_speed+self.IV_speed+int(self.EV_speed/4))*self.level)/100)+5)

    def update_stats(self):
        self.update_hp()
        self.update_attack()
        self.update_defense()
        self.update_sp_attack()
        self.update_sp_defense()
        self.update_speed()
    
    def damage(self, damage):
        self.hp -= damage

    def attack_target(self, target, move):
        #ajouter condition en fonction du type pour les faiblesses
        if move.accuracy == 100 or random.randint(0,99) < move.accuracy:
            if move.category == "Physical":
                attackType = self.attack
                defenseType = self.defense
            elif move.category == "Special":
                attackType = self.sp_attack
                defenseType = self.sp_defense
            else:
                attackType = self.attack
                defenseType = self.defense
            if self.type1 == move.type_move or self.type2 == move.type_move:
                STAB = 1
            else:
                STAB = 0.75
            Mod1 = 1
            Mod2 = 1
            Mod3 = 1
            CC = 1
            R = random.randint(85,100)
            Type1 = 1
            Type2 = 1
            target.damage(math.floor((((((((self.level*0.4)+2)*move.power*attackType/50)/defenseType)*Mod1)+2)*CC*Mod2*R/100)*STAB*Type1*Mod3))
            
                
"""
test = Pokemon(12,"yes","feu","vol",55,42,63,35,28,14,False)
test2 = Pokemon(14,"no","feu","vol",55,42,63,35,28,14,False)
attaque1 = Move(1,"feuuu","feu","Special",100,100,15)
attaque2 = Move(2,"boom","sol","Physical",80,100,10)


print(f"nom : {test.get_name()}")
print(f"hp actu {test.get_hp()}")
print(f"atck actu {test.get_attack()}")
print(f"def actu {test.get_defense()}")
print(f"aspe actu {test.get_sp_attack()}")
print(f"dspe actu {test.get_sp_defense()}")
print(f"speed actu {test.get_speed()}")
print(f"lvl actu {test.get_level()}")
test.set_level(50)
test2.set_level(50)
test.update_stats()
test2.update_stats()
print("------------------------------------------------")
print(f"lvl mtn {test.get_level()}")
print(f"hp mtn {test.get_hp()}")
print(f"atck actu {test.get_attack()}")
print(f"def actu {test.get_defense()}")
print(f"aspe actu {test.get_sp_attack()}")
print(f"dspe actu {test.get_sp_defense()}")
print(f"speed actu {test.get_speed()}")
print("----------------------------------------------")
print(f"hp avant attaque: {test2.get_hp()}")
test.attack_target(test2,attaque1)
print(f"Il reste {test2.get_hp()}")
"""