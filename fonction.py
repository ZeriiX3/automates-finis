def feur():
    return True

def choix_automate():

    while True:
        try:
            print("0: Quitter le programme")
            A = int(input("Veuillez choisir l'automate à utiliser entre 1 et 44: "))
            while(A < 1 or A > 44) :
                if A == 0:
                    return False
                print("Aucune choisie valide")
                A = int(input(">>> "))
            break

        except ValueError:
            print(">>>>>> Veuillez choisir un ENTIER <<<<<<<")

    return A