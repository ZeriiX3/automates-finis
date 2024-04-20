# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH

# IMPORT

# Lecture des fichiers Automates et affichage du tableau des transitions
def lire_fichier_transition(nom_fichier):
    transitions = []
    affichage = []
    with open(nom_fichier, 'r') as f:
        # Lire la première ligne pour le nombre de symboles dans l'alphabet
        nombre_symboles = int(f.readline().strip())

        # Lire la deuxième ligne pour le nombre d'états
        nombre_etats = int(f.readline().strip())

        # Lire la troisième ligne pour le nombre d'états initiaux et leurs numéros
        nombre_etats_initiaux, *etats_initiaux = map(int, f.readline().split())
        # Lire la quatrième ligne pour le nombre d'états terminaux et leurs numéros
        nombre_etats_terminaux, *etats_terminaux = map(int, f.readline().split())
        # Lire la cinquième ligne pour le nombre de transitions
        nombre_transitions = int(f.readline().strip())

        # Lire les transitions à partir de la sixième ligne
        for i in range(nombre_transitions):
            ligne = f.readline().strip()
            etat_depart, symbole, etat_arrivee = ligne[:1], ligne[1], ligne[2:]
            transitions.append([etat_depart, symbole, etat_arrivee, ])

        print("I/O    Etat    ", end='')
        for i in range(1, nombre_symboles + 1):
            # print(chr(ord('a') + i - 1),"    ", end='')
            print("{:<8}".format(chr(ord('a') + i - 1)), end='')
        print("")
        for i in range(nombre_etats):
            a = 8
            if i in etats_initiaux and i in etats_terminaux:
                print("I/O    ", end='')
            elif i in etats_initiaux:
                print("I      ", end='')
            elif i in etats_terminaux:
                print("O      ", end='')
            else:
                print("-      ", end='')
            print(i, "      ", end='')
            for j in range(nombre_transitions):
                if int(transitions[j][0]) == i:
                    if transitions[j][1] == 'a':
                        print(transitions[j][2], end='')
                        a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8
            for k in range(nombre_transitions):
                if int(transitions[k][0]) == i:
                    if transitions[k][1] == 'b':
                        print(transitions[k][2], end='')
                        a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8
            for o in range(nombre_transitions):
                if int(transitions[o][0]) == i:
                    if transitions[o][1] == 'c':
                        print(transitions[o][2], end='')
                        a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8
            for p in range(nombre_transitions):
                if int(transitions[p][0]) == i:
                    if transitions[p][1] == 'd':
                        print(transitions[p][2], end='')
                        a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8
            print()

    return transitions, etats_initiaux, etats_terminaux, nombre_symboles, nombre_etats

