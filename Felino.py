from CarnivorousMammal import CarnivorousMammal

class Felino(CarnivorousMammal):
    """Classe per i felini, sottoclasse di CarnivorousMammal."""
    descrizione =("FELINI:\tFamiglia di mammiferi carnivori caratterizzati da un corpo agile,"+\
                       "\n\tartigli retrattili e abilità di caccia eccezionali.")
    
    def __init__(self,age,life,personality,fur_type,color,race,habitat,prey):
        super().__init__(age,life,personality,fur_type,color,race)

        self.__habitat = habitat
        self.__prey = prey
    
    def get_habitat(self):
        return self.__habitat
    def set_habitat(self,new_habitat):
        self.__habitat = new_habitat

    def get_prede(self):
        return self.__prede
    def set_prede(self,new_prede):
        self.__prede =new_prede

    def __str__(self):
        return (super().__str__()+(f"Habitat:{self.__habitat}\n"
                                f"Prede:{self.__prey}\n"))
    
    def print_legenda(self):
        print(Felino.descrizione)