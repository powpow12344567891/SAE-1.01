from Score import *
from morpion import *
from devinette import *

def menu():
    choix: int 
    print("***********************************************************************************************")
    print("*                                         MENU                                                *")
    print("*                                    1) DEVINETTE                                             *")
    print("*                                    2) ALLUMETTE                                             *")
    print("*                                    3) MORPION                                               *")
    print("*                                    4) SCORE                                                 *")
    print("***********************************************************************************************")
    
    choix= int(input("choisir une option : "))
    while choix not in [1, 2, 3, 4]:
        choix= int(input("erreur, choisir une option : "))
    if (choix == 1):
        lancement()
        menu()
    if (choix == 2):
        lancement()
        menu()
    if (choix == 3):
        morpion()
        menu()
    if (choix == 4):
        affichescore()
        menu()
        
if __name__ == "__main__":
    menu()