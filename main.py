# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH


# IMPORT
from fonction import *
from affichage import *


# Debut du Main
start = True
while start != False:

    print("PROJET AUTOMATES FINIS\n")

    num = choix_automate()
    if num == False:
        choice = 0
        start = False
        print("\nMerci de votre utilisation, à bientôt !")
    else:
        choice = 9999

    while choice != 0: # Boucle du menu principal avec ses conditions

            print("\n########################       Menu Principal       ########################\n")

            print("Automate n°", num, "\n")
            print("1: Afficher l'automate")
            print("2: Information sur l'automate")
            print("3: Opérations sur l'automate")
            print("4: Reconnaissance de mots")
            print("0: Changer d'automate\n")

            try:
                choice = int(input(">>> "))
            except ValueError:
                print(">>>>>> Veuillez entrer un ENTIER <<<<<<<")


            # Lecture des fichiers txt
            automate = "automates/B7-" + str(num) + ".txt"
            tr, ei, et, nb_symb, nb_etats, nb_tr = lire_fichier_transition(automate)


            # Affichage de l'automate
            if choice == 1:
                print("\n")
                affichage(tr, ei, et, nb_symb, nb_etats, nb_tr)

            elif choice == 2:   # Information sur l'automate
                print("--------------------------------------------------------------------")
                if est_standard(tr, ei):
                    print("L'automate est standard")
                else:
                    print("L'automate n'est pas standard")

                if est_deter(tr, ei):
                    print("L'automate est deterministe")
                else:
                    print("L'automate n'est pas deterministe")

                if est_complet(tr, nb_symb, nb_etats):
                    print("L'automate est complet")
                else:
                    print("L'automate n'est pas complet")
                print("--------------------------------------------------------------------")

            elif choice == 3:
                print("======= Standardisation =======")

            elif choice == 4:
                print("======= Reconnaissance =======")
