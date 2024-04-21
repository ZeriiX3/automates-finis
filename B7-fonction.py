# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH


#Import
from affichage import print_red, print_light_green, print_yellow, print_blue


# Demande à l'utilisateur l'automate qu'il veut utiliser
def choix_automate():

    while True:
        try:
            print_light_green("\nVeuillez choisir l'automate à utiliser entre 1 et 44\n")
            print_yellow("0: Quitter le programme")
            A = int(input(">>> "))

            if A == 0:
                return False

            if 1 <= A <= 44:
                return A

        except ValueError:
            print_red("\n>>> Veuillez saisir un nombre ENTIER valide <<<\n")


# Lecture des fichiers Automates et affichage du tableau des transitions
def lire_fichier(nom_fichier):

    transitions = []
    affichage = []
    liste_etats = []

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

            etat_depart, symbole, etat_arrivee = int(ligne[:u]), ligne[u], int(ligne[u + 1:])
            transitions.append([str(etat_depart), symbole, str(etat_arrivee)])
            # Mettre les états de départ et d'arriver dans une liste contenant tous les états
            liste_etats.append(etat_depart)
            liste_etats.append(etat_arrivee)

    # Faire de même pour les E et S
    liste_etats += etats_initiaux
    liste_etats += etats_terminaux

    # Liste des états en int, en supprimant les doublons et en rangeant dans l'ordre croissant
    liste_etats = sorted(set(liste_etats))
    # Pour tout mettre en str
    liste_etats = [str(e) for e in liste_etats]

    return transitions, etats_initiaux, etats_terminaux, nombre_symboles, nombre_etats, nombre_transitions, liste_etats


def est_standard(transitions, etats_initiaux) :

    # Vérifie s'il y a plus d'une entrée
    if len(etats_initiaux) > 1:
        return False
    else :
        # Vérifie si il y a une transition vers l'entrée
        for i in range(len(transitions)):
            if str(transitions[i][2]) == str(etats_initiaux[0]) :
                return False
    return True


def standardiser(transitions, etats_initiaux, etats_terminaux, nombre_etats, nombre_transitions, liste_etats):

    nb_trans = nombre_transitions
    if not est_standard(transitions,etats_initiaux) :
        nombre_etats += 1
        temp = 0
        liste_etats.append("E")

        for i in range(len(etats_initiaux)) :
            if etats_initiaux[i] in etats_terminaux :
                temp = 1
        for i in range(nombre_transitions) :
            if transitions[i][0] in etats_initiaux :
                if ["E", transitions[i][1], transitions[i][2]] not in transitions:
                    transitions.append(["E", transitions[i][1], transitions[i][2]])
                    nb_trans += 1
        etats_initiaux = ["E"]

        if temp == 1 :
            etats_terminaux.append("E")
        return transitions, etats_initiaux, etats_terminaux, nombre_etats, nb_trans, liste_etats

    else :
        print_blue("Déja standard")
        return transitions, etats_initiaux, etats_terminaux, nombre_etats, nb_trans, liste_etats


def est_deter(transitions, etats_initiaux) :

    # Vérifie s'il y a plus d'une entrée
    if len(etats_initiaux) > 1:
        return False
    # Vérifie que pour chaque état, il y a une transition avec le même alphabet
    else :
        for i in range(len(transitions)):
            for j in range(len(transitions)):
                if i != j :
                    if str(transitions[i][0]) == str(transitions[j][0]) :
                        if transitions[i][1] == transitions[j][1] :
                            return False
    return True


def est_complet(transitions, nombre_symboles, nombre_etats,liste_etats) :

    count = 0
    if len(transitions) < nombre_symboles * nombre_etats :
        return False

    for i in range(nombre_etats - 1) :
        for j in range(len(transitions)):
            if str(transitions[j][0]) == str(liste_etats[i]):
                count += 1
        if count < nombre_symboles :
            return False
        count = 0

    for i in range(nombre_etats - 1) :
        for j in range(nombre_symboles):
            if transitions[count][1] != chr(ord('a') + j):
                return False
            count += 1
    return True

"""
def complementariser(etats_terminaux):
    # Inverser les états initiaux et terminaux
    nouveaux_etats_initiaux = etats_terminaux
    nouveaux_etats_terminaux = etats_initiaux

    return nouveaux_etats_initiaux, nouveaux_etats_terminaux
    """
