from Felino import Felino

class Gatto(Felino):
    """Classe per i gatti, sottoclasse di Felino."""
    descrizione =("GATTI:\tPiccoli mammiferi carnivori domestici appartenenti alla famiglia dei felini,"+\
                      "\n\tnoti per la loro agilità, indipendenza e abilità di caccia.")
    
    def __init__(self,age,life,personality,fur_type,color,race,habitat,prey,name):
        super().__init__(age,life,personality,fur_type,color,race,habitat,prey)
        self.__name=name

    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name

    def __str__(self):
        return (f"Nome:{self.__name}\n"+super().__str__()+"\n")
    
    def print_legenda(self):
        print(Gatto.descrizione)
    
    def comunicate(self):
        print("Il gatto miagola")