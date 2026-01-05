from Canide import Canide   

class Cane(Canide):
    """Classe per i cani, sottoclasse di Canide."""
    descrizione =("CANI:\tMammiferi carnivori domestici appartenenti alla famiglia dei canidi,"+\
                     "\n\tnoti per la loro lealtà, addestrabilità e varietà di razze.")
    def __init__(self,age,life,personality,fur_type,color,race,size,origin,name,used_for):
        super().__init__(age,life,personality,fur_type,color,race,size,origin)
        self.__name=name
        self.__used_for=used_for

    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name 
    
    def get_used_for(self):
        return self.__used_for
    def set_used_for(self,new_used_for):
        self.__used_for=new_used_for

    def __str__(self):
        return (f"Nome:{self.__name}\n"+super().__str__()+(f"Usato per:{self.__used_for}\n"))
    
    def print_legenda(self):
        print(Cane.descrizione)
    
    def comunicate(self):
        print("Il cane abbaia")