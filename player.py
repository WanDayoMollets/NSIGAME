class Player:

    def __init__(self,playerName : str,team : list,bag : list,stage=1,*currentPokemon):
        self.playerName = playerName
        self.team = team #au début [Pokemon1,Pokemon2,Pokemon3->statut none si pas dans l'equipe]
        self.bag = bag #[[nbObjet,objet]]
        self.stage = stage
        self.currentPokemon = self.team[0]

    def get_name(self):
        return self.playerName

    def get_pokemon(self,nb):
        return self.team[nb]
    
    def set_pokemon(self,nb,pokemon):
        self.team[nb] = pokemon
    
    def get_stage(self):
        return self.stage
    
    def set_stage(self,stage):
        self.stage = stage
    
    def get_currentPokemon(self):
        return self.currentPokemon

    def set_currentPokemon(self,pokemon):
        self.currentPokemon = pokemon
