# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès


# IMPORT
from fonction import *
from affichage import *



start = True
while start != False:

    print("PROJET AUTOMATES FINIS\n")

    A = choix_automate()
    if A == False:
        choice = 0
        start = False
        print("\nMerci de votre utilisation, à bientôt !")
    else:
        choice = 9999
        print(choice)

    while choice != 0: # Boucle du menu principal avec ses conditions

            print("\n########################        Menu Principal        ########################\n")

            print("Automate n°",A,"\n")
            print("1: Afficher l'automate")
            print("2: Information sur l'automate")
            print("3: Opérations sur l'automate")
            print("4: Reconnaissance de mots")
            print("0: Changer d'automate\n")

            try:
                choice = int(input(">>> "))
            except ValueError:
                print(">>>>>> Veuillez choisir un ENTIER <<<<<<<")

            if choice == 1:
                AF = lire_automate(A)
                afficher_automate(AF)

            elif choice == 2:   # Information sur l'automate
                print("--------------------------------------------------------------------")
                if feur():
                    print("L'automate est standard")
                else:
                    print("L'automate n'est pas standard")

                if feur():
                    print("L'automate est deterministe")
                else:
                    print("L'automate n'est pas deterministe")

                if feur(G):
                    print("L'automate est complet")
                else:
                    print("L'automate n'est pas complet")
                print("--------------------------------------------------------------------")

            elif choice == 3:
                print("======= Standardisation =======")

            elif choice == 4:
                print("======= Reconnaissance =======")
