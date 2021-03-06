import random
import math
import moves

class Pokemon:

    def __init__(self,pokemon_id : int,name : str,type1 : str,type2 : str,Base_hp : int,Base_attack : int,Base_defense : int,Base_sp_attack : int,Base_sp_defense : int,Base_speed : int, generation : int,legendary : bool,moveset : list):
        """creer un pokemon avec son id, son som, son type 1, son type 2, ses stats de base, sa generation, si legendaire ou non et ses attaques"""
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
        self.saved_hp = Base_hp
        self.saved_attack = Base_attack
        self.saved_defense = Base_defense
        self.saved_sp_attack = Base_sp_attack
        self.saved_sp_defense = Base_sp_defense
        self.saved_speed = Base_speed
        self.level = 1
        self.legendary = legendary
        self.EV_hp = random.randint(1,255)
        self.EV_attack = random.randint(1,255)
        self.EV_defense = random.randint(1,255)
        self.EV_sp_attack = random.randint(1,255)
        self.EV_sp_defense = random.randint(1,255)
        self.EV_speed = random.randint(1,255)
        self.IV_hp = random.randint(0,31)
        self.IV_attack = random.randint(0,31)
        self.IV_defense = random.randint(0,31)
        self.IV_sp_attack = random.randint(0,31)
        self.IV_sp_defense = random.randint(0,31)
        self.IV_speed = random.randint(0,31)
        self.moveSet = moveset
        self.generation = generation
        
    def get_generation(self):
        return self.generation
       
    def get_pokemon_move(self,moveNb):
        """recupere 1 des 4 moves du pokemon"""
        return self.moveSet[moveNb-1].name
    def get_pokemon_move_category(self,moveNb):
        """Donne la cat??gorie d'1 des 4 moves du pokemon"""
        return self.moveSet[moveNb-1].category
    
    def get_pokemon_move_power(self,moveNb):
        """Donne la cat??gorie d'1 des 4 moves du pokemon"""
        return self.moveSet[moveNb-1].power
    
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
    
    def get_saved_hp(self):
        return self.saved_hp

    def get_saved_attack(self):
        return self.saved_attack

    def get_saved_defense(self):
        return self.saved_defense

    def get_saved_sp_attack(self):
        return self.saved_sp_attack

    def get_saved_sp_defense(self):
        return self.saved_sp_defense

    def get_saved_speed(self):
        return self.saved_speed
    
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
    
    def set_saved_hp(self,hp):
        self.saved_hp = hp

    def set_saved_attack(self,attack):
        self.saved_attack = attack

    def set_saved_defense(self,defense):
        self.saved_defense = defense

    def set_saved_sp_attack(self,sp_attack):
        self.saved_sp_attack = sp_attack

    def set_saved_sp_defense(self,sp_defense):
        self.saved_sp_defense = sp_defense

    def set_saved_speed(self,speed):
        self.saved_speed = speed

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

    def level_up(self,level):
        """Ajoute des niveaux ?? un Nomekop"""
        self.set_level(level)
        self.update_stats()
    
    def save_stats(self):
        """Enregistre les stats du Nomekop"""
        self.set_saved_hp(self.get_hp())
        self.set_saved_attack(self.get_attack())
        self.set_saved_defense(self.get_defense())
        self.set_saved_sp_attack(self.get_sp_attack())
        self.set_saved_sp_defense(self.get_sp_defense())
        self.set_saved_speed(self.get_speed())
    
    def reset_stats(self):
        """Remet les stats enregistrer d'un Nomekop"""
        self.set_hp(self.get_saved_hp())
        self.set_attack(self.get_saved_attack())
        self.set_defense(self.get_saved_defense())
        self.set_sp_attack(self.get_saved_sp_attack())
        self.set_sp_defense(self.get_saved_sp_defense())
        self.set_speed(self.get_saved_speed())
    
    def damage(self, damage):
        """Enleve de la vie en fonction des damages re??us"""
        self.hp -= damage

    def attack_target(self, target, move):
        """Attaque une cible, et lui fait des d??gats ou statut"""
        global attackType
        global defenseType
        if move.accuracy == 100 or random.randint(0,99) < move.accuracy:
            if move.category == "Physical":
                attackType = self.attack
                defenseType = target.defense
            elif move.category == "Special":
                attackType = self.sp_attack
                defenseType = target.sp_defense
            elif move.category == "Status":
                print("not implemented yet")
            if self.type1 == move.type_move or self.type2 == move.type_move:
                STAB = 1.5
            else:
                STAB = 1
            Mod1 = 1
            Mod2 = 1
            Mod3 = 1
            CC = 1
            R = random.randint(85,100)/100
            Type1 = 1
            Type2 = 1
            damage = math.floor(((((((self.level*0.4)+2)*move.power*attackType/50)/defenseType)*Mod1)/2)*CC*Mod2*R)*STAB*Type1*Type2*Mod3
            if damage == 0:
                target.damage(1)
            else:
                target.damage(damage)
            print(damage)
        else:
            print("attaque a ??chou??")
            
