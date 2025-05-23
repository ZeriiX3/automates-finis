# Project Automates finis et Expressions rationnelles: Traitement d'un automate
# Professeur: Federico ZALAMEA
# Avril 2024

# Par Sébastien XU, Maxence DURAND, Matthieu BACHELERIE, Angel BOURDIOL, Farès DARGOUTH


# Changement de la couleur des textes
def print_red(message):
    # Code d'échappement ANSI pour définir la couleur du texte sur rouge vif (91)
    print("\033[1;91m",end="")  # Rouge vif

    # Affichage du message en rouge
    print(message, end="")

    # Réinitialisation de la couleur du texte à la valeur par défaut (blanc)
    print("\033[0m")  # Réinitialise la couleur du texte à la valeur par défaut (blanc)

# La même chose mais avec les print("...", end="") pour que les arguments fonctionnent
def print_red_end(message, end):
    print("\033[1;91m",end="")  # Rouge vif
    print(message, end="")
    print("\033[0m", end="")

def print_blue(message):
    print("\033[1;34m", end="")  # Bleu clair
    print(message, end="")
    print("\033[0m")

def print_blue_end(message, end):
    print("\033[1;34m", end="")  # Bleu clair
    print(message, end="")
    print("\033[0m", end="")

def print_yellow(message):
    print("\033[1;93m", end="")  # Jaune vif
    print(message, end="")
    print("\033[0m")

def print_yellow_end(message, end):
    print("\033[1;93m", end="")  # Jaune vif
    print(message, end="")
    print("\033[0m", end="")

def print_green(message):
    print("\033[1;32m", end="")
    print(message, end="")
    print("\033[0m")

def print_light_green(message):
    print("\033[1;92m", end="")
    print(message, end="")
    print("\033[0m")

def print_green_end(message, end):
    print("\033[1;32m", end="")
    print(message, end="")
    print("\033[0m",end="")


# Affichage des automates
def affichage(transitions, etats_initiaux, etats_terminaux, nombre_symboles, nombre_etats, nombre_transitions, liste_etats) :
    print("E/S    Etat    ", end='')
    for i in range(1, nombre_symboles+1) :
        print("{:<8}".format(chr(ord('a') + i - 1)), end='')
    print("")
    for i in range(nombre_etats) :
        a = 8
        if liste_etats[i] in str(etats_initiaux) and liste_etats[i] in str(etats_terminaux) :
            print("E/S    ", end='')
        elif liste_etats[i] in str(etats_initiaux) :
            print("E      ", end='')
        elif liste_etats[i] in str(etats_terminaux) :
            print("S      ", end='')
        else :
            print("-      ", end='')
        if len(liste_etats[i]) >= 2 :
            print(liste_etats[i],"     ", end='')
        else :
            print(liste_etats[i],"      ", end='')
        for k in range(nombre_symboles) :
            for j in range(nombre_transitions) :
                if str(transitions[j][0]) == liste_etats[i] :
                    if transitions[j][1] == chr(ord('a') + k):
                        if a != 8 :
                            print("/",end='')
                            a -= 1
                        print(transitions[j][2], end='')
                        a -= 1
                        if len(str(transitions[j][2])) >= 2:
                            a -= 1
            if a == 8 :
                print("-", end='')
                a -= 1
            for y in range(a):
                print((' '), end='')
            a = 8
        print()
    return

def logo():

    # Codes d'échappement ANSI pour définir la couleur du texte sur bleu clair
    print("\033[1;34m")  # Bleu clair

    # Texte ASCII art à afficher avec le style et la couleur définis
    print(r"""
   _____  _____   ____       _ ______ _______                                                                      
  |  __ \|  __ \ / __ \     | |  ____|__   __|                                                                     
  | |__) | |__) | |  | |    | | |__     | |                                                                        
  |  ___/|  _  /| |  | |_   | |  __|    | |                                                                        
  | |    | | \ \| |__| | |__| | |____   | |                                                                        
  |_|____|_|  \_\\____/ \____/|______|  |_|      _         _ _               _                        _            
  |__   __|      (_) |                          | |       | ( )   /\        | |                      | |           
     | |_ __ __ _ _| |_ ___ _ __ ___   ___ _ __ | |_    __| |/   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___  ___ 
     | | '__/ _` | | __/ _ \ '_ ` _ \ / _ \ '_ \| __|  / _` |   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \/ __|
     | | | | (_| | | ||  __/ | | | | |  __/ | | | |_  | (_| |  / ____ \ |_| | || (_) | | | | | | (_| | ||  __/\__ \
   __|_|_|_ \__,_|_|\__\___|_| |_| |_|\___|_| |_|\__|  \__,_| /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___||___/
  |  ____(_)     (_)                                                                                               
  | |__   _ _ __  _ ___                                                                                            
  |  __| | | '_ \| / __|                                                                                           
  | |    | | | | | \__ \                                                                                           
  |_|    |_|_| |_|_|___/                                                                                           

    """)

    # Réinitialisation de la couleur du texte à la valeur par défaut (blanc)
    print("\033[0m")
