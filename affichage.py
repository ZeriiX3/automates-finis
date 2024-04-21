# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH

# IMPORT



def affichage(transitions, etats_initiaux, etats_terminaux, nombre_symboles, nombre_etats, nombre_transitions, liste_etats) :

    print("I/O    Etat    ", end='')
    for i in range(1, nombre_symboles+1) :
        print("{:<8}".format(chr(ord('a') + i - 1)), end='')
    print("")

    for i in range(nombre_etats) :
        a = 8
        if i in etats_initiaux and i in etats_terminaux :
            print("I/O    ", end='')
        elif i in etats_initiaux :
            print("I      ", end='')
        elif i in etats_terminaux :
            print("O      ", end='')
        else :
            print("-      ", end='')
        if i >= 10 :
            print(i,"     ", end='')
        else :
            print(i,"      ", end='')

        for k in range(nombre_symboles) :
            for j in range(nombre_transitions) :

                if int(transitions[j][0]) == i :
                    if transitions[j][1] == chr(ord('a') + k):
                        if a != 8 :
                            print("/",end='')
                            a -= 1
                        print(transitions[j][2], end='')
                        a -= 1

                        if int(transitions[j][2]) >= 10 :
                            a -= 1
            if a == 8 :
                print("-", end='')
                a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8

        print()
    return
