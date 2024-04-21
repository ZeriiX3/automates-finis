# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH


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
            u = -1
            j = 0
            while u == -1:
                u = ligne.find(chr(ord('a') + j))
                j += 1
            etat_depart, symbole, etat_arrivee = ligne[:u], ligne[u], ligne[u + 1:]
            transitions.append([etat_depart, symbole, etat_arrivee, ])

    return transitions, etats_initiaux, etats_terminaux, nombre_symboles, nombre_etats, nombre_transitions


def est_standard(transitions, etats_initiaux) :
    if len(etats_initiaux) > 1:
        return False
    else :
        for i in range(len(transitions)):
            if int(transitions[i][2]) == int(etats_initiaux[0]) :
                return False
    return True

def est_deter(transitions, etats_initiaux) :
    if len(etats_initiaux) > 1:
        return False
    else :
        for i in range(len(transitions)):
            for j in range(len(transitions)):
                if i != j :
                    if int(transitions[i][0]) == int(transitions[j][0]) :
                        if transitions[i][1] == transitions[j][1] :
                            return False
    return True

def est_complet(transitions, nombre_symboles, nombre_etats) :
    count = 0
    if len(transitions) < nombre_symboles*nombre_etats :
        return False
    for i in range(nombre_etats-1) :
        for j in range(len(transitions)):
            if int(transitions[j][0]) == i:
                count += 1
        if count < nombre_symboles :
            return False
        count = 0
    for i in range(nombre_etats-1) :
        for j in range(nombre_symboles):
            if transitions[count][1] != chr(ord('a') + j):
                return False
            count += 1
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