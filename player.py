from pygame.image import save
import pokemon
import moves

class Player:

    def __init__(self,playerName : str,team : list,bag : list,stage=1):
        self.playerName = playerName
        self.team = team 
        self.bag = bag #[[nbObjet,objet]]
        self.stage = stage
        self.currentPokemon = self.team[0]

    def get_name(self):
        return self.playerName

    def get_pokemon(self,nb):
        return self.team[nb-1]
    
    def set_pokemon(self,nb,pokemon):
        self.team[nb-1] = pokemon
    
    def get_stage(self):
        return self.stage
    
    def set_stage(self,stage):
        self.stage = stage
    
    def get_currentPokemon(self):
        return self.currentPokemon

    def set_currentPokemon(self,pokemon):
        self.currentPokemon = pokemon
    
    def has_pokemon_remaining(self):
        pokemonInTeam = 0
        for pokemon in self.team:
            if pokemon.get_name() != "None":
                pokemonInTeam += 1
        if pokemonInTeam == 0:
            return False
        return True
    
    def get_currentPokemon_position(self):
        for i in range(len(self.team)):
            if self.team[i].get_name() == self.currentPokemon.get_name():
                return i
    
    def update_team(self):
        for i in range(len(self.team)):
            if self.team[i].get_name() != "None":
                self.team[i].update_stats()
    
    #save les stats du pokemon

    def save_team(self):
        for i in range(len(self.team)):
            self.team[i].save_stats()
    
    def reset_team(self):
        for i in range(len(self.team)):
            self.team[i].reset_stats()
                 