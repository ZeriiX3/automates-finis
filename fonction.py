# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH



def feur():
    return True

def choix_automate():
    while True:
        try:
            print("Veuillez choisir l'automate à utiliser entre 1 et 44")
            print("0: Quitter le programme")
            A = int(input(">>> "))

            if A == 0:
                return False

            if 1 <= A <= 44:
                return A


        except ValueError:
            print("\nVeuillez saisir un nombre entier valide.\n")