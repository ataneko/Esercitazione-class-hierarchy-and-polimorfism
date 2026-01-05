# Esercitazione: Gerarchia delle Classi e Polimorfismo in Python

Questo progetto approfondisce l'uso dell'**ereditarietà** e del **polimorfismo** attraverso la modellazione di una gerarchia di mammiferi.

## Obiettivi Didattici
* **Ereditarietà:** Creazione di una classe base `Mammifero` e classi derivate (es. `Gatto`, `Cane`).
* **Polimorfismo:** Gestione di oggetti diversi tramite un'interfaccia comune.
* **Override dei Metodi:** Personalizzazione del comportamento nelle classi figlie (es. `__str__`, `comunica()`).
* **Keyword `super()`:** Estensione dei metodi della classe padre senza riscrivere il codice.

## Funzionalità
* **Menu Interattivo:** Interfaccia testuale per gestire e visualizzare gli animali.
* **Gestione Trasparente:** La funzione `display_animal(animal)` nel `main.py` sfrutta il polimorfismo: non ha bisogno di conoscere la specie esatta per stampare le informazioni o far "comunicare" l'animale.