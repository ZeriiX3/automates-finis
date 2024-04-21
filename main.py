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

    logo()

    num = choix_automate()
    if num == False:
        choice = 0
        start = False
        print("\nMerci de votre utilisation, à bientôt !")
    else:
        choice = 99991

        # Lecture des fichiers txt
        automate = "automates/B7-" + str(num) + ".txt"
        tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats = lire_fichier(automate)

    while choice != 0: # Boucle du menu principal avec ses conditions

            print("\n=====================       Menu Principal       =====================\n")

            print("Automate n°", num, "\n")
            print("1: Afficher l'automate")
            print("2: Information sur l'automate")
            print("3: Opérations sur l'automate")
            print("4: Reconnaissance de mots")
            print("0: Changer d'automate\n")

            try:
                choice = int(input(">>> "))
            except ValueError:
                print_red(">>>>>> Veuillez entrer un ENTIER <<<<<<<")


            # Affichage de l'automate
            if choice == 1:
                print("\n")
                affichage(tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats)

            elif choice == 2:   # Information sur l'automate
                print("\n--------------------------------------------------------------------")
                if est_standard(tr, ei):
                    print("L'automate est standard")
                else:
                    print("L'automate n'est pas standard")

                if est_deter(tr, ei):
                    print("L'automate est deterministe")
                else:
                    print("L'automate n'est pas deterministe")

                if est_complet(tr, nb_symb, nb_etats, liste_etats):
                    print("L'automate est complet")
                else:
                    print("L'automate n'est pas complet")
                print("--------------------------------------------------------------------")

            elif choice == 3:
                op = -1
                while op != 0:
                    print("")
                    print("1: Standardiser")
                    print("2: Déterminiser")
                    print("0: Retour")
                    try:
                        op = int(input(">>> "))
                    except ValueError:
                        print_red(">>>>>> Veuillez entrer un ENTIER <<<<<<<")

                    if op == 1:
                        print("\n======= Standardisation =======\n")
                        tr, ei, et, nb_etats, nb_tr, liste_etats = standardiser(tr, ei, et, nb_etats, nb_tr, liste_etats)
                        affichage(tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats)

                    elif op == 2:
                        print("\n======= Déterminisation =======\n")
                        print("En cours de développement...")

            elif choice == 4:
                print("======= Reconnaissance =======")
