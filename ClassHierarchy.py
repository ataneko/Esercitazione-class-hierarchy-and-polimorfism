import CarnivorousMammal
import Felino
import Canide
import Gatto
import Cane

def Carnivorous(age,life,personality,fur_type,color,race):
    return CarnivorousMammal.CarnivorousMammal(age,life,personality,fur_type,color,race)

def Felin(age,life,personality,fur_type,color,race,habitat,prey):
    return Felino.Felino(age,life,personality,fur_type,color,race,habitat,prey)

def Cat(age,life,personality,fur_type,color,race,habitat,prey,name):
    return Gatto.Gatto(age,life,personality,fur_type,color,race,habitat,prey,name)

def Canid(age,life,personality,fur_type,color,race,size,origin):
    return Canide.Canide(age,life,personality,fur_type,color ,race,size,origin)

def Dog(age,life,personality,fur_type,color,race,size,origin,name,used_for):
    return Cane.Cane(age,life,personality,fur_type,color,race,size,origin,name,used_for) 