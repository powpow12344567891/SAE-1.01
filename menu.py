import os
from Score import *
from morpion import *
from devinette import *
from allumette import *
def clear():
    os.system('cls')
def menu():
    clear()
    while True:
        print("***********************************************************************************************")
        print("*                                         MENU                                                *")
        print("*                                    1) DEVINETTE                                             *")
        print("*                                    2) ALLUMETTE                                             *")
        print("*                                    3) MORPION                                               *")
        print("*                                    4) SCORE                                                 *")
        print("*                                    5) QUITTER                                               *")
        print("***********************************************************************************************")
        try:
            choix = int(input("Choisir une option : "))
            if choix not in [1, 2, 3, 4, 5]:
                print("Erreur, veuillez choisir une option valide (1, 2, 3 ou 4).")
                continue
        except ValueError:
            print("Erreur, veuillez entrer un nombre entier correspondant à une option.")
            continue
        if choix == 1:
            clear()
            lancement()
        elif choix == 2:
            clear()
            joueur1 = str(input("Entrez le nom du joueur 1: "))
            joueur2 = str(input("Entrez le nom du joueur 2: "))
            allumette(joueur1, joueur2)
        elif choix == 3:
            clear()
            morpion()
        elif choix == 4:
            clear()
            affichescore()

        # Redemander au joueur s'il souhaite continuer ou quitter
        elif choix ==5:
            clear()
            print("Merci d'avoir joué ! À bientôt.")
            break
if __name__ == "__main__":
    menu()