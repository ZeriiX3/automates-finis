# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH


# IMPORT
from B7_fonction import *
from B7_affichage import *


# Debut du Main
start = True
while start != False:

    logo()

    num = choix_automate()
    if num == False:
        choice = 0
        start = False
        print_blue("\nMerci de votre utilisation, à bientôt !")
    else:
        choice = 99991

        # Lecture des fichiers txt
        automate = "B7_automates/B7-" + str(num) + ".txt"
        tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats = lire_fichier(automate)

    while choice != 0: # Boucle du menu principal avec ses conditions

            print_green("\n=====================       Menu Principal       =====================\n")

            print("Automate n°", num, "\n")
            print("1: Afficher l'automate")
            print("2: Information sur l'automate")
            print("3: Opérations sur l'automate")
            print("4: Reconnaissance de mots")
            print_yellow("0: Changer d'automate\n")

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
                    print_blue("L'automate est standard")
                else:
                    print_red("L'automate n'est pas standard")

                if est_deter(tr, ei):
                    print_blue("L'automate est deterministe")
                else:
                    print_red("L'automate n'est pas deterministe")

                if est_complet(tr, nb_symb, nb_etats, liste_etats):
                    print_blue("L'automate est complet")
                else:
                    print_red("L'automate n'est pas complet")
                print("--------------------------------------------------------------------")

            # Opérations
            elif choice == 3:
                op = -1
                while op != 0:
                    print("")
                    print_light_green("1: Standardiser")
                    print_light_green("2: Déterminiser")
                    print_light_green("3: Compléter")
                    print_light_green("4: Complémentariser")
                    print_yellow("0: Retour")
                    try:
                        op = int(input(">>> "))
                    except ValueError:
                        print_red(">>>>>> Veuillez entrer un ENTIER <<<<<<<")

                    if op == 1:
                        print_light_green("\n========== Standardisation ==========\n")
                        tr, ei, et, nb_etats, nb_tr, liste_etats = standardiser(tr, ei, et, nb_etats, nb_tr, liste_etats)
                        affichage(tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats)

                    elif op == 2:
                        print_light_green("\n========== Déterminisation ==========\n")
                        print("En cours de développement...")

                    elif op == 3:
                        print_light_green("\n========== Complétation ==========\n")
                        tr, nb_symb, nb_etats, nb_tr, liste_etats = completer(tr, nb_symb, nb_etats, nb_tr, liste_etats)
                        affichage(tr, ei, et, nb_symb, nb_etats, nb_tr, liste_etats)

                    elif op == 4:
                        print_light_green("\n========== Complémentarisation ==========\n")
                        if est_standard(tr, ei) and est_complet(tr, nb_symb, nb_etats, liste_etats):
                            print("En cours de développement...")
                        else:
                            print_red("Ne peut pas être complémentariser")

            elif choice == 4:
                print_light_green("\n======= Reconnaissance =======\n")
                print("En cours de développement...")
