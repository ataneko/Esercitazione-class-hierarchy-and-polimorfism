MAMMAL =1
FELINE =2
CAT = 3
CANID = 4
DOG = 5
EXIT = 6

import ClassHierarchy
def ask_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Per favore, inserisci un numero valido.")
def ask_base_info():
    age = ask_number("Inserisci l'età dell'animale: ")
    life = ask_number("Inserisci l'aspettativa di vita dell'animale: ")
    personality = input("Inserisci la personalità dell'animale: ")
    fur_type = input("Inserisci il tipo di pelo dell'animale: ")
    color = input("Inserisci il colore dell'animale: ")
    race = input("Inserisci la razza dell'animale: ")
    return age, life, personality, fur_type, color, race

def ask_felino_info():
    habitat = input("Inserisci l'habitat del felino: ")
    prey = input("Inserisci le prede del felino: ")
    return habitat, prey

def ask_gatto_info():
    name = input("Inserisci il nome del gatto: ")
    return name

def  ask_canide_info():
    size = input("Inserisci la taglia del canide: ")
    origin = input("Inserisci l'origine del canide: ")
    return size, origin

def ask_cane_info():
    name = input("Inserisci il nome del cane: ")
    used_for = input("Inserisci l'addestramento del cane: ")
    return name, used_for

def display_animal(animal):
    print("\nDettagli dell'animale:")
    animal.print_legenda()
    print(animal)
    animal.comunicate()
    print("-" * 40)

def display_menu():
    print("Seleziona il tipo di animale da creare:")
    print("1. Mammifero Carnivoro")
    print("2. Felino")
    print("3. Gatto")
    print("4. Canide")
    print("5. Cane")
    print("6. Esci")

def main():
    while True:
        display_menu()
        choice = ask_number("Inserisci la tua scelta (1-5): ")
        if choice in (MAMMAL, FELINE, CAT, CANID, DOG):
            age, life, personality, fur_type, color, race = ask_base_info()
            if choice == MAMMAL:
                animale = ClassHierarchy.Carnivorous(age, life, personality, fur_type, color, race)
                display_animal(animale)
            elif choice == FELINE:
                habitat, prey = ask_felino_info()
                animale = ClassHierarchy.Felin(age, life, personality, fur_type, color, race, habitat, prey)
                display_animal(animale)
            elif choice == CAT:
                habitat, prey = ask_felino_info()
                name = ask_gatto_info()
                animale = ClassHierarchy.Cat(age, life, personality, fur_type, color, race, habitat, prey, name)
                display_animal(animale)
            elif choice == CANID:
                size, origin = ask_canide_info()
                animale = ClassHierarchy.Canid(age, life, personality, fur_type, color, race, size, origin)
                display_animal(animale)
            elif choice == DOG:
                size, origin = ask_canide_info()
                name, used_for = ask_cane_info()
                animale = ClassHierarchy.Dog(age, life, personality, fur_type, color, race, size, origin, name, used_for)
                display_animal(animale)
        elif choice == EXIT:
            print("Uscita dal programma.")
            break


if __name__ == "__main__":
    main()