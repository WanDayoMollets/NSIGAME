class Move:

    def __init__(self,id_move : int,name : str,type_move : str,category : str,power : int,accuracy : int,pp : int):
        self.id_move = id_move
        self.name = name
        self.type_move = type_move
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

    def get_id_move(self):
        return self.id_move

    def get_name(self):
        return self.name

    def get_type_move(self):
        return self.type_move

    def get_category(self):
        return self.category

    def get_power(self):
        return self.power

    def get_accuracy(self):
        return self.accuracy

    def get_pp(self):
        return self.pp

    def set_pp(self,pp):
        self.pp = pp
