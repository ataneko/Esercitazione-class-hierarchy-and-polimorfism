from CarnivorousMammal import CarnivorousMammal

class Canide(CarnivorousMammal):
    """Classe per i canidi, sottoclasse di CarnivorousMammal."""
    descrizione =("CANIDI:\tFamiglia di mammiferi carnivori che comprende cani, lupi,"+\
                       "\n\tvolpi e altri animali simili, noti per il loro comportamento sociale"+\
                       "\n\te le loro abilità di caccia in branco.")
    
    def __init__(self,age,life,personality,fur_type,color,race,size,origin):
        super().__init__(age,life,personality,fur_type,color,race)
        self.__size=size
        self.__origin = origin

    def get_size(self):
        return self.__size
    def set_size(self,new_size):
        self.__size=new_size

    def get_origin(self):
        return self.__origin
    def set_origin(self,new_origin):
        self.__origin=new_origin

    def __str__(self):
        return (super().__str__()+(f"Taglia:{self.__size}\n"
                                f"Origine:{self.__origin}\n"))
    
    def print_legenda(self):
        print(Canide.descrizione)

    def comunicate(self):
        print("Il canide ulula")