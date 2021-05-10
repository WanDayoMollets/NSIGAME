import random

class Pokemon:

    def __init__(self,pokemon_id,name,type1,type2,Base_hp,Base_attack,Base_defense,Base_sp_attack,Base_sp_defense,Base_speed,legendary,level=1,EV=random.randint(0, 255),IV_hp=0,IV_attack=0,IV_defense=0,IV_sp_attack=0,IV_sp_defense=0,IV_speed=0,hp=0,attack=0,defense=0,sp_attack=0,sp_defense=0,speed=0):
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
        self.EV = EV
        self.IV_hp = IV_hp
        self.IV_attack = IV_attack
        self.IV_defense = IV_defense
        self.IV_sp_attack = IV_sp_attack
        self.IV_sp_defense = IV_sp_defense
        self.IV_speed = IV_speed
        self.hp = hp 
        self.attack = Base_attack
        self.defense = Base_defense
        self.sp_attack = Base_sp_attack
        self.sp_defense = Base_sp_defense
        self.speed = Base_speed
        self.legendary = legendary
        self.level = level
        

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
    
    def get_EV(self):
        return self.EV

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
    
    def set_EV(self,EV):
        self.EV = EV
    
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
    
    def update_IV_hp(self):
        self.IV_hp = ((100*(self.hp-self.level-10))/self.level)-(self.EV/4)-2*self.Base_hp

    def update_hp(self):
        self.hp = (self.IV_hp +2*self.Base_hp+(self.EV/4))*(self.level/100)+10+self.level
    
    def damage(self, damage):
        self.hp -= damage

    def attack_target(self, target):
        target.damage(self.attack)

test = Pokemon(15,"Jibril","feu","eau",180,20,60,25,75,30,False)
test2= Pokemon(15,"Jibril","feu","eau",180,20,60,25,75,30,False)
