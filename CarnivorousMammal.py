class CarnivorousMammal:
    """Classe base per i mammiferi carnivori."""

    descrizione =("MAMMIFERI CARNIVORI:\tAnimali mammiferi che si nutrono principalmente di carne"+\
                                    "\n\te possiedono caratteristiche fisiche e comportamentali"+\
                                    "\n\tad esempio artigli affilati, denti canini sviluppati e"+\
                                    "\n\tistinti predatori.")
    
    def __init__(self,age,life,personality,fur_type,color,race):
        self.__age = age
        self.__life = life
        self.__personality = personality
        self.__fur_type = fur_type
        self.__color = color
        self.__race = race

    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age=new_age

    def get_life(self):
        return self.__life
    def set_life(self,new_life):
        self.__life=new_life

    def get_personality(self):
        return self.__personality
    def set_personality(self,new_personality):
        self.__personality = new_personality
    
    def get_fur_type(self):
        return self.__fur_type
    def set_fur_type(self,new_fur):
        self.__fur_type = new_fur
    
    def get_color(self):
        return self.__color
    def set_color(self,new_color):
        self.__color = new_color

    def get_race(self):
        return self.__race
    def set_race(self,new_race):
        self.__race = new_race

    def __str__(self):
        return (f"Razza:{self.__race}\n"
                f"Personalità:{self.__personality}\n"
                f"Pelo:{self.__fur_type}\n"
                f"Età:{self.__age}\n"
                f"Colore:{self.__color}\n"
                f"Vita:{self.__life}\n")
    
    def print_legenda(self):
        print(CarnivorousMammal.descrizione)
    
    def comunicate(self):
        print("Non e possibile stabilire un suono generico per i mammiferi carnivori")
    
    



