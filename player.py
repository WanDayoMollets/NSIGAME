class Player:

    def __init__(self,playerName : str,team : list,bag : list,stage=1):
        self.playerName = playerName
        self.team = team #au début [Pokemon1,Pokemon2,Pokemon3->statut none si pas dans l'equipe]
        self.bag = bag #[[nbObjet,objet]]
        self.stage = stage

    def get_name(self):
        return self.playerName
