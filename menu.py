from Score import *
from morpion import *

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
    while((choix != 1) and (choix != 2) and (choix != 3) and (choix != 4)):
        choix= int(input("erreur, choisir une option : "))
    if (choix == 3):
        morpion()
    if (choix == 4):
        affichescore()
        
if __name__ == "__main__":
    menu()