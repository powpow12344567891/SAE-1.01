import os  # Pour interagir avec le système d'exploitation
from Score import affichescore  # Importer uniquement la fonction affichescore
from morpion import menumorpion  # Importer uniquement la fonction morpion
from devinette import lancement  # Importer uniquement la fonction lancement
from allumette import choix_pvpve  # Importer uniquement la fonction allumette
from puissance4 import jeuhumain

# Fonction pour effacer l'écran de la console
def clear():
    os.system('cls')  # Commande Windows pour nettoyer la console

# Fonction principale du menu
def menu():
    choixmenu : int

    clear()  # Efface l'écran au debut
    while True:  # Boucle infinie pour afficher le menu jusqu'à ce que l'utilisateur quitte
        # Affichage du menu principal
        choixmenu = 0
        print("***********************************************************************************************")
        print("*                                         MENU                                                *")
        print("*                                    1) DEVINETTE                                             *")
        print("*                                    2) ALLUMETTE                                             *")
        print("*                                    3) MORPION                                               *")
        print("*                                    4) puissance 4                                           *")
        print("*                                    5) SCORE                                                 *")
        print("*                                    6) QUITTER                                               *")
        print("***********************************************************************************************")
        
        try:
            choixmenu = int(input("Choisir une option : "))  # Lecture de l'option choisie par l'utilisateur
            # Vérifie si l'option choisie est valide
            if choixmenu not in [1, 2, 3, 4, 5, 6]:
                print("Erreur, veuillez choisir une option valide (1, 2, 3, 4 ou 5).")
                continue  # Recommence la boucle en cas de choix invalide
        except ValueError:
            # Gestion de l'erreur si l'entrée n'est pas un entier
            print("Erreur, veuillez entrer un nombre entier correspondant à une option.")
            continue  # Recommence la boucle

        # Exécute une action en fonction du choix
        if choixmenu == 1:
            clear()  # Efface l'écran
            lancement()  # Appelle la fonction
        elif choixmenu == 2:
            clear()  # Efface l'écran
            choix_pvpve()  # Lance le jeu ALLUMETTE
        elif choixmenu == 3:
            clear()  # Efface l'écran
            menumorpion()  # Lance le jeu MORPION
        elif choixmenu == 4:
            clear()  # Efface l'écran
            jeuhumain()
  # Appelle la fonction pour afficher le score
        #quitter le programme
        elif choixmenu == 5:
             affichescore()
        elif choixmenu == 5:
            clear()  # Efface l'écran
            print("Merci d'avoir joué ! À bientôt.")
            break  # Sort de la boucle

if __name__ == "__main__":
    menu()  # Appelle la fonction menu pour démarrer le programme